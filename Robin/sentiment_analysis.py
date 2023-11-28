from transformers import pipeline

text_to_classify = 'I love using transformers. The best part is wide range of support and its easy to use'
classifier_model = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', top_k=None)

prediction_of_classifier = classifier_model(text_to_classify)

result_prediction_rounded = {item['label']: round(item['score'], 5) for item in prediction_of_classifier[0]}

print('Result:', result_prediction_rounded)