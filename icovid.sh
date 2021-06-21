#!/usr/bin/bash

EXECUTIONDATE=$(date +%Y%m%d); # para los backups
UNIXTIME=$(date +%s);                # genera unix time para diferencias las carpetas de backup cuando hay más de una generada por día
PATHDOC="/mnt/c/Users/${1}/Documents"; # ponemos el nombre usuario en Windows
# PATHDOC=$1
ROOTPATH="${HOME}/datagov/scripts-icovid";
# ROOTPATH2="${HOME}/datagovuc/icovid";

echo "[$(date +"%F %T")] Git pull al repo de ICOVID"

# cd ${ROOTPATH}/ICOVID;
cd ${HOME}/datagovuc/icovid/ICOVID;
git pull;

# cd ${HOME}/datagov/icovid/icovid-scripts;
cd ${HOME}/python/scripts-icovid;

echo "[$(date +"%F %T")] Generamos los archivos para las dimensiones de la 1 a la 4"

python3 icovid-dimensiones/step_one.py;
python3 icovid-dimensiones/step_two.py;

echo "[$(date +"%F %T")] Copiamos los archivos generados en la ruta ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE}"

if [ ! -d "${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE}" ]; then
  sudo mkdir -p ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-dimensiones/archivos-step-one/${EXECUTIONDATE}/*.xlsx ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-dimensiones/archivos-step-two/${EXECUTIONDATE}/*.xlsx ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE};
else
  sudo mkdir -p ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE}_${UNIXTIME};
  sudo mv ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE}/*.xlsx ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE}_${UNIXTIME};
  sudo cp ${ROOTPATH}/icovid-dimensiones/archivos-step-one/${EXECUTIONDATE}/*.xlsx ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-dimensiones/archivos-step-two/${EXECUTIONDATE}/*.xlsx ${PATHDOC}/ICOVID/resumen/${EXECUTIONDATE};
fi

echo "[$(date +"%F %T")] Copiamos las carpetas del repo actualizadas en la ruta ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE}"

if [ ! -d "${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE}" ]; then
  sudo mkdir -p ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension1 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension2 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension3 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension4 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
else
  sudo mkdir -p ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE}_${UNIXTIME};
  sudo mv ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE}/* ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE}_${UNIXTIME};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension1 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension2 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension3 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
  sudo cp -r ${ROOTPATH}/ICOVID/dimension4 ${PATHDOC}/ICOVID/icovid-repo/${EXECUTIONDATE};
fi

echo "[$(date +"%F %T")] Generamos los archivos para fallecidos"

bash icovid-dead/dead.sh;

echo "[$(date +"%F %T")] Generamos los archivos para hospitalizados"

python3 icovid-hosp/hospitalizados.py;

echo "[$(date +"%F %T")] Generamos los archivos para vacunados"

python3 icovid-vacunacion/vacunas.py;
python3 icovid-vacunacion/nuevos_vacunas.py;


if [ ! -d "${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE}" ]; then
  sudo mkdir -p ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-dead/fallecidos-etario/${EXECUTIONDATE}/fallecidos-etario.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-hosp/archivos_hospitalizados/${EXECUTIONDATE}/hospitalizados_etario.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-vacunacion/archivos_vacunas/*.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-vacunacion/archivos_nuevos_vacunas/*.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
else
  sudo mkdir -p ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE}_${UNIXTIME};
  sudo mv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE}/* ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE}_${UNIXTIME};
  sudo cp ${ROOTPATH}/icovid-dead/fallecidos-etario/${EXECUTIONDATE}/fallecidos-etario.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-hosp/archivos_hospitalizados/${EXECUTIONDATE}/hospitalizados_etario.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-vacunacion/archivos_vacunas/*.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
  sudo cp ${ROOTPATH}/icovid-vacunacion/archivos_nuevos_vacunas/*.csv ${PATHDOC}/ICOVID/nuevas-visualizaciones/${EXECUTIONDATE};
fi

echo "[$(date +"%F %T")] Proceso finalizado con éxito"