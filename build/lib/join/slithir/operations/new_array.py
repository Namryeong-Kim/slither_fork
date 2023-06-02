from typing import List, Union, TYPE_CHECKING
from join.slithir.operations.lvalue import OperationWithLValue
from join.slithir.operations.call import Call
from join.core.declarations.solidity_type.type import Type

if TYPE_CHECKING:
    from join.core.declarations.solidity_type.type_alias import TypeAliasTopLevel
    from join.slithir.variables.constant import Constant
    from join.slithir.variables.temporary import TemporaryVariable
    from join.slithir.variables.temporary_ssa import TemporaryVariableSSA


class NewArray(Call, OperationWithLValue):
    def __init__(
        self,
        depth: int,
        array_type: "TypeAliasTopLevel",
        lvalue: Union["TemporaryVariableSSA", "TemporaryVariable"],
    ) -> None:
        super().__init__()
        assert isinstance(array_type, Type)
        self._depth = depth
        self._array_type = array_type

        self._lvalue = lvalue

    @property
    def array_type(self) -> "TypeAliasTopLevel":
        return self._array_type

    @property
    def read(self) -> List["Constant"]:
        return self._unroll(self.arguments)

    @property
    def depth(self) -> int:
        return self._depth

    def __str__(self):
        args = [str(a) for a in self.arguments]
        lvalue = self.lvalue
        return (
            f"{lvalue}({lvalue.type}) = new {self.array_type}{'[]' * self.depth}({','.join(args)})"
        )
