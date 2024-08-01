import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 400:
        emotion = {key: None for key in ['anger', 'disgust','fear','joy','sadness','dominant_emotion']}
    else:
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dominant_score = max(emotion.values())
        for key, value in emotion.items():
            if value == dominant_score:
                emotion['dominant_emotion'] = key
                break
    return emotion
