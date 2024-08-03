import os
import sys
import subprocess
from ansible.module_utils.basic import AnsibleModule

def run_main_script():
    # Log the execution of the main script
    result = subprocess.run(
        [sys.executable, 'huawei_cloud/main.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result

def run_module():
    module_args = dict(
        src_file_path=dict(type='str', required=True),
        config_file_path=dict(type='str', required=True),
        server_ip=dict(type='str', required=True),
        server_user=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Extract parameters from the module
    src_file_path = module.params['src_file_path']
    config_file_path = module.params['config_file_path']
    server_ip = module.params['server_ip']
    server_user = module.params['server_user']

    # Set environment variables
    os.environ['SRC_FILE_PATH'] = src_file_path
    os.environ['CONFIG_FILE_PATH'] = config_file_path
    os.environ['SERVER_IP'] = server_ip
    os.environ['SERVER_USER'] = server_user
    
    # Environment variables for external services
    os.environ['TELEGRAM_BOT_TOKEN'] = os.getenv('TELEGRAM_BOT_TOKEN', '')
    os.environ['TELEGRAM_CHAT_ID'] = os.getenv('TELEGRAM_CHAT_ID', '')
    os.environ['HUAWEICLOUD_SDK_AK'] = os.getenv('HUAWEICLOUD_SDK_AK', '')
    os.environ['HUAWEICLOUD_SDK_SK'] = os.getenv('HUAWEICLOUD_SDK_SK', '')
    os.environ['REGION'] = os.getenv('REGION', '')
    os.environ['REPOSITORY'] = os.getenv('REPOSITORY', '')
    os.environ['BRANCH'] = os.getenv('BRANCH', '')
    os.environ['OPERATOR'] = os.getenv('OPERATOR', '')
    os.environ['ACTION_URL'] = os.getenv('ACTION_URL', '')

    # Run the Python script
    process = run_main_script()

    if process.returncode != 0:
        module.fail_json(msg=process.stderr.decode('utf-8'), **result)
    else:
        result['changed'] = True
        result['message'] = process.stdout.decode('utf-8')

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
