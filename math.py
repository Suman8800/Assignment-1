A= int(input('enter your number: '))
B= int(input('enter your number: '))

addition = A + B
subtraction = A - B
multiplication = A * B

if B != 0:
    division = A / B
else:
    division = 'undefined (division by zero)'
print(f'\nResults:')
print(f'Addition: {A} + {B} = {addition}')
print(f'Subtraction: {A} - {B} = {subtraction}')
print(f'Multiplication: {A} * {B} = {multiplication}')
print(f'Division: {A} / {B} = {division}')