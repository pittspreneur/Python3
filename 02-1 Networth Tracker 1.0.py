'''This is the first version of the Networth Tracker'''

#Input_Variables
inputDate = " "
wamWF = 0.0
americanExpress = 0.0
collegeCashBack = 0.0
stashInvest = 0.0
stashSpend = 0.0
acornsInvest = 0.0
acornsLater = 0.0
acornsSpend = 0.0
albert = 0.0
digitRainyDay = 0.0
digitLoanOperations = 0.0
digitCreditCard = 0.0
fundrise = 0.0
robinhood = 0.0
ceteria = 0.0
coinbaseCrypto = 0.0
regionsLoan = 0.0
userResponse = " "


#User_Input
inputDate = input('Input Date (xx-xx-xx): ')
wamWF = float(input('WAM Account Balance: $'))
americanExpress = float(input('American Express Account Balance: $'))
collegeCashBack = float(input('College Cash Back Account Balance: $'))
stashInvest = float(input('Stash Invest Account Balance: $'))
stashSpend = float(input('Stash Spend Account Balance: $'))
acornsInvest = float(input('Acorns Invest Account Balance: $'))
acornsLater = float(input('Acorns Later Account Balance: $'))
acornsSpend = float(input('Acorns Spend Account Balance: $'))
albert = float(input('Albert Account Balance: $'))
digitRainyDay = float(input('Digit Rainy Day Account Balance: $'))
digitLoanOperations = float(input('Digit Loan Operations Account Balance: $'))
digitCreditCard = float(input('Digit Credit Card Account Balance: $'))
fundrise = float(input('Fundrise Account Balance: $'))
robinhood = float(input('Robinhood Account Balance: $'))
ceteria = float(input('Ceteria Account Balance: $'))
coinbaseCrypto = float(input('Coinbase Account Balance: $'))
regionsLoan = float(input('Regions Loan Account Balance: $'))

print("...")
print("...")
print("...")

#Yes_No_Loop
userResponse = input("Type 'Yes' and press enter if your data is correct. If not, press enter.")
if userResponse == "Yes" or userResponse == "Y" or userResponse == "y":
    print()
    print()
    print("Calculating...")
    print()
    print("Calculating...")
    print()
    print("Calculating...")
else:
    quit()

print()

#Calculations_and_Currency_Conversions
cashBalance = (wamWF + stashSpend + acornsSpend + albert + digitRainyDay + digitCreditCard + digitLoanOperations)
retirementBalance = (acornsLater + ceteria)
assets = (wamWF + stashInvest + stashSpend + acornsInvest + acornsSpend + acornsLater + albert
+ digitRainyDay + digitCreditCard + digitLoanOperations + fundrise + robinhood + ceteria + coinbaseCrypto )
liabilities = (americanExpress + collegeCashBack)
netWorth = (assets - liabilities)


wamWFFormat = "{:,.2f}".format(wamWF)
americanExpressFormat = "{:,.2f}".format(americanExpress)
collegeCashBackFormat = "{:,.2f}".format(collegeCashBack)
stashInvestFormat = "{:,.2f}".format(stashInvest)
stashSpendFormat = "{:,.2f}".format(stashSpend)
acornsInvestFormat = "{:,.2f}".format(acornsInvest)
acornsLaterFormat = "{:,.2f}".format(acornsLater) 
acornsSpendFormat = "{:,.2f}".format(acornsSpend)
albertFormat = "{:,.2f}".format(albert)
digitRainyDayFormat = "{:,.2f}".format(digitRainyDay)
digitLoanOperationsFormat = "{:,.2f}".format(digitLoanOperations)
digitCreditCardFormat = "{:,.2f}".format(digitCreditCard)
fundriseFormat = "{:,.2f}".format(fundrise)
robinhoodFormat = "{:,.2f}".format(robinhood)
ceteriaFormat = "{:,.2f}".format(ceteria)
coinbaseCryptoFormat = "{:,.2f}".format(coinbaseCrypto) 
regionsLoanFormat = "{:,.2f}".format(regionsLoan)
cashBalanceFormat = "{:,.2f}".format(cashBalance)
retirementBalanceFormat = "{:,.2f}".format(retirementBalance)
assetsFormat = "{:,.2f}".format(assets)
liabilitiesFormat = "{:,.2f}".format(liabilities)
netWorthFormat = "{:,.2f}".format(netWorth)




#Screenshot Lines
print("|                                                |")
print()
print()

#Payload
print("    Date: " + str(inputDate) + "") 
print()
print()

print("    Accounts")
print("    WAM Balance................$" + str(wamWFFormat) + "")
print("    American Express Balance...$" + str(americanExpressFormat) + "")
print("    College Cash Back Balance..$" + str(collegeCashBackFormat) + "")
print("    Stash Invest Balance.......$" + str(stashInvestFormat) + "")
print("    Stash Spend Balance........$" + str(stashSpendFormat) + "")
print("    Acorns Invest Balance......$" + str(acornsInvestFormat) + "")
print("    Acorns Later Balance.......$" + str(acornsLaterFormat) + "")
print("    Acorns Spend Balance.......$" + str(acornsSpendFormat) + "")
print("    Albert Balance.............$" + str(albertFormat) + "")
print("    Digit Rainy Day Balance....$" + str(digitRainyDayFormat) + "")
print("    Digit Loan Ops Balance.....$" + str(digitLoanOperationsFormat) + "")
print("    Digit Credit Card Balance..$" + str(digitCreditCardFormat) + "")
print("    Fundrise Balance...........$" + str(fundriseFormat) + "")
print("    Robinhood Balance..........$" + str(robinhoodFormat) + "")
print("    Ceteria Balance............$" + str(ceteriaFormat) + "")
print("    Coinbase Balance...........$" + str(coinbaseCryptoFormat) + "")
print("    Regions Loan Balance.......$" + str(regionsLoanFormat) + "")

print()
print()

print("    Statistics")
print("    Cash Balance...............$"+ str(cashBalanceFormat) + "")

print("    Retirement Balance.........$"+ str(retirementBalanceFormat) + "")

print("    Assets Balance.............$"+ str(assetsFormat) + "")

print("    Liabilities Balance........$"+ str(liabilitiesFormat) + "")

print()
print()


print("    Networth...................$"+ str(netWorthFormat) + "")


#Screenshot Lines
print()
print("    Networth Tracker 1.0")
print()
print("|                                                |")































