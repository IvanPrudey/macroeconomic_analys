from abc import ABC, abstractmethod
from typing import List, Dict, Any


class Report(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def headers(self) -> List[str]:
        pass

    @abstractmethod
    def calculate(
            self, data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        pass
