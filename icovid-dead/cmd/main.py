#!/usr/bin/python3

import pandas as pd 
import numpy as np 
import os
import shutil
from datetime import datetime

def main():
    path_fallecidos = "/home/pas/python/icovid-dead/work-files/fallecidos_rango.csv"
    df = pd.read_csv(path_fallecidos)

    # df["date"] = pd.to_datetime(df.fecha, format="%d-%m-%Y")
    df["date"] = pd.to_datetime(df.fecha, format="%Y-%m-%d")
    df["week"] = df.date.dt.strftime("%U").astype(int)
    df["year"] = df.date.dt.strftime("%Y")
    df = df[["fecha", "date", "year", "week", "sexo", "grupo_etario"]].reset_index(drop=True)

    df["for_counting"] = 1

    # Al restar 1, la ultima final_df 2020 queda en la misma final_df que la primera del 2021
    df.week = np.where(df.year == "2021", df.week + 53, df.week)
    df.week = np.where(df.week >= 53, df.week - 1, df.week)

    # generamos las columnas de fecha min y max agrupando por número de final_df
    df["min_dates"] = df.groupby("week")["date"].transform("min")
    df["max_dates"] = df.groupby("week")["date"].transform("max")

    # df.to_csv("/home/pas/python/icovid-dead/here.csv")

    df["largo_semana"] = 1 + (df.max_dates - df.min_dates).dt.days
    df["semana_texto"] = df.min_dates.dt.strftime("%d %b") + ' - ' + df.max_dates.dt.strftime("%d %b %y")
    # df = df.sort_values(by=["grupo_etario", ", "date"])
    df = df.rename(columns={"week": "semana", "min_dates": "fecha_inicio_semana"})

    df_general = df.groupby(["grupo_etario", "semana", "largo_semana", "fecha_inicio_semana", "semana_texto"]).for_counting.sum().reset_index()
    df_general = df_general.rename(columns={"for_counting": "casos_semanales"})

    df_general["casos_semanales_ant"] = df_general.casos_semanales.shift().fillna(0)
    df_general["delta"] = df_general.casos_semanales - df_general.casos_semanales_ant
    df_general["cambio_porcentual_semanal"] = round((df_general.delta / df_general.casos_semanales_ant) * 100, 1)
    df_general["casos_diarios_prom"] = round(df_general.casos_semanales / df_general.largo_semana)
    df_general["casos_diarios_prom"] = df_general.casos_diarios_prom.astype(int)
    df_general["casos_diarios_prom_ant"] = df_general.casos_diarios_prom.shift().fillna(0)
    df_general["delta_casos_diarios"] = df_general.casos_diarios_prom - df_general.casos_diarios_prom_ant
    df_general["cambio_porcentual_diarios"] = round((df_general.delta_casos_diarios / df_general.casos_diarios_prom_ant) * 100, 1)


    # df_general = df_general.rename(columns={"week": "semana", "min_dates": "fecha_inicio_semana"})
    df_gen_reducido = df_general[["grupo_etario", "semana", "semana_texto", "fecha_inicio_semana", "casos_semanales", "cambio_porcentual_semanal", "casos_diarios_prom", "cambio_porcentual_diarios"]]

    # desagregado por sexo
    df_sex = df.groupby(["grupo_etario", "sexo", "semana", "largo_semana", "fecha_inicio_semana", "semana_texto"]).for_counting.sum().reset_index()
    df_sex = df_sex.rename(columns={"for_counting": "casos_semanales"})

    df_sex["casos_semanales_ant"] = df_sex.casos_semanales.shift().fillna(0)
    df_sex["delta"] = df_sex.casos_semanales - df_sex.casos_semanales_ant
    df_sex["cambio_porcentual_semanal"] = round((df_sex.delta / df_sex.casos_semanales_ant) * 100, 1)
    df_sex["casos_diarios_prom"] = round(df_sex.casos_semanales / df_sex.largo_semana)
    df_sex["casos_diarios_prom"] = df_general.casos_diarios_prom.astype(int)
    df_sex["casos_diarios_prom_ant"] = df_sex.casos_diarios_prom.shift().fillna(0)
    df_sex["delta_casos_diarios"] = df_sex.casos_diarios_prom - df_sex.casos_diarios_prom_ant
    df_sex["cambio_porcentual_diarios"] = round((df_sex.delta_casos_diarios / df_sex.casos_diarios_prom_ant) * 100, 1)

    # df_sex = df_general.rename(columns={"week": "semana", "min_dates": "fecha_inicio_semana"})
    df_sex_reducido = df_sex[["grupo_etario", "sexo", "semana", "semana_texto", "fecha_inicio_semana", "casos_semanales", "cambio_porcentual_semanal", "casos_diarios_prom", "cambio_porcentual_diarios"]]

    return df_gen_reducido, df_sex_reducido, df_general, df_sex

if __name__ == "__main__":
    # nota: se presenta la semana de domingo a sábado
    today = datetime.now().strftime("%Y%m%d")
    path_results = f"/home/pas/python/icovid-dead/fallecidos-etario/{today}"

    # fallecidos etario
    if os.path.exists(path_results):
        shutil.rmtree(path_results)
    
    os.makedirs(path_results)

    ruta_fallecidos_gen = path_results + "/fallecidos-etario.csv"
    ruta_fallecidos_sex = path_results + "/fallecidos-etario-sexo.csv"
    ruta_fallecidos_gen_sabana = path_results + "/fallecidos-etario-sabana.csv"
    ruta_fallecidos_sex_sabana = path_results + "/fallecidos-etario-sexo-sabana.csv"

    df_fallecidos_gen, df_fallecidos_sex, df_gen_sabana, df_sex_sabana = main()
    df_fallecidos_gen.to_csv(ruta_fallecidos_gen, index=False)
    df_fallecidos_sex.to_csv(ruta_fallecidos_sex, index=False)
    df_gen_sabana.to_csv(ruta_fallecidos_gen_sabana, index=False)
    df_sex_sabana.to_csv(ruta_fallecidos_sex_sabana, index=False)
