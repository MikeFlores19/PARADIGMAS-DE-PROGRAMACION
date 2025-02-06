import numpy as np

# Carga el archivo .npz
archivo_npz = np.load('retinamnist.npz')

# Accede a los nombres de las matrices dentro del archivo
nombres_matrices = archivo_npz.files

# Imprime los nombres de las matrices
print("Nombres de las matrices en el archivo:")
for nombre_matriz in nombres_matrices:
    print(nombre_matriz)
    

# Cierra el archivo después de usarlo
archivo_npz.close()
