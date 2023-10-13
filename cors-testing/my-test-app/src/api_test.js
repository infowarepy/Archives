import React, { useState } from 'react';

const ApiTestComponent = () => {
  const [responseText, setResponseText] = useState('');
  const [errorText, setErrorText] = useState('');

  const handleFetchData = async () => {
    try {
      const requestBody = {
        "month": "august",
        "day": "21",
        "year":"1223",
        "pin": 9189,  
        "user_id": 1,  
        "test_id": 1  
    };

      const response = await fetch('https://mmse-api.onrender.com/orientation_test', {
        method: 'POST',
        headers: {
                 'Content-Type':'application/json'
                },
        body: JSON.stringify(requestBody)
      });

      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
      }

      const responseData = await response.json();
      setResponseText(JSON.stringify(responseData, null, 2));
      setErrorText('');
    } catch (error) {
      setErrorText(`Error: ${error.message}`);
      setResponseText('');
    }
  };

  return (
    <div>
      <h1>API Test</h1>
      <button onClick={handleFetchData}>Fetch Data</button>
      <pre>{responseText}</pre>
      <p style={{ color: 'red' }}>{errorText}</p>
    </div>
  );
};

export default ApiTestComponent;

