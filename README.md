# ewn-box-opener

Box Opener client for mining EWN tokens.

## How to run

There are two ways to run the the Box Opener:

### 1. Docker (recommended)

The easiest way to run the Box Opener is to use Docker. [Find out more on how to run with Docker](https://docs.erwin.lol/docs/box-openers/box-opener-node).

### 2. Deploy with balena

If you want to run this on a device like a Raspberry Pi, Orange Pi or other single board computer, you can run this app using balenaCloud for free.

Simply click the "Deploy with balena" button below (you will need to create an account if you haven't already got one):

[![Deploy with button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/Erwin-Schrodinger-Token/ewn-box-opener&defaultDeviceType=raspberrypi4-64)

You will then need to add a `Device Variable` with the name `API_KEY` and the value set to the API key you got from the [Fetch Your API Key](https://docs.erwin.lol/docs/box-openers/box-opener-node/#fetch-your-api-key) section of the docs.

### 3. Standalone (advanced)

Another way to run the Box Opener is to run the Python script standalone. Docs will follow.
