// Select the target element
const targetElement = document.getElementById('counternumber');

// Define the server URL
const serverUrl = 'http://localhost:3000/update';

// Function to send data to the server
function postToServer(data) {
    fetch(serverUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: data }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        console.log("Update sent successfully:", data);
    })
    .catch(error => {
        console.error("Failed to send update:", error);
    });
}

// Store the last known textContent
let lastKnownContent = targetElement.textContent.trim();

// Callback function to execute when mutations are observed
const observerCallback = (mutationsList) => {
    for (const mutation of mutationsList) {
        if (mutation.type === 'characterData' || mutation.type === 'childList') {
            // Get the updated textContent
            const currentContent = targetElement.textContent.trim();

            // Compare with the last known content
            if (currentContent !== lastKnownContent) {
                console.log("Detected change:", currentContent);

                // Update the last known content
                lastKnownContent = currentContent;

                // Post the updated value to the server
                postToServer(currentContent.replace(/,/g, ''));
            }
        }
    }
};

// Create a MutationObserver instance
const observer = new MutationObserver(observerCallback);

// Configure the observer
observer.observe(targetElement, {
    characterData: true, // Observe changes to text content
    childList: true,     // Observe changes to children
    subtree: true,       // Observe descendants
});
