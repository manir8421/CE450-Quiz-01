


from operator import add, neg
# lambda function
g = lambda m: (lambda a,b:a(m)+ b(m)) (abs,neg)
print(f"Output is: {g(-123)}")  # Output: 246
