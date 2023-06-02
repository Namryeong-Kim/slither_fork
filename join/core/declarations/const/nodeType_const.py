from enum import Enum

class NodeType(Enum):
    ENTRYPOINT = "ENTRY_POINT"  # no expression

    # Nodes that may have an expression

    EXPRESSION = "EXPRESSION"  # normal case
    RETURN = "RETURN"  # RETURN may contain an expression
    IF = "IF"
    VARIABLE = "NEW VARIABLE"  # Variable declaration
    ASSEMBLY = "INLINE ASM"
    IFLOOP = "IF_LOOP"

    # Nodes where control flow merges
    # Can have phi IR operation
    ENDIF = "END_IF"  # ENDIF node source mapping points to the if/else "body"
    STARTLOOP = "BEGIN_LOOP"  # STARTLOOP node source mapping points to the entire loop "body"
    ENDLOOP = "END_LOOP"  # ENDLOOP node source mapping points to the entire loop "body"

    # Below the nodes do not have an expression but are used to expression CFG structure.

    # Absorbing node
    THROW = "THROW"

    # Loop related nodes
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"

    # Only modifier node
    PLACEHOLDER = "_"

    TRY = "TRY"
    CATCH = "CATCH"

    # Node not related to the CFG
    # Use for state variable declaration
    OTHER_ENTRYPOINT = "OTHER_ENTRYPOINT"