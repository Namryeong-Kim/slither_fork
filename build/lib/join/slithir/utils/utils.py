from typing import Union, Optional

from join.core.declarations.variables.local_variable import LocalVariable
from join.core.declarations.variables.state_variable import StateVariable

from join.core.declarations.variables.solidity_variables import SolidityVariable
from join.core.declarations.top_levels.variable_top_level import TopLevelVariable

from join.slithir.variables.temporary import TemporaryVariable
from join.slithir.variables.constant import Constant
from join.slithir.variables.reference import ReferenceVariable
from join.slithir.variables.tuple import TupleVariable
from join.core.source_mapping.source_mapping import SourceMapping

RVALUE = Union[
    StateVariable,
    LocalVariable,
    TopLevelVariable,
    TemporaryVariable,
    Constant,
    SolidityVariable,
    ReferenceVariable,
]

LVALUE = Union[
    StateVariable,
    LocalVariable,
    TemporaryVariable,
    ReferenceVariable,
    TupleVariable,
]


def is_valid_rvalue(v: Optional[SourceMapping]) -> bool:
    return isinstance(
        v,
        (
            StateVariable,
            LocalVariable,
            TopLevelVariable,
            TemporaryVariable,
            Constant,
            SolidityVariable,
            ReferenceVariable,
        ),
    )


def is_valid_lvalue(v: Optional[SourceMapping]) -> bool:
    return isinstance(
        v,
        (
            StateVariable,
            LocalVariable,
            TemporaryVariable,
            ReferenceVariable,
            TupleVariable,
        ),
    )
