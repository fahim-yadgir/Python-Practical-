def fact_find(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    return fact

print(fact_find(5))