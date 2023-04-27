require("dotenv").config();
const express = require("express");
const axios = require("axios").default;
const { v4: uuidv4 } = require("uuid");
const numberConvert = require("number-to-words");

const app = express();
const port = 3000;

const azureKey = process.env.AZURE_ACCESS_KEY;
const azureEndpoint = process.env.AZURE_ENDPOINT;
const azureLocation = process.env.AZURE_LOCATION;

// Endpoint to translate a number to the specified language code
// Use example: http://localhost:3000/translate?number=123&langCode=fr
app.get("/translate", async (req, res) => {
  const { number, langCode } = req.query;

  // Convert the number to English word format
  const englishWord = numberConvert.toWords(Number(number));

  // Call the Azure Cognitive Service Translator API to translate the English word to the specified language code
  try {
    const response = await axios({
      baseURL: azureEndpoint,
      url: "/translate",
      method: "post",
      headers: {
        "Ocp-Apim-Subscription-Key": azureKey,
        "Ocp-Apim-Subscription-Region": azureLocation,
        "Content-type": "application/json",
        "X-ClientTraceId": uuidv4().toString(),
      },
      params: {
        "api-version": "3.0",
        from: "en",
        to: [langCode],
      },
      data: [
        {
          text: englishWord,
        },
      ],
      responseType: "json",
    });

    // Return the translated text as the API response
    const translatedText = response.data[0].translations[0].text;
    res.send(translatedText);
  } catch (error) {
    console.error(error);
    res.status(500).send("Internal server error");
  }
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
