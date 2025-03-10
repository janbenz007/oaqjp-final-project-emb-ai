    from flask import Flask, render_template, request
    from EmotionDetection.emotion_detection import emotion_detector

    app = Flask("Emotion Detector")

    @app.route("/emotionDetector")
    
    def sent_detector():
        # Retrieve the text to analyze from the request arguments
        text_to_analyze = request.args.get('textToAnalyze')

        # Pass the text to the sentiment_analyzer function and store the response
        response = sentiment_analyzer(text_to_analyze)

        # Extract the label and score from the response
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = esponse['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']

        # Return a formatted string with the sentiment label and score
        For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy. 
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)