#!/usr/bin/env python3

import numpy as np

turns = {
  -1: [0, 1],
  0:  [0,1],
  1:  [-1],
}

n = 3
arr = np.zeros(n)
acc = [0]

def set_person(i):
  if i == n:
    print(list(map(int, arr)))
    acc[0] += 1
    return
  for possible in turns[arr[i-1]]:
    arr[i] = possible
    set_person(i+1)

def main() -> None:
  arr[0] = -1
  set_person(1)
  arr[0] = 0
  set_person(1)
  arr[0] = 1
  set_person(1)

  print(acc[0])

if __name__ == "__main__":
  main()