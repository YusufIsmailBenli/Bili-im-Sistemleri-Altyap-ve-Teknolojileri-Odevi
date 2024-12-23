# Bilisim-Sistemleri-Altyapi-ve-Teknolojileri-Odevi

Dizin İzleme ve Loglama Servisi
Bu proje, belirlenen bir dizindeki değişiklikleri izleyen ve bu değişiklikleri JSON formatında log dosyasına kaydeden bir Python servisini içermektedir. Servis, Linux ortamında çalışacak ve başlangıçta bir sistem servisi olarak yapılandırılacaktır.

Projenin Adımları
1. Sanal Makine (Opsiyonel)
Projeyi izole bir ortamda çalıştırmak isterseniz, VirtualBox, VMware veya KVM kullanarak bir sanal makine oluşturabilirsiniz.

3. Python Kurulumu
Linux üzerinde Python 3.8 veya daha güncel bir sürümün kurulu olduğundan emin olun:
```
sudo apt update
sudo apt install python3 python3-pip
```
Gerekli Python kütüphanelerini yüklemek için pip kullanabilirsiniz:
```
pip install watchdog
```
3. Log Dizini Oluşturma
Değişikliklerin kaydedileceği log dizinini oluşturun:
```
mkdir -p /home/user/bsm/logs
```
4. Python Scripti Yazımı
Aşağıdaki Python scripti, belirtilen dizini izleyerek değişiklikleri JSON formatında kaydeder.
```
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        log_event = {
            "event": "created",
            "path": event.src_path,
        }
        self.log_event(log_event)

    def on_deleted(self, event):
        if event.is_directory:
            return
        log_event = {
            "event": "deleted",
            "path": event.src_path,
        }
        self.log_event(log_event)

    def on_moved(self, event):
        if event.is_directory:
            return
        print(f"Moved file: {event.src_path} -> {event.dest_path}")
        log_event = {
            "event": "renamed",
            "old_file": event.src_path,
            "new_file": event.dest_path,
        }
        self.log_event(log_event)

    def log_event(self, log_event):
        log_file_path = "/home/yusuf/bsm/logs/changes.json"
        
        try:
            with open(log_file_path, "r") as log_file:
                data = json.load(log_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(log_event)

        with open(log_file_path, "w") as log_file:
            json.dump(data, log_file, indent=2)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path="/home/yusuf/bsm/test", recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
```
5. Scripti Sistem Servisi Olarak Yapılandırma
Python scriptinizi bir sistem servisi olarak çalıştırmak için aşağıdaki adımları takip edin.
Servis Dosyası: bsm.service

Servis dosyasını oluşturun:
```
sudo nano /etc/systemd/system/bsm.service
```
Aşağıdaki içeriği dosyaya yapıştırın:
```
[Unit]
Description=Dizin İzleme Servisi
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/user/bsm/bsm.py
Restart=always
User=user
Group=user

[Install]
WantedBy=multi-user.target
```
6. Servisi Etkinleştirme ve Başlatma
Servisi etkinleştirin ve başlatın:
```
sudo systemctl daemon-reload
sudo systemctl enable directory_watcher.service
sudo systemctl start directory_watcher.service
```
7. Servis Durumunu Kontrol Etme
Servisin çalışıp çalışmadığını kontrol edin:
```
sudo systemctl status directory_watcher.service
```
Proje Yapısı
```
bsm/
├── logs/
│   └── changes.json
├── test/
└── directory_watcher.py
```
Notlar
Log dosyası: /home/user/bsm/logs/changes.json

İzlenecek dizin: /home/user/bsm/test

Sistem servisi her yeniden başlatıldığında otomatik olarak çalışır.
