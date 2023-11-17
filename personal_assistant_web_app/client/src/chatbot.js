import React, { useState } from 'react';
import './css/chatbot.css';

// Import user and AI profile images
import userImage from './resources/user.png';
import aiImage from './resources/ai.png';

const Chatbot = () => {
  const [userMessage, setUserMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  const handleUserMessageChange = (e) => {
    setUserMessage(e.target.value);
  };

  const handleSendMessage = async () => {
    // Send user message to the Python backend
    const response = await fetch('http://localhost:5000/chatbot', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ userMessage }),
    });

    // Parse and get the bot response
    const data = await response.json();
    const botResponse = data.botResponse;

    console.log(data)

    // Update chat history
    setChatHistory((prevHistory) => [
      ...prevHistory,
      { type: 'user', message: userMessage, image: userImage },
      { type: 'bot', message: botResponse, image: aiImage},
    ]);

    // Clear the input field after sending the message
    setUserMessage('');
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-messages">
        {/* Display chat history */}
        {chatHistory.map((message, index) => (
          
          <div key={index} className={message.type === 'user' ? 'user-msg-container' : 'bot-msg-container'}>
            {message.type === 'bot' && (
                <img src={message.image} alt={message.type} className="bot-image" />
            )}
            
            <div className={message.type === 'user' ? 'user-message' : 'bot-response'}>
              {message.message}
            </div>

            {message.type === 'user' && (
              <img src={message.image} alt={message.type} className="user-image" />
            )}
            
          </div>
        ))}
      </div>

      {/* Input field for user message */}
      <div className="chatbot-input">
        <input
          type="text"
          placeholder="Type a message..."
          value={userMessage}
          onChange={handleUserMessageChange}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
