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
print("Size of preference matrix:", pref_mat.shape)


generator_fnc = lambda i, j: np.random.binomial(n=1, p=pref_mat[int(i)][int(j)], size=1)
regret_fn = lambda i, j: pref_mat[best_arm][int(i)] + pref_mat[best_arm][int(j)] - 1
f_rmed = lambda k: 0.3 * (k**1.01)

# algo_list = ["RMED1", "RMED2", "IF", "BTM", "DOUBLER", "SAVAGE", "RUCB", "RCS", "THOMPSON"]
algo_list= args.models
_d = {key+"_regrets": [] for key in algo_list}
winner = {key+"_winner": [] for key in algo_list}

n_arms_ = args.n_arms if args.n_arms > 0 else len(pref_mat)
print("Number of arms:", n_arms_)

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
            x = DOUBLER(horizon, pref_mat, regret_fn, n_arms=n_arms_).run()
        case "SAVAGE":
            x = SAVAGE(horizon, pref_mat, regret_fn, n_arms=n_arms_).run()
        case "RUCB":
            x = RUCB(horizon, pref_mat,  n_arms=n_arms_).run()
        case "RCS":
            x = RCS(horizon, pref_mat,  n_arms=n_arms_).run()
        case "THOMPSON":
            x = THOMPSON(horizon, pref_mat, regret_fn, n_arms=n_arms_).run()
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

import seaborn as sns
extend_array = lambda input_array: np.array(list(map(lambda arr: arr + [arr[-1]] * (max(map(len, input_array)) - len(arr)), input_array)))
for key, val in _d.items():
    a= extend_array(val)
    a[a < 0] = 0
    plt.plot(np.mean(a, axis=0), label=key.split('_')[0])
# for key, val in _d.items():
#     data= extend_array(val)
#     mean_=np.mean(data, axis=0)
#     std_=np.std(data, axis=0)
#     plt.plot(mean_, label=key.split('_')[0])
#     plt.fill_between(range(len(mean_)), mean_-std_, mean_+std_, alpha=0.2)

#     # use seaborn for better plots
#     sns.relplot(data=extend_array(val), kind='line', errorbar='sd')
# import pandas as pd
# plt.figure(figsize=(8, 4))
# sns.set_theme(style="whitegrid")
# for key, val in _d.items():
#     ss= np.array(extend_array(val))
#     mean= np.mean(ss, axis=0)
#     std= np.std(ss, axis=0)
#     plt.plot(mean, label=key.split('_')[0])
#     plt.fill_between(range(horizon), mean-std, mean+std, alpha=0.2)
#     #log scale
# plt.xscale('log')
# # plt.yscale('log')
# plt.xlabel(f'Time (log scale)')
# plt.ylabel('Cumulative Regret (log scale)')
# plt.tight_layout()
# plt.legend()
# plt.savefig(f'{filename}_.png')
    

    # sampled_indices = np.linspace(0, ss.shape[1] - 1 - 1, 77777, dtype=int)
    # sampled_array = ss[:, sampled_indices].T
    # sampled_array_flat = sampled_array.flatten()
    # indices_flat = np.array([sampled_indices for _ in range(ss.shape[0])]).flatten()
    # # create df with value and index
    # breakpoint()
    # df_ = pd.DataFrame.from_dict({ "value": sampled_array_flat, "index": indices_flat})
    # sns.relplot(data=df_, x="index", y="value", kind='line', legend=False)

    # create df with keyfra
    # sampled_array = ss[0, sampled_indices].T
    # mean_regret = np.mean(sampled_array, axis=0)
    # std_regret = np.std(sampled_array, axis=0)
    # plt.plot(np.std(extend_array(val), axis=0), label=key.split('_')[0])

    # # breakpoint()    
    # sns.relplot(data=sampled_array, kind='line', errorbar='sd', legend=False)
    # plt.legend([],[], frameon=False)


# # breakpoint()
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time (log scale)')
plt.ylabel('Cumulative Regret (log scale)')
plt.savefig(f'{filename}_.png')
print(f"Performance plots saved as {filename}_.png")