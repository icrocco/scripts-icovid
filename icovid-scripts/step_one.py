import sys
# sys.path.append("pkg")

# from github_csv import github
import pandas as pd
import io
import time

import requests
import os

def github(url: str):
    # token = os.environ.get("GITHUB_DATAGOV_TOKEN")
    token = "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"
    try:
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3.raw"}
        return requests.get(url, headers=headers)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

################################################################
####                   RESUMEN NACIONAL                    ####
################################################################

#### URLS ####
carga_nacional_ajustada: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension1/carga/nacional/carga.nacional.ajustada.csv"
r_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension1/R/nacional/r.nacional_n.csv"
tasa_test_semanal_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension2/tasatest/nacional/tasa%20test%20semanal%20nacional.csv"
positividad_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension2/positividad/nacional/Positividad%20nacional.csv"
prob48_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/proptemprano/Nacional/prob48.nacional.csv"
lab24_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/laboratorio/Nacional/lab24.nacional.csv"
not48_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/notificacion/Nacional/not48.nacional.csv"
total72_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/total/Nacional/total72.nacional.csv"
uso_camas_uci_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension4/uci/nacional/Uso%20de%20camas%20UCI%20Nacional.csv"
uso_camas_uci_covid19_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension4/ucicovid/nacional/Uso%20de%20camas%20UCI%20Covid-19%20Nacional.csv"
tasa_var_semanal_hosp_covid19_nacional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension4/varhosp/nacional/tasa%20de%20variacion%20semanal%20hospitalizaciones%20Covid-19%20Nacional.csv"

#### ARCHIVOS EN BYTES DESDE EL REPO PRIVADO ####
file_carga_nacional_ajustada: bytes = github(carga_nacional_ajustada).content
file_r_nacional: bytes = github(r_nacional).content
file_tasa_test_semanal_nacional: bytes = github(tasa_test_semanal_nacional).content
file_positividad_nacional: bytes = github(positividad_nacional).content
file_prob48_nacional: bytes = github(prob48_nacional).content
file_lab24_nacional: bytes = github(lab24_nacional).content
file_not48_nacional:bytes = github(not48_nacional).content
file_total72_nacional: bytes = github(total72_nacional).content
file_uso_camas_uci_nacional: bytes = github(uso_camas_uci_nacional).content
file_uso_camas_uci_covid19_nacional: bytes = github(uso_camas_uci_covid19_nacional).content
file_tasa_var_semanal_hosp_covid19_nacional: bytes = github(tasa_var_semanal_hosp_covid19_nacional).content

####  DATAFRAMES RESUMEN NACIONAL ####
A1_nacional = pd.read_csv(io.StringIO(file_carga_nacional_ajustada.decode("utf-8")), sep=";")
A2_nacional = pd.read_csv(io.StringIO(file_r_nacional.decode("utf-8")), sep=";")
B1_nacional = pd.read_csv(io.StringIO(file_tasa_test_semanal_nacional.decode("utf-8")), sep=",")
B2_nacional = pd.read_csv(io.StringIO(file_positividad_nacional.decode("utf-8")), sep=",")
C2_nacional = pd.read_csv(io.StringIO(file_prob48_nacional.decode("utf-8")), sep=";")
C3_nacional = pd.read_csv(io.StringIO(file_lab24_nacional.decode("utf-8")), sep=";")
C4_nacional = pd.read_csv(io.StringIO(file_not48_nacional.decode("utf-8")), sep=";")
C5_nacional = pd.read_csv(io.StringIO(file_total72_nacional.decode("utf-8")), sep=";")
D1_nacional = pd.read_csv(io.StringIO(file_uso_camas_uci_nacional.decode("utf-8")), sep=",")
D2_nacional = pd.read_csv(io.StringIO(file_uso_camas_uci_covid19_nacional.decode("utf-8")), sep=",")
D4_nacional = pd.read_csv(io.StringIO(file_tasa_var_semanal_hosp_covid19_nacional.decode("utf-8")), sep=",")

################################################################
####                   RESUMEN REGIONAL                     ####
################################################################

#### URLS ####
carga_regional_ajustada: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension1/carga/regional/carga.regional.ajustada.csv"
r_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension1/R/regional/r.regional_n.csv"
tasa_test_semanal_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension2/tasatest/regional/tasa%20test%20semanal%20regional.csv"
positividad_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension2/positividad/regional/Positividad%20por%20region.csv"
prob48_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/proptemprano/Regional/prob48.regional.csv"
lab24_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/laboratorio/Regional/lab24.regional.csv"
not48_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/notificacion/Regional/not48.regional.csv"
total72_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension3/total/Regional/total72.regional.csv"
uso_camas_uci_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension4/uci/regional/Uso%20de%20camas%20UCI%20por%20region.csv"
uso_camas_uci_covid19_regional: str = "https://raw.githubusercontent.com/datagovuc/ICOVID/master/dimension4/ucicovid/regional/Uso%20de%20camas%20UCI%20Covid-19%20Regional.csv"

