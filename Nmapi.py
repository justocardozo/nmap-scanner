import nmap
print("""

            ¡Bienvenido!  
 __   __     __    __     ______     ______   __    
/\ "-.\ \   /\ "-./  \   /\  __ \   /\  == \ /\ \   
\ \ \-.  \  \ \ \-./\ \  \ \  __ \  \ \  _-/ \ \ \  
 \ \_\\"\_\  \ \_\ \ \_\  \ \_\ \_\  \ \_\    \ \_\ 
  \/_/ \/_/   \/_/  \/_/   \/_/\/_/   \/_/     \/_/ 
                                                    
                            by Justo Cardozo


""")
# Inicializar el escáner de nmap
t = nmap.PortScanner()

# Solicitar el objetivo al usuario
target = input("Target --->  ")

# Realizar el escaneo con los argumentos proporcionados
t.scan(target, arguments="-sV -Pn -T4")

# Verificar si el escaneo contiene datos para el objetivo
if target in t.all_hosts():
    print(f"Estado general de {target}: {t[target].state()}\n")
    
    # Iterar sobre los protocolos y puertos
    for protocol in t[target].all_protocols():
        print(f"Protocolo: {protocol}")
        ports = t[target][protocol].keys()
        for port in sorted(ports):
            port_info = t[target][protocol][port]
            state = port_info.get('state', 'desconocido')
            name = port_info.get('name', 'desconocido')
            product = port_info.get('product', 'desconocido')
            version = port_info.get('version', 'desconocido')
            extra_info = port_info.get('extrainfo', 'desconocido')
            
            print(f"  Puerto: {port}")
            print(f"    Estado: {state}")
            print(f"    Servicio: {name}")
            print(f"    Producto: {product}")
            print(f"    Versión: {version}")
            print(f"    Información extra: {extra_info}")
        print()
else:
    print(f"No se encontraron resultados para el objetivo: {target}. Verifica si es válido y accesible.")
