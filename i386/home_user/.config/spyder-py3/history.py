# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

##---(Mon Jul 10 17:22:44 2017)---
from sympy import *
A = Matrix([[1,3,5], [2,1,1], [4,1,0]])
P, L, D, U = A.LUdecompositionFF()
P, L, D, U
P
init_printing(use_latex = 'mathjax')
P
clear
P, L, D, U
L, U , p = A.LUdecomposition()
L, U , p
L, U , p = A.LUdecomposition_Simple()
L, p = A.LUdecomposition_Simple()
L, p
clear
L, U , _ = A.LUdecomposition_Simple()
clear
L, U , _ = A.LUdecomposition()
L * U == A
U