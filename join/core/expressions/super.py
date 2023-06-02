from join.core.expressions.call_expression import CallExpression
from join.core.expressions.identifier import Identifier

class SuperCallExpression(CallExpression):
    pass


class SuperIdentifier(Identifier):
    def __str__(self):
        return "super." + str(self._value)