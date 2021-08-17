import json
import os


class CommandController:
    def __init__(self):
        self.command = ''
        self.templates = {}
        self.template_name = ''

    def init(self):
        with open('configuration/template_config.json', 'r') as f:
            config = json.load(f)
        
        for key in config:
            self.templates[key] = [str(config[key]['template']), str(config[key]['config'])]

    def replace_placeholder(self, placeholder = {}, template = '', key = ''):
        generated_script = template
        for key in placeholder:
           generated_script = generated_script.replace(f'##{key}##', placeholder[key])

        return generated_script

    def format_data(self, node, contents):
        if node == 'btq_of_origin':
            return ', '.join(map(lambda x: "'" + x.strip() + "'", str(contents).split(',')))

        if node in ['pool_language', 'country', 'salutation']:
            return "'" + str(contents) + "'"

        return str(contents)

    def isfile(self, file_name_and_path: str):
        if os.path.isfile(file_name_and_path):
            return True
        
        print(f'File not found: {file_name_and_path}')
        return False

    def generate_script(self, key: str, template_name: str, directory_name: str):
        if template_name == '':
            template_name = 'standard'
        
        template_name_and_path = 'templates/' + self.templates[template_name][0]
        config_file = 'configuration/' + self.templates[template_name][1]
        
        if not self.isfile(template_name_and_path) or not self.isfile(config_file):
            return

        with open(template_name_and_path, 'r') as file_template:
            template = file_template.read()

        placeholder = {}
        with open(config_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            try:
                for node in json_data[key]:                    
                    placeholder[node] = self.format_data(node, str(json_data[key][node]))
                
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

        generated_script = self.replace_placeholder(placeholder, template, key)
        
        directory_path = f'output/{directory_name}/'
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

        file_name_and_path = f'output/{directory_name}/standard_script_{key}.sql'
        if os.path.isfile(file_name_and_path):
            os.remove(file_name_and_path)

        with open(f'output/{directory_name}/standard_script_{key}.sql', 'w') as f:
            f.write(generated_script)

    def europe(self):
        directory = 'Europe'
        print('Generating script for Europe ...')
        print()
        
        self.generate_script(key='BESC', template_name=self.template_name, directory_name=directory)
        print('BESC done ...')

        self.generate_script(key='CH', template_name=self.template_name, directory_name=directory)
        print('CH done ...')

        self.generate_script(key='FR', template_name=self.template_name, directory_name=directory)
        print('FR done ...')

        self.generate_script(key='GR', template_name=self.template_name, directory_name=directory)
        print('GR done ...')

        self.generate_script(key='IB', template_name=self.template_name, directory_name=directory)
        print('IB done ...')

        self.generate_script(key='NEU', template_name=self.template_name, directory_name=directory)
        print('NEU done ...')

        self.generate_script(key='SEE', template_name=self.template_name, directory_name=directory)
        print('SEE done ...')

        self.generate_script(key='TR', template_name=self.template_name, directory_name=directory)
        print('TR done ...')

        self.generate_script(key='UK', template_name=self.template_name, directory_name=directory)
        print('UK done ...')

        print()
        print('... Done')

    def besc(self):
        print('Generating script for BESC ...')
        self.generate_script(key='BESC', template_name=self.template_name, directory_name='BESC')
        print('... Done')

    def ch(self):
        print('Generating script for CH ...')
        self.generate_script(key='CH', template_name=self.template_name, directory_name='CH')
        print('... Done')

    def fr(self):
        print('Generating script for FR ...')
        self.generate_script(key='FR', template_name=self.template_name, directory_name='FR')
        print('... Done')

    def gr(self):
        print('Generating script for GR ...')
        self.generate_script(key='GR', template_name=self.template_name, directory_name='GR')
        print('... Done')

    def ib(self):
        print('Generating script for IB ...')
        self.generate_script(key='IB', template_name=self.template_name, directory_name='IB')
        print('... Done')

    def neu(self):
        print('Generating script for NEU ...')
        self.generate_script(key='NEU', template_name=self.template_name, directory_name='NEU')
        print('... Done')

    def see(self):
        print('Generating script for SEE ...')
        self.generate_script(key='SEE', template_name=self.template_name, directory_name='SEE')
        print('... Done')

    def tr(self):
        print('Generating script for TR ...')
        self.generate_script(key='TR', template_name=self.template_name, directory_name='TR')
        print('... Done')

    def uk(self):
        print('Generating script for UK ...')
        self.generate_script(key='UK', template_name=self.template_name, directory_name='UK')
        print('... Done')


    def do_command(self, command):
        command_method = getattr(self, command.method.__name__)
        if command_method:
            command_method()