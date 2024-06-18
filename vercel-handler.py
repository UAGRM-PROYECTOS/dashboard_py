# vercel-handler.py

import os
from subprocess import Popen

# Configurar la ruta del directorio de tu proyecto Django
os.chdir(os.path.join(os.path.dirname(__file__), 'dashboard'))

# Comando para ejecutar Gunicorn o tu servidor WSGI
command = 'gunicorn'
args = [
    '--bind', '0.0.0.0:' + os.environ.get('PORT', '8000'),
    'dashboard.wsgi:application'
]

# Ejecutar el servidor
Popen([command] + args).wait()
