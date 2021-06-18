#!/usr/bin/bash

EXECUTIONDATE=`date +%Y%m%d%H%M`;   # YYYYMMDDHHmm
EXECUTIONDATEBACKUP=`date +%d%m%Y`; # para los backups
UNIXTIME=`date +%s`;                # genera unix time para diferencias las carpetas de backup cuando hay más de una generada por día
PATHDOCVALE="/mnt/c/Users/valea/Documents";

echo "[`(date +"%F %T")`] Git pull al repo de ICOVID"

cd /home/vale/datagov/icovid/ICOVID;
# cd /home/pas/datagovuc/icovid/ICOVID;
git pull;

echo "[`(date +"%F %T")`] Creación carpeta /archivos-step-one/${EXECUTIONDATE}/"
echo "[`(date +"%F %T")`] Creación carpeta /archivos-step-two/${EXECUTIONDATE}/"

# # cd /home/pas/python/icovid-scripts;
# mkdir /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-one/${EXECUTIONDATE};
# mkdir /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-two/${EXECUTIONDATE};

cd /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/;
mkdir /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-one/${EXECUTIONDATE};
mkdir /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-two/${EXECUTIONDATE};

echo "[`(date +"%F %T")`] Ejecutamos el py script que generas los archivos para el sitio ICOVID"

python3 step_two.py ${EXECUTIONDATE}

echo "[`(date +"%F %T")`] Copiamos los archivos generados para el sitio ICOVID en la ruta /backup/generated/"

# /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/
if [ ! -d "${PATHDOCVALE}/ICOVID/resumen/${EXECUTIONDATEBACKUP}" ]; then
  mkdir /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP};
  cp /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-one/${EXECUTIONDATE}/*.xlsx /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP};
  cp /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-two/${EXECUTIONDATE}/*.xlsx /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP};
else
  mkdir /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  mv /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP}/* /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  cp /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-one/${EXECUTIONDATE}/*.xlsx /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP};
  cp /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/archivos-step-two/${EXECUTIONDATE}/*.xlsx /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/generated/${EXECUTIONDATEBACKUP};
fi

echo "[`(date +"%F %T")`] Copiamos las carpetas de interés del repo actualizadas en la ruta /backup/repo/"

# /home/vale/datagov/icovid/scripts/scripts-icovid/icovid-scripts/backup/repo/
if [ ! -d "${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}" ]; then
  mkdir ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension1 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension2 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension3 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension4 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
else
  mkdir ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  mv ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}/* ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP}_${UNIXTIME};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension1 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension2 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension3 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
  cp -r /home/vale/datagov/icovid/ICOVID/dimension4 ${PATHDOCVALE}/ICOVID/icovid-repo/${EXECUTIONDATEBACKUP};
fi

echo "[`(date +"%F %T")`] Proceso finalizado con éxito"