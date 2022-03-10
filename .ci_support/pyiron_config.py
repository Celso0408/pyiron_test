import os


def main():
    current_path = os.path.abspath(os.path.curdir)
    top_level_path = current_path.replace('\\', '/')
    resource_path = os.path.join(current_path, "pyiron", "resources").replace('\\', '/')
    pyiron_config = os.path.expanduser('~/.pyiron').replace('\\', '/')
    conda_prefix = os.getenv('CONDA')
    additional_resource = os.path.join(conda_prefix, "share", "pyiron").replace('\\', '/')
    if os.path.exists(additional_resource):
        resource_path = resource_path + ", " + additional_resource
    
    print(f"resource_path:{resource_path}")
    if not os.path.exists(pyiron_config):
        with open(pyiron_config, 'w') as f:
            f.writelines(['[DEFAULT]\n',
                            'TOP_LEVEL_DIRS = ' + top_level_path + '\n',
                            'RESOURCE_PATHS = ' + resource_path + '\n'])
    else:
        print('config exists')


if __name__ == '__main__':
    main()
