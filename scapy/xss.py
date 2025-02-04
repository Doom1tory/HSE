from scapy.all import sniff

# Функция для проверки пакетов на наличие XSS
def detect_xss(packet):
    # Проверяем, есть ли в пакете полезная нагрузка (Raw)
    if packet.haslayer("Raw"):
        try:
            # Извлекаем данные из полезной нагрузки
            payload = packet["Raw"].load.decode(errors="ignore")
            
            # Проверяем наличие подозрительных строк
            if "<script>" in payload or "alert(" in payload:
                print("[Обнаружена XSS-атака] ->", payload)
        except Exception as error:
            print("Ошибка при обработке пакета:", error)

# Выводим сообщение о запуске программы
print("Запуск обнаружения XSS-атак...")

# Запускаем мониторинг сетевого трафика
sniff(
    iface="\\Device\\NPF_{E2535DD2-E092-4923-8A26-16502BA032E6}",  # Указываем интерфейс
    filter="tcp port 80",  # Фильтруем HTTP-трафик
    prn=detect_xss,  # Передаем функцию для обработки пакетов
    store=False)  # Не сохраняем пакеты в памяти