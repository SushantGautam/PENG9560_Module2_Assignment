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
                        (Optional) List of models for the experiment. Sets all by default: RMED1  RMED2 IF BTM DOUBLER SAVAGE RUCB RCS THOMPSON
  --best_arm BEST_ARM   Index of the best arm. Optional; Recommended
  --save_result SAVE_RESULT Save the results as JSON. Optional
  --run_name RUN_NAME   Name of the run to prepend to output. Optional
```


## Algorithms:


#### BTM:
Yue, Yisong and Thorsten Joachims. "ICML'11: Proceedings of the 28th International Conference on International Conference on Machine Learning." Beat the mean bandit. Omnipress, 28 June 2011, https://doi.org/10.5555/3104482.3104513.

#### IF:
Yue, Yisong, et al. "The K-armed dueling bandits problem." J. Comput. System Sci., 2012, https://doi.org/10.1016/j.jcss.2011.12.028.

#### THOMPSON:
Agrawal, Shipra and Navin Goyal. "Conference on Learning Theory." Analysis of Thompson Sampling for the Multi-armed Bandit Problem. JMLR Workshop and Conference Proceedings, 16 June 2012, pp. 39.1-39.26, https://proceedings.mlr.press/v23/agrawal12.html.

#### RMED1/2:
Komiyama, Junpei, et al. "Conference on Learning Theory." Regret Lower Bound and Optimal Algorithm in Dueling Bandit Problem. PMLR, 26 June 2015, https://proceedings.mlr.press/v40/Komiyama15.html.

#### SAVAGE:
Urvoy, Tanguy, et al. "International Conference on Machine Learning." Generic Exploration and K-armed Voting Bandits. PMLR, 13 May. 2013, https://proceedings.mlr.press/v28/urvoy13.html.

#### DOUBLER:
Ailon, Nir, et al. "International Conference on Machine Learning." Reducing Dueling Bandits to Cardinal Bandits. PMLR, 18 June 2014, pp. 856-64, https://proceedings.mlr.press/v32/ailon14.html.

#### RUCB:
Zoghi, Masrour, et al. "International Conference on Machine Learning." Relative Upper Confidence Bound for the K-Armed Dueling Bandit Problem. PMLR, 18 June 2014, pp. 10-18, https://proceedings.mlr.press/v32/zoghi14.html.

#### RCS:
Zoghi, Masrour, et al. "WSDM '14: Proceedings of the 7th ACM international conference on Web search and data mining." Relative confidence sampling for efficient on-line ranker evaluation. Association for Computing Machinery, 24 Feb. 2014, pp. 73-82, https://doi.org/10.1145/2556195.2556256.


## Good resources
#### https://pratikgajane.github.io/files/PhD-thesis-Pratik-Gajane.pdf
#### https://github.com/methi1999/dueling-bandits
