# IPGeoLocation
====
* Alat untuk mengambil informasi IP Geolocation
* Didukung oleh [ip-api](http://ip-api.com/docs/)


Persyaratan
=====
* Python 3.x
* termcolor
* colorama


Unduh / Instalasi
====
* git clone https://github.com/adjiepramandana/lacak-ip
* pip3 instal -r requirement.txt --user

jika pip3 tidak ada:
* apt-get install python3-setuptools
* easy_install3 pip
* pip3 instal -r requirement.txt


fitur
====
* Ambil IP atau Domain Geolokasi.
* Ambil Geolokasi IP Anda sendiri.
* Ambil Geolokasi untuk IP atau Domain yang diambil dari file. Setiap target di baris baru.
* Tetapkan string Agen Pengguna kustom Anda sendiri.
* Pilih string Agen-Pengguna acak dari file. Setiap string Agen Pengguna di baris baru.
* Dukungan proxy.
* Pilih proxy acak dari file. Setiap URL proxy di baris baru.
* Buka geolokasi IP di Google Maps menggunakan browser default.
* Ekspor hasil ke format csv, xml dan txt.


Informasi Geolokasi
====
* ASN
* Kota
* Negara
* Kode negara
* ISP
* Garis Lintang
* Longtitude
* Organisasi
* Kode Wilayah
* Nama Wilayah
* Zona waktu
* Kode Pos

Pemakaian
====
```
$ ./ip2geolocation.py
penggunaan: ipgeolocation.py [-h] [-m] [-t TARGET] [-T file] [-u Pengguna-Agen]
                        [-U file] [-g] [--noprint] [-v] [--nolog] [-x PROXY]
                        [-X file] [-e file] [-ec file] [-ex file]

IPGeolocation 2.0.4

- [Ambil informasi IP Geolokasi dari ip-api.com
- [Hak Cipta (c) 2015-2016 maldevel (@maldevel)
- [layanan ip-api.com akan secara otomatis melarang semua alamat IP yang melakukan lebih dari 150 permintaan per menit.

argumen opsional:
  -h, --help tampilkan pesan bantuan ini dan keluar
  -m, --my-ip Dapatkan info Geolokasi untuk alamat IP saya.
  -TARGET, --tARget TARGET
                        Alamat IP atau Domain yang akan dianalisis.
  File -T, file --tlist
                        Daftar target IP / Domain, masing-masing target di baris baru.
  -u Pengguna-Agen, - Pengguna-agen Pengguna-Agen
                        Tetapkan tajuk permintaan Agen Pengguna (default: IP2GeoLocation 2.0.3).
  File -U, file - daftar
                        Daftar string Agen-Pengguna, setiap string di baris baru.
  -g Buka lokasi IP di Google maps dengan browser default.
  --noprint IPGeolocation akan mencetak info IP Geolocation ke terminal. Dimungkinkan untuk memberi tahu IPGeolokasi n
atau untuk mencetak hasil ke terminal dengan opsi ini.
  -v, --verbose Mengaktifkan keluaran verbose.
  --nolog IPGeolocation akan menyimpan file .log. Dimungkinkan untuk memberi tahu IPGeolocation untuk tidak menyimpan log itu
file dengan opsi ini.
  -x PROXY, --proxy PROXY
                        Setup proxy server (contoh: http://127.0.0.1:8080)
  -X file, --xlist file
                        Daftar proxy, setiap url proxy di baris baru.
  -e file, --txt file Ekspor hasil.
  file -ec, file --csv Mengekspor hasil dalam format CSV.
  -ex file, --xml file Ekspor hasil dalam format XML.
```

Contohnya
====
** Ambil Geolokasi IP Anda **
* ./ip2geolocation.py -m

** Ambil IP Geolokasi **
* ./ip2geolocation.py -t x.x.x.x

** Ambil Geolokasi Domain **
* ./ip2geolocation.py -t example.com

** Jangan menyimpan file .log **
* ./ip2geolocation.py -t example.com --nolog

** String Agen Pengguna Khusus **
* ./ip2geolocation.py -t x.x.x.x -u "Mozilla / 5.0 (Windows NT 6.3; WOW64; Trident / 7.0; rv: 11.0) seperti Gecko"

** Menggunakan Proxy **
* ./ip2geolocation.py -t x.x.x.x -x http://127.0.0.1:8080

** Menggunakan Proxy acak **
* ./ip2geolocation.py -t x.x.x.x -X /path/to/proxies/filename.txt

** Pilih string User-Agent secara acak **
* ./ip2geolocation.py -t x.x.x.x -U /path/to/user/agent/strings/filename.txt

** Ambil geolokasi IP dan buka lokasi di Google maps dengan browser default **
* ./ip2geolocation.py -t x.x.x.x -g

** Ekspor hasil ke file CSV **
* ./ip2geolocation.py -t x.x.x.x --csv /path/to/results.csv

** Ekspor hasil ke file XML **
* ./ip2geolocation.py -t x.x.x.x --xml /path/to/results.xml

** Ekspor hasil ke file TXT **
* ./ip2geolocation.py -t x.x.x.x -e /path/to/results.txt

** Ambil IP Geolokasi untuk banyak target **
* ./ip2geolocation.py -T /path/to/targets/targets.txt

** Ambil IP Geolokasi untuk banyak target dan hasil ekspor ke xml **
* ./ip2geolocation.py -T /path/to/targets/targets.txt --xml /path/to/results.xml

** Jangan mencetak hasil ke terminal **
* ./ip2geolocation.py -m -e /path/to/results.txt --noprint
