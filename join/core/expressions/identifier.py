from typing import TYPE_CHECKING, Optional, Union

from join.core.declarations.top_levels.contract_level import ContractLevel
from join.core.declarations.top_levels.using_for_top_level import TopLevel
from join.core.expressions.expression import Expression
from join.core.declarations.variables.variable import Variable


if TYPE_CHECKING:
    from join.core.declarations.solidity_type.type import Type
    from join.core.declarations.contract.contract import Contract
    from join.core.declarations.variables.solidity_variables import SolidityVariable, SolidityFunction
    from join.solc_parsing.yul.evm_functions import YulBuiltin


class Identifier(Expression):
    def __init__(
        self,
        value: Union[
            Variable,
            "TopLevel",
            "ContractLevel",
            "Contract",
            "SolidityVariable",
            "SolidityFunction",
            "YulBuiltin",
        ],
    ) -> None:
        super().__init__()

        # pylint: disable=import-outside-toplevel
        from join.core.declarations.contract.contract import Contract
        from join.core.declarations.variables.solidity_variables import SolidityVariable, SolidityFunction
        from join.solc_parsing.yul.evm_functions import YulBuiltin

        assert isinstance(
            value,
            (
                Variable,
                TopLevel,
                ContractLevel,
                Contract,
                SolidityVariable,
                SolidityFunction,
                YulBuiltin,
            ),
        )

        self._value: Union[
            Variable,
            "TopLevel",
            "ContractLevel",
            "Contract",
            "SolidityVariable",
            "SolidityFunction",
            "YulBuiltin",
        ] = value
        self._type: Optional["Type"] = None

    @property
    def type(self) -> Optional["Type"]:
        return self._type

    @type.setter
    def type(self, new_type: "Type") -> None:
        self._type = new_type

    @property
    def value(
        self,
    ) -> Union[
        Variable,
        "TopLevel",
        "ContractLevel",
        "Contract",
        "SolidityVariable",
        "SolidityFunction",
        "YulBuiltin",
    ]:
        return self._value

    def __str__(self) -> str:
        return str(self._value)
