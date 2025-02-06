import numpy as np

# Carga el archivo .npz
archivo_npz = np.load('retinamnist.npz')

# Nombre de la matriz que deseas imprimir
nombre_matriz_deseada = 'test_labels'

# Verifica si la matriz deseada está en el archivo
if nombre_matriz_deseada in archivo_npz:
    # Accede a los datos de la matriz específica
    matriz_deseada = archivo_npz[nombre_matriz_deseada]
    print(f'Nombre de la matriz: {nombre_matriz_deseada}')
    print(f'Datos de la matriz:\n{matriz_deseada}')
else:
    print(f'La matriz "{nombre_matriz_deseada}" no se encontró en el archivo.')

# Cierra el archivo después de usarlo
archivo_npz.close()







