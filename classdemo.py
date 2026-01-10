class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        # %.2f formats the number to 2 decimal places (e.g., 100.50)
        return "Position = %s, Name = %s, Pay = %.2f" % (self.position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' % (self.name)
        hours = input(prompt)
        
        prompt = 'Enter the hourly rate for %s: ' % (self.name)
        hourlyRate = input(prompt)
        
        # Changed int() to float() to allow decimals (e.g., 12.50 or 40.5 hours)
        self.pay = float(hours) * float(hourlyRate)
        return self.pay