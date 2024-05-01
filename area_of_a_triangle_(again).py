import math

s1 = int(input('Side one length: '))
s2 = int(input('Side two length: '))
s3 = int(input('Side three length: '))

s = (s1+s2+s3) / 2

a = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

print(f'Area: {a}')