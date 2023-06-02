from typing import Union, TYPE_CHECKING
from join.core.expressions.expression import Expression
from join.core.declarations.solidity_type.element_type import ElementaryType

from join.core.declarations.solidity_type.type import Type

if TYPE_CHECKING:
    from join.core.declarations.solidity_type.type_alias import TypeAliasTopLevel


class NewArray(Expression):

    # note: dont conserve the size of the array if provided
    def __init__(
        self, depth: int, array_type: Union["TypeAliasTopLevel", "ElementaryType"]
    ) -> None:
        super().__init__()
        assert isinstance(array_type, Type)
        self._depth: int = depth
        self._array_type: Type = array_type

    @property
    def array_type(self) -> Type:
        return self._array_type

    @property
    def depth(self) -> int:
        return self._depth

    def __str__(self):
        return "new " + str(self._array_type) + "[]" * self._depth


class NewContract(Expression):
    def __init__(self, contract_name: str) -> None:
        super().__init__()
        self._contract_name: str = contract_name
        self._gas = None
        self._value = None
        self._salt = None

    @property
    def contract_name(self) -> str:
        return self._contract_name

    @property
    def call_value(self):
        return self._value

    @call_value.setter
    def call_value(self, v):
        self._value = v

    @property
    def call_salt(self):
        return self._salt

    @call_salt.setter
    def call_salt(self, salt):
        self._salt = salt

    def __str__(self) -> str:
        return "new " + str(self._contract_name)


class NewElementaryType(Expression):
    def __init__(self, new_type):
        assert isinstance(new_type, ElementaryType)
        super().__init__()
        self._type = new_type

    @property
    def type(self) -> ElementaryType:
        return self._type

    def __str__(self):
        return "new " + str(self._type)
