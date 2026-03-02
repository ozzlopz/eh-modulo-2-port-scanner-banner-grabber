import socket

# IP objetivo
ip_objetivo = '127.0.0.1'
# rango de puertos
puerto_inicio = 1
puerto_fin = 200
timeout_segundos = 2

print(f'Escaneando {ip_objetivo} de puerto {puerto_inicio} a {puerto_fin}...')
print('-' * 50)

for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conexion.settimeout(timeout_segundos)
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        if resultado == 0:
            print(f'Puerto {puerto}: ABIERTO')
            # intentar capturar banner
            try:
                banner = socket_conexion.recv(1024)
                banner_texto = banner.decode('utf-8', errors='ignore')
                print(f'Banner: {banner_texto.strip()}')
            except:
                print('Banner: No disponible')
            print('-' * 50)
        socket_conexion.close()
    except:
        print(f'Error en puerto {puerto}')
print('Escaneo completado')