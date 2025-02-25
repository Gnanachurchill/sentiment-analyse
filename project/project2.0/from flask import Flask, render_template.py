from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiment_label = 'Positive'
    elif sentiment < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
    return sentiment_label, sentiment

@app.route('/')
def home():
    # Serve the HTML page
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # Perform sentiment analysis
    sentiment_label, sentiment_score = analyze_sentiment(user_input)
    
    # Generate a response based on sentiment
    if sentiment_label == 'Positive':
        bot_response = "That's great to hear!"
    elif sentiment_label == 'Negative':
        bot_response = "I'm sorry you're feeling that way."
    else:
        bot_response = "I see. Let's talk more!"

    # Return the bot response and sentiment information
    return jsonify({
        'user_input': user_input,