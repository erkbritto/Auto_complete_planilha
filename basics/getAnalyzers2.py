from typing import List
from basics.analyzers_autopilot_usuario.analyzer1 import Analyzer1
from basics.analyzers_autopilot_usuario.analyzer2 import Analyzer2
def getAnalyzers():
    return [
        Analyzer1(),
        Analyzer2(),
    ]
