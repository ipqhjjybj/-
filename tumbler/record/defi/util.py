import os
import json
import functools
from typing import Union, List, Tuple

from web3 import Web3

from .types import AddressLike, Address, Contract
from .exceptions import InvalidToken


def str_to_addr(s: Union[AddressLike, str]) -> Address:
    """Idempotent"""
    if isinstance(s, str):
        if s.startswith("0x"):
            return Address(bytes.fromhex(s[2:]))
        else:
            raise Exception(f"Couldn't convert string '{s}' to AddressLike")
    else:
        return s


def addr_to_str(a: AddressLike) -> str:
    if isinstance(a, bytes):
        # Address or ChecksumAddress
        addr: str = Web3.toChecksumAddress("0x" + bytes(a).hex())
        return addr
    elif isinstance(a, str) and a.startswith("0x"):
        addr = Web3.toChecksumAddress(a)
        return addr

    raise InvalidToken(a)


def is_same_address(a1: Union[AddressLike, str], a2: Union[AddressLike, str]) -> bool:
    return str_to_addr(a1) == str_to_addr(a2)


def validate_address(a: AddressLike) -> None:
    assert addr_to_str(a)


def load_abi(name: str) -> str:
    path = f"{os.path.dirname(os.path.abspath(__file__))}/assets/"
    with open(os.path.abspath(path + f"{name}.abi")) as f:
        abi: str = json.load(f)
    return abi


@functools.lru_cache()
def load_contract(w3: Web3, abi_name: str, address: AddressLike) -> Contract:
    address = Web3.toChecksumAddress(address)
    return w3.eth.contract(address=address, abi=load_abi(abi_name))


def load_contract_erc20(w3: Web3, address: AddressLike) -> Contract:
    return load_contract(w3, "erc20", address)


def _encode_path(token_in: AddressLike, route: List[Tuple[int, AddressLike]]) -> bytes:
    """
    Needed for multi-hop swaps in V3.

    https://github.com/Uniswap/uniswap-v3-sdk/blob/1a74d5f0a31040fec4aeb1f83bba01d7c03f4870/src/utils/encodeRouteToPath.ts
    """
    raise NotImplementedError
