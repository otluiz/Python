#!/usr/bin/env python
# coding: utf-8

# In[26]:


class No:
    def __init__(self, valor):
        self.valor = valor  # vai receber um valor quando criar o primeiro Nó da futura lista
        self.proximo = None # vai apontar para 'nenhum' só durante a criação do primeiro Nó
        
    def mostraNo(self):
        print(self.valor)


# In[38]:


class ListaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __lista_vazia(self): ## novo método
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor) ## criamos um novo nó para ser inserido na lista
        if self.__lista_vazia():
            self.ultimo = novo ## aqui insere de uma maneira especial, com uma lista vazia
        ## caso já tenha elementos na lista
        novo.proximo = self.primeiro
        self.primeiro = novo
        
    def insere_final(self, valor):
        novo = No(valor) ## criamos um novo nó para ser inserido na lista
        if self.__lista_vazia():
            self.primeiro = novo ## aqui insere de uma maneira especial, com uma lista vazia
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo
    #--------------------------------------------------------------------------------------------    
    def exclui_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return     ## sai do método
        
        temp = self.primeiro               ## o primeiro objeto da lista que é apontado pela cabeça
        if self.primeiro.proximo == None:  ## o primeiro apontado para None, está no ultimo elemento
            self.ultimo = None
        self.primeiro = self.primeiro.proximo ## o primeiro agora será o segundo da lista 
        return temp
            
    #--------------------------------------------------------------------------------------------    
    def mostrar(self): ## este método eu copiei e colei da lista simples, porque é do mesmo jeito
        if self.__lista_vazia():
            print('A lista está vazia')
            return     ## sai do método
        
        atual = self.primeiro
        while atual != None: ## vamos percorrer a lista toda, um nó de cada vez
            atual.mostraNo() ## vem da classe Nó o nó que está é o objeto que apontado pela cabeça da lista 
            atual = atual.proximo ## atualizamos a variável atual para apontar para o endereço de memória do 1º


# Cria a lista, insere no início e mostra os endereços

# In[4]:


lista = ListaExtremidadeDupla()


# In[5]:


lista.insere_inicio(1)


# In[6]:


lista.primeiro, lista.ultimo


# In[8]:


lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)


# In[7]:


lista.mostrar()


# In[9]:


lista.primeiro, lista.ultimo


# Insere no final

# In[10]:


lista = ListaExtremidadeDupla()


# In[11]:


lista.insere_final(1)


# In[12]:


lista.primeiro, lista.ultimo ## os dois apontadores terão que ter os mesmos endereços


# In[13]:


lista.insere_final(2)
lista.insere_final(3)


# In[14]:


lista.mostrar()


# In[15]:


lista.insere_inicio(0)
lista.insere_final(4)
lista.mostrar()


# In[16]:


lista.insere_final(5)


# In[17]:


lista.mostrar()


# Exlcuir do início

# In[39]:


lista = ListaExtremidadeDupla()


# In[40]:


lista.insere_inicio(1)
lista.insere_final(3)
lista.mostrar()


# In[41]:
## Diretivas para testar a exclusão de elementos da lista

lista.exclui_inicio() # vai excluir o primeiro elemento da lista : 1
lista.mostrar()


# In[42]:


lista.exclui_inicio()
lista.exclui_inicio() ## A lista não possui mais nenhum elemento


# In[43]:


lista.mostrar()


# In[ ]:




