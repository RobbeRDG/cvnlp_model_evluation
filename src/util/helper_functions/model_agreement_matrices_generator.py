import numpy as np
import pandas as pd

def generate_model_agreement_matrix_per_emotion_class(combined_class_filtered_combined_model_results, emotion_classes):
    for emotion_class in emotion_classes:
        # Filter the combined model results to only include the current emotion class
        class_filtered_combined_model_results = combined_class_filtered_combined_model_results.loc[combined_class_filtered_combined_model_results['ground_truth_emotion'] == emotion_class]

        # Generate the model agreement matrix for the current emotion class
        model_agreement_matrix = generate_model_agreement_matrix(class_filtered_combined_model_results)


def generate_model_agreement_matrix(class_filtered_combined_model_results):
    # Calculate how many times the text and speech model agreed and had the correct prediction
    both_agreed_and_correct_count = class_filtered_combined_model_results.loc[
        (class_filtered_combined_model_results['text_predicted_emotion'] == class_filtered_combined_model_results['speech_predicted_emotion']) & 
        (class_filtered_combined_model_results['text_predicted_emotion'] == class_filtered_combined_model_results['ground_truth_emotion_one_hot_index'])
        ].count()[0]
    
    # Calculate how many times the text model was correct but the speech model was wrong
    text_correct_speech_wrong_count = class_filtered_combined_model_results.loc[
        (class_filtered_combined_model_results['text_predicted_emotion'] == class_filtered_combined_model_results['ground_truth_emotion_one_hot_index']) &
        (class_filtered_combined_model_results['text_predicted_emotion'] != class_filtered_combined_model_results['speech_predicted_emotion'])
        ].count()[0]
    
    # Calculate how many times the speech model was correct but the text model was wrong
    speech_correct_text_wrong_count = class_filtered_combined_model_results.loc[
        (class_filtered_combined_model_results['speech_predicted_emotion'] == class_filtered_combined_model_results['ground_truth_emotion_one_hot_index']) &
        (class_filtered_combined_model_results['text_predicted_emotion'] != class_filtered_combined_model_results['speech_predicted_emotion'])
        ].count()[0]
    
    # Calculate how many times both models were wrong
    both_wrong_count = class_filtered_combined_model_results.loc[
        (class_filtered_combined_model_results['text_predicted_emotion'] != class_filtered_combined_model_results['ground_truth_emotion_one_hot_index']) &
        (class_filtered_combined_model_results['speech_predicted_emotion'] != class_filtered_combined_model_results['ground_truth_emotion_one_hot_index'])
        ].count()[0]

    
    return np.array([[both_agreed_and_correct_count, text_correct_speech_wrong_count], [speech_correct_text_wrong_count, both_wrong_count]])