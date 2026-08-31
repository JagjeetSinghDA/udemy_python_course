# def serve_chai():
#     yield "Cup 1: Masala Chai"
#     yield "Cup 2: Ginger Chai"
#     yield "Cup 3: Elachi Chai"


# stall = serve_chai()

# # for cup in stall:
# #     print(cup)

# print(stall)


def get_chai_list():
    return ["Cup 1", "cup 2", "cup 3"]

# generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
# print(chai)
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai))

print("---------------")
for chai in get_chai_gen():
    print(chai)