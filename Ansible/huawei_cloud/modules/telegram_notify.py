import os
import requests

def send_success_telegram_message(host_ip, username, repo, branch, triggered_by, action_run_url, volume_name, volume_id, prev_size, new_size, ext_size, operation_type):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    message = f"""
    💻 SAP Server Disk Management Complete!

    ⚙️ Operation   : {operation_type}
    📡 Server-IP   : {host_ip}
    🧑‍💻 Username    : {username}
    🗂️ Volume Name : {volume_name}
    🆔 Volume ID   : {volume_id}
    📏 Prev Size   : {prev_size} GB
    📏 New Size    : {new_size} GB
    📏 Ext Size    : {ext_size} GB
    📁 Repository  : {repo}
    🌲 Branch/Tag  : {branch}
    👤 Operator    : {triggered_by}

    🔍 [View Action Run]({action_run_url})
    """

    
    if bot_token is None or chat_id is None:
        raise ValueError("Telegram bot token and chat ID must be set in the environment variables.")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode':'Markdown'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
    
    print("Message sent successfully!")

def send_fail_telegram_message(host_ip, username, repo, branch, volume_name, triggered_by, action_run_url, volume_id, current_size, operation_type):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    message = f"""
💻 SAP Server Disk Management Failed!

⚙️ Operation   : {operation_type}
📡 Server-IP   : {host_ip}
🧑‍💻 Username    : {username}
🗂️ Volume Name : {volume_name}
🆔 Volume ID   : {volume_id}
📏 Prev Size   : {current_size} GB
📁 Repository  : {repo}
🌲 Branch/Tag  : {branch}
👤 Operator    : {triggered_by}

🔍 [View Action Run]({action_run_url})
"""
    
    if bot_token is None or chat_id is None:
        raise ValueError("Telegram bot token and chat ID must be set in the environment variables.")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode':'Markdown'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
    
    print("Message sent successfully!")


# Generate Message
def generate_message(host_ip, username, repo, branch, triggered_by, action_run_url, volume_name, volume_id, prev_size, new_size, ext_size, operation_type):
    message = f"""
    💻 SAP Server Disk Management Complete!

    ⚙️ Operation   : {operation_type}
    📡 Server-IP   : {host_ip}
    🧑‍💻 Username    : {username}
    🗂️ Volume Name : {volume_name}
    🆔 Volume ID   : {volume_id}
    📏 Prev Size   : {prev_size} GB
    📏 New Size    : {new_size} GB
    📏 Ext Size    : {ext_size} GB
    📁 Repository  : {repo}
    🌲 Branch/Tag  : {branch}
    👤 Operator    : {triggered_by}

    🔍 [View Action Run]({action_run_url})
    """

    return message

# send message
def send_tg_message(message):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if bot_token is None or chat_id is None:
        raise ValueError("Telegram bot token and chat ID must be set in the environment variables.")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode':'Markdown'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
    
    print("Message sent successfully!")