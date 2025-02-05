import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

# Шаг 1: Проверка наличия файла
file_path = 'events.json'

if not os.path.exists(file_path):
    print(f"Файл {file_path} не найден. Проверьте путь или создайте файл с данными.")
    # Используем тестовые данные
    data = {
        "events": [
            {"timestamp": "2023-08-21T08:00:00", "signature": "MALWARE-CNC Win.Trojan.Jadtre variant outbound connection"},
            {"timestamp": "2023-08-21T09:00:00", "signature": "EXPLOIT-KIT Drive-by exploit attempt"},
            {"timestamp": "2023-08-21T10:00:00", "signature": "MALWARE-BACKDOOR Remote access tool activity detected"}
        ]
    }
else:
    # Загрузка данных из JSON-файла
    with open(file_path, 'r') as file:
        data = json.load(file)

# Шаг 2: Преобразование данных в DataFrame
df = pd.DataFrame(data["events"])

# Шаг 3: Анализ данных
event_counts = df['signature'].value_counts()
print("Распределение событий по типам:")
print(event_counts)

# Шаг 4: Визуализация данных
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="signature", palette="viridis")
plt.title("Распределение типов событий безопасности", fontsize=16)
plt.xlabel("Тип события", fontsize=12)
plt.ylabel("Количество", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение графика и вывод на экран
plt.savefig('event_distribution.png')
plt.show()