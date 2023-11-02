from auto_return import auto_return


@auto_return
def foo():
    x = 6
    if None:
        return 87
    else:
        if 0:
            pass
        else:
            for i in range(5, 100):
                pass
            if 0:
                8
            else:
                if 9:
                    42


print(foo())


class Foo:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @auto_return
    def add_coords(self):
        if self.x == 1:
            return 'Foo'
        else:
            self.x + self.y

    @auto_return
    @staticmethod
    def const():
        (1, 2)


f = Foo(2, 4)
print(f.add_coords())
print(f.const())
