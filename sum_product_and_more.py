number1 = int(input('Enter first number'))
number2 = int(input('Enter second number'))
number3 = int(input('Enter third number'))

sum = number1 + number2 + number3 
print('the sum is :', sum)

average = number1 + number2 + number3 / 3
print('the average is: ', average)

product = number1 * number2 * number3
print('the product is: ', product)

smallest = number1
largest = number1

if( number2 < smallest):smallest = number2
if( number3 < smallest):smallest = number3
print('smallest number is: ', smallest)

if(number2 > largest):largest = number2
if(number3 > largest):largest = number3
print('lagest number is: ', largest)

