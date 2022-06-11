import sys
import os


def prime(s):
  num = int(s)
  if num == 2:
    return True
  for i in range(2, num):
    if num % i == 0:
      return False
  else:
    return True
    

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
