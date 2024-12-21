# Bili-im-Sistemleri-Altyap-ve-Teknolojileri-Odevi
Bu ödevde linux ortamında çalışan bir python scripti yazdım. Bu script belli bir dizini sürekli kontrol ederek o dizinde herhangi bir değişiklik olduğunda bunu .json formatında kaydetmeli.

Aşağıda kullandığım bazı komutlar bulunuyor:
1-Dizin izleme servisi çalışıyor mu? 
systemctl status bsm.service

2-Changes.json dosyasının içi dolu mu?
cat /home/yusuf/bsm/logs/changes.json

3-Changes.json dolu ise içini temizle.
> /home/yusuf/bsm/logs/changes.json

4-Test klasörünün içine yeni dosya oluştur, düzenle ve sil.
touch /home/yusuf/bsm/test/test_file.txt
mv /home/yusuf/bsm/test/test_file.txt /home/yusuf/bsm/test/new_test_file.txt
rm /home/yusuf/bsm/test/new_test_file.txt

5-Changes.json tekrar kontrol et.
cat /home/yusuf/bsm/logs/changes.json
