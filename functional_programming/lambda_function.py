# print((lambda n1, n2, n3 : n1**3 + n2**3 + n3**3)(1, 2, 3));


# print((lambda *vargs : sum([i**3 for i in vargs]))(3, 4, 5))

anonymous_func = lambda **var_kargs : f"Hello {var_kargs['name']}, Good morning. Your marks is {var_kargs['marks']}."
print(anonymous_func(name="Md Khateebur Rab", marks=100))