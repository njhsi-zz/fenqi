#!/bin/env python

'''
Fenqi aka amortization calculator for loan and credicards.
'''

def amortizationSchedule( principal, term, rate ):
   pmt = ( principal * rate * ( 1 + rate)**term ) / (( 1 + rate)**term - 1)
   pmt = round(pmt,2) # people rarely pay in fractional pennies
   remainingPrincipal = principal
   for pd in range(1,term+1):
      if pd < term:
          pdInterest = rate * remainingPrincipal
          pdInterest = round(pdInterest,2)
          pdPmt = pmt
      else:
          pdInterest = 0
          pdPmt = remainingPrincipal
      pdPrincipal = pdPmt - pdInterest
      remainingPrincipal -= pdPrincipal
      yield pd, pdPmt, pdInterest, pdPrincipal, remainingPrincipal
 
 
 

 
##################################
#from monthdelta import MonthDelta
import datetime
## copied this from MonthDelta
def MonthAddN(other, n): 
      day = other.day
      # subract one because months are not zero-based
      month = other.month + n - 1
      year = other.year + month // 12
      # now add it back
      month = month % 12 + 1
      if month == 2:
          if day >= 29 and not year%4 and (year%100 or not year%400):
              day = 29
          elif day > 28:
              day = 28
      elif month in (4,6,9,11) and day > 30:
          day = 30
      try:
          return other.replace(year, month, day)
      except ValueError:
          raise OverflowError('date value out of range')


## plan : (Date, Principal, Months, Interest rate by month)
### interest rate hisotry of china : http://data.bank.hexun.com/ll/dkll.aspx?page=1
plans_f = [
    (datetime.date(2009,4,20), 360000, 15*12, 3.87/12.0/100.0),
    (datetime.date(2011,1,20), 0,0, 4.30/12.0/100.0),
    (datetime.date(2012,1,20), 0,0, 4.90/12.0/100.0),
    (datetime.date(2013,1,20), 0,0, 4.50/12.0/100.0),
    (datetime.date(2015,1,20), 0,0, 4.20/12.0/100.0),
    ]
plans_f = [
    (datetime.date(2013,4,27), 570000,20*12, 6.55/12.0/100.0),
    (datetime.date(2015,1,27), 0,0, 6.15/12.0/100.0),
    (datetime.date(2015,4,27), 0-200000,0-10*12, 6.15/12.0/100.0),
    ]

plans = plans_f

## term : <date: (remaining n terms, pay, principal part of pay, remaining principal)>
terms = {}
D,P,N,I =0,0,0,0
for (pD, pP, pN, pI) in plans:
    (N,fdsaf,dsaf,P) = terms.get(MonthAddN(pD,-1),(0,0,0,0))    
    terms = {d:terms[d] for d in terms if d<pD}
    D, P, N, I = pD, P+pP, N+pN, pI

    print("------------",D, P, N, I)

    for(i, pmt, int, princ, remaining) in amortizationSchedule(P, N, I):
        terms[MonthAddN(D,(i-1))] = (N-i, round(pmt,2), round(princ,2), round(remaining,2))
    

##############################
paid_principal, paid_interest = 0, 0

l = sorted(terms.keys())
for d in l:
  paid_principal, paid_interest = round(paid_principal+terms[d][2],2), round(paid_interest+(terms[d][1]-terms[d][2]),2)
  print(d, terms[d], "PaidAll:", round(paid_principal+paid_interest,2), "PaidInt:", paid_interest)
