import sys
import pandas as pd
import time
import os
import shutil
# from step_one import nacional_csv, nacional_T1_csv, regional_csv, regional_T1_csv

########################################
#####      VARIABLES GLOBALES      #####
########################################

# today = sys.argv[1]
hoy = time.strftime("%Y%m%d")     # guardamos la fecha de generación del archivo en formato YYYYMMDDhhmmss
dir_path = os.path.abspath(os.path.dirname(__file__))
ruta_base = f"{dir_path}/archivos-step-one/{hoy}"
ruta_base_paso2 = f"{dir_path}/archivos-step-two/{hoy}/"

if os.path.exists(f"{dir_path}/archivos-step-two/{hoy}"):
        shutil.rmtree(f"{dir_path}/archivos-step-two/{hoy}")

os.makedirs(ruta_base_paso2)

###############################################################################
#####      GENERACIÓN DATAFRAME DE MAESTRO DIMENSIÓN TIEMPO/PERIODOS      #####
###############################################################################

url_dimension_tiempo = "https://icovid.blob.core.windows.net/datos-dimensiones/dimension_tiempo.csv?sp=r&st=2021-01-17T20:00:23Z&se=2023-01-01T04:00:23Z&spr=https&sv=2019-12-12&sr=b&sig=nFvI4GcNskkysnT1GrxOOiHVIr6gqLIb2z64ZmV5v%2BA%3D"
url_dimension_tiempo_v2 = "https://icovid.blob.core.windows.net/datos-dimensiones/DimPeriodoV2Resumen.csv?sp=r&st=2021-01-19T01:59:05Z&se=2023-01-01T09:59:05Z&spr=https&sv=2019-12-12&sr=b&sig=71W5vwlWwrwn11jJYToWLUyX%2FmrA64Y2x0ghimM5vic%3D"
url_dimension_tiempo_v3 = "https://icovid.blob.core.windows.net/datos-dimensiones/DimPeriodoV3Resumen.csv?sp=r&st=2021-01-19T02:00:16Z&se=2023-01-01T10:00:16Z&spr=https&sv=2019-12-12&sr=b&sig=cMSfrqsfBUlR97kacOde6T%2ByGBbK%2FJYUCHAcFycVL%2Fk%3D"

dim_periodos = pd.read_csv(url_dimension_tiempo)
dim_periodos.sort_values(by=["fecha"])                         # hacemos un sort por el campo fecha just in case
dim_periodos["fecha"] = pd.to_datetime(dim_periodos["fecha"])  # cambiamos el tipo de dato del campo fecha a datetime64

dim_periodos_v2 = pd.read_csv(url_dimension_tiempo_v2)
dim_periodos_v2.sort_values(by=["fecha"])                               # hacemos un sort por el campo fecha just in case
dim_periodos_v2["fecha"] = pd.to_datetime(dim_periodos_v2["fecha"])     # cambiamos el tipo de dato del campo fecha a datetime64

dim_periodos_v3 = pd.read_csv(url_dimension_tiempo_v3)
dim_periodos_v3.sort_values(by=["fecha"])                               # hacemos un sort por el campo fecha just in case
dim_periodos_v3["fecha"] = pd.to_datetime(dim_periodos_v3["fecha"])     # cambiamos el tipo de dato del campo fecha a datetime64

########################################################################################
#####      ARCHIVOS .CSV NACIONAL Y REGIONAL TABLA 1 GENERADOS POR RESUMEN.PY      #####
########################################################################################

regional_T1 = pd.read_csv(f"{ruta_base}/regional_T1_{hoy}.csv")
nacional_T1 = pd.read_csv(f"{ruta_base}/nacional_T1_{hoy}.csv")
regional_T2 = pd.read_csv(f"{ruta_base}/regional_{hoy}.csv")
nacional_T2 = pd.read_csv(f"{ruta_base}/nacional_{hoy}.csv")

regional_T1["fecha"] = pd.to_datetime(regional_T1["fecha"])    # cambiamos el tipo de dato del campo fecha a datetime64
nacional_T1["fecha"] = pd.to_datetime(nacional_T1["fecha"])    # cambiamos el tipo de dato del campo fecha a datetime64
regional_T2["fecha"] = pd.to_datetime(regional_T2["fecha"])    # cambiamos el tipo de dato del campo fecha a datetime64
nacional_T2["fecha"] = pd.to_datetime(nacional_T2["fecha"])    # cambiamos el tipo de dato del campo fecha a datetime64

