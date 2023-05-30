import os
import platform

# SCRIPT COMPRA EN EL SUPERMERCADO 

# Diccionarios: 

# Panadería: 

panaderia = [
     {"tipo_pan": "Hallulla",
     "precio_kilo": 1500
     },
     {"tipo_pan": "Hallulla Integral",
      "precio_kilo": 1990    
     },
     {"tipo_pan": "Pan Francés",
      "precio_kilo": 1490
     },
     {"tipo_pan": "Pan Francés Integral",
      "precio_kilo": 1790
     },
     {"tipo_pan": "Pan Italiano",
      "precio_kilo": 1990     
     }
    ]

tortas = [
    {"tipo_torta": "Torta Selva Negra Sin azúcar",
     "precio_torta": 9900
    },
    {"tipo_torta": "Torta Mil Hojas",
     "precio_torta": 12990
    },
    {"tipo_torta": "Torta Piña",
     "precio_torta": 10990
    },
    {"tipo_torta": "Torta Manjar Nuez",
     "precio_torta": 10990
    }
    ]

# Lácteos: 

leches = [
    {"tipo_leche": "Leche Descremada",
     "marca": "Colun",
     "precio_leche": 990
     },
     {"tipo_leche": "Leche con Chocolate",
     "marca": "Colun",
     "precio_leche": 1190   
     },
     {"tipo_leche": "Leche Entera",
     "marca": "Soprole",
     "precio_leche": 890
     },
     {"tipo_leche": "Leche con Avena",
     "marca": "Ori",
     "precio_leche": 1290    
     }
     ]

yogures = [
    {"tipo_yogurt": "yogurt griego",
     "marca": "Danone",
     "precio_yogurt": 690
    },
    {"tipo_yogurt": "yogurt sabor damasco",
     "marca": "Soprole",
     "precio_yogurt": 490
    },
    {"tipo_yogurt": "yogurt sin azúcar sabor frutilla",
     "marca": "Colun",
     "precio_yogurt": 590
    },
    {"tipo_yogurt": "yogurt sin lactosa",
     "marca": "Loncoleche",
     "precio_yogurt": 690
    } 
    ]

quesos = [
    {"tipo_queso": "Queso Mantecoso Laminado 500grs",
     "marca": "Rio Bueno",
     "precio_queso": 5990
    },
    {"tipo_queso": "Queso Mantecoso Laminado 250grs",
     "marca": "Quilque",
     "precio_queso": 3490
    },
    {"tipo_queso": "Queso Ranco Laminado bolsa 500grs",
     "marca": "Colun",
     "precio_queso": 5290
    },
    {"tipo_queso": "Queso Gauda Laminado 500grs",
     "marca": "Soprole",
     "precio_queso": 5490
    }
    ]


# Carnicería:

carnes = [
    {"tipo_carne": "Vacuno",
     "precio_kilo": 5890
    },
    {"tipo_carne": "Pollo",
     "precio_kilo": 4490
    },
    {"tipo_carne": "Cordero",
     "precio_kilo": 7990
    }
    ]

# Aseo:

aseo = [
    {"articulo_aseo": "limpia vidrios",
     "precio_unidad": 3290
    },
    {"articulo_aseo": "lustra muebles",
     "precio_unidad": 2290
    },
    {"articulo_aseo": "trapo limpiador",
     "precio_unidad": 2490
    },
    {"articulo_aseo": "clorinda",
     "precio_unidad": 1290
    }
    ]

# Congelados:

congelados = [
    {"alimento": "Choclo en grano congelado",
     "valor": 1290
    },
    {"alimento": "Papas prefritas kilo",
     "valor": 3290
    },
    {"alimento": "Papas duquesas kilo",
     "valor": 4490
    },
    {"alimento": "sofrito con ajo 160 grs.",
     "valor": 650
    }
    ]    

#Bebestibles:

bebestibles = [
    {"bebestible": "Cerveza en lata sin alcohol",
     "valor_unidad": 790
    },
    {"bebestible": "Bebida Pepsi 1,5lts",
     "valor_unidad": 1390
    },
    {"bebestible": "Champange Valdivieso 750ml",
     "valor_unidad": 3490
    },
    {"bebestible": "lata Coca-Cola",
     "valor_unidad": 990
    }
    ]    

