"""
Special variable to model import with renaming
"""
from typing import Union

from join.core.declarations.import_and_pragma.import_directive import Import
from join.core.declarations.contract.contract import Contract
from join.core.declarations.variables.solidity_variables import SolidityVariable
from join.core.declarations.solidity_type.element_type import ElementaryType
from join.core.declarations.variables.variable import Variable


class SolidityImportPlaceHolder(Variable):
    """
    Placeholder for import on top level objects
    See the example at https://blog.soliditylang.org/2020/09/02/solidity-0.7.1-release-announcement/
    In the long term we should remove this and better integrate import aliases
    """

    def __init__(self, import_directive: Import) -> None:
        super().__init__()
        assert import_directive.alias is not None
        self._import_directive = import_directive
        self._name = import_directive.alias
        self._type = ElementaryType("string")
        self._initialized = True
        self._visibility = "private"
        self._is_constant = True

    @property
    def type(self) -> ElementaryType:
        return ElementaryType("string")

    def __eq__(self, other: Union[Contract, SolidityVariable]) -> bool:
        return (
            self.__class__ == other.__class__
            and self._import_directive.filename == self._import_directive.filename
        )

    @property
    def import_directive(self) -> Import:
        return self._import_directive

    def __hash__(self):
        return hash(str(self.import_directive))