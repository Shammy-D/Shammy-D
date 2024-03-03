async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatDisplay = document.getElementById('chat-display');
    
    // Display user message
    chatDisplay.innerHTML += `<div>User: ${userInput}</div>`;
    
    // Send user message to ChatGPT
    const response = await openai.complete({
        engine: 'text-davinci-003', // Use the desired GPT model
        prompt: userInput,
        maxTokens: 150 // Adjust as needed
    });
    
    // Display ChatGPT response
    chatDisplay.innerHTML += `<div>ChatGPT: ${response.choices[0].text.trim()}</div>`;
}
