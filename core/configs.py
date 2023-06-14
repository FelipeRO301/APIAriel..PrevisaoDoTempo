from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    ''' 
    Configuracoes Gerais da API
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+aiomysql://apiprevisaodotempof14tomcat20e20#@localhost:3306/apiprevisaodotempo'
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True
        
settings = Settings()