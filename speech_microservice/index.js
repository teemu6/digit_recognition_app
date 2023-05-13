require("dotenv").config();
const express = require("express");
const cors = require("cors");
const {
  SpeechSynthesizer,
  SpeechConfig,
  AudioConfig,
} = require("microsoft-cognitiveservices-speech-sdk");

const app = express();
app.use(cors());
app.use(express.json());

const subscriptionKey = process.env.AZURE_ACCESS_KEY;
const region = process.env.AZURE_LOCATION;
const port = 5007;

app.post("/text-to-speech", (req, res) => {
  const { languageCode, text } = req.body;

  const speechConfig = SpeechConfig.fromSubscription(subscriptionKey, region);
  speechConfig.speechSynthesisLanguage = languageCode;
  speechConfig.speechSynthesisOutputFormat = "audio-16khz-128kbitrate-mono-mp3";

  const synthesizer = new SpeechSynthesizer(
    speechConfig,
    AudioConfig.fromDefaultSpeakerOutput()
  );

  let audioData = [];

  synthesizer.speakTextAsync(text, (result) => {
    if (result.errorDetails) {
      console.error(result.errorDetails);
      res.status(500).send("Error synthesizing audio");
    } else {
      audioData = result.audioData;
      const base64AudioData = Buffer.from(audioData).toString("base64");
      res.set("Content-Type", "application/json");
      res.send({ audio: base64AudioData });
    }
  });
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
