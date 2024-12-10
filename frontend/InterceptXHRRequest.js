// Save the original XMLHttpRequest open and send methods
const originalOpen = XMLHttpRequest.prototype.open;
const originalSend = XMLHttpRequest.prototype.send;

// Override the open method to capture the request details
XMLHttpRequest.prototype.open = function (method, url) {
  this._method = method; // Store the method
  this._url = url; // Store the URL
  return originalOpen.apply(this, arguments);
};

// Override the send method to capture the response
XMLHttpRequest.prototype.send = function () {
  // Check if it's a GET request and match the specific URL
  if (this._method === 'GET' && this._url === 'c.php') {
    console.log('Intercepted GET XMLHttpRequest to:', this._url); // Log the URL
    
    // Add an event listener for when the request is complete
    this.addEventListener('load', function () {
      console.log('Response:', this.responseText); // Log the response data

      // Send the response data to your local server (localhost)
      fetch('http://localhost:3000/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: this.responseText, // Send the response data as JSON
      })
      .then(serverResponse => serverResponse.json())
      .then(serverData => {
        console.log('Server response:', serverData); // Log the server response
      })
      .catch(error => {
        console.error('Error sending data to local server:', error);
      });
    });
  }

  // Call the original send method to actually send the request
  return originalSend.apply(this, arguments);
};