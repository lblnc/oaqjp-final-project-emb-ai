"""
using IBM's watson AI tool to generate emotion detection from user string
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def render_index():
    """
    render index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def em_detector():
    """
    run emotion detector on provided string
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        result = "Invalid text! Please try again!"
    else:
        result = f"For the given statement, the system response is\
                'anger': {response['anger']},\
                'disgust': {response['disgust']},\
                'fear': {response['fear']},\
                'joy': {response['joy']},\
                'sadness': {response['sadness']}. \
                The dominant emotion is {response['dominant_emotion']}."
    return result

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
