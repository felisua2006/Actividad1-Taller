
●Qué ventajas tienen las estructuras elegidas para almacenar los datos de las 
columnas y roles  con respecto a otras de las vistas en la teoría? 

●¿Qué valores elegiste para los roles y los  porcentajes de completitud y por qué? 
    Elegí valores variados y realistas (por ejemplo, ESTADO al 100%, ITF al 75%, GDECCFR al 70%)
    
¿Cómo garantizaste que el programa pueda ser validado con diferentes roles, 
criterios de ordenamiento y umbrales?  
    Hice que la función generar_informe tenga diferentes criterios 

●  ¿Por qué conviene separar la configuración de los roles (ROLES) de la lógica que 
genera el informe?
    porque si quisieramos cambiar algun dato de los roles tendriamos que cambiar el código fuente

●  ¿Qué parámetros se pueden definir con valores por defecto? 
    yo defini 3 rol=none en caso de que no entre ningun rol-dataset_columnas=COLUMNAS para que use el diccionario principal-configuracion_roles=ROLES para usar la configuracion estandar 

●  Si agregás una nueva columna al dataset, ¿en qué partes del código impacta? ¿Y si 
solo se quiere que un rol existente incluya esa nueva columna? 
    solo impacta en COLUMNAS 
    Tenés que ir al diccionario ROLES y agregar el nombre de esa columna dentro de la lista "columnas" en el rol existente 

●  ¿Qué pasaría si un rol tuviera un criterio de orden distinto a los especificados 
"nombre" o "completitud" (por ejemplo, "promedio")? ¿Cómo lo detectarías y 
qué harías para que el programa no falle? 
    Si apareciera un criterio nuevo, el código actual caería en el else y usaría obtener_completitud
    tendria que mejorar usando  (if/elif/else) 

●  ¿Qué cambiarías si por defecto se pide el informe debiera salir según uno de los 
roles?
    Simplemente cambiaría el valor por defecto del parámetro rol=None en la firma de la función por el nombre del rol que quiero que actúe por defecto (por ejemplo, rol="docente")
    
# Bitácora de la Actividad 1

Acá anoto más o menos lo que fui haciendo en el código para no perderme y tenerlo de referencia.

## ¿Qué fui armando en el código (`src/programa.py`)?
- Primero creé un diccionario grande con las `COLUMNAS` y otro con los `ROLES` (docente, investigador, analista) para guardar los datos y las configuraciones de cada uno que nos daba una ventaja al buscar mas rapido por clave-valor y nos daba una mejor organizacion
- Hice dos funciones auxiliares cortitas (`obtener_completitud` y `obtener_nombre`) para que el `sorted` sepa qué usar cuando tiene que ordenar.
- Después armé la función principal `generar_informe`:
  - Si no le ponés ningún rol, te devuelve todas las columnas de una, ordenadas de mayor a menor por la completitud (usando `reverse=True`).
  - Si le pasás un rol, busca las columnas que le tocan.
  - Para sacar las que pasaban el umbral primero use if pero luego me decante por usar `filter` al sumar valor,combinandolo con una funcion interna `cumple_umbral` 
  - Al final agrege los docstrings `"""` arriba de todo en cada función porque lo pedía la consigna

## (Problemas técnicos)
- **El nombre del archivo en VS Code:** Le quise poner una barra diagonal con el número de sub-legajo (`.../3.ipynb`) y VS Code creía que era una carpeta.Y no me abría el archivo. Tuve que borrar la barra, ponerle un guión  (`-3.ipynb`) y ahí recién me dejó trabajar.
- También con la extensión de Jupyter, tuve que tocar unas cosas de las asociaciones de archivos en la configuración.

## Pruebas
- Abrí el notebook, importé el archivo `programa.py` y corrí los tres perfiles y me tiro los tres perfiles 