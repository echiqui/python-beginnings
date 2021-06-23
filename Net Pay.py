'''
This program calculates an employee's net pay, gross pay and tax deduction
'''

name = input("Please enter your name:") #name input gets the employee's name
hours = input("Enter your hours:") #hours input gets employee's hours that was worked
rate = input("Enter your rate per hour:") #rate input gets employee's rate that they get paid per hour
taxrate = (float(hours) * float(rate)) * .10 #will calculate the tax rate of 10% which is writtien as 0.10

if float(hours) <= 40: #if statement to calculate hours equal to or less than 40
    print("Hello", name,"below is the breakdown of your work week") #this line will greet the employee's name 
    print("Your net pay is", (float(hours) * float(rate) - taxrate), "dollars") #calculates the net pay which is the pay minus the taxes that was deducted
    print("Your gross pay is", float(hours) * float(rate), "dollars") #calculates the gross pay which is the pay before taxes is deducted
    print((taxrate), "dollars was deducted in taxes") #prints out the amount of taxes that was deducted
          
elif float(hours) > 40: #else statement to calculate all hours greater than 40
    print("Hello", name,"below is the breakdown of your work week") #this line will greet the employee's name
    print("Your net pay is", ((float(hours) - 40) * (float(rate) *1.5) + 40 * float(rate)) - taxrate, "dollars") #calculates the net pay which is the pay minus the taxes that was deducted
    print("Your gross pay is", (float(hours) - 40) * (float(rate) *1.5) + 40 * float(rate), "dollars") #calculates the gross pay which is the pay before taxes is deducted
    print((taxrate), "dollars was deducted in taxes") #prints out the amount of taxes that was deducted


