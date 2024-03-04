const OpenAI2 = new OpenAI2('apikey');
// Initialize OpenAI API


// Function to send message to ChatGPT
async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatDisplay = document.getElementById('chat-display');
    
    // Display user message
    chatDisplay.innerHTML += `<div>User: ${userInput}</div>`;
    
    // Send user message to ChatGPT
    const response = await OpenAI2.complete({
        engine: 'text-davinci-003', // Use the desired GPT model
        prompt: userInput,
        maxTokens: 150 // Adjust as needed
    });
    
    // Display ChatGPT response
    chatDisplay.innerHTML += `<div>ChatGPT: ${response.choices[0].text.trim()}</div>`;
}

// You can include other functions or code related to your chat interface here
// For example, functions to handle UI events, initialize the chat interface, etc.

