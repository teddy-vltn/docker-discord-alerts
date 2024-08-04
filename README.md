
# Docker Discord Notifier

Monitor your Docker containers effortlessly and receive real-time alerts in Discord with rich, customizable embeds. This project leverages Docker Compose to run the monitoring script as a continuous service, ensuring you stay informed on container events such as start, stop, restart, and failures.

## Features

- **Real-Time Monitoring**: Listens for Docker container events (`start`, `restart`, `stop`, `die`).
- **Discord Notifications**: Sends event alerts to a Discord channel using webhooks.
- **Rich Embeds**: Includes detailed information with fields for event type, timestamp, and shutdown reasons.
- **Configurable**: Easily customize alerts using a JSON configuration file.
- **Dockerized**: Run the script as a background service using Docker Compose.

## Prerequisites

- Docker and Docker Compose installed on your system.
- A Discord account and a webhook URL from your server.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/docker-discord-monitor.git
   cd docker-discord-monitor
   ```

2. **Set Up the Configuration File**

   Create a `config.json` file in the project directory, or modify the provided example:

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

1. **Build and Start the Service**

   Use Docker Compose to build and start the service in the background:

   ```bash
   docker-compose up -d
   ```

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

- Ensure Docker and Docker Compose are running correctly.
- Verify that the Discord webhook URL is correct and active.
- Check for any errors in the container logs:

  ```bash
  docker logs docker-discord-monitor
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
