import numpy as np
import json
import os
from matplotlib import pyplot as plt

from algo.IF1 import InterleavedFilter
from algo.RMED import RMED
from algo.BTM import BeatTheMean
from algo.DOUBLER import DOUBLER
from algo.savage import SAVAGE
from algo.rucb import RUCB
from algo.rcs import RCS
from algo.thompson import THOMPSON
import argparse
import warnings; warnings.filterwarnings("ignore", category=DeprecationWarning) 


parser = argparse.ArgumentParser(description="Arguments for the experiment.")
parser.add_argument("--horizon", type=int, default=100, help="Horizon for the experiment.")
parser.add_argument("--samples", type=int, default=3, help="Number of samples for the experiment.")
parser.add_argument("--models", type=str, nargs='+', help="List of models for the experiment.", default=["RMED1", "RMED2", "IF", "BTM", "DOUBLER", "SAVAGE", "RUCB", "RCS", "THOMPSON"])
parser.add_argument("--dataset", type=str, default="data/10_art.text", help=".text dataset path for the experiment.")
parser.add_argument("--best_arm", type=int, default=0, help="Index of the best arm.")
parser.add_argument("--save_result", type=bool, default=True, help="Save the results as JSON.")
parser.add_argument("--run_name", type=str, default="", help="Name of the run to prepend to output.")
parser.add_argument("--n_arms", type=int, default=2, help="Number of arms for the experiment.") 

args = parser.parse_args()
print(args)

horizon = args.horizon
samples = args.samples
dataset = args.dataset
best_arm = args.best_arm

with open(dataset, 'rb') as f:
    pref_mat = np.loadtxt(f)    


generator_fnc = lambda i, j: np.random.binomial(n=1, p=pref_mat[int(i)][int(j)], size=1)
regret_fn = lambda i, j: pref_mat[best_arm][int(i)] + pref_mat[best_arm][int(j)] - 1
f_rmed = lambda k: 0.3 * (k**1.01)

# algo_list = ["RMED1", "RMED2", "IF", "BTM", "DOUBLER", "SAVAGE", "RUCB", "RCS", "THOMPSON"]
algo_list= args.models
_d = {key+"_regrets": [] for key in algo_list}
winner = {key+"_winner": [] for key in algo_list}

def run_algorithm(algo_name):
    match algo_name:
        case "RMED1":
            x = RMED('RMED1', len(pref_mat), horizon,  generator_fnc, f_rmed, regret_fn).algo()
        case "RMED2":
            x = RMED('RMED2', len(pref_mat), horizon,  generator_fnc, f_rmed, regret_fn).algo()
        case "IF":
            x = InterleavedFilter(len(pref_mat), horizon,  generator_fnc,  regret_fn).algo()
        case "BTM":
            x = BeatTheMean(len(pref_mat), horizon,  generator_fnc,  regret_fn).algo()
        case "DOUBLER":
            x = DOUBLER(horizon, pref_mat, regret_fn, n_arms=args.n_arms).run()
        case "SAVAGE":
            x = SAVAGE(horizon, pref_mat, regret_fn, n_arms=args.n_arms).run()
        case "RUCB":
            x = RUCB(horizon, pref_mat,  n_arms=args.n_arms).run()
        case "RCS":
            x = RCS(horizon, pref_mat,  n_arms=args.n_arms).run()
        case "THOMPSON":
            x = THOMPSON(horizon, pref_mat, regret_fn, n_arms=args.n_arms).run()
        case _:
            raise ValueError("Invalid algorithm name")
    print(f"{algo_name}:", x[1], end=" ")
    _d[f"{algo_name}_regrets"].append(x[0])
    winner[f"{algo_name}_winner"].append(x[1])


        
for i in range(samples):
    print("\nSample:", i, " | ", end=" ")
    for algorithms in algo_list:
        run_algorithm(algorithms)

filename= os.path.basename(dataset).split('.')[0] + "_" +args.run_name
if args.save_result: 
    with open(filename+"_.json", 'w') as f: json.dump(_d, f)
    print("\nResults saved as", filename+"_.json")

extend_array = lambda input_array: np.array(list(map(lambda arr: arr + [arr[-1]] * (max(map(len, input_array)) - len(arr)), input_array)))
for key, val in _d.items():
    plt.plot(np.mean(extend_array(val), axis=0), label=key.split('_')[0])

plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time')
plt.ylabel('Cumulative Regret')
plt.savefig(f'{filename}_.png')
print(f"Performance plots saved as {filename}_.png")