### Required
- Chrome based browser
- Node.JS

### In Browser

- Open Developer Tools > go to console
- Paste the content of `frontend/InterceptXHRRequest.js` in the console.
- This will just print `f () {...}` the function definition
- Every time the site makes the call to c.php the request will be intercepted and the repossess posted to the local server

### In a terminal
- Navigate to `backend/`
- Run `npm install`
- Run `node listen.js`
- The server will listen to POSTs from the intercepted browser function.
- It will log and append to a CSV file the values.