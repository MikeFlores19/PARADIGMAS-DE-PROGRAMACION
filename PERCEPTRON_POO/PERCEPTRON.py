import numpy as np
import matplotlib.pyplot as plt

class perceptron():
    def __init__(self,
                 peso=[0.5,0.5],
                 x=np.array([[0.0, 0.0],
                            [0.0, 1.0],
                            [1.0, 0.0],
                            [1.0, 1.0]]),
                 y=np.array([-1,1,1,1]),
                tasa_aprendizaje=0.01
                 ):
        self.peso=peso
        self.x=x
        self.y=y  
        self.tasa_aprendizaje=tasa_aprendizaje

    def set_weight(self):
        self.peso = np.random.rand(2,)

    def get_rate(self,tasa):
        self.tasa_aprendizaje=tasa

    def compute_output(self, w, x):
        return np.sum(w*x, axis=1)
    
    def activation_function(self, w, x):
        return [1 if x>0 else -1 for x in self.compute_output(w,x)]
    
    def learning(self,iteraciones):
        for i in range(iteraciones):
            print('-----------------------------')
            print("running one iteration ...")
            print('predicted:',self.activation_function(self.x,self.peso))
            print('real:',self.y)
            delta_w = np.sum(self.tasa_aprendizaje*(self.y-self.compute_output(self.peso,self.x))*self.x.T, axis=1)
            print("current weigths", self.peso)
            self.peso = self.peso + delta_w
            print("new weights", self.peso)
            print('-----------------------------')

    def graphics(self):
        ax = plt.figure().add_subplot(projection='3d')
        points=self.compute_output(self.x,self.peso)
        plane=np.array([np.linspace(0,1,100),np.linspace(0,1,100)]).T
        z_p=self.compute_output(self.peso, plane)
        ax.scatter(plane[:,0], plane[:,1], zs=z_p)
        ax.scatter(self.x[:,0], self.x[:,1], zs=points)
        ax.set_xlabel('X_0')
        ax.set_ylabel('X_1')
        ax.set_zlabel('W')
        ax.view_init(elev=20., azim=50)
        plt.show()

#Creacion de perceptron
neurona=perceptron()
#Se establece los pesos aleatorios
#neurona.set_weight()
#Se establece  la tasa de aprendizaje
neurona.get_rate(0.1)
#Se realiza el proceso de aprendizaje con 10 iteraciones
neurona.learning(10)
#Grafica el plano obtenido
neurona.graphics()