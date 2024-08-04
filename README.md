
# Docker Container Monitoring with Discord Notifications

This script monitors Docker container events and sends notifications to a Discord channel using embeds. It tracks events such as container start, restart, stop, and termination, providing detailed information in each notification.

## Features

- **Monitors Docker Events**: Listens for Docker container events (`start`, `restart`, `stop`, `die`).
- **Discord Integration**: Sends event notifications to a Discord channel using webhooks.
- **Rich Embeds**: Notifications include detailed embeds with fields for event type, timestamp, and shutdown reasons.
- **Configurable**: Uses a JSON configuration file for easy customization.

## Prerequisites

- Docker installed and running.
- Python 3.x installed.
- Discord account and a webhook URL from your server.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/docker-discord-monitor.git
   cd docker-discord-monitor
   ```

2. **Install Required Python Packages**

   Use `pip` to install the Docker SDK for Python:

   ```bash
   pip install docker
   ```

3. **Set Up the Configuration File**

   Create a `config.json` file in the same directory as your script, or modify the provided example:

   ```json
   {
     "webhook_url": "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN",
     "events": {
       "start": {
         "title": "🚀 Container Started: {name}",
         "description": "The container '{name}' has started successfully.",
         "color": 3066993
       },
       "restart": {
         "title": "🔄 Container Restarted: {name}",
         "description": "The container '{name}' has been restarted.",
         "color": 15844367
       },
       "stop": {
         "title": "🛑 Container Stopped: {name}",
         "description": "The container '{name}' has been stopped.",
         "color": 15158332
       },
       "die": {
         "title": "💀 Container Died: {name}",
         "description": "The container '{name}' has stopped working.",
         "color": 10038562
       }
     }
   }
   ```

   Replace `"YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"` with your actual Discord webhook URL.

## Usage

1. **Run the Script**

   Execute the script using Python:

   ```bash
   python monitor.py
   ```

   Replace `monitor.py` with the name of your script file if different.

2. **Trigger Docker Events**

   Start, stop, or restart Docker containers to trigger notifications:

   ```bash
   docker start your_container_name
   docker stop your_container_name
   docker restart your_container_name
   ```

3. **Check Discord**

   Notifications will appear in the designated Discord channel with details about each container event.

## Customization

- **Modify Embed Messages**: Edit the `config.json` file to change the titles, descriptions, and colors of the embed messages.

- **Add More Events**: Extend the script to handle additional Docker events by updating the `config.json` and modifying the script logic.

## Troubleshooting

- Ensure Docker is running and the Python Docker SDK is installed.
- Verify that the Discord webhook URL is correct and active.
- Check for any errors in the script output or console for troubleshooting.
