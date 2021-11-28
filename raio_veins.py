# -*- coding: utf-8 -*-
# Calcula raio de transmissao em metros

import os
import sys
import math

T = float(input('(T) Sensitivity (dBm): '))
P = float(input('(P) TxPower (mW): '))

d = 0.00404913 * pow(10, (-T/20)) * math.sqrt(P)

print('Raio (m):',"{:.2f}".format(d))