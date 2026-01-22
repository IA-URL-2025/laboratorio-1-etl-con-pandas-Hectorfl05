import pandas as pd

def run_etl():
    """
    Implementa el proceso ETL.
    No cambies el nombre de esta función.
    """
    #Extraccion de la informacion
    df = pd.read_csv('data/citas_clinica.csv')

    #Transofmracion de la informacion

    #Normalizacion de texto
    df["paciente"] = df["paciente"].str.title()
 
    df["especialidad"] = df["especialidad"].str.upper()

    #Fechas
    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"],format="%Y-%m-%d", errors='coerce')

    #Reglas de Negocio
    df = df[(df["estado"] == "CONFIRMADA") & (df["costo"] >0)]

    #Valores Nulos
    df["telefono"] = df["telefono"].fillna("NO REGISTRA")

    #Carga de la informacion
    df.to_csv('data/output.csv', index=False)




if __name__ == "__main__":
    run_etl()
