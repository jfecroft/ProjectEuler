from utils import is_palindrome

def lychrel_number(num, max_rec=50, rec=0):
    if is_palindrome(num):
        return True
    elif rec >= max_rec:
        return False
    else:
        return lychrel_number(num + int(str(num)[::-1]), rec=rec+1) 

def main():
    total = 0
    for i in range(10000):
        total += not lychrel_number(i)
    print total

if __name__ == "__main__":
    main()
