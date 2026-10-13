# Sistema de Gestión de Clientes — CRUD con MVC y POO

Práctica: **G001-S04-SOFTWARE2019-PRESENCIAL-Programación Orientada a Objetos-A1**
Objetivo (según la guía oficial): construir un CRUD de Clientes con MVC orientado a
objetos usando las cuatro colecciones de Python (`list`, `tuple`, `set`, `dict`).

Esta versión incluye **solo lo que pide el objetivo**: sin colores de consola, sin
menús extra (buscar, estadísticas) ni clases de más — solo el CRUD completo.

## Requisitos
- Python 3.8 o superior (no necesita librerías externas).

## Estructura del proyecto
```
proyecto_clientes/
├── main.py                  # VISTA: menú de consola (clase MenuClientes)
├── views.py                 # CONTROLADOR: Crear, Leer, Actualizar, Eliminar (clase ClienteController)
├── models.py                # MODELO: clase Cliente
├── data/
│   └── clientes.json        # almacenamiento persistente (se crea/actualiza solo)
└── shared/
    ├── __init__.py
    └── json_manager.py      # clase GestorJSON: lee y guarda el archivo JSON
```

## Cómo ejecutarlo
```bash
cd proyecto_clientes
python main.py        # en Windows
python3 main.py       # en Linux/Mac
```

## Qué hace cada capa (MVC)
- **Vista** (`main.py`): muestra el menú, pide datos con `input()` e imprime resultados
  con `print()`. No valida ni calcula nada.
- **Controlador** (`views.py`): las operaciones Crear, Leer (listar/obtener), Actualizar
  y Eliminar. Nunca usa `print()` ni `input()`.
- **Modelo** (`models.py`): la clase `Cliente` se defiende sola con atributos privados y
  `@property` que validan (nombre y apellido obligatorios, email con formato válido,
  teléfono solo numérico). Si un dato es inválido, lanza `ValueError` y el controlador
  lo convierte en un mensaje para el usuario.

## Las cuatro colecciones en uso
| Colección | Dónde se usa |
|---|---|
| `list` | la colección de registros (`_registros()`, `listar()`) |
| `tuple` | `CAMPOS` y `OBLIGATORIOS` (configuración fija del Modelo) |
| `set` | `emails_registrados()`, para detectar emails duplicados al instante |
| `dict` | cada registro de cliente, y `data/clientes.json` en disco |

## Menú disponible
1. Crear cliente
2. Ver todos
3. Ver por id
4. Actualizar (deja en blanco el campo que no quieras cambiar)
5. Eliminar (pide confirmación sí/no)
0. Salir

## Prueba sugerida
Crea un cliente escribiendo el nombre con espacios de más y el email en mayúsculas —
verás cómo las propiedades del Modelo lo limpian y lo guardan en minúsculas. Luego
intenta crear otro con el mismo email (debe rechazarlo) y otro con letras en el
teléfono (debe rechazarlo también).

Probado de punta a punta: crear, listar, ver por id, actualizar y eliminar — todo
funciona y persiste correctamente en `data/clientes.json`.
