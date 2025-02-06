import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

class KNN:
    def __init__(self, k):
        self.k = k

    def carga(self, archivo):
        # Carga las imágenes y etiquetas desde el archivo proporcionado
        data = np.load(archivo)
        self.datos_entrenamiento = data['train_images']
        self.etiquetas_entrenamiento = data['train_labels']
        self.datos_prueba = data['test_images']
        self.etiquetas_prueba = data['test_labels']
        self.val_images = data['val_images']  # Agregar imágenes de validación
        self.val_labels = data['val_labels']  # Agregar etiquetas de validación

    def distancia_euclidiana(self, x1, x2):
        # Calcula la distancia euclidiana entre dos imágenes
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predicc(self, imagenes):
        predicciones = []

        for dato in imagenes:
            # Calcula la distancia entre la imagen de prueba y todas las imágenes de entrenamiento
            distancias = [self.distancia_euclidiana(dato.flatten(), x.flatten()) for x in self.datos_entrenamiento]
            # Obtiene los índices de las k imágenes más cercanas
            k_indices = np.argsort(distancias)[:self.k]
            # Obtiene las etiquetas de las k imágenes más cercanas
            k_etiquetas_mas_cercanas = [tuple(self.etiquetas_entrenamiento[i]) for i in k_indices]
            # Determina la etiqueta más común entre las k imágenes más cercanas
            etiqueta_mas_comun = Counter(k_etiquetas_mas_cercanas).most_common(1)[0][0]
            # Agrega la etiqueta más común a las predicciones
            predicciones.append(etiqueta_mas_comun)

        return predicciones

    def evaluar(self):
        # Evaluar el rendimiento del modelo en el conjunto de validación
        predicciones_val = self.predicc(self.val_images)
        self.precision_val = accuracy_score(self.val_labels, predicciones_val)
        print("Precisión en el conjunto de validación (k={}): {:.2f} %".format(self.k, self.precision_val * 100))


# Generar la curva de validación
valores_k = [1, 5, 10, 16, 20, 25]
precisiones = []

for k in valores_k:
    knn = KNN(k)
    knn.carga('retinamnist.npz')
    knn.evaluar()
    precisiones.append(knn.precision_val)

# Graficar los resultados
plt.plot(valores_k, precisiones, marker='o')
plt.title('Curva de Validación de KNN')
plt.xlabel('Valor de k')
plt.ylabel('Precisión en el conjunto de validación')
plt.grid(True)
plt.show()

