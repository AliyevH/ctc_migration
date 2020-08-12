import yaml


class Config:
    def __init__(self, config_yaml):
        self.config_file = config_yaml

        with open(self.config_file) as f:
            self.config_data = yaml.load(f, Loader=yaml.FullLoader)

        self.version = self.config_data.get("version")
        self.config = self.config_data.get("Config")

        self.sourceConfig = self.config[0].get("SourceConfig")
        self.destinationConfig = self.config[1].get("DestinationConfig")

        self.sourceURI = self.sourceConfig.get("dbURI")
        self.destinationURI = self.destinationConfig.get("dbURI")

        self.migrationTables = self.config_data.get("migrationTables")

