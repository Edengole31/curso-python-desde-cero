import pandas as pd

data = {
    "Piezas": ["Llave de tuerca", "Llave francesa", "Destornillador plano", "Destornillador phillips",
               "Pinza universal", "Alicate de corte", "Llave tubo", "Martillo",
               "Cinta métrica", "Sierra manual", "Gato hidráulico", "Compresor de aire",
               "Manómetro", "Torquímetro", "Foco portátil", "Caja de herramientas"],

    "Centimetros": [33, 28, 15, 16, 18, 19, 20, 30,
                    500, 40, 35, 60, 10, 38, 22, 45]
}

df = pd.DataFrame(data)

df.to_excel("herramientas_medidas.xls",index=False)

