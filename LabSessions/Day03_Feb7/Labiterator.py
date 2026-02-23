#custom iterator that prints numbers from 1 to 5
class OnetoFive:
    def __init__(self):
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 5:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
for number in OnetoFive():
    print(number)
