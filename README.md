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

Esto debería generar los siguientes directorios dentro del directorio `datagov`:

```bash
datagov
├── ICOVID
└── scripts-icovid
```

## Generación archivos para subir a Drive ICOVID

Para generar los archivos que se cargan en Google Drive debemos, primero, cambiarnos al directorio `scripts-icovid`:

```bash
cd scripts-icovid
```

Y luego ejecutar lo siguiente:

```bash
./icovid.sh <usuario_windows>
```

Donde `<usuario_windows>` es el nombre de usuario que tienen en Windows, por ejemplo, `valea`. Esto es necesario pues así vamos a hacer una copia de solo los archivos necesario dentro de la carpeta `Documentos` de Windows. Siguiendo con el ejemplo, el comando a ejcutar sería:

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

Ejecutar este comando va a generar tres carpetas dentro de `Documentos`:
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

## Rutas de carga a Drive de los archivos generados

+ Los archivos que se generan dentro de `resumen` se deben subir en [**este drive**](https://drive.google.com/drive/u/0/folders/1OUYrFVFs4dcbqkgaBCqP8HKRHUe7XE94), excepto los archivos `nacional_T1.xlsx` y `regional_T1.xlsx`, que deben subir a [**este drive**](https://drive.google.com/drive/u/0/folders/1atrwkcYo3JUWm7zwxjwr5DkPZptYTCH2).

+ Los archivos que se generan dentro de `nuevas-visualizaciones` se deben subir en [**este drive**](https://drive.google.com/drive/u/0/folders/1azKFQpv5_lC99Tw1N_0U5K89IKNBivQm), excepto `total_nacional_vacunas.csv`, `vacunacion_regiones.csv` y `consolidado_vacunas.csv`, que se deben subir [**este drive**](https://drive.google.com/drive/u/0/folders/1zGH75dM4yQJ2qJ7tBIRmz9ttE4fWLAF2)

+ Las carpetas que se generan dentro de `icovid-repo` se deben subir en [**este drive**](https://drive.google.com/drive/u/0/folders/0AIZz-0H8A-VcUk9PVA)

## Visualizaciones y envío de mail a redactores del informe semanal

Una vez cargados todos los archivos en Drive, estos se deben actualizar en Tableu. Si todo sale bien, el siguiente paso es enviar un mail a las personas encargadas de redactar el informe de la semana. La información con las personas redactoras por semana y sus emails se encuentra en [**este documento**](https://docs.google.com/document/d/1r2JJ586hB3jLfTw-bKvfXGqPGxnsywJJXpMs2r43LVk/edit)