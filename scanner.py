import socket 

def leer_archivo(filename):
    #Con el archivo abierto haz esto
    with open(filename, "r") as file:
        lineas  = file.readlines()
        lineaslimpias=[]
        for linea in lineas:
            lineaslimpias.append(linea.rstrip())
        return lineaslimpias



hosts = leer_archivo('ips.txt')
ports = leer_archivo('puertos_comunes.txt')



#Para cada host 
for host in hosts:
    #Para cada uno de los puertos
    for port in ports:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, int(port)))
        if result == 0:
            print(f"El puerto {port} está abierto")
        else: 
            print(f"El puerto {port} está cerrado")
        sock.close()
    








