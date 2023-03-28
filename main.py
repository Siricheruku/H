import configparser
from hello1 import read_file

config = configparser.ConfigParser()
config.read('config.ini')

source_filename = config['source_file']['name']
destination_filename = config['destination_file']['name']

source_content = read_file(source_filename)
with open(destination_filename, 'w') as file:
    file.write(source_content)