# Frutas y Verduras: 

frutas_verduras = [
    {"fruta_verdura": "Tomates",
     "valor_kilo": 1690
    },
    {"fruta_verdura": "Manzana Fuji",
     "valor_kilo": 1790
    },
    {"fruta_verdura": "Palta",
     "valor_kilo": 6490
    },
    {"fruta_verdura": "Plátano",
     "valor_kilo": 1690
    }
    ] 

# Limpia la pantalla según el sistema operativo

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Función que pasa a las siguientes secciones:

def receive_menu():
    while True:
        menu_section = int(input("""Presione a qué sección desea ir:
            1. Panadería y Pastelería
            2. Lácteos
            3. Carnicería
            4. Limpieza y Aseo
            5. Congelados
            6. Bebestibles
            7. Frutas y Verduras
            0. Volver a mostrar el menú
        """))

        if menu_section == 1:
            get_list_panaderia(panaderia, tortas)
        elif menu_section == 2:
            get_list_lacteos(leches, yogures, quesos)
        elif menu_section == 3:
            get_list_carniceria(carnes)
        elif menu_section == 4:
            get_list_aseo(aseo)
        elif menu_section == 5:
            get_list_congelados(congelados)
        elif menu_section == 6:
            get_list_bebestibles(bebestibles)
        elif menu_section == 7:
            get_list_frutas_verdura(frutas_verduras)
        elif menu_section == 0:
            continue  # Reiniciar el bucle y mostrar el menú nuevamente
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

        break  # Salir del bucle while después de mostrar una sección


    
    

     


suma_total_productos_panaderia = 0
suma_total_lacteos = 0
total_carne = 0 
total_articulos_aseo = 0
total_alimentos_congelados = 0
total_bebestibles = 0
total_frutas_verduras = 0
total_acumulado = 0


# Sección 1 Panaderia:   

