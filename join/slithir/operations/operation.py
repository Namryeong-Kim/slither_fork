import abc
from typing import Any, List, Optional, TYPE_CHECKING
from join.core.declarations.context.context import Context
from join.core.expressions.expression import Expression
from join.core.declarations.variables.variable import Variable
from join.utils.unroll import unroll

if TYPE_CHECKING:
    from join.core.compilation_unit import JoinCompilationUnit
    from join.core.cfg.node import Node


class AbstractOperation(abc.ABC):
    @property
    @abc.abstractmethod
    def read(self):
        """
        Return the list of variables READ
        """
        pass  # pylint: disable=unnecessary-pass

    @property
    @abc.abstractmethod
    def used(self):
        """
        Return the list of variables used
        """
        pass  # pylint: disable=unnecessary-pass


class Operation(Context, AbstractOperation):
    def __init__(self) -> None:
        super().__init__()
        self._node: Optional["Node"] = None
        self._expression: Optional[Expression] = None

    def set_node(self, node: "Node") -> None:
        self._node = node

    @property
    def node(self) -> "Node":
        assert self._node
        return self._node

    @property
    def compilation_unit(self) -> "JoinCompilationUnit":
        return self.node.compilation_unit

    @property
    def used(self) -> List[Variable]:
        """
        By default used is all the variables read
        """
        return self.read

    # if array inside the parameters
    @staticmethod
    def _unroll(l: List[Any]) -> List[Any]:
        return unroll(l)

    def set_expression(self, expression: Expression) -> None:
        self._expression = expression

    @property
    def expression(self) -> Optional[Expression]:
        return self._expression