#### ARCHIVOS EN BYTES DESDE EL REPO PRIVADO ####
file_carga_regional_ajustada: bytes = github(carga_regional_ajustada).content
file_r_regional: bytes = github(r_regional).content
file_tasa_test_semanal_regional: bytes = github(tasa_test_semanal_regional).content
file_positividad_regional: bytes = github(positividad_regional).content
file_prob48_regional: bytes = github(prob48_regional).content
file_lab24_regional: bytes = github(lab24_regional).content
file_not48_regional:bytes = github(not48_regional).content
file_total72_regional: bytes = github(total72_regional).content
file_uso_camas_uci_regional: bytes = github(uso_camas_uci_regional).content
file_uso_camas_uci_covid19_regional: bytes = github(uso_camas_uci_covid19_regional).content

####  DATAFRAMES RESUMEN REGIONAL ####
A1_regional = pd.read_csv(io.StringIO(file_carga_regional_ajustada.decode("utf-8")), sep=";")
A2_regional = pd.read_csv(io.StringIO(file_r_regional.decode("utf-8")), sep=";")
B1_regional = pd.read_csv(io.StringIO(file_tasa_test_semanal_regional.decode("utf-8")), sep=",")
B2_regional = pd.read_csv(io.StringIO(file_positividad_regional.decode("utf-8")), sep=",")
C2_regional = pd.read_csv(io.StringIO(file_prob48_regional.decode("utf-8")), sep=";")
C3_regional = pd.read_csv(io.StringIO(file_lab24_regional.decode("utf-8")), sep=";")
C4_regional = pd.read_csv(io.StringIO(file_not48_regional.decode("utf-8")), sep=";")
C5_regional = pd.read_csv(io.StringIO(file_total72_regional.decode("utf-8")), sep=";")
D1_regional = pd.read_csv(io.StringIO(file_uso_camas_uci_regional.decode("utf-8")), sep=",")
D2_regional = pd.read_csv(io.StringIO(file_uso_camas_uci_covid19_regional.decode("utf-8")), sep=",")

################################################################
####                   RESUMEN TABLA 1                      ####
################################################################

########## NACIONAL ##########

A1_nacional_T1 = A1_nacional
A2_nacional_T1 = A2_nacional
B1_nacional_T1 = B1_nacional
B2_nacional_T1 = B2_nacional
C2_nacional_T1 = C2_nacional
C3_nacional_T1 = C3_nacional
C4_nacional_T1 = C4_nacional
C5_nacional_T1 = C5_nacional
D1_nacional_T1 = D1_nacional
D2_nacional_T1 = D2_nacional
D4_nacional_T1 = D4_nacional

########## REGIONAL ##########

A1_regional_T1 = A1_regional
A2_regional_T1 = A2_regional
B1_regional_T1 = B1_regional
B2_regional_T1 = B2_regional
C2_regional_T1 = C2_regional
C3_regional_T1 = C3_regional
C4_regional_T1 = C4_regional
C5_regional_T1 = C5_regional
D1_regional_T1 = D1_regional
D2_regional_T1 = D2_regional

################################################################
####            CARGA INDICADORES NACIONALES                ####
################################################################

A1_nacional = A1_nacional[["fecha","carga.lisup"]]
A2_nacional = A2_nacional[["fecha","r.lisup80"]]
B1_nacional = B1_nacional[["fecha","tasatest"]]
B2_nacional = B2_nacional[["fecha","positividad"]]
C2_nacional = C2_nacional[["fecha","prob48.linf"]]
C3_nacional = C3_nacional[["fecha_notificacion","prop1d"]]
C4_nacional = C4_nacional[["fecha_primeros_sintomas","prop2d"]]
C5_nacional = C5_nacional[["fecha_primeros_sintomas","prop3d"]]
D1_nacional = D1_nacional[["fecha","Nacional"]]
D2_nacional = D2_nacional[["fecha","COVID UCI Nacional"]]
D4_nacional = D4_nacional[["fecha","Totales"]]

################################################################
####            CARGA INDICADORES REGIONALES                ####
################################################################

A1_regional = A1_regional[["fecha","region","carga.lisup"]]
A2_regional = A2_regional[["fecha","region","r.lisup80"]]
B1_regional = B1_regional[["fecha","codigo_region","tasatest"]]
B2_regional = B2_regional[["fecha","codigo_region","positividad"]]
C2_regional = C2_regional[["fecha","region","prob48.linf"]]
D1_regional = D1_regional[["fecha","codigo_region","Porcentaje Camas UCI"]]
D2_regional = D2_regional[["fecha","codigo_region","COVID UCI"]]
C3_regional = C3_regional[["fecha_notificacion","region","prop1d"]]
C4_regional = C4_regional[["fecha_primeros_sintomas","region","prop2d"]]
C5_regional = C5_regional[["fecha_primeros_sintomas","region","prop3d"]]

