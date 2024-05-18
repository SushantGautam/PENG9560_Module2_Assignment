import glob
import json
import matplotlib.pyplot as plt
#recusively get all json files in the directory
all_jsons = glob.glob('final_simula/**/*.json', recursive=True)

import numpy as np
extend_array = lambda input_array: np.array(list(map(lambda arr: arr + [arr[-1]] * (max(map(len, input_array)) - len(arr)), input_array)))

for json_file in all_jsons:
    with open(json_file, 'r') as f:
        if not "soccer_data_arm_2" in json_file:
            continue
        _d = json.load(f)
        plt.figure(figsize=(8, 4))
        for key, val in _d.items():
            print(key)
            if not key in ['SAVAGE_regrets', 'RUCB_regrets', 'RCS_regrets']:
                continue
            data= extend_array(val)
            mean_=np.mean(data, axis=0)
            print(mean_)
            std_=np.std(data, axis=0)
            plt.plot(mean_, label=key.split('_')[0])
            plt.fill_between(range(len(mean_)), mean_-std_, mean_+std_, alpha=0.2)
filename="temp"

plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time (log scale)')
plt.ylabel('Cumulative Regret (log scale)')
plt.tight_layout()
plt.savefig(f'{filename}_.png')
print(f"Performance plots saved as {filename}_.png")