import os


class FileManager:
    def __init__(self):
        self.verify_config_file()

    def verify_config_file(self):
        if not self.has_config_file():
            self.create_configuration_file()

    @staticmethod
    def has_config_file():
        return os.path.isfile('config.pi')

    @staticmethod
    def create_configuration_file():
        try:
            with open('config.pi', 'w') as config:
                config.write('')
        except OSError:
            print("Erro ao criar config.pi")

    @staticmethod
    def save_config_file(data):
        keys = dict(data).keys()
        try:
            with open('config.pi', 'w') as file:
                for key in keys:
                    file.write(key + '=' + data[key])
                    file.write('\n')
        except OSError:
            print('Erro ao escrever as config.pi')

    @staticmethod
    def get_attributes_from_config_file():
        attributes = dict()
        try:
            with open('config.pi', 'r') as file:
                for line in file:
                    fields = line.strip().split("=")
                    key = fields[0]
                    value = fields[1]
                    attributes[key] = value
        except OSError:
            print('Erro ao abrir o arquivo')
        return attributes
