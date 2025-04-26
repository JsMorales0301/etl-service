import time
from typing import Any

from src.domain.interfaces.rule import Rule
from .rules import all_rules

class CandidatesStrategy:
    rules: list[Rule]

    def __init__(self):
        self.rules = [rule() for rule in all_rules]

    def run(self, df, context: dict[str, Any] = None):
        start = time.time()
        for rule in self.rules:
            rule.apply(df, context)
        end = time.time()
        print(f"Tiempo de ejecución: {end - start:.6f} segundos")
        return df