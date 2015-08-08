def digit_sum(num):
    num = str(num)
    if not num:
        return 0
    total = int(num[0])
    total += int(digit_sum(num[1:]))
    return total

MAXA = 100
MAXB = 100
def main():
    print max(digit_sum(a**b) for a in range(MAXA+1) for b in range(MAXB+1))


if __name__ == "__main__":
    main()
