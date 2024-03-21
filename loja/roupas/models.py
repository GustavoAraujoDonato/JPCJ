from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='loja/imagem', blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='produto_marca')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class CarrinhoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    itens = models.ManyToManyField(CarrinhoItem)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
