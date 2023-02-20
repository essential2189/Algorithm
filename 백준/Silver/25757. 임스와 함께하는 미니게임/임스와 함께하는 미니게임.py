def solution(person, game):
    if game == "Y":
        return len(person)

    if game == "F":
        return len(person) // 2

    if game == "O":
        return len(person) // 3


n, game = input().split()

person = set()
for _ in range(int(n)):
    person.add(input())


print(solution(person, game))