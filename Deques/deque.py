import numpy as np

class  Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.num_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade -1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    ## Método para inserir no início do Deque
    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return
        ## Se o deque estiver vazio
        if self.inicio == -1:
            self.inicio = 0 # mete um zero na posição
            self.final = 0
        ## Se o início estiver na primeira posição
        elif self.inicio == 0:
            self.incio == self.capacidade - 1 ## para descobrir se está do lado direito ou esquerdo
        else:
            self.inicio -= -1

        self.valores[self.inicio] = valor

    ## Método para inserir no final do Deque
        if self.inicio == -1:
            self.incio = 0
            self.final = 0
        # Se o final do deque estiver na última posição
        elif self.final == self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1
            
        self.valores[self.final] = valor


    ## Método para retirar um elemento do Deque (no início)
    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque está vazio')
            return

        ## Se possui somente um elemento no Deque
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1

        else:
            # Volta para a posição inicial
            if self.inicio == self.capacidade - 1:
                self.inicio = 0
            else:
                # Incrementar inicio para remover o inicio atual
                self.inicio += 1


    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque está vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
            
        elif self.inicio == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio() or self.final < 0:
            print('O deque está vazio')
            return

        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('O deque está vazio')
            return

        return self.valores[self.final]