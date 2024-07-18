from typing import List
from basics.analyzers.analyzer1 import Analyzer1
from basics.analyzers.analyzer2 import Analyzer2
from basics.analyzers.analyzer3 import Analyzer3
from basics.analyzers.analyzer4 import Analyzer4
from basics.analyzers.analyzer5 import Analyzer5
from basics.analyzers.analyzer6 import Analyzer6
from basics.analyzers.analyzer7 import Analyzer7
from basics.analyzers.analyzer8 import Analyzer8
from basics.analyzers.analyzer9 import Analyzer9

def getAnalyzers():
    return[
        Analyzer1(),
        Analyzer2(),
        Analyzer3(),
        Analyzer4(),
        Analyzer5(),
        Analyzer6(),
        Analyzer7(),
        Analyzer8(),
        Analyzer9(),
    ]