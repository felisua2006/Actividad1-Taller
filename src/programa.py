# 1 Estructura que almacena los datos de cada columna:
# Usamos un diccionario donde la clave es el nombre de la columna y el valor
# es otro diccionario con su tipo de dato y su porcentaje de completitud
COLUMNAS = {
    "PONDERA": {"tipo": "int", "completitud": 95.0},
    "ESTADO": {"tipo": "int", "completitud": 100.0},
    "CAT_OCUP": {"tipo": "int", "completitud": 80.0},
    "EDAD": {"tipo": "int", "completitud": 99.5},
    "REGION": {"tipo": "int", "completitud": 100.0},
    "AGLOMERADO": {"tipo": "int", "completitud": 100.0},
    "ANO4": {"tipo": "int", "completitud": 100.0},
    "TRIMESTRE": {"tipo": "int", "completitud": 98.0},
    "ITF": {"tipo": "int", "completitud": 75.0},
    "MAS_500": {"tipo": "string", "completitud": 90.0},
    "GDECCFR": {"tipo": "int", "completitud": 70.0},
    "NIVEL_ED": {"tipo": "int", "completitud": 88.0} # modificacion para incluir la columna NIVEL_ED
}

# 2 Estructura para almacenar los roles:
# Usamos un diccionario de diccionarios para acceder por el nombre del rol
ROLES = {
    "docente": {
        "columnas": ["EDAD", "REGION", "ESTADO", "CAT_OCUP"],
        "criterio": "nombre",
        "orden": "A",
        "umbral": 85.0
    },
    "investigador": {
        "columnas": ["PONDERA", "ESTADO", "EDAD", "ITF", "GDECCFR", "MAS_500", "NIVEL_ED"],
        "criterio": "completitud",
        "orden": "B",
        "umbral": 75.0
    },
    "analista": {
        "columnas": ["ANO4", "TRIMESTRE", "REGION", "AGLOMERADO", "ITF"],
        "criterio": "completitud",
        "orden": "A",
        "umbral": None  # no se especifica umbral
    },
    "auditor": {                            #Modificacion para incluir el rol auditor
        "columnas": list(COLUMNAS.keys()),  # Incluye todas las columnas 
        "criterio": "nombre",
        "orden": "B",                       # "B" indica orden descendente 
        "umbral": None                      # Sin umbral de completitud para ver todas
    }                 
}

#FUNCIONES AUXILIARES 

def obtener_completitud(columna):
    """Devuelve el porcentaje de completitud"""
    return columna["completitud"]


def obtener_nombre(columna):
    """Devuelve el nombre"""
    return columna["nombre"]


#FUNCION PRINCIPAL 

def generar_informe(rol=None, dataset_columnas=COLUMNAS, configuracion_roles=ROLES):
    """
    Genera un informe filtrado y ordenado de las columnas según el rol
    
    Si no se especifica un rol: retorna todas las columnas ordenadas 
    por completitud de forma descendente
     
    Si se indica un rol válido: 
    filtra por las columnas de interés, aplica el umbral de completitud
    y ordena según el rol
    """
    # CASO 1 Si no se especifica el rol
    if rol is None or rol not in configuracion_roles:
        columnas_base = [
            {
                "nombre": nombre,"tipo": datos["tipo"],"completitud": datos["completitud"]
            }
            for nombre, datos in dataset_columnas.items()
        ]
        #reverse= TRUE ordena de mayor a menor
        return sorted(columnas_base, key=obtener_completitud, reverse=True)

    # CASO 2: Se especifica un rol valido
    config_rol = configuracion_roles[rol]
    columnas_interes = config_rol["columnas"]
    criterio = config_rol.get("criterio", "completitud")
    orden = config_rol.get("orden", "B")
    umbral = config_rol.get("umbral")

    #1 Obtenemos las columnas interes
    columnas_validas =[
        {
            "nombre": col,"tipo": dataset_columnas[col]["tipo"],"completitud": dataset_columnas[col]["completitud"]
        }
        for col in columnas_interes if col in dataset_columnas
     ]

    #2 Filtramos por umbral de completitud las columnas_validas
 
    if umbral is not None:
        def cumple_umbral(columna):
            """Verifica si una columna cumple con el umbral de completitud"""
            return columna["completitud"] >= umbral
    
        columnas_filtradas = list(filter(cumple_umbral, columnas_validas))#usamos la funcion filter         
    else:
        columnas_filtradas = columnas_validas

    #3 Elegir la funcion de criterio de orden segun lo configurado en el rol
     #docente ordena por Nombre
     #investigador ordena por completitud
     #analista ordena por completitud
    if criterio == "nombre":
        funcion_criterio = obtener_nombre
    else:
        funcion_criterio = obtener_completitud

    #4 Definimos la direccion de ordenamiento ('A' ascendente / 'B' descendente)
    es_descendente = True if orden == "B" else False

    #5 Devolvemos la lista ordenada
    return sorted(columnas_filtradas, key=funcion_criterio, reverse=es_descendente)