const axios = require('axios');
const fs = require('fs');

// ElevenLabs API Configuration
const API_KEY = process.env.ELEVENLABS_API_KEY || 'your_api_key_here';
const VOICE_ID = 'your_preferred_voice_id'; // You can find this in ElevenLabs dashboard

async function textToSpeech(text, outputPath = 'output.mp3') {
    try {
        // API endpoint for text-to-speech
        const url = `https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`;

        // Request payload
        const payload = {
            text: text,
            model_id: "eleven_monolingual_v1", // Default model
            voice_settings: {
                stability: 0.5,
                similarity_boost: 0.5
            }
        };

        // Make the API call
        const response = await axios.post(url, payload, {
            headers: {
                'Accept': 'audio/mpeg',
                'Content-Type': 'application/json',
                'xi-api-key': API_KEY
            },
            responseType: 'arraybuffer' // Important for binary audio data
        });

        // Save the audio file
        fs.writeFileSync(outputPath, response.data);
        
        console.log(`Audio saved to ${outputPath}`);
        return outputPath;
    } catch (error) {
        console.error('Error in text-to-speech conversion:', error.response ? error.response.data : error.message);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        const text = "Hello! This is a test of ElevenLabs text-to-speech API.";
        await textToSpeech(text);
    } catch (error) {
        console.error('Failed to generate speech:', error);
    }
}

// Run the main function
main();
