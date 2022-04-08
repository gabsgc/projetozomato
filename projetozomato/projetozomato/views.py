from django.shortcuts import render
from projetozomato.comentario import Comentario

from projetozomato.restaurante import Restaurante

comentario1 = Comentario(1, "Jean Marcos", "Sensacional!")
comentario2 = Comentario(2, "Gabriela James", "Maravilha esse restaurante!")
comentario3 = Comentario(3, "Isabela Marques", "A comida é bastante refinada, mas devo acrescentar que deveriam melhorar o cardápio de sobremesas")
comentario4 = Comentario(4, "Jacquin", "A sobremesa é ótima!")
comentario5 = Comentario(5, "Pedro Augusto", "Muito bom o ambiente e o cardápio do prato principal é excepcional.")
comentario6 = Comentario(6, "Sofia Mendes", "Promissor...")

comentarios_restaurante1 = [comentario1, comentario4]
comentarios_restaurante2 = [comentario2, comentario6]
comentarios_restaurante3 = [comentario3, comentario5]

restaurante1 = Restaurante(1, 'Rock Truck', 'https://media-cdn.tripadvisor.com/media/photo-s/0b/12/73/fd/rock-e-ribs-steakhouse.jpg', 'Rua A Nº 263, Centro, Vassouras - RJ', "Segunda a sexta - 18:00 às 00:00", comentarios_restaurante1)
restaurante2 = Restaurante(2, 'Grano de Ouro', 'https://blog.goomer.com.br/wp-content/uploads/2016/10/6-dicas-para-deixar-o-seu-restaurante-moderno.jpeg', 'Rua Margarida Nº 15, Vila Santana, Itaguaí - RJ', "Segunda a sábado - 11:00 às 23:00", comentarios_restaurante2)
restaurante3 = Restaurante(3, 'Sabor Refinado', 'https://revistamenu.com.br/wp-content/uploads/2020/09/restaurantegero.jpg', 'Avenida Principal Nº 302, Centro, Resende - RJ', "Quinta a domingo - 17:00 às 00:00", comentarios_restaurante3)

restaurantes = [restaurante1, restaurante2, restaurante3]

def index(request):
    return render(request=request, template_name='index.html', context={'restaurantes': restaurantes})

def detalhes_restaurante(request, id:int):
    for restaurante in restaurantes:
        if restaurante.get_id() == id:
            return render(request=request, template_name='restaurante.html', context={'restaurante': restaurante})
    return render(request=request, template_name='restaurante.html', context={'restaurante': restaurante})