"""
La policía descubre el cuerpo de un inversionista. Para resolver el crimen es decisivo
determinar cuando se cometió el homicidio. El forense llegó al medio día y de
inmediato observa que la temperatura del cuerpo es de 30◦ C . Así mismo, observa que
la temperatura de la habitación es constante a 27◦ C . Suponiendo que la temperatura
de la víctima era normal en el momento de su fallecimiento (37◦ C ), determinar la
hora en que se cometió el crimen. La ecuación diferencial es:
dT/dt = k(T − Ta )

con k = −0.4056
"""

#UTILIZANDO DIFERENCIACION HACIA ATRÁS

Temperaturas = [30]
h = 0.1
Tf = 37
k = -0.4056
Ta = 27

while (Temperaturas[-1] < Tf):
    Temperaturas.append(-h*(k*(Temperaturas[-1]-Ta)) + Temperaturas[-1])
print(Temperaturas[-1])
print(12 - (len(Temperaturas) * h))

