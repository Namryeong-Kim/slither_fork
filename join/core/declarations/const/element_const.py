import itertools

class Elementary:
    Int = [
        "int",
        "int8",
        "int16",
        "int24",
        "int32",
        "int40",
        "int48",
        "int56",
        "int64",
        "int72",
        "int80",
        "int88",
        "int96",
        "int104",
        "int112",
        "int120",
        "int128",
        "int136",
        "int144",
        "int152",
        "int160",
        "int168",
        "int176",
        "int184",
        "int192",
        "int200",
        "int208",
        "int216",
        "int224",
        "int232",
        "int240",
        "int248",
        "int256",
    ]

    Max_Int = {k: 2 ** (8 * i - 1) - 1 if i > 0 else 2**255 - 1 for i, k in enumerate(Int)}
    Min_Int = {k: -(2 ** (8 * i - 1)) if i > 0 else -(2**255) for i, k in enumerate(Int)}

    Uint = [
        "uint",
        "uint8",
        "uint16",
        "uint24",
        "uint32",
        "uint40",
        "uint48",
        "uint56",
        "uint64",
        "uint72",
        "uint80",
        "uint88",
        "uint96",
        "uint104",
        "uint112",
        "uint120",
        "uint128",
        "uint136",
        "uint144",
        "uint152",
        "uint160",
        "uint168",
        "uint176",
        "uint184",
        "uint192",
        "uint200",
        "uint208",
        "uint216",
        "uint224",
        "uint232",
        "uint240",
        "uint248",
        "uint256",
    ]

    Max_Uint = {k: 2 ** (8 * i) - 1 if i > 0 else 2**256 - 1 for i, k in enumerate(Uint)}
    Min_Uint = {k: 0 for k in Uint}


    Byte = [
        "byte",
        "bytes",
        "bytes1",
        "bytes2",
        "bytes3",
        "bytes4",
        "bytes5",
        "bytes6",
        "bytes7",
        "bytes8",
        "bytes9",
        "bytes10",
        "bytes11",
        "bytes12",
        "bytes13",
        "bytes14",
        "bytes15",
        "bytes16",
        "bytes17",
        "bytes18",
        "bytes19",
        "bytes20",
        "bytes21",
        "bytes22",
        "bytes23",
        "bytes24",
        "bytes25",
        "bytes26",
        "bytes27",
        "bytes28",
        "bytes29",
        "bytes30",
        "bytes31",
        "bytes32",
    ]

    Max_Byte = {k: 2 ** (8 * (i + 1)) - 1 for i, k in enumerate(Byte[2:])}
    Max_Byte["bytes"] = None
    Max_Byte["string"] = None
    Max_Byte["byte"] = 255
    Min_Byte = {k: 0 for k in Byte}
    Min_Byte["bytes"] = 0x0
    Min_Byte["string"] = 0x0
    Min_Byte["byte"] = 0x0

    MaxValues = dict(dict(Max_Int, **Max_Uint), **Max_Byte)
    MinValues = dict(dict(Min_Int, **Min_Uint), **Min_Byte)

    # https://solidity.readthedocs.io/en/v0.4.24/types.html#fixed-point-numbers
    M = list(range(8, 257, 8))
    N = list(range(0, 81))
    MN = list(itertools.product(M, N))

    Fixed = [f"fixed{m}x{n}" for (m, n) in MN] + ["fixed"]
    Ufixed = [f"ufixed{m}x{n}" for (m, n) in MN] + ["ufixed"]

    ElementaryTypeName = ["address", "bool", "string", "var"] + Int + Uint + Byte + Fixed + Ufixed