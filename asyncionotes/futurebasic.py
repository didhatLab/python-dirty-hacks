from asyncio import Future


a = Future()

print(f"Is Future done? {a.done()}")

a.set_result(42)

print(f"Is future done? {a.done()}")
print(f"Future result: {a.result()}")
