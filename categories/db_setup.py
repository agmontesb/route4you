import django
django.setup()

from django.contrib.auth.models import User
from categories.models import Category, Site, Comment

usuarios = [
    dict(username='user1', password='user1621124'),
    dict(username='user2', password='user2621124'),
    dict(username='user3', password='user3621124'),
]

categorias = ['Museos', 'Parques', 'Parroquias', 'Sitios']
catlogos   = ['./museo.jpg', './parque.png', './iglesia.jpg', './sitio.png']

sitios = [
        # Museos
         (0,"Museo de Arte Moderno De Barranquilla","11.00188","-74.8033213" ),
         (0,"Museo Romántico","10.994924","-74.7964657" ),
         (0,"Museo patrimonial Cl","10.986272","-74.7807537" ),
         (0,"MUSEO DEL ATLANTICO Cra ","10.9966056","-74.7976207" ),
        # Parques
         (1,"Parque del Sagrado Corazón","10.9932311","-74.8194191" ),
         (1,"Parque del Golf Cl","11.0104601","-74.8100578" ),
         (1,"Parque Venezuela Carrera","11.0013831","-74.8263979" ),
         (1,"Parque Eugenio Macías Cra ","10.9979024","-74.8166551" ),
         (1,"Parque Cisneros Calle","11.001033","-74.7946866" ),
         (1,"Parque Electrificadora","11.0140744","-74.8160016" ),
         (1,"Parque del Sol Cra","10.9880175","-74.8133862" ),
         (1,"Parque Bellavista Cl.","11.0027437","-74.7980595" ),
         (1,"Parque Los Andes Cl","10.9745766","-74.8060217" ),
         (1,"Parque Las Mercedes Carrera","10.983689","-74.8202332" ),
         (1,"PARQUE CULTURAL DEL CARIBEL","10.9864109","-74.7805854" ),
         (1,"Parque de las Americas Calle","10.9939921","-74.8018501" ),
        # Parroquias
         (2,"PARROQUIA LA TRANSFIGURACION DEL SEÑOR","11.0065718","-74.8341535" ),
         (2,"Parroquia San Charbel","11.0205836","-74.8178456" ),
         (2,"DESPACHO PARROQUIA SAN FRANCISCO DE ASÍS","10.9850532","-74.8125842" ),
         (2,"Arquidiocesis De Barranquilla","10.9936182","-74.8133708" ),
         (2,"Parroquia Nuestra Señora de La Caridad del Cobre","10.9956881","-74.8242433" ),
         (2,"Parroquia San Felipe Cl","10.9733644","-74.8129805" ),
         (2,"Parroquia San Jeronimo","10.9978615","-74.8081311" ),
         (2,"Parroquia Nuestra Señora del Carmen","10.9913696","-74.7952762" ),
         (2,"Parroquia La Sagrada Familia","10.9827603","-74.7962971" ),
         (2,"PARROQUIA SANTA BERNARDITA ","10.9868538","-74.821693" ),
         (2,"Parroquia Nuestra Señora del Perpetuo Socorro Carrera","10.9913293","-74.8025443" ),
         (2,"Parroquia Santa Eduviges","10.9776212","-74.8443154" ),
         (2,"PARROQUIA SANTISIMA TRINIDAD","11.0117204","-74.8025443" ),
         (2,"Parroquia Nuestra Señora de La Merced","10.9775901","-74.8026134" ),
         (2,"Parroquia Maria Auxiliadora","10.9442044","-74.7967056" ),
         (2,"Iglesia santa marta","10.9440072","-74.7799695" ),
         (2,"Parroquia Nuestra Señora de las Nieves","10.952753","-74.7811219" ),
         (2,"PARROQUIA DE GUADALUPE ","10.9994781","-74.7906598" ),
         (2,"Parroquia San Isidro Labrador","10.9692137","-74.7992667" ),
        # Sitios
         (3,"Malecón Turístico León Caridi Calle Avenida del rio","10.9970684","-74.7727025" ),
         (3,"Malecón puerta de oro Barranquilla","11.0252804","-74.8011937" ),
         (3,"Donde mama Cra ","10.9998183","-74.7971679" ),
         (3,"Cucayo Cra","11.0000067","-74.8128088" ),
         (3,"Cocina 33 Cra","11.0030375","-74.8096124" ),
         (3,"Parroquia San Isidro Labrador","10.9984438","-74.8221463" ),
         (3,"EL TOTUMAZO Calle 18  Soledad","10.9177959","-74.7671999" ),
         (3,"Narcobollo Cra","10.999088","-74.8241547" ),
         (3,"El Humito","10.9946","-74.8030299" ),
         (3,"Salvators pizza","10.9945999","-74.809596" ),
        ]

comments = [   # site, owner, rating, comment
    (5, 'user1', '3', 'comment' ),
    (10, 'user1', '3', 'comment' ),
    (15, 'user1', '3', 'comment' ),
    (5, 'user2', '3', 'comment' ),
    (15, 'user2', '3', 'comment' ),
    (5, 'user3', '3', 'comment' ),
    (10, 'user3', '3', 'comment' ),
]

def dbSetup():

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

    catList = Category.objects.all()
    for catid, sname, lat, long in sitios:
        newcat = catList[catid]
        newSite = Site(category=newcat, name=sname, address='Calle x Carrera y', latitud=lat, longitud=long)
        newSite.site_logo.name = catlogos[catid]
        newSite.save()

    for siteid, username, rating, comment in comments:
        user = usermap[username]
        site = Site.objects.get(pk=siteid)
        newcomm = Comment(site=site, user=user, rating=rating, comment=comment)
        newcomm.save()


if __name__ == '__main__':
    try:
        dbSetup()
    except:
        pass
