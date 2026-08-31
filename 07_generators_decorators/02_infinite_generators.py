def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()
# print(next(refill))
# print(next(refill))
# print(next(refill))
# print(next(refill))
# print(next(refill))

# we can run it with the loop as well as with multiple prints

for _ in range(9):
    print(next(refill))
print("------------------another user------------------")
for _ in range(5):
    print(next(user2))
# for refill in infinite_chai():
#     print(refill)