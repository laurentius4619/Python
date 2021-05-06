class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
        


a = FourCal()
b = FourCal()

a.setdate(4,2)
b.setdate(3,7)
print(a.first)
print(a.second)
print(b.first)
print(b.second)

print(id(a.first))
print(id(b.first))
