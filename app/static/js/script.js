document.getElementById('talkForm').onsubmit = function(event) {
    event.preventDefault();
    const userInput = document.getElementById('userInput').value;
    
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.choices[0].text;
    })
    .catch(error => console.error('Error:', error));
};
