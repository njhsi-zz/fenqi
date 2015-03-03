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
import datetime
import monthdelta

P,Y,R,I,detail = 360000,15,3.87,6000,1
## (Date, Principal, Months, Interest rate)
plans = [
    (datetime.date(2009,4,1), 360000, 15*12, 3.87/12.0/100.0),
    ]

## <date: (pay, principal part of pay, interest part of pay, remaining principal)>
terms = {}
D,P,N,I =0,0,0,0
for (pD, pP, pN, pI) in plans:    
    D, P, N, I = pD, P+pP, N+pN, pI    
    for(i, pmt, int, princ, remaining) in amortizationSchedule(P, N, I):
        terms[D+monthdelta.MonthDelta(i)] = (pmt, princ, int, remaining)
    #todo: remove terms after D


    
for t in terms:
  print(t, terms[t])
