from os.path import join
import pandas as pd
import numpy as np
import torch
import random

# Add the global modules to the python path
import sys
sys.path.append('/workspaces/cvnlp_model_evaluation/code_mount/modules')

# Set the random seeds
seed = 0
np.random.seed(seed)
torch.manual_seed(seed)
random.seed(seed)

# Set the device
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Get the speech and text model results dataframes
MODEL_RESULTS_BASE_FOLDER_PATH = join(BASE_PATH, 'resources/model_evaluation_results')
SPEECH_MODEL_RESULTS = pd.read_csv(join(MODEL_RESULTS_BASE_FOLDER_PATH, 'speech_model', 'baseline_weighted__11_05_2023_12_19_56_val_results_7.csv'))
TEXT_MODEL_RESULTS = pd.read_csv(join(MODEL_RESULTS_BASE_FOLDER_PATH, 'text_model', 'baseline_weighted__11_05_2023_12_19_56_val_results_7.csv'))

# Emotion label to one-hot index mapping
EMOTION_LABEL_TO_ONE_HOT_INDEX = {
    'neutral': 0,
    'surprise': 1,
    'fear': 2,
    'sadness': 3,
    'joy': 4,
    'disgust': 5,
    'anger': 6
}

# Emotion label strings
EMOTION_LABELS_STRINGS = list(EMOTION_LABEL_TO_ONE_HOT_INDEX.keys())

# Bins
SAMPLE_LENGTH_BINS = np.arange(0, 10, 0.5)
SAMPLE_PITCH_RANGE_BINS = np.arange(0, 2500, 500)
