#!/usr/bin/env python3

"""
Author: Guilherme Viegas
Name: Main function
Purpose: Get predictions of house prices in São José - SC
"""

import os.path

from scrap_class import VR
from rf_model_class import RF

# Main function
def main():
    if not os.path.isfile('data/sj_imoveis_scraped.csv'):
        primeira_pagina='https://www.vivareal.com.br/venda/santa-catarina/sao-jose/apartamento_residencial/'
        vr = VR(primeira_pagina)
        vr.run(200)
    
    RFobject = RF(df_address='data/sj_imoveis_scraped.csv')
    RFobject.run()
    RFobject.make_prediction([80, 1, 1, 1])
    print(RFobject.prediction_txt)

    
if __name__ == '__main__':
    main()
