from os.path import join
import pandas as pd
import numpy as np
import random

# Set the random seeds
seed = 0
np.random.seed(seed)
random.seed(seed)

# Set the base folder path
BASE_FOLDER = '/workspaces/cvnlp_model_evaluation'

# Set the resources folder paths
RESOURCES_FOLDER_PATH = join(BASE_FOLDER, 'resources')
GROUND_TRUTH_FOLDER_PATH = join(RESOURCES_FOLDER_PATH, 'ground_truth')
MODEL_EVALUATION_RESULTS_FOLDER_PATH = join(RESOURCES_FOLDER_PATH, 'model_evaluation_results')
SPEECH_MODEL_RESULTS_FOLDER_PATH = join(MODEL_EVALUATION_RESULTS_FOLDER_PATH, 'speech_model')
TEXT_MODEL_RESULTS_FOLDER_PATH = join(MODEL_EVALUATION_RESULTS_FOLDER_PATH, 'text_model')

# Set the ground truth labels
RAW_GROUND_TRUTH_LABELS = pd.read_csv(join(GROUND_TRUTH_FOLDER_PATH, 'raw', 'test_sent_clean.csv'))
GROUND_TRUTH_LABELS = pd.read_csv(join(GROUND_TRUTH_FOLDER_PATH, 'ground_truth.csv'))

# Set the model evaluation results
SPEECH_MODEL_RESULTS = pd.read_csv(join(SPEECH_MODEL_RESULTS_FOLDER_PATH, 'baseline_weighted__12_05_2023_00_14_44_val_results_26.csv'))
TEXT_MODEL_RESULTS = pd.read_csv(join(TEXT_MODEL_RESULTS_FOLDER_PATH, 'converted_abhishake_results_1.csv'))

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

# Homero conversion one-hot index to our one-hot index mapping
HOMER_CONVERSION_ONE_HOT_INDEX_TO_OUR_ONE_HOT_INDEX = {
    4: 0,
    6: 1,
    2: 2,
    5: 3,
    3: 4,
    1: 5,
    0: 6
}

# Emotion label strings
EMOTION_LABELS_STRINGS = list(EMOTION_LABEL_TO_ONE_HOT_INDEX.keys())

# Bins
SAMPLE_LENGTH_BINS = np.arange(0, 10, 0.5)
SAMPLE_PITCH_RANGE_BINS = np.arange(0, 2500, 500)
