
def print_classification_report(classification_report):
    # Extract the classification report data for each emotion
    neutral_precision = classification_report['neutral']['precision']
    neutral_recall = classification_report['neutral']['recall']
    neutral_f1_score = classification_report['neutral']['f1-score']
    neutral_support = classification_report['neutral']['support']

    surprise_precision = classification_report['surprise']['precision']
    surprise_recall = classification_report['surprise']['recall']
    surprise_f1_score = classification_report['surprise']['f1-score']
    surprise_support = classification_report['surprise']['support']

    fear_precision = classification_report['fear']['precision']
    fear_recall = classification_report['fear']['recall']
    fear_f1_score = classification_report['fear']['f1-score']
    fear_support = classification_report['fear']['support']

    sadness_precision = classification_report['sadness']['precision']
    sadness_recall = classification_report['sadness']['recall']
    sadness_f1_score = classification_report['sadness']['f1-score']
    sadness_support = classification_report['sadness']['support']

    joy_precision = classification_report['joy']['precision']
    joy_recall = classification_report['joy']['recall']
    joy_f1_score = classification_report['joy']['f1-score']
    joy_support = classification_report['joy']['support']

    disgust_precision = classification_report['disgust']['precision']
    disgust_recall = classification_report['disgust']['recall']
    disgust_f1_score = classification_report['disgust']['f1-score']
    disgust_support = classification_report['disgust']['support']

    anger_precision = classification_report['anger']['precision']
    anger_recall = classification_report['anger']['recall']
    anger_f1_score = classification_report['anger']['f1-score']
    anger_support = classification_report['anger']['support']

    # Print the classification report
    print('Neutral')
    print('------------------------------------')
    print(f'precision: {neutral_precision}')
    print(f'recall: {neutral_recall}')
    print(f'f1-score: {neutral_f1_score}')
    print(f'support: {neutral_support}')
    print()

    print('Surprise:')
    print('------------------------------------')
    print(f'precision: {surprise_precision}')
    print(f'recall: {surprise_recall}')
    print(f'f1-score: {surprise_f1_score}')
    print(f'support: {surprise_support}')
    print()

    print('Fear:')
    print('------------------------------------')
    print(f'precision: {fear_precision}')
    print(f'recall: {fear_recall}')
    print(f'f1-score: {fear_f1_score}')
    print(f'support: {fear_support}')
    print()

    print('Sadness:')
    print('------------------------------------')
    print(f'precision: {sadness_precision}')
    print(f'recall: {sadness_recall}')
    print(f'f1-score: {sadness_f1_score}')
    print(f'support: {sadness_support}')
    print()

    print('Joy:')
    print('------------------------------------')
    print(f'precision: {joy_precision}')
    print(f'recall: {joy_recall}')
    print(f'f1-score: {joy_f1_score}')
    print(f'support: {joy_support}')
    print()

    print('Disgust:')
    print('------------------------------------')
    print(f'precision: {disgust_precision}')
    print(f'recall: {disgust_recall}')
    print(f'f1-score: {disgust_f1_score}')
    print(f'support: {disgust_support}')
    print()

    print('Anger:')
    print('------------------------------------')
    print(f'precision: {anger_precision}')
    print(f'recall: {anger_recall}')
    print(f'f1-score: {anger_f1_score}')
    print(f'support: {anger_support}')
    print()   