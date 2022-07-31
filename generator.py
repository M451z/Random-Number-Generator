import random
from loading import *

load()

while True:
  digit = input("How many digits do you want the number to be (max:9999): ")
  try:
    digit = int(digit)
    while not 0<digit<10000:
      print("Please enter a valid digit number. It should be between 0 and 10000.")
      digit = int(input("How many digits do you want the number to be: "))
      if digit>0:
        continue
  except:
    print("Invalid input!")
    exit()
    
  range_start =10**(digit-1)
  range_end = (10**digit)-1
    
  typeofn = input("Press and Enter (1) If You Want It To Be an Integer\nPress and Enter (2) If You Want It To Be a Decimal Number\nPress and Enter (3) If It Doesn't Matter\n")
  
  try:
    typeofn = int(typeofn)
    while not 1<=typeofn<=3:
      print("Please press and enter a valid number. It should be 1,2 or 3.")
      typeofn = int(input("Press and Enter (1) If You Want It To Be an Integer\nPress and Enter (2) If You Want It To Be a Decimal Number\nPress and Enter (3) If It Doesn't Matter\n"))
      if True:
        continue
  except:
    print("Invalid input!")
    exit()
    
  norp = input("Press and Enter (1) If You Want It To Be Positive\nPress and Enter (2) If You Want It To Be Negative\nPress and Enter (3) If It Doesn't Matter\n")
  try:
    norp = int(norp)
    while not 1<=norp<=3:
      print("Please press and enter a valid number. It should be 1,2 or 3.")
      norp = int(input("Press and Enter (1) If You Want It To Be Positive\nPress and Enter (2) If You Want It To Be Negative\nPress and Enter (3) If It Doesn't Matter\n"))
      if True:
        continue
  except:
    print("Invalid input!")
    
  if typeofn == 1:
    if norp == 1:
      randomNumber = random.randint(range_start, range_end)
      print(randomNumber)
    elif norp == 2:
      randomNumber = -random.randint(range_start, range_end)
      print(randomNumber)
    elif norp==3:
      opt1 = random.randint(range_start, range_end)
      opt2 = -random.randint(range_start, range_end)
      olist = [opt1, opt2]
      randomNumber = random.choice(olist)
      print(randomNumber)
      
  if typeofn == 2:
    if norp == 1:
      randomNint = random.randint(range_start, range_end)
      randomNr = str(randomNint).zfill(digit+1)
      randomNumber = randomNr[:1] + "." + randomNr[1:]
      print(randomNumber)
    elif norp == 2:
      randomNint = -random.randint(range_start, range_end)
      randomNr = str(randomNint).zfill(digit+2)
      randomNumber = randomNr[:2] + "." + randomNr[2:]
      print(randomNumber)
    elif norp==3:
      olist = [1, 2]
      choice = random.choice(olist)
      if choice == 1:
        randomNint = random.randint(range_start, range_end)
        randomNr = str(randomNint).zfill(digit+1)
        randomNumber = randomNr[:1] + "." + randomNr[1:]
        print(randomNumber)
      elif choice==2:
        randomNint = -random.randint(range_start, range_end)
        randomNr = str(randomNint).zfill(digit+2)
        randomNumber = randomNr[:2] + "." + randomNr[2:]
        print(randomNumber)
      
    
  elif typeofn == 3:
    tlist = [1, 2]
    choice = random.choice(tlist)
    if choice == 1:
      if norp == 1:
        randomNumber = random.randint(range_start, range_end)
        print(randomNumber)
      elif norp == 2:
        randomNumber = -random.randint(range_start, range_end)
        print(randomNumber)
      else:
        opt1 = random.randint(range_start, range_end)
        opt2 = -random.randint(range_start, range_end)
        olist = [opt1, opt2]
        randomNumber = random.choice(olist)
        print(randomNumber)
    elif choice==2:
      if norp == 1:
        randomNint = random.randint(range_start, range_end)
        randomNr = str(randomNint).zfill(digit+1)
        randomNumber = randomNr[:1] + "." + randomNr[1:]
        print(randomNumber)
      elif norp == 2:
        randomNint = -random.randint(range_start, range_end)
        randomNr = str(randomNint).zfill(digit+2)
        randomNumber = randomNr[:2] + "." + randomNr[2:]
        print(randomNumber)
      elif norp==3:
        olist = [1, 2]
        choice = random.choice(olist)
        if choice == 1:
          randomNint = random.randint(range_start, range_end)
          randomNr = str(randomNint).zfill(digit+1)
          randomNumber = randomNr[:1] + "." + randomNr[1:]
          print(randomNumber)
        elif choice == 2:
          randomNint = -random.randint(range_start, range_end)
          randomNr = str(randomNint).zfill(digit+2)
          randomNumber = randomNr[:2] + "." + randomNr[2:]
          print(randomNumber)
  
    q = input("Press and Enter (0) To Exit\nPress and Enter (1) To Continue\n")
    try:
      q = int(q)
      if q == 0:
        print("Thanks for using...")
        exit()
      elif q ==1:
        print("Restarting...")
        time.sleep(2)
        continue
    except ValueError:
      print("Invalid input!")
      exit()