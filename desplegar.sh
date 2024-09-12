#!/bin/bash

# Ruta del sitio web
WEB_DIR="/home/sebastian/Documentos/Sitio_web"
GIT_REPO="git@github.com:SebastianZarate/Sitio_web.git"


# Cambiar al directorio del sitio web
cd /var/www/html || { echo "Error: No se puede cambiar al directorio /var/www/html"; exit 1; }

# Verificar si es un repositorio Git
if [ ! -d ".git" ]; then
  echo "Error: No es un repositorio Git en el directorio actual."
  exit 1
fi

# Hacer pull de la última versión desde GitHub
git pull origin main

# Copiar archivos al servidor de archivos estáticos
sudo cp -r /home/sebastian/Documentos/Sitio_web/* /var/www/html/

# Reiniciar el servidor web (modificar según el servidor que uses)
sudo systemctl restart nginx   

echo "Despliegue completado con éxito."

