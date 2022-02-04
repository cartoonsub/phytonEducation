def s(a, *vs, b=10):
   res = a + b
   print(vs)
   for v in vs:
        res += v
   return res

print((s(11, 10)))