######################################################################
####            CARGA INDICADORES NACIONALES TABLA 1              ####
######################################################################

B1_nacional_T1 = B1_nacional_T1[["fecha","tasatest"]]
B2_nacional_T1 = B2_nacional_T1[["fecha","positividad"]]
D1_nacional_T1 = D1_nacional_T1[["fecha","Nacional"]]
D2_nacional_T1 = D2_nacional_T1[["fecha","COVID UCI Nacional"]]
D4_nacional_T1 = D4_nacional_T1[["fecha","Totales"]]

######################################################################
####            CARGA INDICADORES REGIONALES TABLA 1              ####
######################################################################

B1_regional_T1 = B1_regional_T1[["fecha","codigo_region","tasatest",]]
B2_regional_T1 = B2_regional_T1[["fecha","codigo_region","positividad"]]
D1_regional_T1 = D1_regional_T1[["fecha","codigo_region","Porcentaje Camas UCI"]]
D2_regional_T1 = D2_regional_T1[["fecha","codigo_region","COVID UCI"]]

##################################################################################
####            AGREGA COLUMNAS IND, SUP, INF NACIONALES TABLA 1              ####
##################################################################################

A1_nacional_T1["Indicador"] = "A1"
A2_nacional_T1["Indicador"] = "A2"
B1_nacional_T1["Indicador"] = "B1"
B2_nacional_T1["Indicador"] = "B2"
C2_nacional_T1["Indicador"] = "C2"
C3_nacional_T1["Indicador"] = "C3"
C4_nacional_T1["Indicador"] = "C4"
C5_nacional_T1["Indicador"] = "C5"
D1_nacional_T1["Indicador"] = "D1"
D2_nacional_T1["Indicador"] = "D2"
D4_nacional_T1["Indicador"] = "D4"
B1_nacional_T1["Superior"] = 0
B1_nacional_T1["Inferior"] = 0
B2_nacional_T1["Inferior"] = 0
B2_nacional_T1["Superior"] = 0
C3_nacional_T1["Superior"] = 0
C3_nacional_T1["Inferior"] = 0
C4_nacional_T1["Superior"] = 0
C4_nacional_T1["Inferior"] = 0
C5_nacional_T1["Superior"] = 0
C5_nacional_T1["Inferior"] = 0
D1_nacional_T1["Superior"] = 0
D1_nacional_T1["Inferior"] = 0
D2_nacional_T1["Superior"] = 0
D2_nacional_T1["Inferior"] = 0
D4_nacional_T1["Superior"] = 0
D4_nacional_T1["Inferior"] = 0

######################################################################
####            RENOMBRA COLUMNAS NACIONALES TABLA 1              ####
######################################################################

A1_nacional_T1 = A1_nacional_T1.rename(columns={"fecha": "fecha", "carga.lisup": "Superior","carga.liminf": "Inferior" ,"carga.estimada": "Estimado"})
A2_nacional_T1 = A2_nacional_T1.rename(columns={"fecha": "fecha", "r.lisup80": "Superior", "r.liminf80": "Inferior","r.estimado": "Estimado"})
B1_nacional_T1 = B1_nacional_T1.rename(columns={"fecha": "fecha","tasatest": "Estimado"})
B2_nacional_T1 = B2_nacional_T1.rename(columns={"fecha": "fecha","positividad": "Estimado"})
C2_nacional_T1 = C2_nacional_T1.rename(columns={"fecha": "fecha","prob48.lsup": "Superior","prob48.linf": "Inferior","prob48.estimado": "Estimado"})
C3_nacional_T1 = C3_nacional_T1.rename(columns={"fecha_notificacion": "fecha","prop1d": "Estimado"})
C4_nacional_T1 = C4_nacional_T1.rename(columns={"fecha_primeros_sintomas": "fecha","prop2d": "Estimado"})
C5_nacional_T1 = C5_nacional_T1.rename(columns={"fecha_primeros_sintomas": "fecha","prop3d": "Estimado"})
D1_nacional_T1 = D1_nacional_T1.rename(columns={"fecha": "fecha","Nacional": "Estimado"})
D2_nacional_T1 = D2_nacional_T1.rename(columns={"fecha": "fecha","COVID UCI Nacional": "Estimado"})
D4_nacional_T1 = D4_nacional_T1.rename(columns={"fecha": "fecha","Totales": "Estimado"})

