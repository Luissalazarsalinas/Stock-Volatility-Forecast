# Schema to enviromental variables
import os 
from pydantic import BaseSettings

def full_path_env(filename: str = ".env") -> str:
    """ Return the correct path of .env file """
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    full_path = os.path.join(dir_name, filename)

    return full_path

class Settings(BaseSettings):
    """ Validation data from env variables """
    api_key:str
    database_name:str

    class Config:
        env_file = full_path_env(".env")

## Instance of the class
settings = Settings()
