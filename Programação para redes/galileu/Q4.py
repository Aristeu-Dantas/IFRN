import struct
import socket

def read_pcap_file(file_path):
    with open(file_path, 'rb') as file:
        pcap_header = file.read(24)  # Lê o cabeçalho do arquivo pcap

        # Analisa o cabeçalho do arquivo pcap
        magic_number, maior_version, menor_version, _, _, snap_len, fcs, link_type = struct.unpack('IHHIIIII', pcap_header)

        print(f'Magic Number: {hex(magic_number)}')
        print(f'Maior Version: {maior_version}')
        print(f'Menor Version: {menor_version}')
        print(f'SnapLen: {snap_len}')
        print(f'FCS: {fcs}')
        print(f'LinkType: {link_type}')

        # Leitura de pacotes
        while True:
            packet_header = file.read(16)  # Lê o cabeçalho do pacote

            if not packet_header:
                break  # Fim do arquivo

            timestamp_sec, timestamp_usec, captured_len, original_len = struct.unpack('IIII', packet_header)

            print('\nPacket Info:')
            print(f'Timestamp (Segundos): {timestamp_sec}')
            print(f'Timestamp (Microsegundos): {timestamp_usec}')
            print(f'Captura de Pacote Length: {captured_len}')
            print(f'Pacote Original Length: {original_len}')

            packet_data = file.read(captured_len)  # Lê os dados do pacote

            # Aqui você pode analisar o conteúdo do pacote, dependendo do tipo de link (Ethernet, IPv4, TCP, UDP, etc.)
            # Lembre-se de que isso pode ficar bastante complexo dependendo do que você deseja extrair.

def main():
    file_path = 'S:\IFRN\Programação para redes\galileu\Q4.py'  # Substitua pelo caminho do seu arquivo pcap
    read_pcap_file(file_path)

if __name__ == "__main__":
    main()
