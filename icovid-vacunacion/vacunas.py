import pandas as pd
import os
import shutil
import warnings

warnings.filterwarnings("ignore")

vacunas_primera_dosis = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto78/vacunados_edad_fecha_1eraDosis_std.csv"
vacunas_segunda_dosis = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto78/vacunados_edad_fecha_2daDosis_std.csv"

df_primera = pd.read_csv(vacunas_primera_dosis).dropna()
df_segunda = pd.read_csv(vacunas_segunda_dosis).dropna()

#### PRIMERA DOSIS ####
df_primera = df_primera.rename(columns={"Edad": "edad", "Fecha": "fecha", "Primera Dosis": "primera_dosis"})
df_primera = df_primera.astype({"edad": int, "primera_dosis": int})

copy_primera = df_primera.copy()

copy_primera.loc[df_primera.edad < 50, "edad"] = "<50"
copy_primera.loc[(df_primera.edad < 70) & (df_primera.edad > 49), "edad"] = "50-69"
copy_primera.loc[df_primera.edad > 69, "edad"] = ">=70"

primera_dosis = copy_primera.groupby(["edad", "fecha"]).primera_dosis.sum().reset_index()

#### SEGUNDA DOSIS ####
df_segunda = df_segunda.rename(columns={"Edad": "edad", "Fecha": "fecha", "Segunda Dosis": "segunda_dosis"})
df_segunda = df_segunda.astype({"edad": int, "segunda_dosis": int})

copy_segunda = df_segunda.copy()

copy_segunda.loc[df_segunda.edad < 50, "edad"] = "<50"
copy_segunda.loc[(df_segunda.edad < 70) & (df_segunda.edad > 49), "edad"] = "50-69"
copy_segunda.loc[df_segunda.edad > 69, "edad"] = ">=70"

segunda_dosis = copy_segunda.groupby(["edad", "fecha"]).segunda_dosis.sum().reset_index()

#### INE CENSO POBLACIÓN ####
dir_path = os.path.abspath(os.path.dirname(__file__))
ine = pd.read_csv(f"{dir_path}/ine/ine_2020_2021.csv")
ine = ine.dropna()
ine = ine.replace({"100+": "100"})
ine = ine[18:-1] # consideramos el universo de población desde los 18 años
ine = ine.astype({"EDAD": int, "2020": int, "2021": int})

copy_ine = ine.copy()

ine_tier_one = copy_ine.loc[ine["EDAD"] < 50] # < 50 
ine_tier_two = copy_ine.loc[(ine["EDAD"] < 70) & (ine["EDAD"] > 49)] # 50-69
ine_tier_three = copy_ine.loc[ine["EDAD"] > 69] # >= 70

total_tier_one = ine_tier_one["2021"].sum()     # población total < 50
total_tier_two = ine_tier_two["2021"].sum()     # población total 50-69
total_tier_three = ine_tier_three["2021"].sum() # población total >= 70

copy_primera_dosis = primera_dosis.copy()

primera_dosis_tier_one = copy_primera_dosis.loc[primera_dosis["edad"] == "<50"]
primera_dosis_tier_two = copy_primera_dosis.loc[primera_dosis["edad"] == "50-69"]
primera_dosis_tier_three = copy_primera_dosis.loc[primera_dosis["edad"] == ">=70"]

primera_dosis_tier_one["cantidad"] = primera_dosis_tier_one["primera_dosis"].cumsum()
primera_dosis_tier_two["cantidad"] = primera_dosis_tier_two["primera_dosis"].cumsum()
primera_dosis_tier_three["cantidad"] = primera_dosis_tier_three["primera_dosis"].cumsum()

primera_dosis_tier_one["cobertura_procentual"] = round(primera_dosis_tier_one["cantidad"] / total_tier_one * 100, 2)
primera_dosis_tier_two["cobertura_procentual"] = round(primera_dosis_tier_two["cantidad"] / total_tier_two * 100, 2)
primera_dosis_tier_three["cobertura_procentual"] = round(primera_dosis_tier_three["cantidad"] / total_tier_three * 100, 2)

primera_final = pd.concat([primera_dosis_tier_one, primera_dosis_tier_two, primera_dosis_tier_three])


if os.path.exists(f"{dir_path}/archivos_vacunas"):
    shutil.rmtree(f"{dir_path}/archivos_vacunas")

os.mkdir(f"{dir_path}/archivos_vacunas")
primera_final.to_csv(f"{dir_path}/archivos_vacunas/primera_dosis.csv", index=False)

segunda_dosis_tier_one = segunda_dosis.loc[segunda_dosis["edad"] == "<50"]
segunda_dosis_tier_two = segunda_dosis.loc[segunda_dosis["edad"] == "50-69"]
segunda_dosis_tier_three = segunda_dosis.loc[segunda_dosis["edad"] == ">=70"]

segunda_dosis_tier_one["cantidad"] = segunda_dosis_tier_one["segunda_dosis"].cumsum()
segunda_dosis_tier_two["cantidad"] = segunda_dosis_tier_two["segunda_dosis"].cumsum()
segunda_dosis_tier_three["cantidad"] = segunda_dosis_tier_three["segunda_dosis"].cumsum()

segunda_dosis_tier_one["cobertura_procentual"] = round(segunda_dosis_tier_one["cantidad"] / total_tier_one * 100, 2)
segunda_dosis_tier_two["cobertura_procentual"] = round(segunda_dosis_tier_two["cantidad"] / total_tier_two * 100, 2)
segunda_dosis_tier_three["cobertura_procentual"] = round(segunda_dosis_tier_three["cantidad"] / total_tier_three * 100, 2)

segunda_final = pd.concat([segunda_dosis_tier_one, segunda_dosis_tier_two, segunda_dosis_tier_three])

segunda_final.to_csv(f"{dir_path}/archivos_vacunas/segunda_dosis.csv", index=False)

## CONSOLIDADO PARA LA VISUALIZACIÓN DE AMBAS DOSIS EN UN SOLO GRÁFICO ##
# primera = df_primera.groupby("fecha").primera_dosis.sum().reset_index()
# primera = primera.rename(columns={"primera_dosis": "cantidad_dosis"})
# primera["dosis"] = "primera"

# segunda = df_segunda.groupby("fecha").segunda_dosis.sum().reset_index()
# segunda = segunda.rename(columns={"segunda_dosis": "cantidad_dosis"})
# segunda["dosis"] = "segunda"

# consolidado_total = pd.concat([primera, segunda])
# consolidado_total.to_csv("./consolidado_vacunas.csv", index=False)