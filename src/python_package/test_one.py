import pathlib

current_dir =pathlib.Path.cwd() / 'config' / 'config.json'
env_dir = current_dir

print(current_dir)