# Classes:
# - São moldes para criar novos objetos (ou instâncias)
# - Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações
# - Atributos: dados dentro da classe
# - Métodos: Ações dentro da classe
# - Por convenção, usa-se o PascalCase para criar classes (ex: CriarBaseDeDados)
  
  class Pessoa
    ...

  p1 = pessoa()
  p1.nome = 'Luiz'
  p1.sobrenome = 'Otávio'

  p2 = pessoa()
  p2.nome = 'Maria'
  p2.sobrenome = 'Joaquina'

# - p1 e p2 são objetos da classe Pessoa
# - __init__ é a inicialização de um objeto
#   - Seu primeiro parâmetro sempre deve ser self, porém ele é usado automaticamente pelo python e não precisa ser referenciado na criação do Objeto

  class Pessoa:
    def __init__(self, nome, sobrenome):
      self.nome = nome
      self.sobrenome = sobrenome

  p1 = Pessoa('Luiz', 'Otávio')

  p2 = Pessoa('Maria', 'Joaquina')

# - Métodos em instâncias de classes em python (self):

  class Carro:
    def __init__(self, nome):
      self.nome = nome

    def acelerar(self):
      print(f'{self.nome} está acelerando...')

  fusca = Carro('Fusca')
  fusca.acelerar()    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

  celta = Carro('Celta')
  celta.acelerar()

  

  

      
    
