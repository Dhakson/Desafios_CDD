class Pessoas():
    def __init__(self,nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
      
    def falar(self,falar):
        print(f'{self.nome} está falando {falar}')
    
    def paraFalar(self):
        print(f'{self.nome} parou de falar') 
    
    def comer(self,alimento):
        print(f'{self.nome} está comendo {alimento} ')
    
    def pararComer(self):
        print("Parou de comer") 
    
    def dormir(self):
        print("Estou dormindo...")  
