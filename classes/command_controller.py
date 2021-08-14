import json
import os

from termcolor import colored


class CommandController:
    def __init__(self):
        self.command = ''


    def replace_placeholder(self, placeholder = {}, template = ''):
        generated_script = template
        for key in placeholder:
           generated_script = generated_script.replace(f'##{key}##', placeholder[key])
        return generated_script


    def generate_standard_script(self, directory_name: str, key: str):        
        with open('templates/standard_template.txt', 'r') as file_template:
            template = file_template.read()

        placeholder = {}
        with open('configuration/template_config.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            try:
                placeholder['table_name'] = str(json_data[key]['table_name'])
                placeholder['btq_of_origin'] = str(json_data[key]['btq_of_origin'])
                placeholder['central_one_to_many'] = str(json_data[key]['central_one_to_many'])
                placeholder['external_key'] = str(json_data[key]['external_key'])
                placeholder['pool_language'] = str(json_data[key]['pool_language'])
                
            except KeyError:
                print(colored(f'Key: {key} not found', 'red'))

        #generated_script = self.replace_placeholder(placeholder, template)
        
        #os.makedirs(f'output/{directory_name}')
        #with open(f'output/{directory_name}/standard_script_{key}.sql', 'w') as f:
        #    f.write(generated_script)


    def generate_europe_script(self):
        pass


    def fr(self):
        print(colored('Generating script for FR...', 'yellow'))
        self.generate_standard_script('FR', 'FR')
        print(colored('Done', 'yellow'))


    def uk(self):
        print(colored('Generating script for UK...', 'yellow'))
        self.generate_standard_script('UK', 'UK')
        print(colored('Done', 'yellow'))


    def do_command(self, command):
        command_method = getattr(self, command.method.__name__)
        if command_method:
            command_method()