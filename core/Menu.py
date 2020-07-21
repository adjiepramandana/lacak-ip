#!/usr/bin/env python3
# encoding: UTF-8

"""
    This file is part of IPGeoLocation tool.
    Copyright (C) 2015-2016 @maldevel
    https://github.com/maldevel/IPGeoLocation
    
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__   = 'artzee'
__twitter__  = '@artzee'
__version__  = '3.0.8'
__year__     = '2020-2021'
__made__     = 'Remake From MALDEVEL(ENGLISH) to Indonesia '


from argparse import RawTextHelpFormatter
import argparse, os
from urllib.parse import urlparse
from core.Logger import Red


banner = """
{0} 

{1} Retdapatkan informasi Geolokasi IP dari ip-api.com
{1} Copyright (c) {2} {3} ({4})
{1} Layanan ip-api.com akan secara otomatis mencekal alamat IP yang melakukan lebih dari 150 permintaan per menit.

""".format(Red('IPGeolocation ' + __version__), Red('--['), __year__, __author__, __twitter__, __made__)


def checkFileRead(filename):
    """Check if file exists and we have access to read it"""
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        return filename
    else:
        raise argparse.ArgumentTypeError("Tidak Valid {} file (File tidak ada, izin tidak memadai atau bukan file).".format(filename))


def checkFileWrite(filename):
    """Check if we can write to file"""
    if os.path.isfile(filename):
        raise argparse.ArgumentTypeError("File {} sudah ada.".format(filename))
    elif os.path.isdir(filename):
        raise argparse.ArgumentTypeError("Folder disediakan. Harap berikan file.")
    elif os.access(os.path.dirname(filename), os.W_OK):
        return filename
    else:
        raise argparse.ArgumentTypeError("Tidak Bisa Menulis {} file (Insufficient permissions).".format(filename))
    
    
def checkProxyUrl(url):
    """Check if proxy url is valid"""
    url_checked = urlparse(url)
    if (url_checked.scheme not in ('http', 'https')) | (url_checked.netloc == ''):
        raise argparse.ArgumentTypeError('Tidak Valid {} Proxy URL (Contoh: http://127.0.0.1:8080).'.format(url))
    return url_checked


parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)
    
#pick target/s
parser.add_argument('-m', '--my-ip',  
                    dest='myip',
                    action='store_true', 
                    help='Dapatkan Lokasi IP Saya Dengan IPGeolocation')

parser.add_argument('-t', '--target',  
                    help='IP Address atau Domain untuk dipindai.')

parser.add_argument('-T', '--tlist', 
                    metavar='file',
                    type=checkFileRead, 
                    help='Daftar target IP / Domain, masing-masing target di baris baru.')


#user-agent configuration
parser.add_argument('-u', '--user-agent', 
                    metavar='User-Agent', 
                    dest='uagent',
                    default='IP2GeoLocation {}'.format(__version__), 
                    help='Tetapkan tajuk permintaan Agen Pengguna (default: IP2GeoLocation {}).'.format(__version__))

parser.add_argument('-U', '--ulist', 
                    metavar='file', 
                    type=checkFileRead, 
                    help='Tetapkan tajuk permintaan Agen Pengguna')


#misc options
parser.add_argument('-g', 
                    action='store_true', 
                    help='Buka lokasi IP di peta Google dengan browser default.')

parser.add_argument('--noprint', 
                    action='store_true', 
                    help='IPGeolocation akan mencetak info Geolokasi IP ke terminal. Dimungkinkan untuk memberi tahu IPGeolocation untuk tidak mencetak hasil ke terminal dengan opsi ini. not to print results to terminal with this option.')

parser.add_argument('-v', '--verbose', 
                    action='store_true', 
                    help='Enable verbose output.')

parser.add_argument('--nolog', 
                    action='store_true', 
                    help='IPGeolocation will save a .log file. It is possible to tell IPGeolocation not to save those log files with this option.')


#anonymity options
parser.add_argument('-x', '--proxy', 
                    type=checkProxyUrl, 
                    help='Setup proxy server (example: http://127.0.0.1:8080)')

parser.add_argument('-X', '--xlist', 
                    metavar='file', 
                    type=checkFileRead, 
                    help='A list of proxies, each proxy url in new line.')


#export options
parser.add_argument('-e', '--txt', 
                    metavar='file', 
                    type=checkFileWrite, 
                    help='Export results.')

parser.add_argument('-ec', '--csv', 
                    metavar='file', 
                    type=checkFileWrite, 
                    help='Export results in CSV format.')

parser.add_argument('-ex', '--xml', 
                    metavar='file', 
                    type=checkFileWrite, 
                    help='Export results in XML format.')


args = parser.parse_args()