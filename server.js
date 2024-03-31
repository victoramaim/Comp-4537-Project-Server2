const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

app.use(express.json());

// CORS middleware
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

// Route to handle story generation
app.post('/generate', (req, res) => {
    const { prompt_text } = req.body;

    if (!prompt_text) {
        return res.status(400).json({ error: 'Prompt text is required' });
    }

    // Call Python script to generate story
    const pythonProcess = spawn('python', ['main.py']);

    // Pass prompt text to the Python script
    pythonProcess.stdin.write(prompt_text);
    pythonProcess.stdin.end();

    // Promise to handle the response from Python script
    const promise = new Promise((resolve, reject) => {
        let generatedStory = '';

        // Collect data from Python script
        pythonProcess.stdout.on('data', (data) => {
            generatedStory += data.toString();
        });

        // Error handling
        pythonProcess.stderr.on('data', (data) => {
            console.error(`Error from Python script: ${data}`);
        });

        // When the Python script finishes executing
        pythonProcess.on('close', () => {
            resolve(generatedStory);
        });
    });

    // Respond once the promise is resolved or rejected
    promise.then((generatedStory) => {
        res.json({ story: generatedStory });
    }).catch((error) => {
        console.error(`Error: ${error}`);
        res.status(500).json({ error });
    });
});

// Start server
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
