# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

import time

times_x = [0] * 10
times_y = [0] * 10  # inicializa os tempos de ruídos
ranges = list(range(25, 500, 50)) # essa iteração é para definir os centros das bolas de diâmetro 50 * noise. [25, 75, 125, 175...]

def setup():
    size(500, 500)
    frameRate(10)

def draw():
    background(10) # limpa a tela

    for i, x in enumerate(ranges):  # cria matriz de bolas
        noise_x = noise(times_x[i])
        noise_y = noise(times_y[i])
        e_width = 45 * noise_x
        e_height = 45 * noise_x  # o diâmetro das bolas vai ser sempre derivado do noise de x

        for j, y in enumerate(ranges):
            position_sum = i + j  # isso é para deixar de plotar as bolas nos cantos superior esquerdo e inferior direito

            if 0 < i <= 9:
                p_radius = p_height / 2
                if p_radius > 12:
                    continue

                px = ranges[i-1]
                py1 = y + p_radius
                py2 = y - p_radius  # tem que mudar pra ser o ponto
                if 4 < position_sum <= 14:
                    line(px, py1, x, y - e_height / 2)
                    line(px, py2, x, y + e_height / 2)

            if 4 <= position_sum <= 14:
                ellipse(x, y, e_width, e_height)

            rgb = [255 * noise_x, 255 * noise_y, 200 * noise_x]  # mantenho o vermelho fixo, vario o verde com X e o azul com Y
            fill(*rgb)
            stroke(*rgb) # "escondo" as bordas dos círculos
        p_height = e_height

    for i in range(9, -1, -1):
        if i == 0:
            times_x[i] += 0.11
            times_y[i] += 1   # a posição 0 inicializa o movimento de onda
        else:
            times_x[i] = times_x[i - 1]
            times_y[i] = times_y[i - 1]  # a onda se propaga sempre propagando o valor do índice anterior
