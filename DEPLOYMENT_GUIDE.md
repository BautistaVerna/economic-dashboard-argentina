# 🚀 GUÍA COMPLETA DE DEPLOYMENT - Dashboard Económico Argentina

## 📋 Tabla de Contenidos
1. [Deploy Local (Para Testing)](#deploy-local)
2. [Deploy en Streamlit Cloud (GRATIS - RECOMENDADO)](#deploy-streamlit-cloud)
3. [Deploy en Railway (Alternativa)](#deploy-railway)
4. [Deploy en Render (Otra Alternativa)](#deploy-render)

---

## Deploy Local

### ✅ Paso 1: Preparar el Entorno

```bash
# Verifica que tengas Python instalado
python --version  # Debe ser 3.10 o superior

# Crea una carpeta para el proyecto
mkdir economic-dashboard
cd economic-dashboard

# Descarga los archivos del proyecto (si aún no los tienes)
# Copia: economic_dashboard.py, requirements.txt, README.md
```

### ✅ Paso 2: Crear Entorno Virtual

```bash
# Crea el entorno virtual
python -m venv venv

# Actívalo
# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

### ✅ Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### ✅ Paso 4: Ejecutar la App

```bash
streamlit run economic_dashboard.py
```

La app se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## Deploy en Streamlit Cloud (GRATIS - RECOMENDADO)

### ✅ Paso 1: Crear Cuenta en GitHub

1. Ve a [github.com](https://github.com)
2. Crea una cuenta si no tienes (es gratis)
3. Verifica tu email

### ✅ Paso 2: Crear Repositorio

1. Click en el botón "+" arriba a la derecha
2. Selecciona "New repository"
3. Nombre: `economic-dashboard-argentina`
4. Descripción: "Dashboard económico interactivo con datos de Argentina en tiempo real"
5. Marca como "Public"
6. Click en "Create repository"

### ✅ Paso 3: Subir tus Archivos

**Opción A - Interfaz Web (Más Fácil):**

1. En tu repositorio nuevo, click en "uploading an existing file"
2. Arrastra estos archivos:
   - `economic_dashboard.py`
   - `requirements.txt`
   - `README.md`
3. Escribe un mensaje: "Initial commit - Dashboard económico"
4. Click en "Commit changes"

**Opción B - Git por Terminal:**

```bash
# Inicializa git en tu carpeta del proyecto
git init

# Agrega los archivos
git add economic_dashboard.py requirements.txt README.md

# Haz el primer commit
git commit -m "Initial commit - Dashboard económico"

# Conecta con GitHub
git remote add origin https://github.com/TU-USUARIO/economic-dashboard-argentina.git

# Sube los archivos
git push -u origin main
```

### ✅ Paso 4: Deploy en Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Click en "Sign in with GitHub"
3. Autoriza a Streamlit
4. Click en "New app"
5. Completa:
   - **Repository**: Selecciona `economic-dashboard-argentina`
   - **Branch**: `main`
   - **Main file path**: `economic_dashboard.py`
   - **App URL** (opcional): Elige un nombre personalizado
6. Click en "Deploy!"

### ✅ Paso 5: ¡Listo!

En 2-3 minutos tu app estará disponible en:
`https://TU-NOMBRE-economic-dashboard-argentina.streamlit.app`

**Comparte esta URL en tu portfolio!**

---

## Deploy en Railway (Alternativa)

Railway es otra plataforma gratuita. Es un poco más técnico pero da más control.

### ✅ Requisitos Adicionales

Necesitás crear 2 archivos más:

**1. `Procfile` (sin extensión):**
```
web: streamlit run economic_dashboard.py --server.port=$PORT --server.address=0.0.0.0
```

**2. `runtime.txt`:**
```
python-3.11.5
```

### ✅ Pasos

1. Ve a [railway.app](https://railway.app)
2. Sign up con GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecciona tu repositorio
5. Railway detectará automáticamente que es Python
6. Click en "Deploy"
7. Una vez deployado, ve a Settings → Networking → Generate Domain
8. ¡Listo! Tenés tu URL pública

---

## Deploy en Render (Otra Alternativa)

Render también ofrece plan gratuito.

### ✅ Archivos Adicionales Necesarios

**`render.yaml`:**
```yaml
services:
  - type: web
    name: economic-dashboard
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run economic_dashboard.py --server.port=$PORT --server.address=0.0.0.0
```

### ✅ Pasos

1. Ve a [render.com](https://render.com)
2. Sign up con GitHub
3. "New" → "Web Service"
4. Conecta tu repositorio
5. Configuración:
   - **Name**: economic-dashboard
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run economic_dashboard.py --server.port=$PORT --server.address=0.0.0.0`
6. Click "Create Web Service"
7. Espera 5-10 minutos
8. ¡Listo!

---

## 🎯 ¿Cuál Elegir?

### Streamlit Cloud ⭐ RECOMENDADO
- ✅ **MÁS FÁCIL** - Solo 4 clicks
- ✅ **GRATIS** para siempre
- ✅ **RÁPIDO** - 2 minutos de deploy
- ✅ **OPTIMIZADO** para Streamlit
- ❌ Limitado a apps de Streamlit

### Railway
- ✅ Más flexible
- ✅ Buenos resources en plan free
- ✅ Fácil de usar
- ❌ Plan free tiene límites mensuales

### Render
- ✅ Muy confiable
- ✅ Buen performance
- ❌ El plan free "hiberna" tras 15 min de inactividad
- ❌ Puede ser lento al despertar

---

## 🔧 Troubleshooting Común

### Error: "Module not found"
**Solución**: Asegurate que `requirements.txt` tiene todas las librerías

### Error: "Port already in use"
**Solución**: 
```bash
# Busca el proceso usando el puerto
lsof -i :8501

# Mátalo
kill -9 PID_DEL_PROCESO
```

### La app no carga datos
**Solución**: 
- Verifica tu conexión a internet
- La API puede estar caída temporalmente
- Espera 1-2 minutos y refresca

### El deploy falla en Streamlit Cloud
**Solución**:
- Verifica que `requirements.txt` esté en la raíz del repo
- Chequea que el nombre del archivo principal sea exacto
- Mira los logs en la sección "Manage app"

---

## 📊 Próximos Pasos

Una vez deployado:

1. **Agrega la URL a tu CV/LinkedIn**
2. **Toma screenshots para tu portfolio**
3. **Compártelo en redes sociales**
4. **Muéstralo en aplicaciones de Upwork/Fiverr**

### Mensaje para compartir:

```
🚀 Acabo de lanzar mi Dashboard Económico Argentina!

📊 Datos en tiempo real de:
- Cotizaciones del dólar (Oficial, Blue, MEP, CCL)
- Brecha cambiaria
- Inflación mensual
- Riesgo país

🛠️ Hecho con Python, Streamlit y Plotly

👉 Probalo acá: [TU-URL]

#Python #DataScience #Argentina #Streamlit
```

---

## 💡 Tips Pro

1. **Agrega Google Analytics** para ver cuánta gente lo usa
2. **Comparte en Reddit** (r/argentina, r/merval)
3. **Crea un post en LinkedIn** mostrando el código
4. **Haz un video corto** explicando cómo lo hiciste
5. **Actualiza constantemente** - agrega features

---

## ✅ Checklist Final

Antes de compartir tu proyecto:

- [ ] La app funciona localmente
- [ ] Está deployada y pública
- [ ] El README está completo con tu info
- [ ] Los datos cargan correctamente
- [ ] Se ve bien en mobile
- [ ] Agregaste tu nombre y contacto
- [ ] Subiste screenshots a tu portfolio
- [ ] Actualizaste tu LinkedIn/CV

---

**¿Problemas?** Abre un issue en GitHub o contactame por [tu-email].

**¡Éxitos con tu portfolio! 🚀**
