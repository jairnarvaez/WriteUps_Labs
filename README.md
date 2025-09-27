# WriteUps_Labs

Una aplicación web desarrollada en **Django**, que integra funcionalidades dinámicas con una API interna y una interfaz moderna. El objetivo de la página es documentar mi proceso de aprendizaje en el mundo de la ciberseguridad.

<https://github.com/user-attachments/assets/e9e49630-3cfb-49a2-bf0d-ec364d1fb12b>


---

## Requisitos

- Python 3.10 o superior
- pip
- virtualenv (opcional pero recomendado)
- Git (para clonar el repositorio)

---

## Instalación y Configuración

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. **Crear un entorno virtual**

```bash
python -m venv env
```

3. **Activar el entorno virtual**

- En Linux / macOS:

```bash
source env/bin/activate
```

- En Windows (PowerShell):

```powershell
.\env\Scripts\Activate.ps1
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

5. **Configurar variables de entorno**

Editar el archivo de configuración (por ejemplo `.env` o `settings.py`) y establecer los siguientes valores:

```env
BASE_URL="127.0.0.1:8000"
API_BASE_URL="127.0.0.1:8000/api"
DEBUG=True
```

6. **Aplicar migraciones de la base de datos**

```bash
python manage.py migrate
```

7. **Correr el servidor de desarrollo**

```bash
python manage.py runserver
```

La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Uso

- Acceder al panel de administración de Django en `/admin`  
- Consumir la API interna desde `/api`  
- Modificar contenido dinámico directamente desde el panel de administración

