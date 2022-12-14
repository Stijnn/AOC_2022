import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import requests

from dotenv import load_dotenv
load_dotenv()

missing_day_folders = [True]*25
list_of_dirs = [listing.name for listing in os.scandir() if listing.is_dir()]
list_of_templates = [listing.name for listing in os.scandir('./templates/') if listing.is_file() and listing.name.startswith('template')]

for idx in range(len(missing_day_folders)):
    if f"aoc_{idx}" in list_of_dirs:
        missing_day_folders[idx] = False
        
        
def find_template(extension):
    name = f"template.{extension}"
    if name in list_of_templates:
        return f"templates/{name}"
    return None


def on_template_setup(extension, target_folder):
    if extension == 'py':
        template_path = find_template(extension)
        if template_path is not None:
            with open(template_path, 'r') as template_file:
                with open(f"{target_folder}/main.{extension}", 'x') as entry_file:
                    entry_file.writelines(template_file.readlines())
    elif extension == 'rs':
        os.system(f'cargo init {target_folder}')
        return
    else:
        return


def download_and_template(day_number, year_number, template = 'rs'):
    response = requests.get(f'https://adventofcode.com/{year_number}/day/{day_number}/input', cookies={'session': os.getenv("SESSION_COOKIE")})
    if response.status_code != 200:
        print(f"ERROR {response.status_code}: {response.content.decode()}")
        return False
    
    target_folder = f"aoc_{day_number}"
    
    os.mkdir(target_folder)    
    on_template_setup(template, target_folder)
    
    with open(f"{target_folder}/input.txt", 'x') as input_file:
        input_file.writelines(response.content.decode('UTF-8'))

    return True
                

for index in range(len(missing_day_folders)):
    if missing_day_folders[index]:
        if not download_and_template(index + 1, 2022):
            break