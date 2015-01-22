# a few variables to initialize
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

# this function calculates the product of balance and monthlyPaymentRate
def monthlyPayment(balance, monthlyPaymentRate):
    return balance * monthlyPaymentRate

# the meat of the code when we do most of the computations
# the logic is very simple, at the end of each month just pay the minimum amount of money
for month in range(1,13):
    totalPaid += round(monthlyPayment(balance, monthlyPaymentRate), 2)
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(monthlyPayment(balance, monthlyPaymentRate), 2))
    balance = round(balance + balance * (annualInterestRate/12), 2)
    balance = round(balance - monthlyPayment(balance, monthlyPaymentRate), 2)
    print 'Remaining balance: ' + str(balance)
    
print 'Total paid: ' + str(totalPaid)  
print 'Remaining balance: ' + str(balance)  