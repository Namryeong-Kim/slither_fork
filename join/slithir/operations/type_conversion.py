from typing import List, Union

from join.core.declarations.contract.contract import Contract
from join.core.declarations.solidity_type.element_type import ElementaryType
from join.core.declarations.solidity_type.type_alias import TypeAlias
from join.core.declarations.solidity_type.user_defined_type import UserDefinedType
from join.core.source_mapping.source_mapping import SourceMapping
from join.slithir.operations.lvalue import OperationWithLValue
from join.slithir.utils.utils import is_valid_lvalue, is_valid_rvalue
from join.slithir.variables.temporary import TemporaryVariable
from join.slithir.variables.temporary_ssa import TemporaryVariableSSA


class TypeConversion(OperationWithLValue):
    def __init__(
        self,
        result: Union[TemporaryVariableSSA, TemporaryVariable],
        variable: SourceMapping,
        variable_type: Union[TypeAlias, UserDefinedType, ElementaryType],
    ) -> None:
        super().__init__()
        assert is_valid_rvalue(variable) or isinstance(variable, Contract)
        assert is_valid_lvalue(result)
        assert isinstance(variable_type, (TypeAlias, UserDefinedType, ElementaryType))

        self._variable = variable
        self._type: Union[TypeAlias, UserDefinedType, ElementaryType] = variable_type
        self._lvalue = result

    @property
    def variable(self) -> SourceMapping:
        return self._variable

    @property
    def type(
        self,
    ) -> Union[TypeAlias, UserDefinedType, ElementaryType,]:
        return self._type

    @property
    def read(self) -> List[SourceMapping]:
        return [self.variable]

    def __str__(self) -> str:
        return str(self.lvalue) + f" = CONVERT {self.variable} to {self.type}"
