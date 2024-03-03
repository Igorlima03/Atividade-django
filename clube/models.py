from django.db import models

class Clube(models.Model):
     DIVISAO_CHOICES = (
          ('A' , 'Serie A'),
          ('B' , 'Serie B'),
          ('C' , 'Serie C'),
          ('D' , 'Serie D'),
     )
     SEXO_CHOICES = (
          ('M', 'Masculino'),
          ('F','Feminino')

     )
     nome = models.CharField(max_length=120)
     ano_fundacao = models.CharField('Ano de Fundação', max_length=120,blank=True, null=True)
     divisao =  models.CharField('Divisão',choices=DIVISAO_CHOICES, max_length=20)
     sexo = models.CharField(choices=SEXO_CHOICES, max_length=20, default=None)
     image = models.ImageField('Imagem', upload_to='imagem', blank=True, null=True)


     def __str__(self):
          return self.nome
     

class Jogadore(models.Model):
    POSICAO_CHOICES = (
             ('Gol', 'Goleiro'),
             ('Zag', 'Zagueiro'),
             ('Lat', 'Lateral'),
             ('Vol', 'Volante'),
             ('Mei', 'Meio-Campista') ,
             ('Pont', 'Ponta'),
             ('ATA', 'Atacante')         
       )

    SEXO_CHOICES = (
          ('M', 'Masculino'),
          ('F','Feminino')

     )
      
    nome = models.CharField(max_length=80)
    image = models.ImageField('Imagem', upload_to='imagem', blank=True, null=True)
    clube = models.CharField(max_length=50)
    posicao  = models.CharField('Posição  do jogador', choices=POSICAO_CHOICES, max_length=30)
    numero =  models.PositiveIntegerField(default=0)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=20, default=None)
    def __str__(self):
          return self.nome


class Competicoe(models.Model):


     nome = models.CharField(max_length=100)
     estadual = models.CharField(max_length=100, default=None)
     nacional = models.CharField(max_length=100, default=None)
     internacional = models.CharField(max_length=100, default=None)
     def __str__(self) :
          return self.nome

    
class Titulo(models.Model):
      nome = models.CharField('Clube',max_length=100)
      nome_titulo   = models.CharField('Titulo', max_length=50, null=True)
      ano_conquista =  models.PositiveIntegerField('Ano da consquista',default=0)
      data_exata = models.DateField('Data exata ',blank=True,null=True)
      

      def __str__(self):
           return self.nome