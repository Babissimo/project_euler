def even_fib_gen(limit):
    import math
    even_fibs=[]
    n=1
    while round((((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5))<limit:
        if round((((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5))%2==0:
            even_fibs.append(round((((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5)))
        n+=1
    return even_fibs
print(sum(even_fib_gen(4000000)))
