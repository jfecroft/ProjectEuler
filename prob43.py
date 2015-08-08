from itertools import permutations

NUMS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
MULTS = (2, 3, 5, 7, 11, 13, 17)

def checks(num):
    for i, j in zip(range(1, 7+1), MULTS):
        if int("".join((num[i], num[i+1], num[i+2]))) % j != 0:
            return False
    return True

def main():
    total = 0
    for i in permutations(NUMS):
        if checks(i):
            total += int("".join(x for x in i))
    print total


if __name__ == "__main__":
    main()
