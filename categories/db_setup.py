import os
import random
from json import dumps as json
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'route4you.settings'
django.setup()

from django.contrib.auth.models import User
from categories.models import Category, Site, Comment

usuarios = [
    dict(username='user1', password='user1621124'),
    dict(username='user2', password='user2621124'),
    dict(username='user3', password='user3621124'),
]

categorias = ['Museos', 'Parques', 'Parroquias', 'Restaurantes']
catlogos   = ['./museo.jpg', './parque.png', './iglesia.jpg', './sitio.png']

sitios = [
        # Museos
        (0, "Museo de Arte Moderno De Barranquilla", "Carrera 56 #74-22", "11.002164", "-74.800736", "4"),
        (0, "Museo Romántico", "Carrera 54 #59-199 ", "10.995187", "-74.793762", "5"),
        (0, "Museo patrimonial", "Calle 36 #46 - 66", "10.989129", "-74.766469", "4"),
        (0, "Museo del Atlantico", "Carrera 39 # 35 - 89", "10.978699", "-74.779535", "3"),
        # Parques
        (1, "Parque del Sagrado Corazón", "Carrera 42f # 80", "10.993386", "-74.818460", "5"),
        (1, "Parque Suri Salcedo", "Carrera 47 #70-2 ", "10.994031", "-74.803300", "5"),
        (1, "Parque del Golf", "Calle 81 # 59C", "11.010713", "-74.807333", "5"),
        (1, "Parque Venezuela", "Carrera 43B# 88 ", "11.001604", "-74.823619", "4"),
        (1, "Parque Eugenio Macías", "Carrera 44# 80 ", "10.997829", "-74.814531", "3"),
        (1, "Parque Cisneros", "Calle 68# 65 ", "11.000931", "-74.791389", "3"),
        (1, "Parque Electrificadora", "Calle 86# 64", "11.013969", "-74.813995", "5"),
        (1, "Parque del Sol", "Carrera. 39 #73-105", "10.988249", "-74.810951", "3"),
        (1, "Parque Bellavista", "Calle 72 #61", "11.002638", "-74.795892", "2"),
        (1, "Parque Los Andes", "Calle 63 #26-58", "10.975023", "-74.803806", "4"),
        (1, "Parque Las Mercedes", "Carrera 35C #79b -32 ", "10.983721", "-74.818045", "3"),
        (1, "Parque cultural del caribe", "Via 40 #46-66 ", "10.986275", "-74.778115", "5"),
        (1, "Parque de las Americas", "Calle 65# 50", "10.993978", "-74.798105", "3"),
        (1, "Parque Washington", "Calle 80 # 53", "11.005577", "-74.811146", "4"),
        # Parroquias
        (2, "Parroquia la transfiguracion del Señor", "Calle. 98a #45-32", "11.006614", "-74.832018", "5"),
        (2, "Parroquia San Charbel", "Carrera 71 #91A-26", "11.020615", "-74.815689", "4"),
        (2, "Despacho Parroquia San Francisco de Asis", "Carrera 38a #70B-135", "10.985085", "-74.810438", "5"),
        (2, "Arquidiocesis De Barranquilla", "Calle 75b #42f-1", "10.993660", "-74.811225", "5"),
        (2, "Parroquia Nuestra Señora de La Caridad del Cobre", "Calle 84 #41d42", "10.995678", "-74.821958", "4"),
        (2, "Parroquia San Felipe", "Calle 70c #24B-25", "10.973428", "-74.810824", "3"),
        (2, "Parroquia San Jeronimo", "Calle 74 #49-39", "10.997935", "-74.805964", "3"),
        (2, "Parroquia Nuestra Señora del Carmen", "Carrera 50 #55-176", "10.991631", "-74.792911", "4"),
        (2, "Parroquia La Sagrada Familia", "El Progreso #54-63", "10.982803", "-74.794030", "4"),
        (2, "Parroquia Santa Bernardita", "Carrera 38 #79A-162", "10.986917", "-74.819515", "3"),
        (2, "Parroquia Nuestra Señora del Perpetuo Socorro", "Carrera 46 #66 – 35", "10.991386", "-74.800372", "4"),
        (2, "Parroquia Santa Eduviges", "Carrera 31 #117b-31", "10.977674", "-74.842105", "3"),
        (2, "Parrooquia Santisima Trinidad", "Cale 77 #68-59", "11.011794", "-74.798667", "4"),
        (2, "Parroquia Nuestra Señora de La Merced", "Carrera 30# 58", "10.989451", "-74.807620", "4"),
        (2, "Parroquia Maria Auxiliadora", "Calle 38b # 7b-39", "10.944225", "-74.794538", "3"),
        (2, "Parroquia Nuestra Señora de las Nieves", "Carrera 15 #24-93", "10.952795", "-74.778912", "3"),
        (2, "Parroquia de Guadalupe", "Calle 58 #66-32", "10.999520", "-74.788471", "4"),
        (2, "Parroquia San Isidro Labrador", "Calle 53 #23-56", "10.969235", "-74.797089", "4"),
        ]

