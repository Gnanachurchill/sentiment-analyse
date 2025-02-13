function analyzeSentiment() {
  var text = document.getElementById('textInput').value;
  var resultDiv = document.getElementById('result');
  var sentimentResult = document.getElementById('sentimentResult');

  if (!text.trim()) {
      resultDiv.style.display = 'none';
      alert("Please enter some text for analysis.");
      return;
  }

  // Example API call
  fetch('https://api.example.com/analyze', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer YOUR_API_KEY'
      },
      body: JSON.stringify({ text: text })
  })
  .then(response => response.json())
  .then(data => {
      var sentiment = data.sentiment || 'Neutral';
      sentimentResult.textContent = sentiment;

      if (sentiment === 'Positive') {
          sentimentResult.style.color = 'green';
      } else if (sentiment === 'Negative') {
          sentimentResult.style.color = 'red';
      } else {
          sentimentResult.style.color = 'gray';
      }

      resultDiv.style.display = 'block';
  })
  .catch(error => {
      console.error('Error:', error);
      resultDiv.innerHTML = `<p>There was an error processing your request. Please try again later.</p>`;
      resultDiv.style.display = 'block';
  });
}
