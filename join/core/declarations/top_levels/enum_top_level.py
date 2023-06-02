from typing import TYPE_CHECKING, List

from join.core.declarations.enum.enum import Enum
from join.core.declarations.top_levels.using_for_top_level import TopLevel

if TYPE_CHECKING:
    from join.core.scope.scope import FileScope


class EnumTopLevel(Enum, TopLevel):
    def __init__(
        self, name: str, canonical_name: str, values: List[str], scope: "FileScope"
    ) -> None:
        super().__init__(name, canonical_name, values)
        self.file_scope: "FileScope" = scope
