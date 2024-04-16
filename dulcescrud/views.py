from datetime import date
from django.shortcuts import render

class Usuario:
    credencial=""
    password=""
    
    def __init__(self,credencial,password):
        self.credencial = credencial
        self.password = password
       

    def getCredencial(self):
        return self.credencial

    def getPassword(self):
        return self.password

    def toString(self):
        return self.credencial + ", "+self.password 

u1 = Usuario("Oscar", "Oscar123")
u2 = Usuario("Cristian","Cristian123")
u4 = Usuario("Ximena","Ximena123") 
u5 = Usuario("Ana", "Ana123")
u6 = Usuario("Pedro","Pedro123")
u7 = Usuario("Felipe","Felipe123") 
u8 = Usuario("Jorge","Jorge123") 
u9 = Usuario("Manuel", "Manuel123")
u10 = Usuario("Alberto","Alberto123")

usuarios = [u1, u2, u4, u5, u6, u7, u8, u9, u10]


class Producto:
    codigoD=""
    nombreD=""
    cantidad=""
    precioD=0
    ingredienteP=""
    correo=""
    descripcion=""
    fecha=date
    
    def __init__(self,codigoD,nombreD,cantidad,precioD,ingredienteP,correo,descripcion,fecha):
        self.codigoD = codigoD
        self.nombreD = nombreD
        self.cantidad = cantidad
        self.precioD = precioD
        self.ingredienteP = ingredienteP
        self.correo = correo
        self.descripcion = descripcion
        self.fecha = fecha
       

    def getCodigoDulce(self):
        return self.codigoD

    def getNombreDulce(self):
        return self.nombreD

    def toString(self):
        return self.codigoD + ", "+self.nombreD + ", "+self.cantidad + ", "+str(self.precioD) + ", "+self.ingredienteP + ", "+self.correo + ", "+self.descripcion + ", "+str(self.fecha)

p1 = Producto("1","Torta Bizcocho Durazno","15 personas",20000,"Durazno","oscar@dulces.cl","Deliciosa Torta de Bizcocho Durazno. Con bizcocho de vainilla, trozos de dulces duraznos, manjar artesanal y crema chantilly","2022-09-28")
p2 = Producto("2","Chocolate Sahne Nuss","150g",5990,"Nuez","contacto@cugat.cl","La perfecta combinación de crujientes almendras enteras cuidadosamente seleccionadas, tostadas a nuestra única y particular manera, con un delicioso chocolate firme y cremoso. ","2022-09-28")
p3 = Producto("3","Helado de Piña","5 personas",3590,"Piña","heladodepiña@gmail.com","Delicioso Helado de Piña, trozos de fruta directamente importados de Estados Unidos ","2022-10-10")
p4 = Producto("4","Galletas Triton","150g",790,"Naranja","triton@dulces.cl","Crujientes Galletas sabor naranja, listas para servir en familia","2022-09-28")
p5 = Producto("5","Galletas Cereal Bar","1k",13990,"Avena","CerealBar@galletas.cl","Crujientes Galletass con trozos de Avena para bajar esos kilos de más","2022-09-28")
p6 = Producto("6","Super 8","500g",20000,"Chocolate","Super8@dulces.cl","Deliciosa barra de chocolate crujiente, sabor chocolate con fondo de merengue","2022-09-28")
p7 = Producto("7","Marshmello","30 personas",39000,"Frutilla","Marshmello@dulces.cl","Suaves y esponjosos bombones de textura viscosa deliciosos para compartir en familia","2022-09-28")
p8 = Producto("8","Tiramisu","20 personas",30000,"Café","Tiramisu@dulces.cl","Delicioso Dulce artesanal directamente traído del Sur de Chile listo para debustar despues de almorzar","2022-09-28")
p9 = Producto("9","Frugelé","1k",2300,"Gelatina","FrugeleChile@dulces.cl","Esponjosas gomitas bañadas en azúcar, deliciosas para compartir con los amigos.","2022-09-28")
p10 = Producto("10","Rocklets","150g",400,"Chocolate","Rocklets@dulces.cl","Crujientes chocolates cubiertos de azúcar de diferentes colores","2022-09-28")


productos = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]


def home(request):
    print("home")
    context={}
    return render (request,'dulcescrud/index.html',context)


