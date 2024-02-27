import socket

def download_file(host, path, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, 80))
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        sock.send(request.encode())

        data = sock.recv(4096)
        headers, body = data.split(b"\r\n\r\n", 1)

        content_length = None
        transfer_encoding = None

        for header in headers.split(b"\r\n"):
            if b"Content-Length" in header:
                content_length = int(header.split(b":")[1].strip())
            elif b"Transfer-Encoding" in header and b"chunked" in header:
                transfer_encoding = "chunked"

        if content_length is not None:
            while len(body) < content_length:
                data = sock.recv(4096)
                if not data:
                    break
                body += data

        elif transfer_encoding == "chunked":
            while b"0\r\n\r\n" not in body:
                data = sock.recv(4096)
                if not data:
                    break
                body += data

        with open(filename, "wb") as file:
            file.write(body)

        print(f"Download concluído. Arquivo salvo como {filename}")

    except Exception as e:
        print(f"Erro durante o download: {e}")

    finally:
        sock.close()

# Exemplos de uso:
# download_file("viacep.com.br", "/ws/RN/Natal/Morais/json/", "cep_data.json")
# download_file("httpbin.org", "/image/jpeg", "image.jpg")
