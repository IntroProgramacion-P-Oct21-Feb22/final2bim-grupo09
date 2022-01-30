"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook():
    print("Creando cuenta de Facebook")
    nombre = input("Ingrese su nombre ")
    usuario = input("Ingrese su nombre de usuario ")
    edad = input("Ingrese su edad ")
    ciudad = input("Ingrese su ciudad de residencia ")
    pais = input("Ingrese su pais de residencia ")
    correo = input("Ingrese su correo electronico ")
    mensaje = ("Resumen de cuenta\nNombre: %s\nNombre de usuario: %s\n"
               "Edad: %s\nCiudad: %s\nPais: %s\nCorreo electronico: %s\n" %
               (nombre , usuario , edad , ciudad , pais, correo))
    return mensaje
def crearTwitter():
    cadena = "%s\n" % ("Creando cuenta de Twitter")
    print(cadena)
    usuario = input("Ingrese su nombre de usuario ")
    nombre = input("Ingrese su nombre ")
    apellido = input("Ingrese su apellido")
    edad = input("Ingrese su edad ")
    ciudad = input("Ingrese su ciudad de residencia ")
    pais = input("Ingrese su pais de residencia ")
    idioma = input("Ingrese su idioma")
    correo = input("Ingrese su correo electronico ")
    mensaje = ("Resumen de cuenta\nNombre de usuario: %s\nNombre: %s\nApellido: %s\nEdad: %s\nCiudad: %s\n"
               "Pais: %s\nIdioma: %s\nCorreo: %s\n"
               % (usuario,nombre,apellido,edad,ciudad,pais,idioma,correo))
    print(mensaje)
def crearWhatsapp():
    print("Creando cuenta de Whatsapp")
    usuario = input("Ingrese su nombre de usuario ")
    telefono = input("Ingrese su numero de telefono")
    edad = input("Ingrese su edad ")
    ciudad = input("Ingrese su ciudad de residencia ")
    pais = input("Ingrese su pais de residencia ")
    mensaje = ("Resumen de cuenta\nNombre de usuario: %s\nNumero de telefono: %s\n"
               "EDad: %s\nCiudad: %s\nPais: %s\n" % (usuario,telefono,edad,ciudad,pais))
    return mensaje
def crearTelegram():
    print("Creando cuenta de Telegram")
    usuario = input("Ingrese su nombre de usuario ")
    telefono = input("Ingrese su numero de telefono")
    ciudad = input("Ingrese su ciudad de residencia ")
    pais = input("Ingrese su pais de residencia ")
    interes = input("Ingrese su area de interes ")
    mensaje = ("Resumen de cuenta\nNombre de usuario: %s\nNumero de telefono: %s\n"
               "Ciudad: %s\nPais: %s\nArea de interes: %s\n" % (usuario,telefono,ciudad,pais, interes))
    print(mensaje)
def crearSignal():
    print("Creando cuenta de Signal")
    usuario = input("Ingrese su nombre de usuario ")
    telefono = input("Ingrese su numero de telefono")
    ciudad = input("Ingrese su ciudad de residencia ")
    pais = input("Ingrese su pais de residencia ")
    interes = input("Ingrese su hobby principal ")
    mensaje = ("Resumen de cuenta\nNombre de usuario: %s\nNumero de telefono: %s\n"
               "Ciudad: %s\nPais: %s\nHobby principal: %s\n" % (usuario,telefono,ciudad,pais, interes))
    return mensaje
def crearInstagram():
    print("Creando cuenta de Instagram")
    usuario = input("Ingrese su nombre de usuario ")
    ciudad = input("Ingrese su ciudad de residencia ")
    edad = input("Ingrese su edad ")
    correo = input("Ingrese su correo electronico ")
    mensaje = ("Resumen de cuenta\nNombre de usuario: %s\n"
               "Ciudad: %s\nEdad: %s\nCorreo electronico : %s\n" % (usuario,ciudad,edad, correo))
    print(mensaje)
def crearFlickr():
    print("Creando cuenta de Instagram")
    usuario = input("Ingrese su nombre de usuario ")
    correo = input("Ingrese su hobby principal ")
    mensaje = ("Resumen de cuenta\nNombre de usuario: %s\nCorreo electronico : %s\n" % (usuario, correo))
    return mensaje


# agregar los métodos faltantes

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
if __name__ == "__main__":
    contador = 0
    bandera = True
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    while (bandera == True):
        print("proceso inicial")
        print("Escriba 1 para generar una cuneta de Facebook, 2 para Twiter, 3 para Whattsapp, 4 para Telegram")
        print("5 para Signal, 6 para Instagram y 7 para Flickr")
        mensaje = input()
        if mensaje == "1":
            mensaje = crearFacebook()
            print(mensaje)
        elif mensaje == "2":
            cuenta_twitter = crearTwitter()
        elif mensaje == "3":
            mensaje = crearWhatsapp()
            print(mensaje)
        elif mensaje == "4":
            mensaje = crearTelegram()
        elif mensaje == "5":
            mensaje = crearSignal()
            print(mensaje)
        elif mensaje == "6":
            mensaje = crearInstagram()
        elif mensaje == "7":
            mensaje = crearFlickr()
            print(mensaje)
        else:
            print("Opcion invalida")
            contador = contador - 1
        salida = input("Escriba Salir para terminar el proceso ")
        if salida == "Salir" or salida == "salir" or salida == "SALIR":
            bandera = False
        contador = contador + 1
    print("Cuentas creadas " + str(contador))
    if contador > 0 and contador <= 5:
        print(mensajeFinal[0])
    elif contador > 5 and contador <= 15:
        print(mensajeFinal[1])
    else:
        print("Excelente campaña")