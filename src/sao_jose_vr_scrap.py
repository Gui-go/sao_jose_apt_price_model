"""
Scrap of São José SC real state data
"""

from scrap_class import VR


if __name__ == '__main__':
    primeira_pagina='https://www.vivareal.com.br/venda/santa-catarina/sao-jose/apartamento_residencial/'
    vr = VR(primeira_pagina)
    vr.run(200)

