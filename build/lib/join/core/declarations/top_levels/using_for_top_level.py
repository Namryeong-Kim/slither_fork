from typing import TYPE_CHECKING, List, Dict, Union

from join.core.declarations.contract.contract import USING_FOR_KEY, USING_FOR_ITEM
from join.core.declarations.solidity_type.type import Type
from join.core.source_mapping.source_mapping import SourceMapping

if TYPE_CHECKING:
    from join.core.scope.scope import FileScope


class TopLevel(SourceMapping):
    """
    This class is used to represent objects that are at the top level
    The opposite is ContractLevel

    """


class UsingForTopLevel(TopLevel):
    def __init__(self, scope: "FileScope") -> None:
        super().__init__()
        self._using_for: Dict[Union[str, Type], List[Type]] = {}
        self.file_scope: "FileScope" = scope

    @property
    def using_for(self) -> Dict[USING_FOR_KEY, USING_FOR_ITEM]:
        return self._using_for
