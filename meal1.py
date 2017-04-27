# Calculating Taxes

meal = 44.50
tax = 0.0675
tip = 0.15

tax = meal * tax
meal = meal + tax
tip = meal * tip
total = tip + meal

print("%.2f" % total)


