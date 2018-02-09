import os
import subprocess

root_dir = os.path.dirname(os.path.abspath(__file__))
result_dir = os.path.join(root_dir, 'Result')
sources_dir = os.path.join(root_dir, 'Source')
convert_path = os.path.join(root_dir, 'convert.exe')

try:
    os.mkdir(result_dir)
except FileExistsError:
    print('Директория Result уже существует')

source_files_list = os.listdir(sources_dir)
print('Всего файлов : {}'.format(len(source_files_list)))

for filename in source_files_list:
    command = convert_path + ' ' + os.path.join(sources_dir, filename) + ' -resize 200 ' + os.path.join(result_dir, filename)
    subprocess.run(command)
