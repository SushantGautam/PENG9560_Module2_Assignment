# PENG9560_Module2_Assignment

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SushantGautam/PENG9560_Module2_Assignment/HEAD)

at /home/sushant/D1/Assignments/AI_9560_module2


View in [Overleaf](https://www.overleaf.com/read/bpqxdfxbsxds#deab8a)

Resource Folder at [Google Drive](https://drive.google.com/drive/u/0/folders/1ZamN8_n0ETlPOtv5ehjcDv1lExfxLtVT)

## Usage:
```python
 python experiment.py [-h] [--horizon HORIZON] [--samples SAMPLES] [--dataset DATASET] [--models MODELS [MODELS ...]]
                     [--save_result SAVE_RESULT] [--best_arm BEST_ARM] [--run_name RUN_NAME]

Arguments for the experiment.

options:
  -h, --help            show this help message and exit
  --horizon HORIZON     Horizon for the experiment. 
  --samples SAMPLES     Number of samples for the experiment.
  --dataset DATASET     .npy dataset path for the experiment.
  --models MODELS [MODELS ...]
                        List of models for the experiment. All by default: RMED1  RMED2 IF BTM DOUBLER SAVAGE RUCB RCS 
  --best_arm BEST_ARM   Index of the best arm.
  --save_result SAVE_RESULT Save the results as JSON.
  --run_name RUN_NAME   Name of the run to prepend to output.
```