Fakerestaurantes = [
        (3, "Cucayo", "Calle 85 #52-105", "11.0000067", "-74.8128088", "4",json({'subcat':'Casera', 'desc':'Precios $12.000 - $60.000'})),
        (3, "Donde mama", "Carrera 60 #68-38", "10.999831", "-74.794986", "3",json({'subcat':'Casera', 'desc':'Precios $ 8.000 -$ 25.000'})),
        (3, "Varadero ", "Carrera 51B # 79-97", "11.002959", "-74.809911", "5",json({'subcat':'Mariscos ', 'desc':'Precios $ 17.000 - $ 60.000'})),
        (3, "Cocina 33", "Carrera 52 # 76 -188", "11.003628", "-74.807683", "3",json({'subcat':'Casera', 'desc':'Precios $ 8.000 - $ 30.000'})),
        (3, "Sancochos y asados ", "Carrera 43 # 82 – 210", "10.998623", "-74.819292", "4",json({'subcat':'Casera', 'desc':'Precios $ 10.000 - $ 50.000'})),
        (3, "El totumazo", "Calle 44 # 25-84", "10.995098", "-74.810205", "3",json({'subcat':'Casera', 'desc':'Precios $ 6.000 - $ 45.000'})),
        (3, "Narcobollo", "Carrera 43 #84 -188", "10.999288", "-74.821247", "5",json({'subcat':'Casera', 'desc':'Precios $ 2.000 - $ 35.000'})),
        (3, "El Humito", "Carrera 49 # 68 -99", "10.994853", "-74.800476", "4",json({'subcat':'Casera', 'desc':'Precios $ 15.000 - $ 45.000'})),
        (3, "Salvators pizza", "Carrera 84# 47-60", "10.999893", "-74.818437", "4",json({'subcat':'Pizza', 'desc':'Precios $ 12.000 - $ 60.000'})),
        (3, "Anonimo cocica", "Carrera 52 # 76-71", "11.002890", "-74.806370", "5",json({'subcat':'pastas', 'desc':'Precios $ 20.000 - $ 60.000'})),
        (3, "Pollos arana", "Carrera 43 # 82-39", "10.998143", "-74.817853", "4",json({'subcat':'Parrilla', 'desc':'Precios $ 15.000 - $ 45.000'})),
    ]