##################################################################################
####            AGREGA COLUMNAS IND, SUP, INF REGIONALES TABLA 1              ####
##################################################################################

A1_regional_T1["Indicador"] = "A1"
A2_regional_T1["Indicador"] = "A2"
B1_regional_T1["Indicador"] = "B1"
B2_regional_T1["Indicador"] = "B2"
C2_regional_T1["Indicador"] = "C2"
C3_regional_T1["Indicador"] = "C3"
C4_regional_T1["Indicador"] = "C4"
C5_regional_T1["Indicador"] = "C5"
D1_regional_T1["Indicador"] = "D1"
D2_regional_T1["Indicador"] = "D2"
B1_regional_T1["Superior"] = 0
B1_regional_T1["Inferior"] = 0
B2_regional_T1["Inferior"] = 0
B2_regional_T1["Superior"] = 0
C3_regional_T1["Superior"] = 0
C3_regional_T1["Inferior"] = 0
C4_regional_T1["Superior"] = 0
C4_regional_T1["Inferior"] = 0
C5_regional_T1["Superior"] = 0
C5_regional_T1["Inferior"] = 0
D1_regional_T1["Superior"] = 0
D1_regional_T1["Inferior"] = 0
D2_regional_T1["Superior"] = 0
D2_regional_T1["Inferior"] = 0

######################################################################
####            RENOMBRA COLUMNAS REGIONALES TABLA 1              ####
######################################################################

A1_regional_T1 = A1_regional_T1.rename(columns={"fecha": "fecha", "carga.lisup": "Superior","carga.liminf": "Inferior" ,"carga.estimada": "Estimado","region":"cod_region"})
A2_regional_T1 = A2_regional_T1.rename(columns={"fecha": "fecha", "r.lisup80": "Superior", "r.liminf80": "Inferior","r.estimado": "Estimado", "region":"cod_region"})
B1_regional_T1 = B1_regional_T1.rename(columns={"fecha": "fecha","tasatest": "Estimado", "codigo_region":"cod_region"})
B2_regional_T1 = B2_regional_T1.rename(columns={"fecha": "fecha","positividad": "Estimado","codigo_region":"cod_region"})
C2_regional_T1 = C2_regional_T1.rename(columns={"fecha": "fecha","prob48.lsup": "Superior","prob48.linf": "Inferior","prob48.estimado": "Estimado", "region":"cod_region"})
C3_regional_T1 = C3_regional_T1.rename(columns={"fecha_notificacion": "fecha","prop1d": "Estimado", "region":"cod_region"})
C4_regional_T1 = C4_regional_T1.rename(columns={"fecha_primeros_sintomas": "fecha","prop2d": "Estimado", "region":"cod_region"})
C5_regional_T1 = C5_regional_T1.rename(columns={"fecha_primeros_sintomas": "fecha","prop3d": "Estimado", "region":"cod_region"})
D1_regional_T1 = D1_regional_T1.rename(columns={"fecha": "fecha","Porcentaje Camas UCI": "Estimado","codigo_region":"cod_region"})
D2_regional_T1 = D2_regional_T1.rename(columns={"fecha": "fecha","COVID UCI": "Estimado","codigo_region":"cod_region"})

#########################################################################
####            AGREGA COLUMNAS INDICADORES NACIONALES               ####
#########################################################################

A1_nacional["Indicador"] = "A1"
A2_nacional["Indicador"] = "A2"
B1_nacional["Indicador"] = "B1"
B2_nacional["Indicador"] = "B2"
C2_nacional["Indicador"] = "C2"
C3_nacional["Indicador"] = "C3"
C4_nacional["Indicador"] = "C4"
C5_nacional["Indicador"] = "C5"
D1_nacional["Indicador"] = "D1"
D2_nacional["Indicador"] = "D2"
D4_nacional["Indicador"] = "D4"

#############################################################
####            RENOMBRA COLUMNAS NACIONALES             ####
#############################################################

A1_nacional = A1_nacional.rename(columns={"fecha": "fecha","carga.lisup": "Valor"})
A2_nacional = A2_nacional.rename(columns={"fecha": "fecha","r.lisup80": "Valor"})
B1_nacional = B1_nacional.rename(columns={"fecha": "fecha","tasatest": "Valor"})
B2_nacional = B2_nacional.rename(columns={"fecha": "fecha","positividad": "Valor"})
C2_nacional = C2_nacional.rename(columns={"fecha": "fecha","prob48.linf": "Valor"})
C3_nacional = C3_nacional.rename(columns={"fecha_notificacion": "fecha","prop1d": "Valor"})
C4_nacional = C4_nacional.rename(columns={"fecha_primeros_sintomas": "fecha","prop2d": "Valor"})
C5_nacional = C5_nacional.rename(columns={"fecha_primeros_sintomas": "fecha","prop3d": "Valor"})
D1_nacional = D1_nacional.rename(columns={"fecha": "fecha","Nacional": "Valor"})
D2_nacional = D2_nacional.rename(columns={"fecha": "fecha","COVID UCI Nacional": "Valor"})
D4_nacional = D4_nacional.rename(columns={"fecha": "fecha","Totales": "Valor"})


