# 🏥 Sistema de Historia Clínica

Este es un sistema web desarrollado en Django que implementa la estructura y datos definidos por la Resolución 866 de 2021 del Ministerio de Salud y Protección Social de Colombia. Permite la gestión de pacientes, contactos clínicos y tablas maestras esenciales para la interoperabilidad de la historia clínica electrónica.

## ⚙️ Tecnologías utilizadas

- Python 3.10+
- Django 5.2
- MySQL
- HTML5 + CSS
- PyCharm Community Edition 2025.1

## 🚀 Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/ricomariaca/proyecto-con-Django.git
   cd proyecto-con-Django
   ```

2. Instala las dependencias:

   ```bash
   pip install mysqlclient
   pip install django


   ```

3. Crea la base de datos MySQL:

   ```sql
   CREATE DATABASE clinicadb;
   ```

4. Configura la conexión en settings.py:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'clinicadb',
           'USER': 'root',
           'PASSWORD': '123456',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Aplica las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Crea un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

7. Ejecuta el servidor:

   ```bash
   python manage.py runserver
   ```

---

📌 Recuerda que el sistema incluye autenticación, gestión de pacientes, contactos clínicos, y tablas maestras basadas en la Resolución 866. Las vistas principales están protegidas por login y el panel de administración se encuentra disponible en /admin/.

👨‍⚕️ Desarrollado por Emanuel Rico Mariaca 
