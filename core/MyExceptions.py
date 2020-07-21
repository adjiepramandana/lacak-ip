#!/usr/bin/env python3
# encoding: UTF-8

"""
   File ini adalah bagian dari alat IPGeoLocation.
    Hak Cipta (C) 2015-2016 @maldevel
    https://github.com/maldevel/IPGeoLocation
    
    IPGeoLocation - Ambil informasi Geolokasi IP
    Didukung oleh http://ip-api.com
    
    Program ini adalah perangkat lunak gratis: Anda dapat mendistribusikan dan / atau memodifikasi
    berdasarkan ketentuan Lisensi Publik Umum GNU yang diterbitkan oleh
    Yayasan Perangkat Lunak Bebas, baik versi 3 dari Lisensi, atau
    (sesuai pilihan Anda) versi yang lebih baru.

    Program ini didistribusikan dengan harapan akan bermanfaat,
    tapi TANPA GARANSI APA PUN; bahkan tanpa jaminan tersirat dari
    PERDAGANGAN atau KESESUAIAN UNTUK TUJUAN TERTENTU. Lihat
    Lisensi Publik Umum GNU untuk perincian lebih lanjut.

    Anda seharusnya telah menerima salinan Lisensi Publik Umum GNU
    bersama dengan program ini. Jika tidak, lihat <http://www.gnu.org/licenses/>.
    
    Untuk lebih lanjut lihat file 'LICENSE' untuk izin menyalin.
"" "

__author__ = 'artzee'


class UserAgentFileEmptyError(Exception):
    pass

class InvalidTargetError(Exception):
    pass

class TargetsFileEmptyError(Exception):
    pass

class TargetsFileNotSpecifiedError(Exception):
    pass

class UserAgentFileNotSpecifiedError(Exception):
    pass

class ProxyServerNotReachableError(Exception):
    pass

class ProxiesFileNotSpecifiedError(Exception):
    pass

class ProxiesFileEmptyError(Exception):
    pass

class InvalidProxyUrlError(Exception):
    pass