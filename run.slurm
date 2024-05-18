#!/bin/bash
## We comment lot of arguments with ## as we dont care which partition will execute the job.
#SBATCH -p habanaq
##SBATCH -N 2 # number of nodes
##SBATCH -n 2  # number of cores
##SBATCH --mem 1G # memory pool for all cores
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
 
python -m pip install -r requirements.txt

# change the experiment params before submitting.
srun python experiment.py --horizon 100000 --samples 10 --n_arms 2  --run_name arm_2_$SLURM_JOB_ID --dataset data/10_real.txt  --best_arm 0  --save_result true 


# submit job with:  sbatch run.slurm

