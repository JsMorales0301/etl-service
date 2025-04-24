from .candidates.strategy import CandidatesStrategy

class TransformFactory:
    
    def __init__(self):
        self.strategies = {
            'candidatos': CandidatesStrategy
        }

    def get_strategy(self, strategy: str):
        strategy_selected = self.strategies.get(strategy)
        
        if strategy_selected:
            return strategy_selected()
        else:
            raise ValueError(f"Extensión de archivo no valida: {strategy}")