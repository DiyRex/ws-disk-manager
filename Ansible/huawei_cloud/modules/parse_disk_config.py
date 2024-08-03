import configparser

def parse_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    
    # Convert ConfigParser to a dictionary
    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config.items(section))
    
    return config_dict