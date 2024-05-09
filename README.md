# PENG9560_Module2_Assignment


at /home/sushant/D1/Assignments/AI_9560_module2


View in [Overleaf](https://www.overleaf.com/read/bpqxdfxbsxds#deab8a)

Resource Folder at [Google Drive](https://drive.google.com/drive/u/0/folders/1ZamN8_n0ETlPOtv5ehjcDv1lExfxLtVT)

## Usage:
Example:
```python
 python experiment.py  --horizon 1000 --samples 10 --dataset data/10_art.npy  --best_arm 0   --save_result true --run_name run1  --models RMED1 IF BTM DOUBLER THOMPSON
```
Run quickly on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SushantGautam/PENG9560_Module2_Assignment/HEAD). Start a terminal and enter command above.

Arguments for the experiment.

```python
 python experiment.py [-h] [--horizon HORIZON] [--samples SAMPLES] [--dataset DATASET] [--models MODELS [MODELS ...]]
                     [--save_result SAVE_RESULT] [--best_arm BEST_ARM] [--run_name RUN_NAME]
options:
  -h, --help            show this help message and exit
  --horizon HORIZON     Horizon for the experiment.  Optional; Recommended to set
  --samples SAMPLES     Number of samples for the experiment. Optional; Recommended to set
  --dataset DATASET     .npy dataset path for the experiment. Optional; Recommended to set
  --models MODELS [MODELS ...]
                        (Optional) List of models for the experiment. Sets all by default: RMED1  RMED2 IF BTM DOUBLER SAVAGE RUCB RCS 
  --best_arm BEST_ARM   Index of the best arm. Optional; Recommended
  --save_result SAVE_RESULT Save the results as JSON. Optional
  --run_name RUN_NAME   Name of the run to prepend to output. Optional
```
