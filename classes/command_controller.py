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

        return


    def replace_placeholder(self, placeholder = {}, template = '', key = ''):
        generated_script = template
        for key in placeholder:
           generated_script = generated_script.replace(f'##{key}##', placeholder[key])

        return generated_script

    def unpack_node(self, node, contents):
        if node == 'btq_of_origin':
            return ', '.join(map(lambda x: "'" + x.strip() + "'", str(contents).split(',')))

        if node in ['pool_language', 'country']:
            return "'" + str(contents) + "'"

        return node

    def generate_script(self, key: str, template_name: str, directory_name: str):
        if template_name == '':
            template_name = 'standard'
        try:
            with open('templates/' + self.templates[template_name][0], 'r') as file_template:
                template = file_template.read()

        except KeyError:
            print('Cannot find the template')
            return
        
        config_file = 'configuration/' + self.templates[template_name][1]
        if not os.path.isfile(config_file):
            print(f'Config file not found: {config_file}')
            return

        placeholder = {}
        with open(config_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            try:
                for node in json_data[key]:
                    placeholder[node] = self.unpack_node(node, str(json_data[key][node]))
                
            except KeyError:
                print(f'Key: {key} not found')
                return
            
        if 'pool_language' in json_data[key]:
            language_file = f'configuration/language/{key}.txt'
            if os.path.isfile(language_file):
                with open(language_file) as f:
                    language = f.read()
                    placeholder['pool_language'] = language

        if 'salutation' in json_data[key]:
            salutation_file = f'configuration/salutation/{key}.txt'
            if os.path.isfile(salutation_file):
                with open(salutation_file) as f:
                    salutation = f.read()
                    placeholder['salutation'] = salutation

        generated_script = self.replace_placeholder(placeholder, template, key)
        
        directory_path = f'output/{directory_name}/'
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

        file_name_and_path = f'output/{directory_name}/standard_script_{key}.sql'
        if os.path.isfile(file_name_and_path):
            os.remove(file_name_and_path)

        with open(f'output/{directory_name}/standard_script_{key}.sql', 'w') as f:
            f.write(generated_script)


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
        
        directory_path = f'output/{directory_name}/'
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

        file_name_and_path = f'output/{directory_name}/standard_script_{key}.sql'
        if os.path.isfile(file_name_and_path):
            os.remove(file_name_and_path)

        with open(f'output/{directory_name}/standard_script_{key}.sql', 'w') as f:
            f.write(generated_script)


    def europe(self):
        print('Generating script for Europe ...')
        print()
        
        self.generate_standard_script(directory_name='Europe', key='BESC')
        print('BESC done ...')

        self.generate_standard_script(directory_name='Europe', key='CH')
        print('CH done ...')

        self.generate_standard_script(directory_name='Europe', key='FR')
        print('FR done ...')

        self.generate_standard_script(directory_name='Europe', key='GR')
        print('GR done ...')

        self.generate_standard_script(directory_name='Europe', key='IB')
        print('IB done ...')

        self.generate_standard_script(directory_name='Europe', key='NEU')
        print('NEU done ...')

        self.generate_standard_script(directory_name='Europe', key='SEE')
        print('SEE done ...')

        self.generate_standard_script(directory_name='Europe', key='TR')
        print('TR done ...')

        self.generate_standard_script(directory_name='Europe', key='UK')
        print('UK done ...')

        print()
        print('... Done')


    def besc(self):
        print('Generating script for BESC ...')
        self.generate_standard_script(directory_name='BESC', key='BESC')
        print('... Done')

    def ch(self):
        print('Generating script for CH ...')
        self.generate_standard_script(directory_name='CH', key='CH')
        print('... Done')

    def fr(self):
        print('Generating script for FR ...')
        self.generate_script(key='FR', template_name=self.template_name, directory_name='FR')
        print('... Done')

    def gr(self):
        print('Generating script for GR ...')
        self.generate_standard_script(directory_name='GR', key='GR')
        print('... Done')

    def ib(self):
        print('Generating script for IB ...')
        self.generate_standard_script(directory_name='IB', key='IB')
        print('... Done')

    def neu(self):
        print('Generating script for NEU ...')
        self.generate_standard_script(directory_name='NEU', key='NEU')
        print('... Done')

    def see(self):
        print('Generating script for SEE ...')
        self.generate_standard_script(directory_name='SEE', key='SEE')
        print('... Done')
    
    def tr(self):
        print('Generating script for TR ...')
        self.generate_standard_script(directory_name='TR', key='TR')
        print('... Done')

    def uk(self):
        print('Generating script for UK ...')
        self.generate_standard_script(directory_name='UK', key='UK')
        print('... Done')


    def do_command(self, command):
        command_method = getattr(self, command.method.__name__)
        if command_method:
            command_method()