# Around the world in eighty days! 🌎

## Overview

Our application consists of three components:
- backend
- frontend
- updater

Based on the most recent energy data, the backend calculates the datacenter with the currently highest share of green energy available. The frontend accesses the information of the backend and displays it in a human-understandable way.

In the best case we wouldn't need the updater. It just exists, since we can't get the API-key of the ENTSO-E live-API on the weekend and therefore it simulates getting live data.

## Setup

Please follow following steps to get the application running:

1. [Have poetry installed](https://python-poetry.org/docs/#installation).
2. Install dependencies and select the environment:
   ```console
   $ poetry install
   $ poetry shell
   ```
3. Start the webserver:
   ```console
   $ uvicorn main:app
   ```
4. And in another terminal start the updater:
   ```console
   $ python updater.py
   ```
5. Open [`frontend/index.html`](frontend/index.html) in your browser.

And that is already it. Enjoy!
