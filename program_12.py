t1 = (1,2,5,7,9,2,4,6,8,10)
half_value=len(t1)//2
first_half = t1[ :half_value]
print("first_half", first_half)
second_half = t1[half_value: ]
print("second_half", second_half)
t1 = (1,2,5,7,9,2,4,6,8,10)
even_number= tuple(filter (lambda x: x%2==0,t1))
print("tuple with even number", even_number)
t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)
concatenation = (t1 + t2)
print("tuple with concatenation ", concatenation)
t1= (1, 2, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15)
print("maximum value in t1 is ",max(t1))
print("minimum value in t1 is ",min(t1))
