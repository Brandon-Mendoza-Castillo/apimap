import math
import random

coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.67775, -103.34625),
    'Monterrey': (25.69161, -100.32183),
    'QuintanaRoo': (21.16311, -86.80231),
    'Michohacan': (19.70140, -101.20829),
    'Aguascalientes': (21.87641, -102.26438),
    'CDMX': (19.43271, -99.13318),
    'QRO': (20.59719, -100.38667)
}

def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i+1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])
    return total

def calcular_ruta(ciudades):
    mejor_ruta = list(ciudades.keys())
    random.shuffle(mejor_ruta)
    mejor_dist = evalua_ruta(mejor_ruta, ciudades)

    for _ in range(100):
        nueva = mejor_ruta[:]
        random.shuffle(nueva)
        dist = evalua_ruta(nueva, ciudades)
        if dist < mejor_dist:
            mejor_ruta = nueva
            mejor_dist = dist

    return mejor_ruta, mejor_dist
