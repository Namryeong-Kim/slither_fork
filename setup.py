from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="join-static-analyzer",
    description="join is a Solidity static analysis framework written in Python 3.",
    url="https://github.com/crytic/slither",
    author="Trail of Bits",
    version="0.9.3",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "packaging",
        "prettytable>=3.3.0",
        "pycryptodome>=3.4.6",
        # "crytic-compile>=0.3.1,<0.4.0",
        "crytic-compile@git+https://github.com/crytic/crytic-compile.git@dev#egg=crytic-compile",
        "web3>=6.0.0",
        "eth-abi>=4.0.0",
        "eth-typing>=3.0.0",
        "eth-utils>=2.1.0",
    ],
    extras_require={
        "lint": [
            "black==22.3.0",
            "pylint==2.13.4",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "deepdiff",
            "numpy",
            "coverage[toml]",
            "filelock",
            "pytest-insta",
            "solc-select@git+https://github.com/crytic/solc-select.git@query-artifact-path#egg=solc-select",
        ],
        "doc": [
            "pdoc",
        ],
        # "dev": [
        #     "slither-analyzer[lint,test,doc]",
        #     "openai",
        # ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "join = join.__main__:main",
        ]
    },
)
