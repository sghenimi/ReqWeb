#from 3.12

from typing import Callable, Iterable

type TaggedTuple[*Ts] = tuple[str, *Ts]

def decorator[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs)
    return wrapper

class Container[T]:
    def __init__(self, items: Iterable[T] = ()):
        self.items = list(items)

    def __getitem__(self, item: int) -> T:
        return self.items[item]

    def __setitem__(self, key: int, value: T) -> None:
        self.items[key] = value

    def __delitem__(self, key: int) -> None:
        del self.items[key]

    def __iter__(self) -> Iterable[T]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.items})"
