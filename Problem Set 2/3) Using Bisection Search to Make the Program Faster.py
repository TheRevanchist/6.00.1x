# a few variables to initialize
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12

currentBalance = balance
lowerBound = balance / 12.0
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
epsilon = 0.01
payment = 0

# the while loop which does the computation
while currentBalance > epsilon:
    payment = (lowerBound + upperBound) / 2.0
    currentBalance = balance
    for month in range(1, 13):
        currentBalance -= payment
        currentBalance = currentBalance + currentBalance * monthlyInterestRate
    # here we change the upper or lower bound based on the currentBalance.
    # if the currentBalance > 0 that means that our payment is small so we increase the payment
    # if the currentBalance < 0 that means that our payment is big so we decrease it     
    if currentBalance > 0:
        lowerBound = payment
    else:
        upperBound = payment   
        currentBalance = balance
   
print 'Lowest Payment: ' + str(round(payment, 2)) 
         
           

  