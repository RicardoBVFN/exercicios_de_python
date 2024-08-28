print('calculadora: hipotenusa teorema de pitágoras')
c1 = float(input('digite o comprimento do primeiro cateto: '))
c2 = float(input('dgite o comprimento do segundo cateto: '))
from math import sqrt
h = sqrt(c1 ** 2 + c2 ** 2)
print('a hipotenusa do triângulo cujos catetos medem {} e {} mede {:.1f} unidades métricas'.format(c1, c2, h))
