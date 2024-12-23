# Bilisim-Sistemleri-Altyapi-ve-Teknolojileri-Odevi

Dizin İzleme ve Loglama Servisi
Bu proje, belirlenen bir dizindeki değişiklikleri izleyen ve bu değişiklikleri JSON formatında log dosyasına kaydeden bir Python servisini içermektedir. Servis, Linux ortamında çalışacak ve başlangıçta bir sistem servisi olarak yapılandırılacaktır.

Projenin Adımları
1. Sanal Makine (Opsiyonel)
Projeyi izole bir ortamda çalıştırmak isterseniz, VirtualBox, VMware veya KVM kullanarak bir sanal makine oluşturabilirsiniz.

3. Python Kurulumu
Linux üzerinde Python 3.8 veya daha güncel bir sürümün kurulu olduğundan emin olun:

sudo apt update
sudo apt install python3 python3-pip

Gerekli Python kütüphanelerini yüklemek için pip kullanabilirsiniz:
pip install watchdog

3. Log Dizini Oluşturma
Değişikliklerin kaydedileceği log dizinini oluşturun:
mkdir -p /home/user/bsm/logs
