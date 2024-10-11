import yaml

class ConfigLoader:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_database_config(self):
        return self.config['database']

    def get_table_name(self):
        return self.config['table']['name']

    def get_fields(self):
        return self.config['fields']

    def get_fraud_detection_config(self):
        return self.config['fraud_detection']
