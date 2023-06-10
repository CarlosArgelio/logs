import os
import logging
from datetime import datetime
from pathlib import Path


class Logs:
    def __init__(self, filename=None, format=None):
        
        if filename is not None:
            self.filename = filename
        else:
            filename_hours = datetime.now().strftime("%H%M%S")
            self.filename = str(filename_hours)

        if format is not None:
            self.format = format
        else:
            self.format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.format = format 

    def info(self):
        route_log = self.find_logs()

        if self.filename is not None:
            logging.basicConfig(filename=f'{route_log}/{self.filename}.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        logger = logging.getLogger('Name')
        logger.warning('Este es un mensaje de info')

    def register(self):
        route_log = self.find_logs()

        if self.filename is not None:
            log_logging = logging.basicConfig(filename=f'{route_log}/{self.filename}.log', format=self.format)
        return log_logging

    def find_logs(self):

        route = str(datetime.now().strftime("%Y%m%d_%H"))
        paths = f'logs/{route}'

        paths_validate = Path(paths).exists()
        
        if paths_validate:
            return paths
        else:
            os.makedirs(str(paths))
            return paths