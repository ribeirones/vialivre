import os

from dotenv import load_dotenv


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

def as_bool(value):
    if value:
        return value.lower() in ['true', '1', 'yes', 'y', 'sim', 's']
    return False


class Config:
    ALCHEMICAL_DATABASE_URL = os.getenv('DATABASE_URL') or \
        f"sqlite:///{os.path.join(basedir, 'db.sqlite')}"
    ALCHEMICAL_ENGINE_OPTIONS = {'echo': as_bool(os.getenv('SQL_ECHO', '0')) }

    # Documentação da API
    APIFAIRY_TITLE = 'Vialivre API'
    APIFAIRY_VERSION = '1.0'
