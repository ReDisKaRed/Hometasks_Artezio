def carry(func):

    def curry(*args):
        if len(args) == func.__code__.co_argcount:
            ans = func(*args)
            return ans
        else:
            return lambda *x: curry(*(args+x))
    return curry


@carry
def foo(a, b, c):
    return a + b + c


print(foo(1)(6)(7))