###########################################################################################
#####      CRUCE PARA CALCULAR LOS PROMEDIOS DE LA DATA GENERADA PARA LA TABLA 1      #####
###########################################################################################

########## REGIONAL ##########
regional_T1_merged = regional_T1.merge(dim_periodos, how="left", on="fecha")
regional_T1_usefulcols = regional_T1_merged[["fecha", "cod_region", "Estimado", "Indicador", "Inferior", "Superior", "Domingo_semana"]]                                          # dejamos las columnas que nos interesan
regional_T1_mean = regional_T1_usefulcols.groupby(["Domingo_semana", "Indicador", "cod_region"]).agg({"Estimado":"mean", "Inferior":"mean", "Superior":"mean"}).reset_index()    # agrupamos y aplicamos el promedio

##### Exportamos a .csv
regional_T1_usefulcols_csv = regional_T1_usefulcols.dropna()                                            # just in case
regional_T1_usefulcols_csv.to_csv(f"{ruta_base_paso2}/regional_T1_paso2_{hoy}.csv", index=False)

regional_T1_mean_csv = regional_T1_mean.dropna()                                                        # just in case
regional_T1_mean_csv.to_csv(f"{ruta_base_paso2}/regional_T1_paso2_promedio_{hoy}.csv", index=False)

#### XLSX ####
regional_T1_usefulcols_csv.to_excel(f"{ruta_base_paso2}/Tabla1_regional.xlsx", index=False)
regional_T1_mean_csv.to_excel(f"{ruta_base_paso2}/Tabla1_regional_prom.xlsx", index=False)

########## NACIONAL ##########
nacional_T1_merged = nacional_T1.merge(dim_periodos, how="left", on="fecha")
nacional_T1_usefulcols = nacional_T1_merged[["fecha", "Estimado", "Indicador", "Inferior", "Superior", "Domingo_semana"]]                                                       # dejamos las columnas que nos interesan
nacional_T1_mean = nacional_T1_usefulcols.groupby(["Domingo_semana", "Indicador"]).agg({"Estimado":"mean", "Inferior":"mean", "Superior":"mean"}).reset_index()                 # agrupamos y aplicamos el promedio

##### Exportamos a .csv
nacional_T1_usefulcols_csv = nacional_T1_usefulcols.dropna()                                            # just in case
nacional_T1_usefulcols_csv.to_csv(f"{ruta_base_paso2}/nacional_T1_paso2_{hoy}.csv", index=False)

nacional_T1_mean_csv = nacional_T1_mean.dropna()                                                        # just in case
nacional_T1_mean_csv.to_csv(f"{ruta_base_paso2}/nacional_T1_paso2_promedio_{hoy}.csv", index=False)

#### XLSX ####
nacional_T1_usefulcols_csv.to_excel(f"{ruta_base_paso2}/Tabla1_nacional.xlsx", index=False)
nacional_T1_mean_csv.to_excel(f"{ruta_base_paso2}/Tabla1_nacional_prom.xlsx", index=False)

###########################################################################################
#####      CRUCE PARA CALCULAR LOS PROMEDIOS DE LA DATA GENERADA PARA LA TABLA 2      #####
###########################################################################################

######################################
#####      TABLA 2 REGIONAL      #####
######################################
regional_T2_merged = regional_T2.merge(dim_periodos, how="left", on="fecha")
regional_T2_usefulcols = regional_T2_merged[["fecha","cod_region","Valor", "Indicador","Domingo_semana"]]                          # dejamos las columnas que nos interesan
regional_T2_mean = regional_T2_usefulcols.groupby(["Domingo_semana","Indicador","cod_region"])["Valor"].mean().reset_index()       # agrupamos y aplicamos el promedio a la columna Valor

#### INDICADOR A1: CARGA
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 1) & (regional_T2_mean["Indicador"] == "A1"), "cod_color"] = "1"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 1) & (regional_T2_mean["Valor"] <= 5) & (regional_T2_mean["Indicador"] == "A1") , "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 5) & (regional_T2_mean["Valor"] <= 10) & (regional_T2_mean["Indicador"] == "A1"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 10) & (regional_T2_mean["Indicador"] == "A1"), "cod_color"] = "4"