def login(request):
    print("login")
    mensajes=[]
    context={}
    if request.method=="POST":
        print("POST")
        credencial = request.POST["credencial"]
        password = request.POST["password"]
        ingreso = request.POST.get("opcion","")
        if ingreso == "Ingresar":
            for x in usuarios:
                if x.getCredencial() == credencial:
                    print("encontró el usuario")
                    if x.getPassword() == password:
                        mensajes.append("Inicio de sesion correcto")
                        context= {'productos':productos,'mensaje':mensajes}
                        return render(request,'dulcescrud/index.html',context)
                else:
                    context={'mensaje':" -----------> El usuario o contraseña NO corresponden <-----------"}
                    print("no existe el usuario")
                    return render(request,'dulcescrud/error.html',context)
    return render(request,'dulcescrud/login.html',context)

def dulces_agregar(request):
    print("estoy en dulces_agregar")
    context={}
    if request.method == "POST":
        print("POST")
        op=request.POST.get("opc","")
        if op =="edit" or op =="atras":
            context ={'productos':productos}
            return render(request,"dulcescrud/index.html", context)
        if op == "agregar":
            codigoD=request.POST["codigoD"]
            nombreD=request.POST["nombreD"]
            cantidad=request.POST["cantidad"]
            precioD=request.POST["precioD"]
            ingredienteP=request.POST["ingredienteP"]
            correo=request.POST["correo"]
            descripcion=request.POST["descripcion"]
            fecha=request.POST["fecha"]
            if codigoD != "" and nombreD != "" and cantidad !="" and precioD != "" and ingredienteP != "" and correo != "" and descripcion != "" and fecha != "":
                producto = Producto(codigoD,nombreD,cantidad,precioD,ingredienteP,correo,descripcion,fecha)
                productos.append(producto)
                context={'mensaje':"dulce ingresado con exito"}
            else:
                context={'mensaje':'no pueden haber campos vacios'}
            return render(request,'dulcescrud/index.html',context)
        if op == "actualizar":
            codigoD=request.POST["codigoD"]
            nombreD=request.POST["nombreD"]
            cantidad=request.POST["cantidad"]
            precioD=request.POST["precioD"]
            ingredienteP=request.POST["ingredienteP"]
            correo=request.POST["correo"]
            descripcion=request.POST["descripcion"]
            fecha=request.POST["fecha"]

            if codigoD != "" and nombreD != "" and cantidad !="" and precioD != "" and ingredienteP != "" and correo != "" and descripcion != "" and fecha != "":
                producto = Producto(codigoD,nombreD,cantidad,precioD,ingredienteP,correo,descripcion,fecha)
                pr=0
                for dul in productos:
                    if dul.getCodigoDulce() == producto.getCodigoDulce():
                        productos.remove(dul)
                        productos.insert(pr,producto)
                        break
                    pr=pr+1
                context={'producto':producto,'mensaje':"se actualizaron correctamente los datos del dulce"}
                return render(request,"dulcescrud/dulces_edit.html",context)
            else:
                context={'mensaje':'no pueden haber campos vacios'}
            return render(request,"dulcescrud/index.html",context)
    return render(request,'dulcescrud/dulces_add.html',context)

def dulces_edit(request,pkd):
    print("estoy en dulces_edit")
    mensajes=[]
    errores=[]
    context={}

    for producto in productos:
        if producto.getCodigoDulce() == pkd:
            print("dulces_edit encontró producto")

            context={'producto':producto, 'mensajes':mensajes,'errores':errores}
            break
    return render(request, 'dulcescrud/dulces_edit.html', context)

def dulces_del(request, pkd):
    print("estoy en dulces_del")
    mensajes=[]
    errores=[]
    try:
        context={}
        i = 0
        for producto in productos:
            if producto.getCodigoDulce() == pkd:
                i = 1
                productos.remove(producto)
                mensajes.append("dulce eliminado con exito")
                print("dulces_del producto eliminado")
        if i == 0:
            errores.append("no existe el producto")
            print("dulces_del no eliminado")
        context={'productos':productos,'mensajes':mensajes,'errores':errores}
        return render(request,'dulcescrud/index.html',context)
    except:
        errores.append("dulce no se encuentra.")
        context={'productos':productos,'mensajes':mensajes,'errores':errores}
        return render(request,'dulcescrud/index.html',context)

