s1 = int(input('Enter the 1st side of a triangle: '))
s2 = int(input('Enter the 2nd side of a triangle: '))
s3 = int(input('Enter the 3d side of a triangle: '))

if s1 == s2 == s3:
    print('Your triangle is equilateral.')
elif s1 != s2 == s3 or s1 == s3 != s2 or s1 == s2 != s3:
    print('Your triangle is isosceles.')
elif s1 != s2 != s3:
    print('Your triangle is scalene.')