from enum import Enum
class Assignment(Enum):
    ASSIGN = 0  # =
    ASSIGN_OR = 1  # |=
    ASSIGN_CARET = 2  # ^=
    ASSIGN_AND = 3  # &=
    ASSIGN_LEFT_SHIFT = 4  # <<=
    ASSIGN_RIGHT_SHIFT = 5  # >>=
    ASSIGN_ADDITION = 6  # +=
    ASSIGN_SUBTRACTION = 7  # -=
    ASSIGN_MULTIPLICATION = 8  # *=
    ASSIGN_DIVISION = 9  # /=
    ASSIGN_MODULO = 10  # %=

class Binary(Enum):
    POWER = 0  # **
    MULTIPLICATION = 1  # *
    DIVISION = 2  # /
    MODULO = 3  # %
    ADDITION = 4  # +
    SUBTRACTION = 5  # -
    LEFT_SHIFT = 6  # <<
    RIGHT_SHIFT = 7  # >>>
    AND = 8  # &
    CARET = 9  # ^
    OR = 10  # |
    LESS = 11  # <
    GREATER = 12  # >
    LESS_EQUAL = 13  # <=
    GREATER_EQUAL = 14  # >=
    EQUAL = 15  # ==
    NOT_EQUAL = 16  # !=
    ANDAND = 17  # &&
    OROR = 18  # ||

    # YUL specific operators
    # TODO: investigate if we can remove these
    # Find the types earlier on, and do the conversion
    DIVISION_SIGNED = 19
    MODULO_SIGNED = 20
    LESS_SIGNED = 21
    GREATER_SIGNED = 22
    RIGHT_SHIFT_ARITHMETIC = 23

class BinaryConst:
    POWER = "**"
    MULTIPLICATION = "*"
    DIVISION = "/"
    MODULO = "%"
    ADDITION = "+"
    SUBTRACTION = "-"
    LEFT_SHIFT = "<<"
    RIGHT_SHIFT = ">>"
    AND = "&"
    CARET = "^"
    OR = "|"
    LESS = "<"
    GREATER = ">"
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="
    EQUAL = "=="
    NOT_EQUAL = "!="
    ANDAND = "&&"
    OROR = "||"


class Unary(Enum):
    BANG = 0  # !
    TILD = 1  # ~
    DELETE = 2  # delete
    PLUSPLUS_PRE = 3  # ++
    MINUSMINUS_PRE = 4  # --
    PLUSPLUS_POST = 5  # ++
    MINUSMINUS_POST = 6  # --
    PLUS_PRE = 7  # for stuff like uint(+1)
    MINUS_PRE = 8  # for stuff like uint(-1)