gross_income=float(input("enter the gross income to the nearest penny: $"))
dependents=int(input("enter no of dependents  :"))

taxable_amount=gross_income-10000-(dependents*3000)
income_tax=taxable_amount*0.2

print("Income Tax is $",income_tax)
