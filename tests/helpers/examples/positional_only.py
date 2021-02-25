from dependencies import value


class Foo:
    def __init__(self, a, /, b):
        pass  # pragma: no cover


@value
def foo(a, /, b):
    pass  # pragma: no cover
