from typing import Dict
from abc import ABC, abstractmethod


class FlaskPostgresqlControllerInterface(ABC):

    def get_content_info(self, json_input) -> None:
        pass


    @abstractmethod
    def execute(self) -> Dict:
        pass
