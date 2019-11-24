marks=eval(input('Enter your marks:'))

if(marks<35):
    grade='F'
elif(marks<45):
    grade='S'
elif(marks<65):
    grade='C'
elif(marks<75):
    grade='B'
else:
    grade='A'

print('your grade:',grade)
