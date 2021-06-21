#!/usr/bin/bash

EXECUTIONDATE=`date +%Y%m%d%H%M`;   # YYYYMMDDHHmm
EXECUTIONDATEBACKUP=`date +%d%m%Y`; # para los backups
UNIXTIME=`date +%s`;                # genera unix time para diferencias las carpetas de backup cuando hay más de una generada por día
PATHDOCVALE="/mnt/c/Users/valea/Documents";
PATHSCRIPTS=$(pwd);

echo "[`(date +"%F %T")`] Git pull al repo de ICOVID"

cd /home/vale/datagov/icovid/ICOVID;
git pull;

echo "[`(date +"%F %T")`] Creación carpeta /archivos-step-one/${EXECUTIONDATE}/"
echo "[`(date +"%F %T")`] Creación carpeta /archivos-step-two/${EXECUTIONDATE}/"

cd ${PATHSCRIPTS}/icovid-scripts/;
mkdir -p ${PATHSCRIPTS}/icovid-scripts/archivos-step-one/${EXECUTIONDATE};
mkdir -p ${PATHSCRIPTS}/icovid-scripts/archivos-step-two/${EXECUTIONDATE};

echo "[`(date +"%F %T")`] Ejecutamos el py script que generas los archivos para el sitio ICOVID"

python3 step_two.py

echo "[`(date +"%F %T")`] Copiamos los archivos generados para el sitio ICOVID en la ruta /backup/generated/"

if [ ! -d "${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP}" ]; then
  mkdir -p ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP};
  cp ${PATHSCRIPTS}/icovid-scripts/archivos-step-one/${EXECUTIONDATE}/*.xlsx ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP};
  cp ${PATHSCRIPTS}/icovid-scripts/archivos-step-two/${EXECUTIONDATE}/*.xlsx ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP};
else
  mkdir -p ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  mv ${PATHSCRIPTS}/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP}/* ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  cp ${PATHSCRIPTS}/icovid-scripts/archivos-step-one/${EXECUTIONDATE}/*.xlsx ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP};
  cp ${PATHSCRIPTS}/icovid-scripts/archivos-step-two/${EXECUTIONDATE}/*.xlsx ${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP};
fi

echo "[`(date +"%F %T")`] Copiamos las carpetas de interés del repo actualizadas en la ruta /backup/repo/"

if [ ! -d "${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}" ]; then
  mkdir -p ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension1 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension2 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension3 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension4 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
else
  mkdir -p ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  mv ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}/* ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension1 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension2 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension3 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension4 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
fi

echo "[`(date +"%F %T")`] Proceso finalizado con éxito"