lorem_ipso ='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et eleifend odio. Ut efficitur malesuada elit in sollicitudin. Etiam faucibus ornare condimentum. Pellentesque auctor ex est. Vivamus facilisis at magna vitae gravida. Vestibulum ante lectus, vestibulum eget ante vel, volutpat auctor quam. Vestibulum non aliquet nulla, sed tempor ante. Integer eleifend pulvinar nibh, vel euismod augue mollis non. Aliquam erat volutpat. Mauris sit amet eros vitae turpis posuere venenatis. Praesent mattis quam quis cursus tincidunt. Quisque porta vulputate porta. Quisque tincidunt rhoncus metus sit amet volutpat. Phasellus in nulla finibus, lacinia neque eleifend, commodo leo. Nulla risus felis, pretium at varius et, lacinia sit amet urna. In hac habitasse platea dictumst.
Sed non fringilla dui, eu convallis nibh. Etiam ut odio ex. Nam lobortis quam vitae mollis pretium. Morbi malesuada risus a magna dictum fermentum in id lorem. Aliquam eget ullamcorper sem. In in felis eget neque pulvinar rutrum. Aenean vulputate fringilla eleifend. Nunc molestie massa lacus, id convallis neque auctor nec. Vivamus accumsan sem ut eros semper, eu sagittis sem fermentum. Pellentesque luctus turpis non arcu molestie eleifend. Praesent eu lobortis risus, in dictum felis. Nunc dignissim suscipit diam, non sagittis nulla porta eu.
Vestibulum sodales sed velit in scelerisque. Sed metus est, porta eget vestibulum ac, mattis fringilla velit. Proin non hendrerit odio, eget accumsan mauris. Nam ut dui ipsum. Suspendisse facilisis odio non neque blandit interdum. Proin suscipit velit nisi, vel placerat tortor vulputate sed. Etiam malesuada nisl quis dui sollicitudin, eu viverra odio volutpat. Nam pharetra, orci auctor aliquam cursus, lectus dui egestas nisl, eu volutpat velit sapien efficitur nisi. Integer turpis est, fermentum in urna nec, feugiat finibus diam. Cras quis lacus id nisl gravida dignissim. Proin vestibulum tortor eget dui eleifend, vel scelerisque libero aliquet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Morbi risus odio, facilisis in scelerisque nec, ullamcorper feugiat sem. Nullam sodales consectetur lacus ac dapibus.
Sed ultrices dolor sed leo volutpat pretium. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Integer ac tempor eros. Curabitur quis elit risus. Cras posuere erat et velit dignissim ullamcorper. Nam sollicitudin commodo maximus. Nullam non hendrerit nisi. Quisque nisi nulla, auctor vitae nunc eu, dignissim egestas leo. Pellentesque sit amet turpis tempus, ullamcorper lacus ullamcorper, pretium ante.
Morbi commodo mauris vel vulputate posuere. Aenean porta justo lobortis metus faucibus gravida. Praesent sit amet porta justo. Proin dignissim enim quis justo sollicitudin faucibus et eget erat. Praesent dictum lacus sit amet nisi sodales, in viverra elit aliquam. Phasellus ac ullamcorper tortor. Proin eu volutpat augue. Ut scelerisque, urna a efficitur eleifend, massa ligula interdum magna, at luctus lectus ex vel dui. In posuere vitae lacus dignissim congue. Aliquam dapibus porta ligula, ac sollicitudin nunc pretium ut. Aenean ornare sed nulla non pellentesque. Nunc posuere metus a odio suscipit rhoncus. Pellentesque eleifend, justo sed sagittis volutpat, arcu sem porttitor augue, non lacinia turpis tellus quis velit. Morbi a erat ut arcu sodales dictum quis ut ipsum.
'''
minChar = 50
maxChar = 120
comments = []
for ncom in range(20):
    nSite = random.randint(0, len(sitios)-1)
    nUser = random.randint(0, len(usuarios)-1)
    username = usuarios[nUser]['username']
    rating = str(random.randint(0, 5))
    pini = random.randint(0, len(lorem_ipso) - maxChar)
    pfin = pini + random.randint(minChar, maxChar)
    comment = lorem_ipso[pini:pfin]
    comments.append((nSite, username, rating, comment))

# comments = [   # site, owner, rating, comment
#     (5, 'user1', '3', 'comment' ),
#     (10, 'user1', '3', 'comment' ),
#     (15, 'user1', '3', 'comment' ),
#     (5, 'user2', '3', 'comment' ),
#     (15, 'user2', '3', 'comment' ),
#     (5, 'user3', '3', 'comment' ),
#     (10, 'user3', '3', 'comment' ),
# ]

def dbSetup():

    # Se crea el admin con caracteristica de superuser
    User.objects.create_superuser(username="admin", email="admin@gmail.com", password="admin621124")

    # Se crean los usuarios de la simulacion
    usermap = {}
    for item in usuarios:
        email = '%s@gmail.com' % item['username']
        user = User(username=item['username'], email=email)
        user.set_password(item['password'])
        user.save()
        usermap[user.username] = user

    for categoryName in categorias:
        newcat = Category(name=categoryName)
        newcat.save()

    sitefields = ['category', 'name', 'address', 'latitud', 'longitud', 'rank', 'extras']
    catList = Category.objects.all()
    for catid, sname, address, lat, long, rank in sitios:
        newcat = catList[catid]
        values = [newcat, sname, address, lat, long, str(2*int(rank))]
        kwargs = dict(zip(sitefields, values))
        newSite = Site(**kwargs)
        newSite.site_logo.name = catlogos[catid]
        newSite.save()

    for catid, sname, address, lat, long, rank, extras in Fakerestaurantes:
        newcat = catList[catid]
        values = [newcat, sname, address, lat, long, str(2*int(rank)), extras]
        kwargs = dict(zip(sitefields, values))
        newSite = Site(**kwargs)
        newSite.site_logo.name = catlogos[catid]
        newSite.save()



    for siteid, username, rating, comment in comments:
        user = usermap[username]
        site = Site.objects.get(pk=siteid)
        newcomm = Comment(site=site, owner=user, rating=rating, comment=comment)
        newcomm.save()


if __name__ == '__main__':
    try:
        dbSetup()
    except:
        pass
