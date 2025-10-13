# lca_algebraic workshop

## lca_algebraic package

lca_algebraic package is a python package above brightway that aims :
* to provide basic functions to simplify the use of brightway and add few basic functionalities to build a parameterised LCA model.
* to provide advanced functions to study uncertainties propagation in LCA model (one-at-a time and Global Sensitivity Analysis)

__lca_algebraic documentation__ can be found [here](https://lca-algebraic.readthedocs.io/en/stable/api/index.html)


## Objectives

__The advanced lca_algebraic functions related to uncertainties and statistics calculations are explained in this workshop from part 6.3 to the end.__
The upper parts from 1 to 6.2 show how to use __basic functions__ of lca_algebraic to build a basic LCA with small exercices.
If you want more explanations about basic functions, we highly recommand you to use the lca_algebraic handbook that is more detailed and that shows more functions. 

## Requirements to run this script

* A licence for ecoinvent 3.10 cutoff database
* Python **3.11**
* lca_algebraic version 1.3

## Setup 

1) Create a [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [pip](https://docs.python.org/3/library/venv.html) 
  environment with **Python 3.11** and activate it.

   ```bash
   conda create -n name_env python=3.11
   conda activate name_env
   ```

2) Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

3) Create a **brightway project** and install **Ecoinvent 3.10** in this project:

   * Run the import script called setup.py
   ```bash
   python setup.py
   ```
## How to use this notebook ?

Run Jupyter
```bash
jupyter notebook
```

It should open a browser window.

From here, you can open the notebooks **workshop** and **workshop_answers** file.

In 'workshop' file, you will find small exercices and the answers are shown in 'workshop_answers' file. 

