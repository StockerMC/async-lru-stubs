from functools import _CacheInfo
from typing import overload, Callable, TypeVar, Coroutine, Any, Protocol, Hashable
from typing_extensions import ParamSpec

_T = TypeVar('_T', contravariant=True)
_P = ParamSpec('_P')
_Coro = Coroutine[Any, Any, _T]

__version__: str

class _wrapped_alru_cache(Protocol[_P, _T]):
    _origin: Callable[_P, _Coro[_T]]
    closed: bool
    async def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _T: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    def invalidate(self, *args: Hashable, **kwargs: Hashable) -> bool: ...
    def close(self, *, cancel: bool = ..., return_exceptions: bool = ...) -> _Coro[list[_T]]: ...
    def open(self) -> None: ...

@overload
def alru_cache(
    fn: None = ...,
    maxsize: int | None = ...,
    typed: bool = ...,
    *,
    cache_exceptions: bool = ...,
) -> Callable[[Callable[_P, _Coro[_T]]], _wrapped_alru_cache[_P, _T]]: ...

@overload
def alru_cache(
    fn: Callable[_P, _Coro[_T]],
    maxsize: int | None = ...,
    typed: bool = ...,
    *,
    cache_exceptions: bool = ...,
) -> _wrapped_alru_cache[_P, _T]: ...

def alru_cache(
    fn: Callable[_P, _Coro[_T]] | None = ...,
    maxsize: int | None = ...,
    typed: bool = ...,
    *,
    cache_exceptions: bool = ...,
) -> Callable[[Callable[_P, _Coro[_T]]], _wrapped_alru_cache[_P, _T]] | _wrapped_alru_cache[_P, _T]: ...

def unpartial(fn: Any) -> Any: ...
