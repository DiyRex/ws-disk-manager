import os
import yaml

def create_yaml_and_set_output(operation_type, host_ip, username, volume_name, volume_id, prev_size, new_size, ext_size, repo, branch, triggered_by, action_run_url):
    # Create a dictionary with the data
    data = {
        'operation_type': operation_type,
        'host_ip': host_ip,
        'username': username,
        'volume_name': volume_name,
        'volume_id': volume_id,
        'prev_size': prev_size,
        'new_size': new_size,
        'ext_size': ext_size,
        'repo': repo,
        'branch': branch,
        'triggered_by': triggered_by,
        'action_run_url': action_run_url
    }

    # Convert the dictionary to a YAML formatted string
    yaml_data = yaml.dump(data, default_flow_style=False)
    escaped_yaml_data = yaml_data.replace('\n', '\\n').replace('\r', '')

    # Write the YAML data to a file
    output_file = os.getenv('GITHUB_OUTPUT')
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f'TG_MESSAGE={escaped_yaml_data}\n')