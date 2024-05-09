#!/bin/bash
## We comment lot of arguments with ## as we dont care which partition will execute the job.
##SBATCH -N 2 # number of nodes
##SBATCH -n 2  # number of cores
##SBATCH --mem 1G # memory pool for all cores
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
 
python -m pip install -r requirements.txt

# change the experiment params before submitting.
srun python experiment.py --horizon 1000 --samples 10 --dataset data/10_art.npy  --best_arm 0  --save_result true --run_name $SLURM_JOB_ID  --models RMED1 RMED2 IF BTM DOUBLER


# submit job with:  sbatch run.slurm

