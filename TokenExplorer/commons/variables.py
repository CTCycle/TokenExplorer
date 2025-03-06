import os
from dotenv import load_dotenv

from TokenExplorer.commons.constants import ROOT_DIR
from TokenExplorer.commons.logger import logger

# [IMPORT CUSTOM MODULES]
###############################################################################
class EnvironmentVariables:

    def __init__(self):        
        self.env_path = os.path.join(ROOT_DIR, 'setup', 'variables', '.env')        
        if os.path.exists(self.env_path):
            load_dotenv(dotenv_path=self.env_path, override=True)
        else:
            logger.error(f".env file not found at: {self.env_path}")   
    
    #--------------------------------------------------------------------------
    def get_environment_variables(self):                  
        return {"HF_ACCESS_TOKEN": os.getenv("HF_ACCESS_TOKEN", None)}
    
    #--------------------------------------------------------------------------
    def get_HF_access_token(self):                  
        return os.getenv("HF_ACCESS_TOKEN", None)
       
