import dataclasses as dt


@dt.dataclass
class Parent:
    name: str
    status: bool = dt.field(default=False, init=False)


@dt.dataclass
class Child(Parent):
    surname: str


child = Child(name="Dan", surname="Didhat")
print(f"status: {child.status}")

print("As result we easily and clearly inherit Parent in Child")
print("However we can not redefine value of status in constructor")
print("Because of this it is dirty, but sometimes even usefull")
print("For excmaple I had such case...")
print("I had sublass <AbstarctCommand> and many impps of this class")
print("This class knew how to execute himself, abc class defined <execute> method")
print("And I needed a field where I could store the result of the execution")
print("So, I just defined field like above")
print("I only needed this field after executing the commnand to know if I needed to run it again")
print("Becaue of this I did not evene need this field in __init__")
