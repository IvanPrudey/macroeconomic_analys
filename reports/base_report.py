from abc import ABC
from typing import List, Dict, Any


class Report(ABC):

    def name(self) -> str:
        pass

    def headers(self) -> List[str]:
        pass

    def calculate(
            self, data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        pass
