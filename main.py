import docker
import requests
import json
import time

# Load configuration from a JSON file
def load_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

# Connect to Docker
client = docker.from_env()

# Function to send an embed message to Discord
def send_discord_embed(webhook_url, title, description, color, fields):
    embed = {
        "title": title,
        "description": description,
        "color": color,  # Embed color
        "fields": fields
    }
    payload = {
        "embeds": [embed]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code != 204:
        print(f"Failed to send message to Discord: {response.status_code}")

# Monitor Docker events
def monitor_docker_events(config):
    webhook_url = config['webhook_url']
    for event in client.events(decode=True):
        if event['Type'] == 'container':
            container_name = event['Actor']['Attributes']['name']
            action = event['Action']

            # Check if the action is in the configuration
            if action in config['events']:
                event_config = config['events'][action]
                title = event_config['title'].format(name=container_name)
                description = event_config['description'].format(name=container_name)
                color = event_config['color']

                # Prepare fields for the embed
                fields = [
                    {"name": "Event Type", "value": action, "inline": True},
                    {"name": "Timestamp", "value": f"<t:{int(time.time())}>", "inline": True}
                ]

                # Include shutdown reason if the event is 'die'
                if action == 'die':
                    # Get the exit code and reason
                    exit_code = event['Actor']['Attributes'].get('exitCode', 'Unknown')
                    reason = f"Exited with code {exit_code}"
                    fields.append({"name": "Shutdown Reason", "value": reason, "inline": False})

                # Send the embed to Discord
                send_discord_embed(webhook_url, title, description, color, fields)

if __name__ == "__main__":
    config = load_config('config.json')
    monitor_docker_events(config)
