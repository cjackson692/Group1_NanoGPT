import itertools
import os

base_cmd = (
    "python train.py config/train_shakespeare_char.py "
    "--compile=False --eval_iters=20 --log_interval=5 --device='cuda' "
    "--lr_decay_iters=1000"
)
params = {
    "block_size": [64, 128],
    "n_layer": [4, 6],
    "n_head": [4, 8],
    "n_embd": [128, 256],
    "batch_size": [8, 16],
    "max_iters": [1000, 2000],
    "dropout": [0.1, 0.2],
}
keys = list(params.keys())
combinations = list(itertools.product(*params.values()))
out_path = "/content/train_all_configs.sh"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    f.write("#!/bin/bash\n\n")
    for combo in combinations:
        args = " ".join(f"--{k}={v}" for k, v in zip(keys, combo))
        tag = "_".join(f"{k}{v}" for k, v in zip(keys, combo))
        out_dir = f"out/{tag}"
        wandb_run = f"run_{tag}"
        f.write(
            f"!{base_cmd} {args} "
            f"--out_dir={out_dir} "
            f"--wandb_log=True --wandb_project='owt' --wandb_run_name='{wandb_run}'\n"
        )