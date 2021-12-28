# netpro
This repo (**Easy Streaming**) is a course project of THU 2021 Advanced Computer Network.

We use OBS to push a RTMP stream, and user can pull by FLV/DASH/HLS on web browser.

## Basic requirements
### Nginx
- stream server

we download `nginx-http-flv-module` from https://www.nginx.org.cn/plug/detail/227
```
nginx version: nginx/1.20.2
built by gcc 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04) 
built with OpenSSL 1.1.1  11 Sep 2018
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-http_gzip_static_module --http-client-body-temp-path=/var/temp/nginx/client --http-proxy-temp-path=/var/temp/nginx/proxy --http-fastcgi-temp-path=/var/temp/nginx/fastcgi --http-uwsgi-temp-path=/var/temp/nginx/uwsgi --http-scgi-temp-path=/var/temp/nginx/scgi --with-http_stub_status_module --with-http_ssl_module --with-file-aio --with-http_realip_module --add-module=../nginx-http-flv-module
```
- web server
we install pcre/openssl/zlib from source and build nginx with them
```
nginx version: nginx/1.20.1
built by gcc 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) 
built with OpenSSL 1.1.1l  24 Aug 2021
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-http_gzip_static_module --http-client-body-temp-path=/var/temp/nginx/client --http-proxy-temp-path=/var/temp/nginx/proxy --http-fastcgi-temp-path=/var/temp/nginx/fastcgi --http-uwsgi-temp-path=/var/temp/nginx/uwsgi --http-scgi-temp-path=/var/temp/nginx/scgi --with-http_stub_status_module --with-http_ssl_module --with-file-aio --with-http_realip_module --add-module=../nginx-http-flv-module --with-pcre=../pcre-8.38 --with-openssl=../openssl-1.1.1l --with-zlib=../zlib-1.2.11
```
### Python

We create this virtual environment with conda, here is the output of `conda list -e`
```
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: linux-64
_libgcc_mutex=0.1=main
_openmp_mutex=4.5=1_gnu
ca-certificates=2021.10.26=h06a4308_2
certifi=2021.10.8=py37h06a4308_0
click=8.0.3=pyhd3eb1b0_0
dataclasses=0.8=pyh6d0b6a4_7
flask=2.0.2=pyhd3eb1b0_0
itsdangerous=2.0.1=pyhd3eb1b0_0
jinja2=3.0.2=pyhd3eb1b0_0
ld_impl_linux-64=2.35.1=h7274673_9
libffi=3.3=he6710b0_2
libgcc-ng=9.3.0=h5101ec6_17
libgomp=9.3.0=h5101ec6_17
libstdcxx-ng=9.3.0=hd4cf53a_17
markupsafe=2.0.1=py37h27cfd23_0
ncurses=6.3=h7f8727e_2
openssl=1.1.1l=h7f8727e_0
pip=21.2.2=py37h06a4308_0
python=3.7.11=h12debd9_0
readline=8.1=h27cfd23_0
setuptools=58.0.4=py37h06a4308_0
sqlite=3.36.0=hc218d9a_0
tk=8.6.11=h1ccaba5_0
werkzeug=2.0.2=pyhd3eb1b0_0
wheel=0.37.0=pyhd3eb1b0_1
xz=5.2.5=h7b6447c_0
zlib=1.2.11=h7b6447c_3
```
## Modify urls to run
push url:
- RTMP: rtmp://your.stream.server.ip:1935/live/

pull usl:
- FLV : http://your.stream.server.ip:8080/live?&app=live&stream=your_key
- HLS : http://your.stream.server.ip:8080/hls/your_key.m3u8
- DASH: http://your.stream.server.ip:8080/dash/your_key.mpd

## Folder Structure
```
.
├── back_end
│   ├── README.md
│   └── webapp
│       ├── app.py
│       ├── static
│       │   ├── css
│       │   └── js
│       └── templates
│           ├── dash.html
│           ├── flv.html
│           ├── hls.html
│           └── index.html
├── front_end
│   └── README.md
├── nginx_conf
│   ├── stream_server
│   │   ├── conf.d
│   │   │   ├── netpro.conf
│   │   │   └── rtmp.d
│   │   │       └── netpro.conf
│   │   └── nginx.conf
│   └── web_server
│       ├── conf.d
│       │   ├── netpro.conf
│       │   └── rtmp.d
│       │       └── netpro.conf
│       └── nginx.conf
└── README.md
```