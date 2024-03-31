const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json());

// Allow all origins
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

app.post('/generate', (req, res) => {
    let text = req.body.text;

    // Call Python script to make prediction
    const pythonProcess = spawn('python', ['main.py']);

    // Pass the text to the Python script
    pythonProcess.stdin.write(text);
    pythonProcess.stdin.end();

    // Promise to handle the response from Python script
    const promise = new Promise((resolve, reject) => {
        let generatedText = '';

        // Collect data from Python script
        pythonProcess.stdout.on('data', (data) => {
            generatedText += data.toString();
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`Error from Python script: ${data}`);
            reject('An error occurred while making prediction');
        });

        // When the Python script finishes executing
        pythonProcess.on('close', () => {
            resolve(generatedText);
        });
    });

    // Respond once the promise is resolved or rejected
    promise.then((generatedText) => {
        res.json({ prediction: generatedText });
    }).catch((error) => {
        console.error(`Error: ${error}`);
        res.status(500).json({ error });
    });
});


app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
