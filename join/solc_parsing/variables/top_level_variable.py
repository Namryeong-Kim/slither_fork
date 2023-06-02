from typing import Dict, TYPE_CHECKING

from join.core.declarations.top_levels.variable_top_level import TopLevelVariable
from join.solc_parsing.variables.variable_declaration import VariableDeclarationSolc
from join.solc_parsing.declarations.caller_context import CallerContextExpression

if TYPE_CHECKING:
    from join.solc_parsing.join_compilation_unit_solc import JoinCompilationUnitSolc
    from join.core.compilation_unit import JoinCompilationUnit


class TopLevelVariableSolc(VariableDeclarationSolc, CallerContextExpression):
    def __init__(
        self,
        variable: TopLevelVariable,
        variable_data: Dict,
        join_parser: "JoinCompilationUnitSolc",
    ) -> None:
        super().__init__(variable, variable_data)
        self._join_parser = join_parser

    @property
    def is_compact_ast(self) -> bool:
        return self._join_parser.is_compact_ast

    @property
    def compilation_unit(self) -> "JoinCompilationUnit":
        return self._join_parser.compilation_unit

    def get_key(self) -> str:
        return self._join_parser.get_key()

    @property
    def join_parser(self) -> "JoinCompilationUnitSolc":
        return self._join_parser

    @property
    def underlying_variable(self) -> TopLevelVariable:
        # Todo: Not sure how to overcome this with mypy
        assert isinstance(self._variable, TopLevelVariable)
        return self._variable
