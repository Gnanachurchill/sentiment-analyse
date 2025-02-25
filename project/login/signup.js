function signup() {
    const newUsername = document.getElementById('newUsername').value;
    const newPassword = document.getElementById('newPassword').value;

    // Simulate user signup logic (e.g., storing in a database or localStorage)
    if (newUsername && newPassword) {
        // On successful signup, redirect to the sentiment analysis page
        alert('Signup successful! Redirecting to Sentiment Analysis.');
        window.location.href = 'sentiment_analysis.html';  // Redirect to your main website
    } else {
        alert('Please fill in both fields!');
    }
}
