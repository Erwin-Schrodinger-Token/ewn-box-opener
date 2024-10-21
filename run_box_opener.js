const axios = require('axios');
const bip39 = require('bip39');
require('dotenv').config();

const DEVNET_API_KEY = process.env.DEVNET_API_KEY || "none";
const API_URL = process.env.API_URL || "https://api.erwin.lol";
const API_KEY = DEVNET_API_KEY !== "none" ? DEVNET_API_KEY : process.env.API_KEY;

async function submitGuesses() {
    const passwords = [];
    for (let x = 0; x < 50; x++) {
        passwords.push(bip39.generateMnemonic());
    }

    console.info(`🔑️ Generated ${passwords.length} guesses`);
    console.info("➡️ Submitting to oracle");

    const url = `${API_URL}/submit_guesses`;
    const headers = {
        "x-api-key": API_KEY,
        "content-type": "application/json"
    };

    return await axios.post(url, {
        json: passwords,
        headers: headers,
        timeout: 60000
    }).then(resp => {
        if (resp.status === 202) {
            console.info("✅ Guesses accepted");
            return false;
        }
    }).catch(err => {
        if (err.response.status === 401) {
            console.error(`❌ Guesses rejected (${err.response.status}): Unauthorized,Please check your API key`);
            return false;
        } else if (err.response.status === 404) {
            console.error(`❌ Guesses rejected (${err.response.status}): ${err.response.data}`);
            return false;
        } else if (err.response.status === 500) {
            console.error(`❌ Guesses rejected (${err.response.status}): Internal Server Error`);
            return false;
        } else if (err.response.status === 502) {
            console.error(`❌ Guesses rejected (${err.response.status}): Bad Gateway`);
            return false;
        } else if (err.response.status === 530) {
            console.error(`❌ Guesses rejected (${err.response.status}): Argo Tunnel Error`);
            return false;
        } else {
            console.error(`❌ Guesses rejected (${err.response.status}): Unspecified Error`);
            return true;
        }
    });
}

function doLoop() {
    let sleepTime = 10;
    setInterval(() => {
        console.log("⚙️ Generating guesses");
        submitGuesses().then(rateLimited => {
            if (rateLimited) {
                sleepTime += 10;
            } else {
                sleepTime -= 1;
            }
        }).catch(err => {
            console.error(`⚠️ Error occurred: ${err}`);
        });

        if (sleepTime < 10) {
            sleepTime = 10;
        }

        setTimeout(() => {}, sleepTime * 1000);
    }, sleepTime * 1000);
}

if (require.main === module) {
    if (!API_KEY) {
        console.error("⚠️ API Key not defined, set API_KEY environment variable");
    } else {
        doLoop();
    }
}
