# Traductor de Markdown a HTML

Aplicación de escritorio en Python que traduce un subconjunto de Markdown a HTML usando una gramática definida en ANTLR y una interfaz gráfica desarrollada con PyQt5.

## Información del Curso

* Materia: Programación de Sistemas de Base II  
* Institución: Universidad Autónoma de Tamaulipas (UAT)  
* Semestre: 2025-3  
* Profesor(es): Dante Adolfo Muñoz Quintero  

## Integrantes del Equipo

- Marcos Israel Falcón Alejandre – 2223330152  
- Jorge Alfredo Aquino Reyes – 2213332133  
- Cesar Eduardo Espinosa Arguelles – 2173270075  

## Estructura del Proyecto

El proyecto se organiza para separar el código fuente, los ejemplos de entrada/salida y la documentación técnica del traductor.

- `src/`: contiene la gramática de ANTLR, los analizadores generados y la lógica principal de conversión y GUI.  
- `examples/`: incluye ejemplos de archivos Markdown y sus salidas HTML esperadas.  
- `docs/`: documentación del proyecto (manual de usuario y técnico, etc.).
- Archivos en la raíz: `Driver.py`, `Main.py`, `requirements.txt`, `README.md`.

Ejemplo de árbol del repositorio:

```text
ProgramacionSistemasBase_ProyectoIntegrador/
├─ src/
│  ├─ MarkdownGrammar.g4
│  ├─ MarkdownGrammarLexer.py
│  ├─ MarkdownGrammarParser.py
│  ├─ MarkdownGrammarVisitor.py
│  └─ MarkdownVisitor.py
├─ examples/
│  ├─ valid/
│  │  ├─ ejemplo1.md
│  │  ├─ ejemplo2.md
│  │  └─ ...
│  └─ expected/
│     ├─ ejemplo1.html
│     ├─ ejemplo2.html
│     └─ ...
├─ docs/
│  └─ manual-usuario-tecnico.md
├─ Driver.py
├─ requirements.txt
├─ Main.py
└─ README.md
```

## Requisitos y Dependencias

Software y librerías necesarias para ejecutar el proyecto:

- **Sistema operativo:** Windows, Linux o macOS.  
- **Python:** versión 3.10 o superior (probado con Python 3.11).  
- **Java JRE/JDK:** necesario para regenerar la gramática con ANTLR.  
- **ANTLR 4:** herramienta para generar el lexer y parser a partir de `MarkdownGrammar.g4`.  
- **Dependencias de Python:**
  - `antlr4-python3-runtime`
  - `PyQt5`

Instalación de dependencias (desde la raíz del proyecto):

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux / macOS:
source venv/bin/activate

python -m pip install antlr4-python3-runtime
python -m pip install PyQt5
```

## Instrucciones de Compilación y Ejecución

### 1. Regenerar la gramática (solo si se modifica `MarkdownGrammar.g4`)

Desde la carpeta `src/`:

```bash
cd src
antlr4 -Dlanguage=Python3 -visitor MarkdownGrammar.g4
```

Esto generará o actualizará los archivos:

- `MarkdownGrammarLexer.py`  
- `MarkdownGrammarParser.py`  
- `MarkdownGrammarListener.py`  
- `MarkdownGrammarVisitor.py`  

### 2. Ejecutar la aplicación con interfaz gráfica (GUI)

Desde la raíz del proyecto:

```bash
python Main.py
```

En la GUI se puede:

- Escribir o pegar texto en Markdown.  
- Cargar un archivo `.md` desde el sistema de archivos.  
- Convertir el contenido a HTML.  
- Ver la salida HTML y, opcionalmente, abrirla en el navegador.  
- Visualizar el árbol de sintaxis (AST) del documento Markdown.

### 3. Ejecutar el traductor en modo consola

El script `Driver.py` permite convertir Markdown a HTML sin abrir la interfaz gráfica.

1. Colocar un archivo `entrada.md` en la raíz del proyecto (o ajustar el script para leer otro archivo).  
2. Ejecutar:

```bash
python Driver.py
```

3. Revisar el archivo `salida.html` generado.

## Ejemplos de Uso

### Ejemplo 1: Encabezados y formato básico

**Archivo de entrada (`entrada.md`):**

```markdown
# Reporte de prueba

Este documento contiene **negritas**, *cursivas* y [un enlace](https://example.com).
```

**Salida esperada (`salida.html`):**

```html
<h1>Reporte de prueba</h1>
<p>Este documento contiene <strong>negritas</strong>, <em>cursivas</em> y
<a href="https://example.com">un enlace</a>.</p>
```

### Ejemplo 2: Listas y citas

**Entrada (`entrada.md`):**

```markdown
## Lista de tareas

1. Escribir el Markdown.
2. Convertir a HTML.
3. Revisar el resultado.

> Nota: Solo se soportan los elementos definidos en el alcance del proyecto.
```

**Salida esperada (`salida.html`):**

```html
<h2>Lista de tareas</h2>
<ol>
  <li>Escribir el Markdown.</li>
  <li>Convertir a HTML.</li>
  <li>Revisar el resultado.</li>
</ol>

<blockquote>Nota: Solo se soportan los elementos definidos en el alcance del proyecto.</blockquote>
```

### Ejemplo 3: Uso de los directorios `examples/valid` y `examples/expected`

- `examples/valid/ejemplo1.md` → contiene un caso de prueba válido en Markdown.  
- `examples/expected/ejemplo1.html` → contiene la salida HTML esperada para ese caso.  

Flujo sugerido:

1. Tomar un archivo de `examples/valid/`.  
2. Convertirlo con la GUI o con `Driver.py`.  
3. Comparar el resultado con el archivo correspondiente en `examples/expected/` para validar que el traductor funcione correctamente.