#### INDICADOR A1: CARGA
A1_nacional.loc[A1_nacional["Valor"] <= 1, "cod_color"] = "1"
A1_nacional.loc[(A1_nacional["Valor"] > 1) & (A1_nacional["Valor"] <= 5), "cod_color"] = "2"
A1_nacional.loc[(A1_nacional["Valor"] > 5) & (A1_nacional["Valor"] <= 10), "cod_color"] = "3"
A1_nacional.loc[A1_nacional["Valor"] > 10, "cod_color"] = "4"

#### INDICADOR A2: R
A2_nacional.loc[A2_nacional["Valor"] <= 0.8, "cod_color"] = "1"
A2_nacional.loc[(A2_nacional["Valor"] > 0.8) & (A2_nacional["Valor"] <= 0.9), "cod_color"] = "2"
A2_nacional.loc[(A2_nacional["Valor"] > 0.9) & (A2_nacional["Valor"] <= 1), "cod_color"] = "3"
A2_nacional.loc[A2_nacional["Valor"] > 1, "cod_color"] = "4"

#### INDICADOR B1: N° test por mil hab
B1_nacional.loc[B1_nacional["Valor"] >= 10, "cod_color"] = "1"
B1_nacional.loc[(B1_nacional["Valor"] >= 5) & (B1_nacional["Valor"] < 10), "cod_color"] = "2"
B1_nacional.loc[(B1_nacional["Valor"] < 5) & (B1_nacional["Valor"] >= 1), "cod_color"] = "3"
B1_nacional.loc[B1_nacional["Valor"] < 1, "cod_color"] = "4"


#### INDICADOR B2: Positividad
B2_nacional.loc[(B2_nacional["Valor"] >= 0) & (B2_nacional["Valor"] < 0.03), "cod_color"] = "1"
B2_nacional.loc[(B2_nacional["Valor"] >= 0.03) & (B2_nacional["Valor"] < 0.05), "cod_color"] = "2"
B2_nacional.loc[(B2_nacional["Valor"] >= 0.05) & (B2_nacional["Valor"] < 0.1), "cod_color"] = "3"
B2_nacional.loc[B2_nacional["Valor"] >= 0.1, "cod_color"] = "4"


##### C1 no ienen umbral definido
#C2 si tiene umbral
C2_nacional.loc[C2_nacional["Valor"] <= 0.2, "cod_color"] = "4"
C2_nacional.loc[(C2_nacional["Valor"] <= 0.5) & (C2_nacional["Valor"] > 0.2), "cod_color"] = "3"
C2_nacional.loc[(C2_nacional["Valor"] <= 0.7) & (C2_nacional["Valor"] >0.5), "cod_color"] = "2"
C2_nacional.loc[C2_nacional["Valor"] > 0.7, "cod_color"] = "1"

#C3 si tiene umbral
C3_nacional.loc[C3_nacional["Valor"] <= 0.4, "cod_color"] = "4"
C3_nacional.loc[(C3_nacional["Valor"] <= 0.6) & (C3_nacional["Valor"] > 0.4), "cod_color"] = "3"
C3_nacional.loc[(C3_nacional["Valor"] <= 0.8) & (C3_nacional["Valor"] >0.6), "cod_color"] = "2"
C3_nacional.loc[C3_nacional["Valor"] > 0.8, "cod_color"] = "1"

#C4 si tiene umbral
C4_nacional.loc[C4_nacional["Valor"] <= 0.4, "cod_color"] = "4"
C4_nacional.loc[(C4_nacional["Valor"] <= 0.6) & (C4_nacional["Valor"] > 0.4), "cod_color"] = "3"
C4_nacional.loc[(C4_nacional["Valor"] <= 0.8) & (C4_nacional["Valor"] >0.6), "cod_color"] = "2"
C4_nacional.loc[C4_nacional["Valor"] > 0.8, "cod_color"] = "1"

#C5 si tiene umbral
C5_nacional.loc[C5_nacional["Valor"] <= 0.4, "cod_color"] = "4"
C5_nacional.loc[(C5_nacional["Valor"] <= 0.6) & (C5_nacional["Valor"] > 0.4), "cod_color"] = "3"
C5_nacional.loc[(C5_nacional["Valor"] <= 0.8) & (C5_nacional["Valor"] >0.6), "cod_color"] = "2"
C5_nacional.loc[C5_nacional["Valor"] > 0.8, "cod_color"] = "1"