#### INDICADOR A2: R
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.8) & (regional_T2_mean["Indicador"] == "A2"), "cod_color"] = "1"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 0.8) & (regional_T2_mean["Valor"] <= 0.9) & (regional_T2_mean["Indicador"] == "A2"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 0.9) & (regional_T2_mean["Valor"] <= 1) & (regional_T2_mean["Indicador"] == "A2"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 1) & (regional_T2_mean["Indicador"] == "A2"), "cod_color"] = "4"

#### INDICADOR B1: N° test por mil hab
regional_T2_mean.loc[(regional_T2_mean["Valor"] >= 10) & (regional_T2_mean["Indicador"] == "B1") , "cod_color"] = "1"
regional_T2_mean.loc[(regional_T2_mean["Valor"] >= 5) & (regional_T2_mean["Valor"] < 10) & (regional_T2_mean["Indicador"] == "B1") , "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] < 5) & (regional_T2_mean["Valor"] >= 1) & (regional_T2_mean["Indicador"] == "B1") , "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] < 1) & (regional_T2_mean["Indicador"] == "B1"), "cod_color"] = "4"

#### INDICADOR B2: Positividad
regional_T2_mean.loc[(regional_T2_mean["Valor"] >= 0) & (regional_T2_mean["Valor"] < 0.03)  & (regional_T2_mean["Indicador"] == "B2"), "cod_color"] = "1"
regional_T2_mean.loc[(regional_T2_mean["Valor"] >= 0.03) & (regional_T2_mean["Valor"] < 0.05)  & (regional_T2_mean["Indicador"] == "B2"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] >= 0.05) & (regional_T2_mean["Valor"] < 0.1)  & (regional_T2_mean["Indicador"] == "B2"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] >= 0.1)  & (regional_T2_mean["Indicador"] == "B2"), "cod_color"] = "4"

#### INDICADOR C1 : no tienen umbral definido
# C2 si tiene umbral
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.2) & (regional_T2_mean["Indicador"] == "C2"), "cod_color"] = "4"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.5) & (regional_T2_mean["Valor"] > 0.2) & (regional_T2_mean["Indicador"] == "C2"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.7) & (regional_T2_mean["Valor"] >0.5) & (regional_T2_mean["Indicador"] == "C2"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 0.7) & (regional_T2_mean["Indicador"] == "C2"), "cod_color"] = "1"

# C3 si tiene umbral
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.4) & (regional_T2_mean["Indicador"] == "C3"), "cod_color"] = "4"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.6) & (regional_T2_mean["Valor"] > 0.4) & (regional_T2_mean["Indicador"] == "C3"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.8) & (regional_T2_mean["Valor"] >0.6) & (regional_T2_mean["Indicador"] == "C3"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 0.8) & (regional_T2_mean["Indicador"] == "C3"), "cod_color"] = "1"

# C4 si tiene umbral
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.4) & (regional_T2_mean["Indicador"] == "C4"), "cod_color"] = "4"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.6) & (regional_T2_mean["Valor"] > 0.4) & (regional_T2_mean["Indicador"] == "C4"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.8) & (regional_T2_mean["Valor"] >0.6) & (regional_T2_mean["Indicador"] == "C4"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 0.8) & (regional_T2_mean["Indicador"] == "C4"), "cod_color"] = "1"

# C5 si tiene umbral
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.4) & (regional_T2_mean["Indicador"] == "C5"), "cod_color"] = "4"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.6) & (regional_T2_mean["Valor"] > 0.4) & (regional_T2_mean["Indicador"] == "C5"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 0.8) & (regional_T2_mean["Valor"] >0.6) & (regional_T2_mean["Indicador"] == "C5"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 0.8) & (regional_T2_mean["Indicador"] == "C5"), "cod_color"] = "1"

# INDICADOR D1: uso camas UCI
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 75) & (regional_T2_mean["Valor"] >= 0 )  & (regional_T2_mean["Indicador"] == "D1"), "cod_color"] = "1" 
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 80) & (regional_T2_mean["Valor"] > 75) & (regional_T2_mean["Indicador"] == "D1"), "cod_color"] = "2"
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 85) & (regional_T2_mean["Valor"] > 80) & (regional_T2_mean["Indicador"] == "D1"), "cod_color"] = "3"
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 85) & (regional_T2_mean["Indicador"] == "D1"), "cod_color"] = "4"

