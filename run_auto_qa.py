"""
Ejecución de programación para gestion de calidad en código fuente
1 - Fiximports: separado y ordenado de importado de librerias, funciones, etc
2 - PyCodeStyle: verificación de especificaciones PEP8
3 - ImportChecker: verificacion de uso de elementos importados
"""
import os
import subprocess
import sys

def skip_dirs(directory):
    for skip_dir in [
            '.git', 'venv', '.idea', 'db', '__pycache__',
            'media', 'documentos', 'html_templates']:
        if skip_dir in directory:
            return True
    return directory == os.getcwd()

def main():
    print("\n")
    print("Fixing imports (fiximports)")
    for root, dirs, files in os.walk(os.getcwd()):
        if skip_dirs(root):
            continue
        for f in files:
            if len(f.split('.')) > 1 and 'py' == f.split('.')[1]:
                arch = "{}".format(os.path.join(root, f))
                if "migrations" not in arch:
                    subprocess.call(
                        ['fiximports', arch], stdout=sys.stdout)
    print("\n")
    print("Codestyle Checking (pycodestyle)")
    for root, dirs, files in os.walk(os.getcwd()):
        if skip_dirs(root):
            continue
        for f in files:
            arch = f"{os.path.join(root, f)}"
            if len(f.split('.')) > 1 and 'py' == f.split('.')[1]:
                if "migrations" not in arch:
                    subprocess.call(
                        ['pycodestyle', arch], stdout=sys.stdout)
    print("\n")
    print("Imports Checking (importchecker)")
    for root, dirs, files in os.walk(os.getcwd()):
        if skip_dirs(root):
            continue
        subprocess.call(['importchecker', root], stdout=sys.stdout)



if __name__ == "__main__":
    main()
