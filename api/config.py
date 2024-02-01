from dotenv import load_dotenv
import os
from .models import Vocabulary

env = os.getenv("ENV")
app_base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000")

class Config(object):
    print("Loaded production config")
    vocabularies = [
        Vocabulary(
            name="UNBIS Thesaurus", 
            description="UNBIS Thesaurus is the UN Library's multilingual thesaurus.", 
            short_name="thesaurus",
            local_path=f'{app_base_url}/thesaurus', 
            base_uri="http://metadata.un.org/thesaurus/"
        ),
        Vocabulary(
            name="SDGs Ontology",
            short_name="sdg",
            local_path=f'{app_base_url=}/sdg',
            base_uri="http://metadata.un.org/"
        )
    ]

class DevConfig(Config):
    print("... now loaded dev config")
    pass

class TestConfig(Config):
    pass


def get_config():
    if env == "Dev":
        return DevConfig
    else:
        return Config