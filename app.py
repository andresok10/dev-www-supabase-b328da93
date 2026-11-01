import os

# Ver versión instalada de supabase
os.system("supabase --version")

# Iniciar proyecto supabase en carpeta actual
os.system("supabase init")

# Levantar supabase en local (docker necesario)
os.system("supabase start")

# Hacer deploy a supabase (requiere login)
#os.system("supabase db push")