# INDICADOR D2: camas uci uso covid-19 
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 50) & (regional_T2_mean["Valor"] >= 0) & (regional_T2_mean["Indicador"] == "D2"),"cod_color"] = "1"   
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 70) & (regional_T2_mean["Valor"] > 50) & (regional_T2_mean["Indicador"] == "D2"),"cod_color"] = "2"     
regional_T2_mean.loc[(regional_T2_mean["Valor"] <= 85) & (regional_T2_mean["Valor"] > 70) & (regional_T2_mean["Indicador"] == "D2"),"cod_color"] = "3"  
regional_T2_mean.loc[(regional_T2_mean["Valor"] > 85) & (regional_T2_mean["Indicador"] == "D2"), "cod_color"] = "4"

##########      EXPORTAMOS A .CSV     ##########
regional_T2_mean.to_csv(f"{ruta_base_paso2}/regional_T2_paso2_promedio_{hoy}.csv", index=False)

####  XLSX ####
regional_T2_mean.to_excel(f"{ruta_base_paso2}/tabla2_regional.xlsx", index=False)

######################################
#####      TABLA 2 NACIONAL      #####
######################################
nacional_T2_merged = nacional_T2.merge(dim_periodos, how="left", on="fecha")
nacional_T2_usefulcols = nacional_T2_merged[["fecha", "Valor", "Indicador", "Domingo_semana"]]
nacional_T2_mean = nacional_T2_usefulcols.groupby(["Domingo_semana","Indicador"])["Valor"].mean().reset_index()

#### INDICADOR A1: CARGA
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 1) & (nacional_T2_mean["Indicador"] == "A1"), "cod_color"] = "1"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 1) & (nacional_T2_mean["Valor"] <= 5) & (nacional_T2_mean["Indicador"] == "A1") , "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 5) & (nacional_T2_mean["Valor"] <= 10) & (nacional_T2_mean["Indicador"] == "A1"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 10) & (nacional_T2_mean["Indicador"] == "A1"), "cod_color"] = "4"

#### INDICADOR A2: R
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.8) & (nacional_T2_mean["Indicador"] == "A2"), "cod_color"] = "1"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 0.8) & (nacional_T2_mean["Valor"] <= 0.9) & (nacional_T2_mean["Indicador"] == "A2"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 0.9) & (nacional_T2_mean["Valor"] <= 1) & (nacional_T2_mean["Indicador"] == "A2"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 1) & (nacional_T2_mean["Indicador"] == "A2"), "cod_color"] = "4"

#### INDICADOR B1: N° test por mil hab
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 10) & (nacional_T2_mean["Indicador"] == "B1") , "cod_color"] = "1"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 5) & (nacional_T2_mean["Valor"] < 10) & (nacional_T2_mean["Indicador"] == "B1") , "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] < 5) & (nacional_T2_mean["Valor"] >= 1) & (nacional_T2_mean["Indicador"] == "B1") , "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] < 1) & (nacional_T2_mean["Indicador"] == "B1"), "cod_color"] = "4"

#### INDICADOR B2: Positividad
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 0) & (nacional_T2_mean["Valor"] < 0.03)  & (nacional_T2_mean["Indicador"] == "B2"), "cod_color"] = "1"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 0.03) & (nacional_T2_mean["Valor"] < 0.05)  & (nacional_T2_mean["Indicador"] == "B2"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 0.05) & (nacional_T2_mean["Valor"] < 0.1)  & (nacional_T2_mean["Indicador"] == "B2"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 0.1)  & (nacional_T2_mean["Indicador"] == "B2"), "cod_color"] = "4"

#### INDICADOR C1 : no tienen umbral definido
# C2 si tiene umbral
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.2) & (nacional_T2_mean["Indicador"] == "C2"), "cod_color"] = "4"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.5) & (nacional_T2_mean["Valor"] > 0.2) & (nacional_T2_mean["Indicador"] == "C2"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.7) & (nacional_T2_mean["Valor"] >0.5) & (nacional_T2_mean["Indicador"] == "C2"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 0.7) & (nacional_T2_mean["Indicador"] == "C2"), "cod_color"] = "1"

# C3 si tiene umbral
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.4) & (nacional_T2_mean["Indicador"] == "C3"), "cod_color"] = "4"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.6) & (nacional_T2_mean["Valor"] > 0.4) & (nacional_T2_mean["Indicador"] == "C3"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.8) & (nacional_T2_mean["Valor"] >0.6) & (nacional_T2_mean["Indicador"] == "C3"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 0.8) & (nacional_T2_mean["Indicador"] == "C3"), "cod_color"] = "1"

