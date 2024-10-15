import logging
import time
import os
import requests
from pybip39 import Mnemonic
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
DEVNET_API_KEY = os.environ.get("DEVNET_API_KEY", "none")
API_URL = os.environ.get("API_URL", "https://api.erwin.lol")

if DEVNET_API_KEY != "none":
    API_KEY = DEVNET_API_KEY
else:
    API_KEY = os.environ.get("API_KEY")


def submit_guesses():
    passwords = []

    for x in range(0, 50):
        passwords.append(Mnemonic().phrase)

    logging.info("🔑️ Generated %s guesses" % len(passwords))
    logging.info("➡️ Submitting to oracle")

    url = f"{API_URL}/submit_guesses"
    headers = {
        "x-api-key": API_KEY,
        "content-type": "application/json"
    }
    resp = requests.post(
        url,
        json=passwords,
        headers=headers,
        timeout=60
    )

    if resp.status_code == 202:
        logging.info("✅ Guesses accepted")
        return False
    if resp.status_code == 404:
        logging.info(
            f"❌ Guesses rejected ({resp.status_code}): {resp.text}"
        )
        return False
    else:
    if resp.status_code == 502:
        logging.info(
            f"❌ Guesses rejected ({resp.status_code}): Bad Gateway"
        )
        return False
    else:
        logging.info(
            f"❌ Guesses rejected ({resp.status_code}): {resp.text}"
        )
        return True


def do_loop():
    sleep_time = 10
    while True:
        logging.info("⚙️ Generating guesses")
        try:
            rate_limited = submit_guesses()
            if rate_limited:
                sleep_time += 10
            else:
                sleep_time -= 1
        except Exception as err:
            logging.error(f"⚠️ Error occurred: {str(err)}")

        if sleep_time < 10:
            sleep_time = 10

        time.sleep(sleep_time)


if __name__ == "__main__":
    if not API_KEY:
        logging.error(
            "⚠️ API Key not defined, "
            "set API_KEY environment variable"
        )
    else:
        do_loop()
