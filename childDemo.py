from OopsDemo import Demo


class demochild(Demo):

    def __init__(self):
        Demo.__init__(self, 100, 200)


d1 = demochild()
print(d1.summation())