# C4 si tiene umbral
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.4) & (nacional_T2_mean["Indicador"] == "C4"), "cod_color"] = "4"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.6) & (nacional_T2_mean["Valor"] > 0.4) & (nacional_T2_mean["Indicador"] == "C4"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.8) & (nacional_T2_mean["Valor"] >0.6) & (nacional_T2_mean["Indicador"] == "C4"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 0.8) & (nacional_T2_mean["Indicador"] == "C4"), "cod_color"] = "1"

# C5 si tiene umbral
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.4) & (nacional_T2_mean["Indicador"] == "C5"), "cod_color"] = "4"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.6) & (nacional_T2_mean["Valor"] > 0.4) & (nacional_T2_mean["Indicador"] == "C5"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 0.8) & (nacional_T2_mean["Valor"] >0.6) & (nacional_T2_mean["Indicador"] == "C5"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 0.8) & (nacional_T2_mean["Indicador"] == "C5"), "cod_color"] = "1"

#### INDICADOR D1: uso camas UCI
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 75) & (nacional_T2_mean["Valor"] >= 0 )  & (nacional_T2_mean["Indicador"] == "D1"), "cod_color"] = "1" 
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 80) & (nacional_T2_mean["Valor"] > 75) & (nacional_T2_mean["Indicador"] == "D1"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 85) & (nacional_T2_mean["Valor"] > 80) & (nacional_T2_mean["Indicador"] == "D1"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 85) & (nacional_T2_mean["Indicador"] == "D1"), "cod_color"] = "4"

# INDICADOR D2: camas uci uso covid-19 
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 50) & (nacional_T2_mean["Valor"] >= 0) & (nacional_T2_mean["Indicador"] == "D2"),"cod_color"] = "1"   
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 70) & (nacional_T2_mean["Valor"] > 50) & (nacional_T2_mean["Indicador"] == "D2"),"cod_color"] = "2"     
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] <= 85) & (nacional_T2_mean["Valor"] > 70) & (nacional_T2_mean["Indicador"] == "D2"),"cod_color"] = "3"  
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] > 85) & (nacional_T2_mean["Indicador"] == "D2"), "cod_color"] = "4"

# INDICADOR D3 : ventilacion mecanica intesiva : NO TIENE UMBRALES DEFINIDOS 

# INDICADOR D4: Tasa de variación semanal de hospitalizaciones totales COVID-19
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] < 10) & (nacional_T2_mean["Indicador"] == "D4"), "cod_color"] = "1"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] < 15) & (nacional_T2_mean["Valor"] >= 10) & (nacional_T2_mean["Indicador"] == "D4"), "cod_color"] = "2"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] < 20) & (nacional_T2_mean["Valor"] >= 15) & (nacional_T2_mean["Indicador"] == "D4"), "cod_color"] = "3"
nacional_T2_mean.loc[(nacional_T2_mean["Valor"] >= 20) & (nacional_T2_mean["Indicador"] == "D4") , "cod_color"] = "4"

##########      EXPORTAMOS A .CSV     ##########
nacional_T2_mean.to_csv(f"{ruta_base_paso2}/nacional_T2_paso2_promedio_{hoy}.csv", index=False)

#### XLSX ####
nacional_T2_mean.to_excel(f"{ruta_base_paso2}/tabla2_nacional.xlsx", index=False)

##########################################################
#####      PROMEDIO DE CARGA NACIONAL Y REGIONAL     #####
##########################################################

##### NACIONAL #####
confirmados_nacional = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension1/carga/nacional/confirmados%20nacional.csv"
A1_nacional_T1_prom = pd.read_csv(confirmados_nacional, encoding="utf-8", sep=";")

##### REGIONAL #####
confirmados_regional = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension1/carga/regional/confirmados_regionales.csv"
A1_regional_T1_prom = pd.read_csv(confirmados_regional, encoding="utf-8", sep=";")

A1_nacional_T1_prom["fecha"] = pd.to_datetime(A1_nacional_T1_prom["fecha"])             # Cambiamos el tipo de dato del campo fecha a datetime64
A1_regional_T1_prom["fecha"] = pd.to_datetime(A1_regional_T1_prom["fecha"])             # Cambiamos el tipo de dato del campo fecha a datetime64

