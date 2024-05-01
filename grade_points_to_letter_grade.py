grade = float(input('Enter a grade: '))

grades = {
	4.3 : 'A+',
	4.0 : 'A',
	3.7 : 'A-',
	3.3 : 'B+',
	3.0 : 'B',
	2.7 : 'B-',
	2.3 : 'C+',
	2.0 : 'C',
	1.7 : 'C-',
	1.3 : 'D+',
	1.0 : 'D',
	0   : 'F'
}

if grade in grades:
	print(grades[grade])
elif grade not in grades:
	rounded_grade = round(grade)
	print(grades[rounded_grade])