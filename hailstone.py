def hailstone(answer)
    if answer == 1:
        return 0
    step = 0

    while answer != 1:
        if answer % 2 == 0:
            answer = answer // 2
        elif answer % 2 == 1:
            answer = (answer * 3) + 1
            return answer

answer = hailstone(100)
print(answer)
