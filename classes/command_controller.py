import json
import os
from functions.general import replace_placeholder, format_data, isfile, verify_directory


class CommandController:
    def __init__(self):
        self.templates = {}
        self.globals = {}

    def init(self):
        with open('configuration/template_config.json', 'r') as f:
            config = json.load(f)
        
        for key in config:
            self.templates[key] = [str(config[key]['template']), str(config[key]['config'])]

    def set_global(self, key: str, value):
        self.globals[key] = value

    def get_global(self, key: str):
        if key in self.globals:
            return self.globals[key]
        return ''


    def generate_script(self, key: str, directory_name: str):
        template_name = self.get_global('template')
        file_name = self.get_global('file_name')
        output_directory = verify_directory(self.get_global('output_directory'))

        if template_name == '':
            template_name = 'standard'
        
        if file_name == '':
            file_name = 'standard_script'
        
        template_name_and_path = 'templates/' + self.templates[template_name][0]
        config_file = 'configuration/' + self.templates[template_name][1]
        
        if not isfile(template_name_and_path) or not isfile(config_file):
            return

        with open(template_name_and_path, 'r') as file_template:
            template = file_template.read()

        with open(config_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        placeholder = {}
        placeholder['custom_join'] = ''
        placeholder['custom_condition'] = ''
        try:
            for node in json_data[key]:                    
                placeholder[node] = format_data(node, str(json_data[key][node]))
            
        except KeyError:
            print(f'Key: {key} not found')
            return
        
        if 'pool_language' in json_data[key]:
            language_file = f'configuration/language/{key}.txt'
            if os.path.isfile(language_file):
                with open(language_file) as f:
                    placeholder['pool_language'] = f.read()

        if 'salutation' in json_data[key]:
            salutation_file = f'configuration/salutation/{key}.txt'
            if os.path.isfile(salutation_file):
                with open(salutation_file) as f:
                    placeholder['salutation'] = f.read()

        # Look for custom scripts and apply them if found
        CUSTOM_JOIN_FILE = 'custom/custom_join.txt'
        if os.path.isfile(CUSTOM_JOIN_FILE):
            with open(CUSTOM_JOIN_FILE) as f:
                placeholder['custom_join'] = f.read()
        
        CUSTOM_CONDITION_FILE = 'custom/custom_condition.txt'
        if os.path.isfile(CUSTOM_CONDITION_FILE):
            with open(CUSTOM_CONDITION_FILE) as f:
                    placeholder['custom_condition'] = f.read()

        generated_script = replace_placeholder(placeholder, template, key)
        
        directory_path = f'{output_directory}\\{directory_name}\\'
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

        file_name_and_path = f'{output_directory}\\{directory_name}\\{file_name}_{key}.sql'
        if os.path.isfile(file_name_and_path):
            os.remove(file_name_and_path)

        with open(file_name_and_path, 'w') as f:
            f.write(generated_script)

    def auto_config(self):
        auto_config_file = 'custom/auto_config.json'
        if not isfile(auto_config_file):
            print('auto config file not found')
            return
        
        with open(auto_config_file, 'r') as f:
            config = json.load(f)
        
        self.set_global('template', config['template'])

        print('Generating scripts from auto config ...')
        for market in config['market'].split(','):
            the_market = market.strip().upper()
            self.generate_script(key=the_market, directory_name='autoconfig')
            print(f'{the_market} done ...')

        print('... done')

    def europe(self):
        directory = 'Europe'
        print('Generating scripts for Europe ...')
        print()
        
        self.generate_script(key='BESC', directory_name=directory)
        print('BESC done ...')

        self.generate_script(key='CH', directory_name=directory)
        print('CH done ...')

        self.generate_script(key='FR', directory_name=directory)
        print('FR done ...')

        self.generate_script(key='GR', directory_name=directory)
        print('GR done ...')

        self.generate_script(key='IB', directory_name=directory)
        print('IB done ...')

        self.generate_script(key='NEU', directory_name=directory)
        print('NEU done ...')

        self.generate_script(key='SEE', directory_name=directory)
        print('SEE done ...')

        self.generate_script(key='TR', directory_name=directory)
        print('TR done ...')

        self.generate_script(key='UK', directory_name=directory)
        print('UK done ...')

        print()
        print('... Done')

    def besc(self):
        print('Generating script for BESC ...')
        self.generate_script(key='BESC', directory_name='BESC')
        print('... Done')

    def ch(self):
        print('Generating script for CH ...')
        self.generate_script(key='CH', directory_name='CH')
        print('... Done')

    def fr(self):
        print('Generating script for FR ...')
        self.generate_script(key='FR', directory_name='FR')
        print('... Done')

    def gr(self):
        print('Generating script for GR ...')
        self.generate_script(key='GR', directory_name='GR')
        print('... Done')

    def ib(self):
        print('Generating script for IB ...')
        self.generate_script(key='IB', directory_name='IB')
        print('... Done')

    def neu(self):
        print('Generating script for NEU ...')
        self.generate_script(key='NEU', directory_name='NEU')
        print('... Done')

    def see(self):
        print('Generating script for SEE ...')
        self.generate_script(key='SEE', directory_name='SEE')
        print('... Done')

    def tr(self):
        print('Generating script for TR ...')
        self.generate_script(key='TR', directory_name='TR')
        print('... Done')

    def uk(self):
        print('Generating script for UK ...')
        self.generate_script(key='UK', directory_name='UK')
        print('... Done')


    def do_command(self, command):
        command_method = getattr(self, command.method.__name__)
        if command_method:
            command_method()