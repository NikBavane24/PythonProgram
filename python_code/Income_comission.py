


def Salary(Mon_income):
    if Mon_income>=50000:
        Commission=375+((Mon_income*16)/100)

    elif Mon_income>=40000 and Mon_income<=49999:
        Commission = 370 + ((Mon_income * 14) / 100)

    elif Mon_income>=30000 and Mon_income<=39999:
        Commission = 325 + ((Mon_income * 12) / 100)

    elif Mon_income>=20000 and Mon_income<=29999:
        Commission = 300 + ((Mon_income * 9) / 100)

    elif Mon_income>=10000 and Mon_income<=19999:
        Commission = 250 + ((Mon_income * 5) / 100)

    else:
        Commission = 200 + ((Mon_income * 3) / 100)

    print(f"Commission for {Mon_income} sale is=",Commission)

Salary(45000)