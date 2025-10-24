```
├── README.md
├── all_train_outputs.txt # Contains the collected output from all the training commands
├── config_generation.py # takes the parameter grid in and generates a shell script to run each necessary instance of the model
├── train_all_configs.sh # Shell script containing 128 model configs
└── nanoGPT/ # Minimal Reproduction of nanoGPT, with only necessary files to train and model the shakespeare-char
    ├── train.py
    ├── sample.py
    ├── model.py
    ├── configurator.py
    ├── config/
    │   ├── finetune_shakespeare.py
    │   └── train_shakespeare_char.py
    └── data/
        └── shakespeare_char/
            ├── input.txt
            ├── meta.pkl
            ├── prepare.py
            ├── tain.bin
            └── val.bin
```
The following link accesses the complete saved versions of each iteration of the model (too large to zip and save to github): https://drive.google.com/drive/folders/1TMR02psLbr8Ic2hmhVnRcpljq9AzqC_Y?usp=sharing

The following link accesses the logging on wandb.ai: https://wandb.ai/cjackson692-university-of-north-texas/nanoGPT_testing_gp1?nw=nwusercjackson692
