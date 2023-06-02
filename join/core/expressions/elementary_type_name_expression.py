"""
    This expression does nothing, if a contract used it, its probably a bug
"""
from join.core.expressions.expression import Expression
from join.core.declarations.solidity_type.type import Type
from join.core.declarations.solidity_type.element_type import ElementaryType


class ElementaryTypeNameExpression(Expression):
    def __init__(self, t: ElementaryType) -> None:
        assert isinstance(t, Type)
        super().__init__()
        self._type = t

    @property
    def type(self) -> Type:
        return self._type

    @type.setter
    def type(self, new_type: Type):
        assert isinstance(new_type, Type)
        self._type = new_type

    def __str__(self) -> str:
        return str(self._type)