#### INDICADOR D1: uso camas UCI
D1_nacional.loc[(D1_nacional["Valor"] <= 75) & (D1_nacional["Valor"] >= 0 ), "cod_color"] = "1" 
D1_nacional.loc[(D1_nacional["Valor"] <= 80) & (D1_nacional["Valor"] > 75), "cod_color"] = "2"
D1_nacional.loc[(D1_nacional["Valor"] <= 85) & (D1_nacional["Valor"] > 80), "cod_color"] = "3"
D1_nacional.loc[D1_nacional["Valor"] > 85, "cod_color"] = "4"

#### INDICADOR D2: camas uci uso covid-19 
D2_nacional.loc[(D2_nacional["Valor"] <= 50) & (D2_nacional["Valor"] >= 0),"cod_color"] = "1"   
D2_nacional.loc[(D2_nacional["Valor"] <= 70) & (D2_nacional["Valor"] > 50),"cod_color"] = "2"     
D2_nacional.loc[(D2_nacional["Valor"] <= 85) & (D2_nacional["Valor"] > 70),"cod_color"] = "3"  
D2_nacional.loc[D2_nacional["Valor"] > 85, "cod_color"] = "4"

# INDICADOR D4: Tasa de variación semanal de hospitalizaciones totales COVID-19
D4_nacional.loc[D4_nacional["Valor"] < 10, "cod_color"] = "1"
D4_nacional.loc[(D4_nacional["Valor"] < 15) & (D4_nacional["Valor"] >= 10), "cod_color"] = "2"
D4_nacional.loc[(D4_nacional["Valor"] < 20) & (D4_nacional["Valor"] >= 15), "cod_color"] = "3"
D4_nacional.loc[D4_nacional["Valor"] >= 20 , "cod_color"] = "4"

#########################################################################
####            AGREGA COLUMNAS INDICADORES REGIONALES               ####
#########################################################################

A1_regional["Indicador"] = "A1"
A2_regional["Indicador"] = "A2"
B1_regional["Indicador"] = "B1"
B2_regional["Indicador"] = "B2"
C2_regional["Indicador"] = "C2"
C3_regional["Indicador"] = "C3"
C4_regional["Indicador"] = "C4"
C5_regional["Indicador"] = "C5"
D1_regional["Indicador"] = "D1"
D2_regional["Indicador"] = "D2"

#############################################################
####            RENOMBRA COLUMNAS REGIONALES             ####
#############################################################

A1_regional = A1_regional.rename(columns={"fecha": "fecha", "carga.lisup": "Valor", "region":"cod_region"})
A2_regional = A2_regional.rename(columns={"fecha": "fecha", "r.lisup80": "Valor", "region":"cod_region"})
B1_regional = B1_regional.rename(columns={"fecha": "fecha","tasatest": "Valor", "codigo_region":"cod_region"})
B2_regional = B2_regional.rename(columns={"fecha": "fecha","positividad": "Valor","codigo_region":"cod_region"})
C2_regional = C2_regional.rename(columns={"fecha": "fecha","prob48.linf": "Valor", "region":"cod_region"})
C3_regional = C3_regional.rename(columns={"fecha_notificacion": "fecha","prop1d": "Valor", "region":"cod_region"})
C4_regional = C4_regional.rename(columns={"fecha_primeros_sintomas": "fecha","prop2d": "Valor", "region":"cod_region"})
C5_regional = C5_regional.rename(columns={"fecha_primeros_sintomas": "fecha","prop3d": "Valor", "region":"cod_region"})
D1_regional = D1_regional.rename(columns={"fecha": "fecha","Porcentaje Camas UCI": "Valor","codigo_region":"cod_region"})
D2_regional = D2_regional.rename(columns={"fecha": "fecha","COVID UCI": "Valor","codigo_region":"cod_region"})

#### INDICADOR A1: CARGA
A1_regional.loc[A1_regional["Valor"] <= 1, "cod_color"] = "1"
A1_regional.loc[(A1_regional["Valor"] > 1) & (A1_regional["Valor"] <= 5), "cod_color"] = "2"
A1_regional.loc[(A1_regional["Valor"] > 5) & (A1_regional["Valor"] <= 10), "cod_color"] = "3"
A1_regional.loc[A1_regional["Valor"] > 10, "cod_color"] = "4"

#### INDICADOR A2: R
A2_regional.loc[A2_regional["Valor"] <= 0.8, "cod_color"] = "1"
A2_regional.loc[(A2_regional["Valor"] > 0.8) & (A2_regional["Valor"] <= 0.9), "cod_color"] = "2"
A2_regional.loc[(A2_regional["Valor"] > 0.9) & (A2_regional["Valor"] <= 1), "cod_color"] = "3"
A2_regional.loc[A2_regional["Valor"] > 1, "cod_color"] = "4"

