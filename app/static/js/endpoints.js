document.getElementById('talkForm').onsubmit = function(event) {
    event.preventDefault();
    const userInput = document.getElementById('userInput').value;
    const responseElement = document.getElementById('response');
    
    function fetchResponse(userInput) {
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: userInput })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else if (response.status === 202) {
                // If status code is 202, retry after 2 seconds
                setTimeout(() => fetchResponse(userInput), 2000);
                responseElement.innerText = "Processing your request...";
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            if (data && data.choices && data.choices.length > 0) {
                responseElement.innerText = data.choices[0].text;
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Initial fetch
    fetchResponse(userInput);
};
