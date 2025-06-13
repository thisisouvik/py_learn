class Person:
    name="Souvik"
    def __len__(self):
        i=0
        for c in self.name:
            i=i + 1
        return i
e=Person()
print(e.name)
print(len(e))