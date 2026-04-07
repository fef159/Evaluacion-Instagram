# 📱 Instagram Downloader - Docker

## 📌 Descripción

Aplicación web desarrollada con Flask que permite descargar videos de Instagram.
Está containerizada con Docker y desplegada en AWS EC2.

---

## ⚙️ Tecnologías

* Python 3.11
* Flask
* yt-dlp
* Docker
* AWS EC2

---

## 🚀 Cómo ejecutar

### 1. Clonar repositorio

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
```

### 2. Construir imagen

```bash
docker build -t insta-app .
```

### 3. Ejecutar contenedor

```bash
docker run -d -p 5000:5000 insta-app
```

---

## 🌐 Acceso

Abrir en navegador:

```
http://IP:5000
```

Ejemplo:

```
http://3.236.139.44:5000
```

---

## 📁 Estructura

```
APP/
 ├── app.py
 ├── requirements.txt
 ├── Dockerfile
 ├── Dockerfile.optimizado
 ├── Dockerfile.multistage
 └── .dockerignore
```

---

## 👤 Autor

* Anderson Miguel Ninahuaman Yuto
