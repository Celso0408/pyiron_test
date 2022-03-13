from pathlib import Path

def main():
    top_level_path = Path.cwd()
    resource_path = top_level_path.joinpath("pyiron", "resources")
    config_path = Path("~/.pyiron").expanduser()
    if not config_path.exists():
        with open(config_path, 'w') as f:
            f.writelines(['[DEFAULT]\n',
                            'TOP_LEVEL_DIRS = ' + str(top_level_path) + '\n',
                            'RESOURCE_PATHS = ' + str(resource_path) + '\n'])
    else:
        print('config exists')


if __name__ == '__main__':
    main()