# Stubs for maxminddb.reader (Python 3)

from ipaddress import IPv4Address, IPv6Address

from types import TracebackType
from typing import Any, Mapping, Optional, Sequence, Type, Union

class Reader:
    closed: bool = ...
    def __init__(self, database: bytes, mode: int = ...) -> None: ...
    def metadata(self) -> Metadata: ...
    def get(self, ip_address: str) -> Optional[Any]: ...
    def close(self) -> None: ...
    def __enter__(self) -> Reader: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]] = ..., exc_val: Optional[BaseException] = ..., exc_tb: Optional[TracebackType] = ...) -> None: ...

class Metadata:
    node_count: int = ...
    record_size: int = ...
    ip_version: int = ...
    database_type: str = ...
    languages: Sequence[str] = ...
    binary_format_major_version: int = ...
    binary_format_minor_version: int = ...
    build_epoch: int = ...
    description: Mapping[str, str] = ...
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def node_byte_size(self) -> int: ...
    @property
    def search_tree_size(self) -> int: ...
