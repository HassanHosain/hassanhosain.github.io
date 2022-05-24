def fizzBuzz(n):
    low_bound=1
    high_bound=n
    #print(low_bound%5)   
    while low_bound<high_bound:
        if low_bound%5==0 and low_bound%3==0:
            print('FizzBuzz')
        elif low_bound%3==0:
            print ('Fizz')
        elif low_bound%5==0:
            print ('Buzz')
        else:
            print(low_bound)
        low_bound += 1