# Guía para ejecutar los procesos de generación y transformación de archivos para ICOVID

Si se trabajo en Windows, debemos descargar el subsistema de Linux para Windows (WSL). Para ello debemos seguir cuidadosamente las instrucciones detalladas en https://docs.microsoft.com/en-us/windows/wsl/install-win10

Una vez que tengamos WSL instalado y funcionando en nuestro sistema, vamos a la Microsoft Store y descargamos alguna distribución de Linux, para que sea compatible con esta guía debe ser preferentemente Ubuntu (también puede ser Debian).

## Configuración y estructura del entorno de trabajo

Hecho lo anterior, abrimos la terminal de Linux que hayamos descargado de Microsfot Store y ejecutamos el siguiente comando para crear el directorio `datagov` que es donde guardaremos tanto el repositorio de ICOVID como los scripts que generan los archivos para las visualizaciones. 

```bash
mkdir datagov && cd datagov
```

Luego, clonamos el repositorio de ICOVID:

```bash
git clone https://github.com/datagovuc/ICOVID.git
```

Y el repositorio con los scripts:

```bash
git clone https://github.com/datagovuc/scripts-icovid.git
```

Esto debería generar los siguientes directorios enl directorio `datagov`:

```bash
datagov
├── ICOVID
└── scripts-icovid
```

## Generación archivos para subir a Drive ICOVID

### Ejecución proceso global 

Para generar los archivos que se cargan en Google Drive debemos, primero, cambiarnos al directorio `scripts-icovid`:

```bash
cd scripts-icovid
```

Y luego ejecutar lo siguiente:

```bash
./icovid.sh <usuario_windows>
```

Si no funciona, probar con:

```bash
bash icovid.sh <usuario_windows>
```

Donde `<usuario_windows>` es el nombre de usuario que tienen en Windows, por ejemplo, `valea`. Esto es necesario pues así vamos a hacer una copia de solo los archivos necesario en la carpeta `Documentos` de Windows. Siguiendo con el ejemplo, el comando a ejcutar sería:

```bash
./icovid.sh valea
```

**Nota:** es importante respetar el nombre de usario en Windows tal como lo tienen ahí. Es decir, si empieza con mayúscula, se debe respetar, lo mismo si el nombre tiene espacios. Así, para nombres con mayúscula ejecutamos lo siguiente:

```bash
./icovid.sh Valea
```

Y para nombre con espacio, lo siguiente:

```bash
./icovid.sh "Vale A"
```

Ejecutar este comando va a generar tres carpetas en `Documentos`:
+ `resumen`
+ `icovid-repo`
+ `nuevas-visualizaciones`

En cada una de las carpetas se va a generar una subcarpeta con la fecha de ejecución en formato **yyyymmdd**; en caso de hagan más de una ejecución por día, se generará también una caperta con la siguiente estructura **yyyymmdd_unix**. Por ejemplo, si se hacen dos ejecuciones el día 21 de junio del 2021, las subcarpetas de, digamos, `resumen` serán las siguientes:

```bash
resumen
├── 20210621
└── 20210621_1624323245
```

Es importante notar que los archivos de la última ejecución siempre van a quedar en la carpeta con formato **yyyymmdd**.

### Ejecución proceso por separado

La generación de los archivos también se puede hacer de manera parcelado y por separado, lo cual nos permite mayor flexibilidad si, por ejemplo, se quisiera actualizar solamente una tanda de archivos y no todos a la vez.

El proceso se puede divir de acuerdo a los siguientes subprocesos:

#### Generación archivos Dimensiones 1 a 4

Este subproceso corresponde al primer proceso de generación de archivos relacionados con las 4 dimensiones definidas por el grupo de ICOVID. Para ejecutarlo corremos lo siguiente dentro del directorio `scripts-icovid`:

```bash
python3 icovid-dimensiones/step_one.py && python3 icovid-dimensiones/step_two.py
```

Los archivos generados se guardan en las siguientes rutas dentro de `scripts-icovid`:

```bash
icovid-dimensiones
├── archivos-step-one
│   └── 20210621
└── archivos-step-two
    └── 20210621
```

De aquí se deben considerar solo los archivos en formato `.xlsx` de ambos directorios.

#### Generación archivos hospitalizados

Para la ejecuión de este subproceso, corremos lo siguiente dentro de `scripts-icovid`:

```bash
python3 icovid-hosp/hospitalizados.py
```

Los archivos generados se guardan en las siguientes rutas dentro de `scripts-icovid`:
```bash
icovid-hosp/
└── archivos_hospitalizados
    └── 20210621
```

De aquí se debe considerar solo el archivos `hospitalizados_etario.csv`

#### Generación archivos fallecidos

Para la ejecuión de este subproceso, corremos lo siguiente dentro de `scripts-icovid`:

```bash
bash icovid-dead/dead.sh 
```

Los archivos generados se guardan en las siguientes rutas dentro de `scripts-icovid`:
```bash
icovid-dead/
└── fallecidos-etario
    └── 20210621
```

De aquí se debe considerar solo el archivos `fallecidos-etario.csv`

#### Generación archivos vacnuados

Para la ejecuión de este subproceso, corremos lo siguiente dentro de `scripts-icovid`:

```bash
python3 icovid-vacunacion/vacunas.py && python3 icovid-vacunacion/nuevos_vacunas.py
```

Los archivos generados se guardan en las siguientes rutas dentro de `scripts-icovid`:
```bash
icovid-vacunacion/
├── archivos_nuevos_vacunas
└── archivos_vacunas
```

Consideramos todos los archivos de ambos directorios.

## Rutas de carga a Drive de los archivos generados

Los archivos generados en `resumen` se deben subir a [**este drive**](https://drive.google.com/drive/u/0/folders/1OUYrFVFs4dcbqkgaBCqP8HKRHUe7XE94), excepto los archivos `nacional_T1.xlsx` y `regional_T1.xlsx`, que se suben a [**este drive**](https://drive.google.com/drive/u/0/folders/1atrwkcYo3JUWm7zwxjwr5DkPZptYTCH2).

Los archivos generados en `nuevas-visualizaciones` se deben subir a [**este drive**](https://drive.google.com/drive/u/0/folders/1azKFQpv5_lC99Tw1N_0U5K89IKNBivQm), excepto `total_nacional_vacunas.csv`, `vacunacion_regiones.csv` y `consolidado_vacunas.csv`, que se suben a [**este drive**](https://drive.google.com/drive/u/0/folders/1zGH75dM4yQJ2qJ7tBIRmz9ttE4fWLAF2)

Las carpetas generadas en `icovid-repo` se deben subir a [**este drive**](https://drive.google.com/drive/u/0/folders/0AIZz-0H8A-VcUk9PVA)

## Visualizaciones y envío de mail a redactores del informe semanal

Una vez cargados todos los archivos en Drive, estos se deben actualizar en Tableu. Si todo sale bien, el siguiente paso es enviar un mail a las personas encargadas de redactar el informe de la semana. Primero se actualiza solo el sitio previo para informes y el miércoles ambos sitios, el previo par ainformes y el sitio público. Se les debe informar cuando esto ocurra, y la primera actualización debe estar antes del martes a las 17:00 horas, pues el grupo se reune a los martes a las 17:30. La información con las personas redactoras por semana y sus emails se encuentra en [**este documento**](https://docs.google.com/document/d/1r2JJ586hB3jLfTw-bKvfXGqPGxnsywJJXpMs2r43LVk/edit)