dim_periodo_domingo_semana = dim_periodos_v2[["fecha", "Domingo_semana"]]                  # Dejamos las columnas de interés del maestro de dimensiones periodos
dim_periodo_domingo_semana_sig = dim_periodos_v2[["fecha", "Domingo_semana_siguiente"]]    # Dejamos las columnas de interés del maestro de dimensiones periodos
dim_periodo_domingo_semana_sig_reg = dim_periodos_v3[["fecha", "Domingo_semana"]]          # Dejamos las columnas de interés del maestro de dimensiones periodos

##########################################################
#####         DIFERENCIA DE PROMEDIOS NACIONAL       #####
##########################################################

##### Para domingo de la semana en curso de la data
TT11 = A1_nacional_T1_prom.merge(dim_periodo_domingo_semana, how="left", on="fecha")
TT11_prom_domingo_nacional = TT11.groupby("Domingo_semana").mean()                                   # Promedio por fecha (que corresponde al domingo de la semana actual de la data)

TT22 = A1_nacional_T1_prom.merge(dim_periodo_domingo_semana_sig, how="left", on="fecha")    
TT22_prom_domingo_nacional_ant = TT22.groupby("Domingo_semana_siguiente").mean()                     # Promedio por fecha (que corresponde al domingo de la semana siguiente de la data)

TT3_prom_domingo_nacional = TT11_prom_domingo_nacional.subtract(TT22_prom_domingo_nacional_ant, axis="columns", fill_value=0)

#### Cálculo de cuantiles
TT3_prom_col_domingo_nacional = TT3_prom_domingo_nacional.mean(axis="columns").round(1)              # Promedio del promedio
TT3_q0275_domingo_nacional = TT3_prom_domingo_nacional.quantile(0.0275, axis="columns").round(1)
TT3_q975_domingo_nacional = TT3_prom_domingo_nacional.quantile(0.975, axis="columns").round(1)

#### Resetear columna Domingo_semana
TT3_prom_col_domingo_nacional = TT3_prom_col_domingo_nacional.reset_index()
TT3_q0275_domingo_nacional = TT3_q0275_domingo_nacional.reset_index()
TT3_q975_domingo_nacional = TT3_q975_domingo_nacional.reset_index()

#### Hacemos un merge para dejar un único dataframe
TT3_carga_nacional_dif = TT3_prom_col_domingo_nacional.merge(TT3_q0275_domingo_nacional, how="left", on="index")
TT3_carga_nacional_dif = TT3_carga_nacional_dif.merge(TT3_q975_domingo_nacional, how="left", on="index")

TT3_carga_nacional_dif["region"] = 0
TT3_carga_nacional_dif_rename = TT3_carga_nacional_dif.rename(columns={"index": "Domingo_semana"})    # Renombramos columnas

##########      EXPORTAMOS A .CSV     ##########
TT3_carga_nacional_dif_rename.to_csv(f"{ruta_base_paso2}/carga_nacional_paso2_promedio_dif_{hoy}.csv", index=False)

#### XLSX ####
TT3_carga_nacional_dif_rename.to_excel(f"{ruta_base_paso2}/carga_nacional_prom_dif.xlsx", index=False)

##########################################################
#####         DIFERENCIA DE PROMEDIOS REGIONAL       #####
##########################################################

##### Para domingo de la semana en curso de la data
TT11_regional = A1_regional_T1_prom.merge(dim_periodo_domingo_semana, how="left")
TT11_prom_domingo_regional = TT11_regional.groupby(["Domingo_semana","region"]).mean()

TT22_regional = A1_regional_T1_prom.merge(dim_periodo_domingo_semana_sig_reg, how="left", on="fecha")
TT22_prom_domingo_regional_ant = TT22_regional.groupby(["Domingo_semana", "region"]).mean()

TT33_prom_domingo_regional = TT11_prom_domingo_regional.subtract(TT22_prom_domingo_regional_ant, axis="columns", fill_value=0)

#### Cálculo de cuantiles
TT33_prom_col_domingo_regional = TT33_prom_domingo_regional.mean(axis="columns").round(1)             # promedio de promedio
TT33_q0275_domingo_regional = TT33_prom_domingo_regional.quantile(0.0275, axis="columns").round(1)
TT33_q975_domingo_regional = TT33_prom_domingo_regional.quantile(0.975, axis="columns").round(1)

