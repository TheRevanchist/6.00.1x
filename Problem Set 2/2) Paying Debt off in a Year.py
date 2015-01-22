# a few variables to initialize
balance = 3926
annualInterestRate = 0.2
lowestPayment = 0
monthlyInterestRate = annualInterestRate / 12
currentBalance = balance

# do the computation
while currentBalance > 0:
    lowestPayment += 10
    currentBalance = balance
    for month in range(1,13):
        currentBalance -= lowestPayment
        currentBalance = currentBalance + currentBalance * monthlyInterestRate
   
print 'Lowest Payment: ' + str(lowestPayment)    