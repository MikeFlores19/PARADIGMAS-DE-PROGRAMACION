import urllib.request
import os
import numpy as np
from tensorflow.keras.utils import to_categorical

 #Descargar el archivo desde la URL
url = "https://zenodo.org/record/6496656/files/retinamnist.npz?download=1"
filename, _ = urllib.request.urlretrieve(url, filename="retinamnist_tmp.npz")

# Renombrar el archivo#
os.rename("retinamnist_tmp.npz", "retinamnist.npz")

# Cargar el archivo usando NumPy
data = np.load('retinamnist.npz')

x_train = data['train_images']
print(x_train.shape)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1]*x_train.shape[2]*x_train.shape[3])
x_test = data['test_images']
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1]*x_test.shape[2]*x_test.shape[3])
x_val = data['val_images']
x_val = x_val.reshape(x_val.shape[0], x_val.shape[1]*x_val.shape[2]*x_val.shape[3])

y_train = to_categorical(data['train_labels'])
y_test = to_categorical(data['test_labels'])
y_val = to_categorical(data['val_labels'])

print(x_train.shape)
print(y_train.shape)
