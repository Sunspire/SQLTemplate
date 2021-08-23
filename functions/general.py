import os
import traceback


def replace_placeholder(placeholder = {}, template = '', key = ''):
    generated_script = template
    for key in placeholder:
        generated_script = generated_script.replace(f'##{key}##', placeholder[key])

    return generated_script

def format_data(node, contents):
    if node == 'btq_of_origin':
        return ', '.join(map(lambda x: "'" + x.strip() + "'", str(contents).split(',')))

    if node in ['pool_language', 'country', 'salutation', 'external_key']:
        return "'" + str(contents) + "'"

    return str(contents)

def isfile(file_name_and_path: str):
    if os.path.isfile(file_name_and_path):
        return True
    
    print(f'File not found: {file_name_and_path}')
    return False

def verify_directory(directory_path: str):
    if directory_path is None or directory_path == '':
        return os.path.abspath('Output')

    if os.path.isdir(directory_path):
        return os.path.abspath(directory_path)

    try:
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)
            print(f'Created output directory {os.path.abspath(directory_path)}')
            return os.path.abspath(directory_path)
    except Exception:
        print(f'Cannot create directory {directory_path}')
        print('Generating file(s) in the default directory')
        traceback.print_exc()
        return os.path.abspath('Output')

    return os.path.abspath('Output')