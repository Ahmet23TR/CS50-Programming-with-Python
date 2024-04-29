while True:
  try: 
    x = int(input("What's x? "))
  except ValueError:
    pass
  else:
    break
print(f"x is {x}")