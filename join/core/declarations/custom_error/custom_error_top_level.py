from typing import TYPE_CHECKING

from join.core.declarations.custom_error.custom_error import CustomError
from join.core.declarations.top_levels.using_for_top_level import TopLevel

if TYPE_CHECKING:
    from join.core.compilation_unit import JoinCompilationUnit
    from join.core.scope.scope import FileScope


class CustomErrorTopLevel(CustomError, TopLevel):
    def __init__(self, compilation_unit: "JoinCompilationUnit", scope: "FileScope") -> None:
        super().__init__(compilation_unit)
        self.file_scope: "FileScope" = scope
