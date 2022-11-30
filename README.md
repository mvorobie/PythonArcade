# PythonArcade
## Intro

This repository follows more or less the Arcade Platformer article
at https://realpython.com/platformer-python-arcade/

All game artwork from www.kenney.nl
Game sounds and tile maps by author

## How To
The code uses mainly the arcade package. A conda environment file is provided for 
convenience. You can install all the necessary and activate it with 
```commandline
conda env create -f environment.yaml 
conda activate arcade
```

The game startup is located in the `arcade_platformer/title_view.py` file. 
You can run it from an IDE or the command line using 
```commandline
python arcade_platformer/title_view.py
```