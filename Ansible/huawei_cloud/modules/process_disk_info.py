import yaml

def process_disk_info(file_path):
    # Load YAML file
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    disk_info_list = []
    
    # Process each disk's information
    for disk in data.get('disks', []):
        disk_number = disk.get('disk_number')
        partition_number = disk.get('partition_number')
        drive_letter = disk.get('drive_letter')
        serial_number = disk.get('serial_number')
        size = disk.get('size')
        free = disk.get('free')
        used = disk.get('used')
        unallocated_space = disk.get('unallocated_space')

        # Extract size and free space values and convert to float
        def convert_to_gb(value):
            return float(value.replace(' GB', '').strip())

        size_gb = convert_to_gb(size)
        free_gb = convert_to_gb(free)
        used_gb = convert_to_gb(used)
        unallocated_space_gb = convert_to_gb(unallocated_space)

        # Calculate filled percentage
        total_used = used_gb
        total_size = size_gb
        filled_percentage = (total_used / total_size) * 100 if total_size > 0 else 0

        disk_info = {
            "Disk Number": disk_number,
            "Partition Number": partition_number,
            "Drive Letter": drive_letter,
            "Serial Number": serial_number,
            "Size": size,
            "Free": free,
            "Used": used,
            "Unallocated Space": unallocated_space,
            "Filled Percentage": filled_percentage
        }
        
        # if filled_percentage > 20:
        #     disk_info["Warning"] = "Disk usage exceeds 90%"

        disk_info_list.append(disk_info)

    return disk_info_list
