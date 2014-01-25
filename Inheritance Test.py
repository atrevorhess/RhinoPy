class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print self.data

class SecondClass(FirstClass):
    def display(self):
        print 'Current value = "%s"' % self.data

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

class FourthClass(ThirdClass):
    def __init__(self, value):
        self.data = self._format(value)

    def __getattr__(self, object):
        return self.data

    def __str__(self):
        return self.data

    def _format(self, value):
        return 'Current value = "%s"' % value

if __name__ == '__main__':
    x = FirstClass()
    y = ThirdClass('Melissa')
    z = FourthClass('Monica')
    x.setdata('King Arthur')
    y.setdata(3.14159)
    x.display()
    y.display()
    print z