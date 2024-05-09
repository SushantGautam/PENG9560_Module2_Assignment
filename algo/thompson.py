import numpy as np
import math
import json
import matplotlib.pyplot as plt
from scipy.stats import beta

class sbm():
    def __init__(self, n_arms):
        # Beta parameters for each arm
        self.alpha = np.ones(n_arms)
        self.beta = np.ones(n_arms)
        self.k = n_arms

    def reset(self):
        # Reset beta parameters to uniform
        self.alpha = np.ones(self.k)
        self.beta = np.ones(self.k)

    def advance(self):
        # Sample from beta distributions to decide on the arm
        samples = [beta.rvs(a, b) for a, b in zip(self.alpha, self.beta)]
        choice = np.argmax(samples)
        return choice

    def feedback(self, arm, reward):
        # Update beta distribution based on reward
        if reward == 1:
            self.alpha[arm] += 1
        else:
            self.beta[arm] += 1

class THOMPSON():
    def __init__(self, horizon, pref, regret_func):
        self.pref_matrix = np.array(pref)
        n_arms = len(pref[0])
        self.sbm = sbm(n_arms)
        self.l = np.random.randint(n_arms, size=1)
        self.i, self.t = 1, 1
        self.horizon = horizon
        self.regret_func = regret_func

    def run(self):
        regret = [0]
        while self.t < self.horizon:
            self.sbm.reset()
            new_l = set()
            for j in range(2**self.i):
                xt = np.random.choice(self.l)
                yt = self.sbm.advance()
                new_l.add(yt)
                bt = np.random.binomial(1, self.pref_matrix[xt][yt], 1)
                if bt == 1:
                    self.sbm.feedback(yt, 0)
                    self.sbm.feedback(xt, 1)
                else:
                    self.sbm.feedback(yt, 1)
                    self.sbm.feedback(xt, 0)
                regret.append(regret[-1] + self.regret_func(xt, yt))
                self.t += 1
                if self.t >= self.horizon:
                    break
            self.l = np.array(list(new_l))
            self.i += 1

        # Calculate the expected reward for each arm to find the winner
        expected_rewards = [self.sbm.alpha[a] / (self.sbm.alpha[a] + self.sbm.beta[a]) for a in range(self.sbm.k)]
        winner = np.argmax(expected_rewards)
        return list(np.around(regret, 3)), winner