#### INDICADOR B1: NÚMERO DE TEST POR MIL HABITANTES
B1_regional.loc[B1_regional["Valor"] >= 10, "cod_color"] = "1"
B1_regional.loc[(B1_regional["Valor"] >= 5) & (B1_regional["Valor"] < 10), "cod_color"] = "2"
B1_regional.loc[(B1_regional["Valor"] < 5) & (B1_regional["Valor"] >= 1), "cod_color"] = "3"
B1_regional.loc[B1_regional["Valor"] < 1, "cod_color"] = "4"

#### INDICADOR B2: POSITIVIDAD
B2_regional.loc[(B2_regional["Valor"] >= 0) & (B2_regional["Valor"] < 0.03), "cod_color"] = "1"
B2_regional.loc[(B2_regional["Valor"] >= 0.03) & (B2_regional["Valor"] < 0.05), "cod_color"] = "2"
B2_regional.loc[(B2_regional["Valor"] >= 0.05) & (B2_regional["Valor"] < 0.1), "cod_color"] = "3"
B2_regional.loc[B2_regional["Valor"] >= 0.1, "cod_color"] = "4"


# INDICADOR C1 : no tienen umbral definido
#C2 si tiene umbral
C2_regional.loc[C2_regional["Valor"] <= 0.2, "cod_color"] = "4"
C2_regional.loc[(C2_regional["Valor"] <= 0.5) & (C2_regional["Valor"] > 0.2), "cod_color"] = "3"
C2_regional.loc[(C2_regional["Valor"] <= 0.7) & (C2_regional["Valor"] >0.5), "cod_color"] = "2"
C2_regional.loc[C2_regional["Valor"] > 0.7, "cod_color"] = "1"

#C3 si tiene umbral
C3_regional.loc[C3_regional["Valor"] <= 0.4, "cod_color"] = "4"
C3_regional.loc[(C3_regional["Valor"] <= 0.6) & (C3_regional["Valor"] > 0.4), "cod_color"] = "3"
C3_regional.loc[(C3_regional["Valor"] <= 0.8) & (C3_regional["Valor"] >0.6), "cod_color"] = "2"
C3_regional.loc[C3_regional["Valor"] > 0.8, "cod_color"] = "1"

#C4 si tiene umbral
C4_regional.loc[C4_regional["Valor"] <= 0.4, "cod_color"] = "4"
C4_regional.loc[(C4_regional["Valor"] <= 0.6) & (C4_regional["Valor"] > 0.4), "cod_color"] = "3"
C4_regional.loc[(C4_regional["Valor"] <= 0.8) & (C4_regional["Valor"] >0.6), "cod_color"] = "2"
C4_regional.loc[C4_regional["Valor"] > 0.8, "cod_color"] = "1"

#C5 si tiene umbral
C5_regional.loc[C5_regional["Valor"] <= 0.4, "cod_color"] = "4"
C5_regional.loc[(C5_regional["Valor"] <= 0.6) & (C5_regional["Valor"] > 0.4), "cod_color"] = "3"
C5_regional.loc[(C5_regional["Valor"] <= 0.8) & (C5_regional["Valor"] >0.6), "cod_color"] = "2"
C5_regional.loc[C5_regional["Valor"] > 0.8, "cod_color"] = "1"


#### INDICADOR D1: uso camas UCI
D1_regional.loc[(D1_regional["Valor"] <= 75) & (D1_regional["Valor"] >= 0 ), "cod_color"] = "1" 
D1_regional.loc[(D1_regional["Valor"] <= 80) & (D1_regional["Valor"] > 75), "cod_color"] = "2"
D1_regional.loc[(D1_regional["Valor"] <= 85) & (D1_regional["Valor"] > 80), "cod_color"] = "3"
D1_regional.loc[D1_regional["Valor"] > 85, "cod_color"] = "4"

#### INDICADOR D2: camas uci uso covid-19 
D2_regional.loc[(D2_regional["Valor"] <= 50) & (D2_regional["Valor"] >= 0),"cod_color"] = "1"  
D2_regional.loc[(D2_regional["Valor"] <= 70) & (D2_regional["Valor"] > 50),"cod_color"] = "2"     
D2_regional.loc[(D2_regional["Valor"] <= 85) & (D2_regional["Valor"] > 70),"cod_color"] = "3"  
D2_regional.loc[D2_regional["Valor"] > 85, "cod_color"] = "4"

########################################################################
####            DATAFRAME QUE CONTIENE TODAS LAS TABLAS 1           ####
########################################################################

