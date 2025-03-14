"""
Emotion Detection Page

The purpose of this web page and associated scripts is to analyze input string
for emotional characteristics.

"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    The main function that takes user input on the web page
    sends it to an API for analysis
    and returns the outcome or an error message 
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if anger is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger},"
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}."
        f"The dominant emotion is {dominant_emotion}."
        )

@app.route("/")
def render_index_page():
    """
    triggers the rendering of the page along with the input form
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
