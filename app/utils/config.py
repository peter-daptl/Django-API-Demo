import os

import yaml


class APIConfig:
    """
    Wrapper for the configuration of API app.
    Imports the configuration files at classlevel to only be imported once.
    Includes classmethods to access configuration.
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    environment = os.environ.get("API_CONFIG", "dev")

    config_path = "{abs_path}/../config/config.{env}.yaml".format(
        abs_path=os.path.dirname(os.path.realpath(__file__)), env=environment
    )

    config_source = {}

    with open(config_path) as f:
        config_source = yaml.safe_load(f.read())

    @classmethod
    def get_config_var(self, setting, default=None):
        """
        Retrieves the configuration setting from the proper file.

        Args:
            setting (str): Key to retrieve from configuration
            default (str): value to return if key error

        Returns:
            str: Value from configuration file
        """
        try:
            val = self.config_source[setting]
            return val
        except KeyError:
            if default:
                return default

            error_msg = f"ImproperlyConfigured: Set {setting} environment variable"
            raise OSError(error_msg)
