start_n = int(input(' what is the first number ?'  ))
end_n = int(input('what is the second number ?' ))

if start_n < end_n :
    while start_n <= end_n:
     print(start_n)
     start_n += 1
else :
     while start_n >= end_n:
        print (start_n)
        start_n -= 1
