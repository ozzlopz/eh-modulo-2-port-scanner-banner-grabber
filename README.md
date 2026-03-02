
# Port Scanner + Banner Grabber

Este programa escanea los puertos TCP del 1 al 200 en una IP objetivo para detectar cuáles están abiertos.

También intenta capturar el banner del servicio que corre en cada puerto abierto.

El banner puede mostrar información como el tipo de servicio y su versión.

---

## Cómo funciona

El script:

- Usa sockets TCP (`socket.AF_INET`, `socket.SOCK_STREAM`)
- Usa `connect_ex()` para verificar si un puerto está abierto
- Usa `recv(1024)` para intentar capturar el banner
- Usa un timeout de 2 segundos para evitar bloqueos

---

## Uso

1) Edita en `scanner.py`:

- `ip_objetivo`
- `puerto_inicio`
- `puerto_fin`
- `timeout_segundos`

Ejemplo:

```python
ip_objetivo = '127.0.0.1'
puerto_inicio = 1
puerto_fin = 200
timeout_segundos=5
```

## Ejemplo de salida
```
Escaneando 127.0.0.1 de puerto 1 a 200...
--------------------------------------------------
Puerto 22: ABIERTO
Banner: SSH-2.0-OpenSSH_8.2p1
--------------------------------------------------
Puerto 80: ABIERTO
Banner: HTTP/1.1 200 OK
--------------------------------------------------
Puerto 443: ABIERTO
Banner: No disponible
--------------------------------------------------
Escaneo completado
```

## Requisitos
Requisitos:
- Python 3.x

No requiere librerías adicionales.

