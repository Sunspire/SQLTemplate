import os


class CommandController:
    def __init__(self):
        self.command = ''
    
    def generate_standard_script(self, directory_name: str, market: str, country: str):        
        file_template = open('templates/standard_template.txt', 'r')
        template = file_template.read()
        file_template.close()

        os.makedirs(f'output/{directory_name}')
        with open(f'output/{directory_name}/standard_script_{market}.sql', 'w') as f:
            generated_script = template.replace('##MARKET##', market)
            generated_script = generated_script.replace('##COUNTRY##', country)
            f.write(generated_script)        
    
    def generate_europe_script(self):
        pass
    
    def fr(self):
        self.generate_standard_script('FR', 'FR', 'FR')
    
    def uk(self):
        self.generate_standard_script('UK', 'UK', 'UK')
    
    def do_command(self, command):
        command_method = getattr(self, command.method.__name__)
        if command_method:
            command_method()