#Resetear columan domingo_semana
TT33_q0275_domingo_regional = TT33_q0275_domingo_regional.reset_index() 
TT33_q975_domingo_regional = TT33_q975_domingo_regional.reset_index() 
TT33_prom_col_domingo_regional = TT33_prom_col_domingo_regional.reset_index() 

# Merge para dejar solo un data frame
TT33_carga_regional_dif =  TT33_prom_col_domingo_regional.merge(TT33_q0275_domingo_regional, on=["Domingo_semana", "region"], how="left")
TT33_carga_regional_dif =  TT33_carga_regional_dif.merge(TT33_q975_domingo_regional, on=["Domingo_semana", "region"], how="left")

##########      EXPORTAMOS A .CSV     ##########
TT33_carga_regional_dif.to_csv(f"{ruta_base_paso2}/carga_regional_paso2_promedio_dif_{hoy}.csv", index=False)

#### XLSX ####
TT33_carga_regional_dif.to_excel(f"{ruta_base_paso2}/carga_regional_prom_dif.xlsx", index=False)

########################################################################
#####         PROMEDIO E INTERVALO NACIONAL - CARGA DESDE DO       #####
########################################################################

TT1_intervalo_prom = A1_nacional_T1_prom.merge(dim_periodo_domingo_semana, how="left", on="fecha")
TT1_intervalo_prom_domingo = TT1_intervalo_prom.groupby("Domingo_semana").mean()

# Aplicar promedios e intervalos de confianza a los promedios semanales
TT1_prom_col_domingo = TT1_intervalo_prom_domingo.mean(axis="columns").round(1)
TT1_q0275_domingo = TT1_intervalo_prom_domingo.quantile(0.0275, axis="columns").round(1)
TT1_q975_domingo = TT1_intervalo_prom_domingo.quantile(0.975, axis="columns").round(1)

# Resetear columan domingo_semana
TT1_q0275_domingo = TT1_q0275_domingo.reset_index() 
TT1_q975_domingo = TT1_q975_domingo.reset_index() 
TT1_prom_col_domingo = TT1_prom_col_domingo.reset_index() 

# Merge para dejar solo un data frame
TT1_carga_nacional =  TT1_prom_col_domingo.merge(TT1_q0275_domingo, how="left", on="Domingo_semana")
TT1_carga_nacional =  TT1_carga_nacional.merge(TT1_q975_domingo, how="left", on="Domingo_semana")

TT1_carga_nacional["region"] = 0

##########      EXPORTAMOS A .CSV     ##########
TT1_carga_nacional.to_csv(f"{ruta_base_paso2}/carga_nacional_paso2_promedio_{hoy}.csv", index=False)

#### XLSX ####
TT1_carga_nacional.to_excel(f"{ruta_base_paso2}/carga_nacional_prom.xlsx", index=False)

########################################################################
#####         PROMEDIO E INTERVALO REGIONAL - CARGA DESDE DO       #####
########################################################################

TT1_reg = A1_regional_T1_prom.merge(dim_periodo_domingo_semana, how="left", on="fecha")
TT1_prom_domingo_reg = TT1_reg.groupby(["Domingo_semana", "region"]).mean().reset_index()

# aplicar y fijar columnas como indices
TT1_prom_domingo_reg = TT1_prom_domingo_reg.set_index(["Domingo_semana", "region"]) 

#  Aplicar promedios e intervalos de confianza a los promedios semanales
TT1_prom_col_domingo_reg = TT1_prom_domingo_reg.mean(axis="columns").round(1).reset_index()
TT1_q0275_col_domingo_reg = TT1_prom_domingo_reg.quantile(0.0275, axis="columns").round(1).reset_index()
TT1_q975_col_domingo_reg = TT1_prom_domingo_reg.quantile(0.975, axis="columns").round(1).reset_index()


# Merge para dejar solo un data frame
TT1_carga_regional =  TT1_prom_col_domingo_reg.merge(TT1_q0275_col_domingo_reg, how="left", on=["Domingo_semana","region"])
TT1_carga_regional =  TT1_carga_regional.merge(TT1_q975_col_domingo_reg, how="left", on=["Domingo_semana","region"])

##########      EXPORTAMOS A .CSV     ##########
TT1_carga_regional.to_csv(f"{ruta_base_paso2}/carga_regional_paso2_promedio_{hoy}.csv", index=False)

#### XLSX ####
TT1_carga_regional.to_excel(f"{ruta_base_paso2}/carga_regional_prom.xlsx", index=False)