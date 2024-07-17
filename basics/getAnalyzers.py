from typing import List
from basics.analyzers.analyzer1 import Analyzer1
from basics.analyzers.analyzer2 import Analyzer2

def getAnalyzers():
    return[
        Analyzer1(),
        Analyzer2(),
    ]