def get_list_panaderia(panaderia, tortas):
    print("\n \n")
    print("=====Seccion Panadería y Pastelería=====\n")
    print("\n \n")
     
    seguir = int(input("""
    Ha ingresaso a la Sección de Panadería y Pastelería:
    1. Deseo seguir en esta sección
    2. Salir 
    """))
    
    if seguir == 1:
        while True:
            for posicion, i in enumerate(panaderia):
                pos = posicion + 1
                producto = i["tipo_pan"]
                precio = i["precio_kilo"]
                print(f"{pos}. {producto}, precio x kilo: {precio}")

            opcion_pan_elegido = int(input("Ingrese el número de opción de pan que desea: "))

            if opcion_pan_elegido >= 1 and opcion_pan_elegido <= len(panaderia):
                cantidad = int(input("Ingrese la cantidad de pan que desea llevar (kilos) : "))
                total_pan = panaderia[opcion_pan_elegido - 1]['precio_kilo'] * cantidad
                print(f"Total Pan: {total_pan}")
                break
            else:
                print("Ingrese una opción válida.\n")
               
        opcionTorta = int(input("""¿Desea añadir Tortas?
            1. Sí
            2. No
            """))
        
        while True:
            for posicion, i in enumerate(tortas):
                pos = posicion + 1
                producto = i["tipo_torta"]
                precio = i["precio_torta"]
                print(f"{pos}. {producto}, precio: {precio}")

            opcion_torta_elegida = int(input("Ingrese el número de opción de torta que desea: "))

            if opcion_torta_elegida >= 1 and opcion_torta_elegida <= len(tortas):
                cantidad = int(input("Ingrese la cantidad de tortas que desea llevar: "))
                total_tortas = tortas[opcion_torta_elegida - 1]['precio_torta'] * cantidad
                print(f"Total Tortas: {total_tortas}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            opcion_torta_elegida = 0
            total_tortas = 0
            print("No agrega Tortas")

    else: 
        receive_menu()
        
    suma_total_productos_panaderia = total_pan + total_tortas

    return suma_total_productos_panaderia

# Seccion 2 Lacteos

def get_list_lacteos(leches, yogures, quesos):
    print("\n \n")
    print("====Seccion Lacteos====\n")

    seguir = int(input("""
    Ha ingresaso a la Sección de los Lácteos:
    1. Deseo seguir en esta sección
    2. Salir 
    """))
    
    if seguir == 1: 
        while True:
            for posicion, i in enumerate(leches):
                pos = posicion + 1
                producto = i["tipo_leche"]
                marca = i["marca"]
                precio = i["precio_leche"]
                print(f"{pos}. {producto}, marca: {marca}, precio: {precio}")

            opcion_leche_elegida = int(input("Ingrese el número de opción de leche que desea: "))

            if opcion_leche_elegida >= 1 and opcion_leche_elegida <= len(leches):
                cantidad = int(input("Ingrese la cantidad de leches que desea llevar: "))
                total_leches = leches[opcion_leche_elegida - 1]['precio_leche'] * cantidad
                print(f"Total Leches: {total_leches}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            opcion_leche_elegida = 0
            total_leches = 0
            print("No agrega leche")

    # Yogures

        opcionYogurt = int(input(""" ¿Desea añadir Yogurt?
            1. Sí
            2. No
            """))
    
        while True:
            for posicion, i in enumerate(yogures):
                pos = posicion + 1
                producto = i["tipo_yogurt"]
                marca = i["marca"]
                precio = i["precio_yogurt"]
                print(f"{pos}. {producto}, marca: {marca}, precio: {precio}")

            opcion_yogurt_elegido = int(input("Ingrese el número de opción de yogurt que desea: "))

            if opcion_yogurt_elegido >= 1 and opcion_yogurt_elegido <= len(yogures):
                cantidad = int(input("Ingrese la cantidad de yogurt que desea llevar: "))
                total_yogurt = yogures[opcion_yogurt_elegido - 1]['precio_yogurt'] * cantidad
                print(f"Total Yogurt: {total_yogurt}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            opcion_yogurt_elegido = 0
            total_yogurt = 0
            print("No agrega Yogurt")

    # Quesos
        opcionQueso = int(input(""" ¿Desea añadir Queso?
            1. Sí
            2. No
            """))
         
        while True: 
            for posicion, i in enumerate(quesos):
                pos = posicion + 1
                producto = i["tipo_queso"]
                marca = i["marca"]
                precio = i["precio_queso"]
                print(f"{pos}. {producto}, marca: {marca}, precio: {precio}")

            opcion_queso_elegido = int(input("Ingrese el número de opción de queso que desea: "))

            if opcion_queso_elegido >= 1 and opcion_queso_elegido <= len(quesos):
                cantidad = int(input("Ingrese la cantidad de queso que desea llevar: "))
                total_queso = quesos[opcion_queso_elegido - 1]['precio_queso'] * cantidad
                print(f"Total Queso: {total_queso}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            opcion_queso_elegido = 0
            total_queso = 0
            print("No agrega queso")
    
    else:
        receive_menu()

    suma_total_lacteos = total_leches + total_queso + total_yogurt
    
    total_acumulado = total_acumulado + suma_total_lacteos
    return suma_total_lacteos


#Seccion 3 Carnes
    
def get_list_carniceria(carnes):
    total_carne = 0
    print("\n \n")
    print("====Seccion Carnicería====\n")

    seguir = int(input("""
    Ha ingresaso a la Sección Carnicería:
    1. Deseo seguir en esta sección
    2. Salir 
    """))
  
    if seguir == 1:
        while True: 
            for posicion, i in enumerate(carnes):
                pos = posicion + 1
                producto = i["tipo_carne"]
                precio = i["precio_kilo"]
                print(f"{pos}. {producto}, precio: {precio}")
        
            opcion_carne_elegida = int(input("Ingrese el número de opción de carne que desea: "))
        
            if opcion_carne_elegida >= 1 and opcion_carne_elegida <= len(carnes):
                cantidad = int(input("Ingrese la cantidad de carne que desea llevar: "))
                total_carne = carnes[opcion_carne_elegida - 1]['precio_kilo'] * cantidad
                print(f"Total Carne: {total_carne}")
                break
            else:
                print("Ingrese una opción válida.\n")

        else:
            opcion_carne_elegida = 0
            total_carne = 0
            print("No agrega carne")
    else:
        receive_menu()

    total_acumulado = total_acumulado + total_carne
    return total_carne

# Seccion 4 Aseo
    
def get_list_aseo(aseo):
    print("\n \n")
    print("=====Seccion Limpieza y Aseo====\n")
    
    seguir = int(input("""
    Ha ingresaso a la Sección de Limpieza y Aseo:
    1. Deseo seguir en esta sección
    2. Salir 
    """))

    if seguir == 1:
        while True:
            for posicion, i in enumerate(aseo):
                pos = posicion + 1
                producto = i["articulo_aseo"]
                precio = i["precio_unidad"]
                print(f"{pos}. {producto}, precio: {precio}")
        
            opcion_articulo_elegido = int(input("Ingrese el número de opción de artículo de aseo que desea: "))
        
            if opcion_articulo_elegido >= 1 and opcion_articulo_elegido <= len(aseo):
                cantidad = int(input("Ingrese la cantidad de artículos de aseo que desea llevar: "))
                total_articulos_aseo = aseo[opcion_articulo_elegido - 1]['precio_unidad'] * cantidad
                print(f"Total Artículos de aseo: {total_articulos_aseo}")
                break
            else:
                print("Ingrese una opción válida.\n")
                    
        else:
            opcion_articulo_elegido = 0
            total_articulos_aseo = 0
            print("No agrega Artículos de aseo")
    else:
        receive_menu()
   
    total_acumulado = total_acumulado + total_articulos_aseo
    return total_articulos_aseo

# Seccion 5 Congelados

def get_list_congelados(congelados):
    print("\n \n")
    print("=====Seccion Congelados=====\n")
    
    seguir = int(input("""
    Ha ingresaso a la Sección de Congelados:
    1. Deseo seguir en esta sección
    2. Salir 
    """))
    
    if seguir == 1:
        while True: 
            for posicion, i in enumerate(congelados):
                pos = posicion + 1
                producto = i["alimento"]
                precio = i["valor"]
                print(f"{pos}. {producto}, precio: {precio}")
        
            opcion_congelado_elegido = int(input("Ingrese el número de opción de alimento congelado que desea: "))
        
            if opcion_congelado_elegido >= 1 and opcion_congelado_elegido <= len(congelados):
                cantidad = int(input("Ingrese la cantidad de alimentos congelados que desea llevar: "))
                total_alimentos_congelados = congelados[opcion_congelado_elegido - 1]['valor'] * cantidad
                print(f"Total Alimentos congelados: {total_alimentos_congelados}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            opcion_congelado_elegido = 0
            total_alimentos_congelados = 0
            print("No agrega Alimentos congelados")
    else:
        receive_menu()
        
    total_acumulado = total_acumulado + total_alimentos_congelados
    return total_alimentos_congelados

# Sección 6 Bebestibles
          
def get_list_bebestibles(bebestibles):
    print("\n \n")
    print("=====Seccion de Bebestibles====\n")
    
    seguir = int(input("""
    Ha ingresaso a la Sección de Bebestibles:
    1. Deseo seguir en esta sección
    2. Salir 
    """))

    if seguir == 1: 
        while True:
            for posicion, i in enumerate(bebestibles):
                pos = posicion + 1
                producto = i["bebestible"]
                precio = i["valor_unidad"]
                print(f"{pos}. {producto}, precio: {precio}")
        
            opcion_bebestible_elegido = int(input("Ingrese el número de opción de alimento congelado que desea: "))
        
            if opcion_bebestible_elegido >= 1 and opcion_bebestible_elegido <= len(bebestibles):
                cantidad = int(input("Ingrese la cantidad de bebestibles que desea llevar: "))
                total_bebestibles = bebestibles[opcion_bebestible_elegido - 1]['valor_unidad'] * cantidad
                print(f"Total bebestibles: {total_bebestibles}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            total_bebestibles = 0
            total_bebestibles = 0
            print("No agrega bebestibles")    
    else:
        receive_menu()
        
    total_acumulado = total_acumulado + total_bebestibles
    return total_bebestibles

def get_list_frutas_verdura(frutas_verduras):
    print("\n \n")
    print("=====Seccion Frutas y Verduras=====\n")
    
    seguir = int(input("""
    Ha ingresaso a la Sección de Frutas y Verduras:
    1. Deseo seguir en esta sección
    2. Salir 
    """))
    
    if seguir == 1: 
        while True: 
            for posicion, i in enumerate(frutas_verduras):
                pos = posicion + 1
                producto = i["fruta_verdura"]
                precio = i["valor_kilo"]
                print(f"{pos}. {producto}, precio: {precio}")

            opcion_frutas_verduras = int(input("Ingrese el número de opción de fruta o verdura que desea: "))

            if opcion_frutas_verduras >= 1 and opcion_frutas_verduras <= len(frutas_verduras):
                cantidad = int(input("Ingrese la cantidad de fruta o verdura que desea llevar: "))
                total_frutas_verduras = frutas_verduras[opcion_frutas_verduras - 1]['valor_kilo'] * cantidad
                print(f"Total frutas y verduras: {total_frutas_verduras}")
                break
            else:
                print("Ingrese una opción válida.\n")
        else:
            opcion_frutas_verduras = 0
            total_frutas_verduras = 0
            print("No agrega frutas ni verduras")
    else:
        receive_menu()
            
    total_acumulado = total_acumulado + total_frutas_verduras
    return total_frutas_verduras


def generar_boleta():
    # Obtener totales de cada sección
    total_panaderia = get_list_panaderia(panaderia, tortas)
    total_lacteos = get_list_lacteos(leches, yogures, quesos)
    total_carniceria = get_list_carniceria(carnes)
    total_aseo = get_list_aseo(aseo)
    total_congelados = get_list_congelados(congelados)
    total_bebestibles = get_list_bebestibles(bebestibles)
    total_frutas_verduras = get_list_frutas_verdura(frutas_verduras)

def get_payment():
        # Calcular total general
        
    #lista_valores = [ total_panaderia,
     #   total_lacteos,
      #  total_carniceria,
       # total_aseo,
        #total_congelados,
        #total_bebestibles,
        #total_frutas_verduras,
   # ]


    total_general = total_acumulado
    iva = int(total_general * 0.19)
    total_final = total_general + iva

    suma_total_productos_panaderia = 0
    suma_total_lacteos = 0
    total_carne = 0 
    total_articulos_aseo = 0
    total_alimentos_congelados = 0
    total_bebestibles = 0
    total_frutas_verduras = 0
    
    # Imprimir boleta
    print("\n \n")
    print("======= BOLETA ELECTRONICA RUT 81.678.873-0=======")
    print("Sección Panadería:")
    print(f"Total Panadería: {suma_total_productos_panaderia}")
    print("Sección Lácteos:")
    print(f"Total Leches: {suma_total_lacteos}")
    print(f"Total Yogurts: {suma_total_lacteos}")
    print(f"Total Quesos: {suma_total_lacteos}")
    print("Sección Carnicería:")
    print(f"Total Carnicería: {total_carne}")
    print("Sección Aseo:")
    print(f"Total Artículos de Aseo: {total_articulos_aseo}")
    print("Sección Congelados:")
    print(f"Total Alimentos Congelados: {total_alimentos_congelados}")
    print("Sección Bebestibles:")
    print(f"Total Bebestibles: {total_bebestibles}")
    print("Sección Frutas y Verduras:")
    print(f"Total Frutas y Verduras: {total_frutas_verduras}")
    print("======================")
    print(f"Neto: {total_general}")
    print(f"Total IVA 19%: {iva}")
    print(f"TOTAL: {total_final} ")
    metodos_pago_boleta(total_final)
  

def metodos_pago_boleta(total_final):
    total_metodo_pago = total_final
    metodo_pago = [
        "Efectivo", 
        "Debito", 
        "Crédito"
        ]
     
    for posicion, i in enumerate(metodo_pago):
        pos = posicion +1
        print(f"metodo de pago {pos} : {i}")

    opcion_pago = int(input("ingrese método de pago: "))

    if opcion_pago == 1:
        print(f"ingresaste opción Efectivo, donde el valor total a pagar es: {total_metodo_pago}")
    elif opcion_pago == 2:
        print(f"ingresaste opción Debito, donde el valor total a pagar es: {total_metodo_pago}")
    elif opcion_pago == 3:
        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
        valor_cuotas = int(total_metodo_pago/ cantidad_cuotas)
        enCLP = "${:,.0f}".format(valor_cuotas)
        print(f"""
        Ingresaste opción Crédito, donde el valor total a pagar es: {total_metodo_pago} 
        en {cantidad_cuotas} cuotas,
        valor de cuota es: {enCLP}
        """)

receive_menu()


