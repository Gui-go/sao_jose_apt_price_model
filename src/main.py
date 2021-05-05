#!/usr/bin/env python3

"""
Author: Guilherme Viegas
Name: Main function
Purpose: Get predictions of house prices in São José - SC
"""

# Libraries
import os.path

# Functions and classes
from scrap_class import VR

# Main function
def main():
    if not os.path.isfile('data/sj_imoveis_scraped.csv'):
        primeira_pagina='https://www.vivareal.com.br/venda/santa-catarina/sao-jose/apartamento_residencial/'
        vr = VR(primeira_pagina)
        vr.run(200)
    
    # model here _ _ _ _
    

if __name__ == '__main__':
    main()
