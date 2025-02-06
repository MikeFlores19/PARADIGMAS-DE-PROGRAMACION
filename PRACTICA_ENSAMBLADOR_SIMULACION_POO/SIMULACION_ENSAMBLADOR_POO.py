class MemoryProcessor:
    def __init__(self, filename):  
        self.memory = [[0] * 8 for _ in range(8)]  # Inicialización de la memoria
        self.load_program(filename)  # Carga del programa desde un archivo

    def load_program(self, filename):
        with open(filename, "r") as f:
            for i, line in enumerate(f):
                for j in range(8):
                    self.memory[i][j] = int(line[j])  # Se carga cada instrucción en la memoria

    def load(self):
        direction = 0
        load_val = 0
        for i in range(3, 8):
            direction = direction * 2 + self.memory[0][i]
        for i in range(3, 8):
            load_val = load_val * 2 + self.memory[direction][i]
        return load_val

    def add(self, load_val):
        direction_2 = 0
        sum_val = 0
        val = 0
        for i in range(3, 8):
            direction_2 = direction_2 * 2 + self.memory[1][i]
        for i in range(3, 8):
            val = val * 2 + self.memory[direction_2][i]
        sum_val = load_val + val
        return sum_val

    def store(self, sum_val):
        direction_3 = 0
        print("\nEl acumulador es:", sum_val)
        for i in range(3, 8):
            direction_3 = direction_3 * 2 + self.memory[2][i]
        for i in range(7, 2, -1):
            self.memory[direction_3][i] = sum_val % 2
            sum_val //= 2

    def jump(self):
        direction_4 = 0
        for i in range(3, 8):
            direction_4 = direction_4 * 2 + self.memory[3][i]
        return direction_4

    def execute(self):
        val_ini = self.load()
        print("\nEl acumulador es:", val_ini)
        print("\nMEMORIA\n")
        for i in range(8):
            if i == 6:
                print("asignacion de memoria-> ", end="")
            for j in range(8):
                print(self.memory[i][j], end="")
            print()

        iteration = 1
        while iteration < 31:
            charge = 0
            sum_val = 0
            val = 0
            for i in range(8):
                opc = 0
                for j in range(3):
                    opc = opc * 2 + self.memory[i][j]
                if opc == 4:
                    charge = self.load()
                elif opc == 5:
                    sum_val = self.add(charge)
                elif opc == 6:
                    self.store(sum_val)
                elif opc == 2:
                    val = self.jump()
            iteration += val

            # IMPRESION DE LA MEMORIA POR ITERACION
            print("\nMEMORIA\n")
            for i in range(8):
                if i == 6:
                    print("asignacion de memoria-> ", end="")
                for j in range(8):
                    print(self.memory[i][j], end="")
                print()


def main():
    processor = MemoryProcessor("binario.txt")
    processor.execute()


if __name__ == "__main__":
    main()
