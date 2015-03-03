# fenqi

Amortization calculator for loans or creditcards. It also calculates correctly when change/adjustment occurs upon the remaining principal, remaining terms and interest rate. That saying, this is an utility for your plan, adjustment and decision.

= Just change the plans in script as your own plans, =
### interest rate hisotry of china : http://data.bank.hexun.com/ll/dkll.aspx?page=1

## plan item format : (DATE initial or adjust, PRINCIPAL initial or adjust, MONTHS initial or adjust, INTEREST rate by month)

ex.
plans = [
    ## date(Y,M,D), $500k, months of 20 years, monthly interest rate by percentage.
    (datetime.date(2013,4,27), 500000, 20*12, 6.55/12.0/100.0),              
    (datetime.date(2015,1,27), 0,0, 6.15/12.0/100.0),
    (datetime.date(2015,4,27), 0-200000,0-10*12, 6.15/12.0/100.0),
    ]

look the 3rd item, there are adjustments on the principal (pay 20K in advance) and terms (reduced 10 years in term).


python 2.7+ required.

