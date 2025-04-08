"""
Para un cohete, se recabaron los datos siguientes de la distancia recorrida versus el tiempo:


t(s)
0	25	50	75	100	125
y (km)
0	32	58	78	92	100

Use diferenciación numérica para estimar la velocidad en t=50
"""
h = 25
x0 = 50
x_t = {
    0:0,
    25:32,
    50:58,
    75:78,
    100:92,
    125:100
}

diff_atras = 