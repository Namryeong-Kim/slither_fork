from typing import TYPE_CHECKING, Optional
from join.core.declarations.variables.variable import Variable


if TYPE_CHECKING:
    from join.core.declarations.structure.structure import Structure


class StructureVariable(Variable):
    def __init__(self) -> None:
        super().__init__()
        self._structure: Optional["Structure"] = None

    def set_structure(self, structure: "Structure") -> None:
        self._structure = structure

    @property
    def structure(self) -> "Structure":
        return self._structure
