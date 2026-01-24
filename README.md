# Kidney-Disease-Classification-Deep-Learning-Project

## Workflows


1. Update config.yaml
2. Update secrets.yaml[optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


....
# How to run ?
....
### Steps:

Clone the repository

```bash
https://github.com/Naina-Coder123/Kidney-Disease-Classification-Deep-Learning-Project
```

....
### STEP 01-Create a conda environment after opening the repository

```bash
conda create  -n cnncls pyhton=3.8 -y
```

```bash
conda activate cnncls
```

### Step 02- install the requirements
```bash
pip install -r requirements.txt
```



#### CMD
mlflow ui

### dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/Naina-Coder123/Kidney-Disease-Classification-Deep-Learning-Project.mlflow
MLFLOW_TRACKING_USERNAME=Naina-Coder123
MLFLOW_TRACKING_PASSWORD=f82b8bd9b71164d260ef4671ad7ef51f8643fc79
python script.py


Run this to export as env variables:
```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Naina-Coder123/Kidney-Disease-Classification-Deep-Learning-Project.mlflow
export MLFLOW_TRACKING_USERNAME=Naina-Coder123
export MLFLOW_TRACKING_PASSWORD=f82b8bd9b71164d260ef4671ad7ef51f8643fc79
```
### for terminal cmd
D:\Anaconda\envs\kidney\python.exe main.py