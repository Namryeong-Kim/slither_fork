"""
    Variable used with FunctionType
    ex:
    struct C{
        function(uint) my_func;
    }
"""

from join.core.declarations.variables.variable import Variable


class FunctionTypeVariable(Variable):
    pass
