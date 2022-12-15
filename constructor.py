class Build:
    tax_percentage = 10 #class variable

    def __init__(self,a,b):
        self.salary_income=a
        self.outside_income=b
        print("Hi")

    def Income(self):
        print("Salary Income is", self.salary_income)
        print("Outside Income is", self.outside_income)
        print("Tax percentage is", self.tax_percentage)

obj = Build(200000,30000)
obj.Income()
