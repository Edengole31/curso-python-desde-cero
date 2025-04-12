import pandas as pd

def cm_a_pulgadas(cm):
    return cm/2.56

df = pd.read_excel("herramientas_medidas.xlsx")

#Anadir una columna en pulgadas donde se colocara la conversion

df["pulgadas"]=df["Centimetros"].apply(cm_a_pulgadas)
df.to_excel("herramientas_medidas_pulgadas.xlsx",index=False)
