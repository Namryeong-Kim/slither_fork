from typing import TYPE_CHECKING, Tuple

from join.core.declarations.top_levels.using_for_top_level import TopLevel
from join.core.declarations.top_levels.contract_level import ContractLevel
from join.core.declarations.solidity_type import Type
from join.core.declarations.solidity_type.element_type import ElementaryType

if TYPE_CHECKING:
    from join.core.declarations.contract.contract import Contract
    from join.core.scope.scope import FileScope


class TypeAlias(Type):
    def __init__(self, underlying_type: ElementaryType, name: str) -> None:
        super().__init__()
        self.name = name
        self.underlying_type = underlying_type

    @property
    def type(self) -> ElementaryType:
        """
        Return the underlying type. Alias for underlying_type


        Returns:
            Type: the underlying type

        """
        return self.underlying_type

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return self.underlying_type.storage_size

    def __hash__(self) -> int:
        return hash(str(self))

    @property
    def is_dynamic(self) -> bool:
        return self.underlying_type.is_dynamic


class TypeAliasTopLevel(TypeAlias, TopLevel):
    def __init__(self, underlying_type: ElementaryType, name: str, scope: "FileScope") -> None:
        super().__init__(underlying_type, name)
        self.file_scope: "FileScope" = scope

    def __str__(self) -> str:
        return self.name


class TypeAliasContract(TypeAlias, ContractLevel):
    def __init__(self, underlying_type: ElementaryType, name: str, contract: "Contract") -> None:
        super().__init__(underlying_type, name)
        self._contract: "Contract" = contract

    def __str__(self) -> str:
        return self.contract.name + "." + self.name
