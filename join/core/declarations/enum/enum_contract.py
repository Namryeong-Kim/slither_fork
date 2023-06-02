from typing import TYPE_CHECKING

from join.core.declarations.top_levels.contract_level import ContractLevel
from join.core.declarations.enum.enum import Enum

if TYPE_CHECKING:
    from join.core.declarations.contract.contract import Contract


class EnumContract(Enum, ContractLevel):
    def is_declared_by(self, contract: "Contract") -> bool:
        """
        Check if the element is declared by the contract
        :param contract:
        :return:
        """
        return self.contract == contract
