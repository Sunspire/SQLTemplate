import json
import os


class CommandController:
    def __init__(self):
        self.market = ''


    def replace_placeholder(self, placeholder = {}, template = '', key = ''):
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
                placeholder['btq_of_origin'] = ', '.join(map(lambda x: "'" + x.strip() + "'", str(json_data[key]['btq_of_origin']).split(',')))
                placeholder['central_one_to_many'] = str(json_data[key]['central_one_to_many'])
                placeholder['external_key'] = str(json_data[key]['external_key'])
                placeholder['pool_language'] = "'" + str(json_data[key]['pool_language']) + "'"
                placeholder['country'] = "'" + str(json_data[key]['country']) + "'"
                placeholder['salutation'] = ''
                
            except KeyError:
                print(f'Key: {key} not found')
        
        language_file = f'configuration/language/{key}.txt'
        if os.path.isfile(language_file):
            with open(language_file) as f:
                language = f.read()
                placeholder['pool_language'] = language
        
        salutation_file = f'configuration/salutation/{key}.txt'
        if os.path.isfile(salutation_file):
            with open(salutation_file) as f:
                salutation = f.read()
                placeholder['salutation'] = salutation

        generated_script = self.replace_placeholder(placeholder, template, key)
        
        file_name_and_path = f'output/{directory_name}/standard_script_{key}.sql'
        if os.path.isfile(file_name_and_path):
            os.remove(file_name_and_path)

        directory_path = f'output/{directory_name}/'
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

        with open(f'output/{directory_name}/standard_script_{key}.sql', 'w') as f:
            f.write(generated_script)


    def generate_europe_script(self):
        print('Generating script for Europe ...')
        
        self.generate_standard_script(directory_name='Europe', key='BESC')
        self.generate_standard_script(directory_name='Europe', key='CH')
        self.generate_standard_script(directory_name='Europe', key='FR')
        self.generate_standard_script(directory_name='Europe', key='UK')

        print('... Done')


    def besc(self):
        print('Generating script for CH ...')
        self.generate_standard_script(directory_name='BESC', key='BESC')
        print('... Done')


    def ch(self):
        print('Generating script for CH ...')
        self.generate_standard_script(directory_name='CH', key='CH')
        print('... Done')


    def fr(self):
        print('Generating script for FR ...')
        self.generate_standard_script(directory_name='FR', key='FR')
        print('... Done')


    def uk(self):
        print('Generating script for UK ...')
        self.generate_standard_script(directory_name='UK', key='UK')
        print('... Done')


    def do_command(self, command):
        command_method = getattr(self, command.method.__name__)
        if command_method:
            command_method()