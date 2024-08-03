import argparse
import yaml
import requests
import os

def format_message(data):
    return f"""
    💻 SAP Server Disk Management Complete!

    ⚙️ Operation   : {data['operation_type']}
    📡 Server-IP   : {data['host_ip']}
    🧑‍💻 Username    : {data['username']}
    🗂️ Volume Name : {data['volume_name']}
    🆔 Volume ID   : {data['volume_id']}
    📏 Prev Size   : {data['prev_size']}
    📏 New Size    : {data['new_size']}
    📏 Ext Size    : {data['ext_size']}
    📁 Repository  : {data['repo']}
    🌲 Branch/Tag  : {data['branch']}
    👤 Operator    : {data['triggered_by']}

    🔍 [View Action Run]({data['action_run_url']})
    """

def send_tg_message(message):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if bot_token is None or chat_id is None:
        raise ValueError("Telegram bot token and chat ID must be set in the environment variables.")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
    
    print("Message sent successfully!")

def main():
    parser = argparse.ArgumentParser(description='Send a message to Telegram.')
    parser.add_argument('-m', '--message', required=True, help='The YAML message to send.')
    
    args = parser.parse_args()
    
    # Load YAML data from command-line argument
    yaml_data = args.message
    
    # Unescape newlines
    yaml_data = yaml_data.replace('\\n', '\n')
    
    # Load the YAML data
    data = yaml.safe_load(yaml_data)
    
    # Format the message using the template
    try:
        formatted_message = format_message(data)
    except:
        formatted_message = yaml_data
    # Send the formatted message to Telegram
    send_tg_message(formatted_message)

if __name__ == '__main__':
    main()
