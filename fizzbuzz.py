i = 1
r = ''
while(i<=100):
    r = i
    if i%3 == 0: 
        r = "Fizz"
    if i%5 == 0:
        r = "Buzz"
    if i%5 == 0 and i%3 == 0:
        r = "FizzBuzz"
    i += 1
    print(r)
    
    