# -*- coding: utf-8 -*-
"""Klinkenberg Effect

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mfTfgRP4WsQt-k7xXBGTub757IFJKvpM

### Klinkenberg Effect

Klinkenberg Effect can be used to calculate the absolute permeability when
 only one gas permeability measurement (kg) of a core sample is made at
 pm.

 6.9*kL^(0.64) + pm*kL- pm*kg = 0

This nonlinear equation can be solved iteratively by using the **Newton-Raphson** iterative methods. The proposed solution method can be conveniently written as:

Ki+1=ki-f(x)/f'(x)

Above equation  can be written as,

f(x) = 6.9*kL^(0.64) + pm*kL- pm*kg

f'(x) = 4.416*(kl)**(-0.36)+2.152

# Example 4-10 (Tarek Ahmed)




The permeability of a core plug is measured by air. Only one measure
ment is made at a mean pressure of 2.152 psi. The air permeability is
46.6 md. Estimate the absolute permeability of the core sample. Compare
the result with the actual absolute permeability of 23.66 md.
"""

import matplotlib.pyplot as plt
kl=int(input("Write your initial guess  for Kl value: "))
n=int(input("Total number of iteration need to perform: "))
k_plot=[]

# f(x) = 6.9kL^(0.64) + pmkL- pm*kg
# f'(x) = 4.416(kl)*(-0.36)+2.152
# Given Pm = 2.152 psi & kg= 46.6 mD
for i in range(n):
  kl=kl - (6.9*(kl)**0.64+2.152*kl-2.152*46.6)/(4.416*(kl)**(-0.36)+2.152)
  k_plot.append(kl)
print(f'Value of absolute permeability is {kl}')

plt.plot(k_plot)
plt.axhline(23.66,color='green')