#### REGIONAL
frames_r_T1 = [A1_regional_T1, A2_regional_T1, B1_regional_T1, B2_regional_T1, C2_regional_T1, C3_regional_T1, C4_regional_T1, C5_regional_T1, D1_regional_T1, D2_regional_T1]
result_regional_T1 = pd.concat(frames_r_T1, sort=True) #concatenamos en un solo gran dataframe
result_regional_T1_dropped_cols = result_regional_T1[["Estimado", "Indicador", "Inferior", "Superior", "cod_region", "fecha"]] # Se eliminan las columnas r.liminf y r.lisup
result_regional_T1_final = result_regional_T1_dropped_cols.dropna()

#### NACIONAL
frames_n_T1 = [A1_nacional_T1, B1_nacional_T1, A2_nacional_T1, B2_nacional_T1, C2_nacional_T1, C3_nacional_T1, C4_nacional_T1, C5_nacional_T1, D1_nacional_T1, D2_nacional_T1, D4_nacional_T1]
result_nacional_T1 = pd.concat(frames_n_T1, sort=True) #concatenamos en un solo gran dataframe
result_nacional_T1_dropped_cols = result_nacional_T1[["Estimado", "Indicador", "Inferior", "Superior", "fecha"]] # Se eliminan las columnas r.liminf y r.lisup
result_nacional_T1_final = result_nacional_T1_dropped_cols.dropna()

##########################################################################
####            GENERACIÓN ARCHIVOS .XLSX Y .CSV TABLA 1              ####
##########################################################################

today = sys.argv[1]
hoy = time.strftime("%Y%m%d%H%M%S") #guardamos la fecha de generación del archivo en formato YYYYMMDDhhmmss
# /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-one/
ruta_base = f"/home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-one/{today}/"

#### REGIONAL
# ruta_regional_T1 = f"/home/pas/python/icovid-scripts/archivos-step-one/regional_T1_{hoy}.csv"
ruta_regional_T1 = ruta_base + f"regional_T1_{hoy}.csv"
result_regional_T1_final.to_csv(ruta_regional_T1, index=False)
regional_T1_csv = f"regional_T1_{hoy}.csv" # se llama en step_two.py

#### NACIONAL
# ruta_nacional_T1 = f"/home/pas/python/icovid-scripts/archivos-step-one/nacional_T1_{hoy}.csv"
ruta_nacional_T1 = ruta_base + f"nacional_T1_{hoy}.csv"
result_nacional_T1_final.to_csv(ruta_nacional_T1, index=False)
nacional_T1_csv = f"nacional_T1_{hoy}.csv" # se llama en step_two.py

#### XLSX ####
ruta_regional_excel_T1 = ruta_base + "regional_T1.xlsx"
ruta_nacional_excel_T1 = ruta_base + "nacional_T1.xlsx"

result_regional_T1_final.to_excel(ruta_regional_excel_T1, index=False)
result_nacional_T1_final.to_excel(ruta_nacional_excel_T1, index=False)

##############################################################################
####            DATAFRAME QUE CONTIENE EL RESTO (NO TABLA 1)              ####
##############################################################################

#### REGIONAL
frames_r = [A1_regional, A2_regional, B1_regional, B2_regional, C2_regional, C3_regional, C4_regional, C5_regional, D1_regional, D2_regional]
result_regional = pd.concat(frames_r, sort=True) #concatenamos en un solo gran dataframe
result_regional_final = result_regional.dropna() #we drop NaN values

#### NACIONAL
frames_n = [A1_nacional, A2_nacional, B1_nacional, B2_nacional, C2_nacional, C3_nacional, C4_nacional, C5_nacional, D1_nacional, D2_nacional, D4_nacional]
result_nacional = pd.concat(frames_n, sort=True) #concatenamos en un solo gran dataframe
result_nacional_final = result_nacional.dropna() #we drop the NaN values

###################################################################
####            GENERACIÓN ARCHIVOS .XLSX Y .CSV              ####
##################################################################

#### REGIONAL
# ruta_regional = f"/home/pas/python/icovid-scripts/archivos-step-one/regional_{hoy}.csv"
ruta_regional = ruta_base + f"regional_{hoy}.csv"
result_regional_final.to_csv(ruta_regional, index=False)
regional_csv = f"regional_{hoy}.csv"

#### NACIONAL
# ruta_nacional = f"/home/pas/python/icovid-scripts/archivos-step-one/nacional_{hoy}.csv"
ruta_nacional = ruta_base + f"nacional_{hoy}.csv"
result_nacional_final.to_csv(ruta_nacional, index=False)
nacional_csv = f"nacional_{hoy}.csv"

#### XLSX ####
ruta_regional_excel = ruta_base + "regional.xlsx"
ruta_nacional_excel = ruta_base + "nacional.xlsx"

result_regional_final.to_excel(ruta_regional_excel, index=False)
result_nacional_final.to_excel(ruta_nacional_excel, index=False)