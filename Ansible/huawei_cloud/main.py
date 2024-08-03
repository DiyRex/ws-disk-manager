import os
from modules.process_disk_info import process_disk_info
from modules.list_voluems_hc import get_volumes
from modules.extend_volume import extend_volume
from modules.parse_disk_config import parse_config
from modules.telegram_notify import send_success_telegram_message, send_fail_telegram_message, generate_message
from modules.create_yml_dataset import create_yaml_and_set_output

def main():
    src_file_path = os.getenv('SRC_FILE_PATH', './config/disk_info.yml')
    config_file_path = os.getenv('CONFIG_FILE_PATH', '../default_disk_config.ini')
    max_filled_limit = int(os.getenv('MAX_FILLED_LIMIT', 70))
    server_ip = os.getenv('SERVER_IP', '192.168.1.1')
    server_user = os.getenv('SERVER_USER', 'Admin')

    repository = os.getenv('REPOSITORY', '')
    branch = os.getenv('BRANCH', '')
    operator = os.getenv('OPERATOR', '')
    action_url = os.getenv('ACTION_URL', '')

    disk_info_list = process_disk_info(src_file_path)
    config_data = parse_config(config_file_path)

    infVal = False
    for disk_info in disk_info_list:

        filled_percentage = disk_info["Filled Percentage"]
        max_filled_limit = int(config_data['extend_volume'].get('max_filled_limit'))


        if int(filled_percentage) > max_filled_limit:
            volume_details = get_volumes(partial_volume_id=disk_info["Serial Number"])
            current_size = volume_details["size"]
            volume_id = volume_details["id"]
            volume_name = volume_details["name"]
            extend_capacity = config_data['extend_volume'].get('extend_size')
            operation_type = config_data['extend_volume'].get('operation_type')
            extend_size = int(current_size) + int(extend_capacity)
            isResized = extend_volume(volume_id=volume_id,new_size=extend_size)
            # isResized = True
            infVal = True
            if isResized:
                # send_success_telegram_message(host_ip=server_ip, username=server_user, volume_name=volume_name, volume_id=volume_id, ext_size=extend_capacity, prev_size=current_size, new_size=extend_size, repo=repository, branch=branch, triggered_by=operator, action_run_url=action_url, operation_type=operation_type)
                create_yaml_and_set_output(action_run_url=action_url, branch=branch,ext_size=extend_capacity,host_ip=server_ip,new_size=extend_size,operation_type=operation_type,prev_size=current_size,repo=repository,triggered_by=operator,username=server_user,volume_id=volume_id,volume_name=volume_name)

            else:
                send_fail_telegram_message(host_ip=server_ip, username=server_user, volume_id=volume_id, volume_name=volume_name, current_size=current_size, repo=repository, branch=branch, triggered_by=operator, action_run_url=action_url,operation_type=operation_type)

    if infVal == False:
        output_file = os.getenv('GITHUB_OUTPUT')
        if output_file:
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(f'TG_MESSAGE=No Need to extend')


if __name__ == "__main__":
    main()
