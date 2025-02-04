from scapy.all import sniff

def process_http_packet(packet):
    if packet.haslayer("Raw"):  # Проверяем, содержит ли пакет данные
        try:
            http_data = packet["Raw"].load.decode(errors="ignore")
            if "GET" in http_data or "POST" in http_data:  # Ищем HTTP-запросы
                print("[HTTP Packet Captured] ->", http_data)
        except Exception as decode_error:
            print(f"Error while decoding packet: {decode_error}")

print("Starting HTTP traffic capture on port 80...")
sniff(filter="\\Device\\NPF_{E2535DD2-E092-4923-8A26-16502BA032E6}", prn=process_http_packet, store=False)