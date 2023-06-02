from typing import List, Union

from join.slithir.operations.lvalue import OperationWithLValue
from join.slithir.utils.utils import is_valid_lvalue
from join.slithir.variables.tuple import TupleVariable
from join.core.declarations.variables.local_variable_init_from_tuple import LocalVariableInitFromTuple
from join.slithir.variables.local_variable import LocalIRVariable
from join.slithir.variables.tuple_ssa import TupleVariableSSA


class Unpack(OperationWithLValue):
    def __init__(
        self,
        result: Union[LocalVariableInitFromTuple, LocalIRVariable],
        tuple_var: Union[TupleVariable, TupleVariableSSA],
        idx: int,
    ) -> None:
        assert is_valid_lvalue(result)
        assert isinstance(tuple_var, TupleVariable)
        assert isinstance(idx, int)
        super().__init__()
        self._tuple = tuple_var
        self._idx = idx
        self._lvalue = result

    @property
    def read(self) -> List[Union[TupleVariableSSA, TupleVariable]]:
        return [self.tuple]

    @property
    def tuple(self) -> Union[TupleVariable, TupleVariableSSA]:
        return self._tuple

    @property
    def index(self) -> int:
        return self._idx

    def __str__(self):
        return f"{self.lvalue}({self.lvalue.type})= UNPACK {self.tuple} index: {self.index} "
