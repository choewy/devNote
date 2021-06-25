# Linux (CentOS 7) 서버 구축

## VirtualBox 다운로드 및 설치

- VirtualBox는 Oracle에서 제공하는 무료 가상머신 실행 소프트웨어이다.

- [여기](https://download.virtualbox.org/virtualbox/6.1.22/VirtualBox-6.1.22-144080-OSX.dmg) 를 클릭하여 `VirtualBox(6.1.22 - 2021.06.03. 최신버전)`을 다운로드한다.

- 다운로드가 완료되면 설치 파일을 실행하여 VirtualBox를 설치한다.

## CentOS 7 (minimal) 다운로드

- `CentOS 7 (minimal)`은 최소한의 기능으로만 구성되어 있는 버전이다.

- [여기](http://mirror.navercorp.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso) 를 클릭하여 `CentOS 7(x86_64-Minimal-2009)`를 다운로드한다.
    
## CentOS 7 가상머신 설치

1. 새로운 가상머신 생성

    - VirtualBox를 실행하고 `새로 만들기(N)`를 클릭한다.
    
    - 아래 표를 참고하여 새로운 가상머신의 정보를 입력/설정하여 가상머신을 생성한다.

    |항목|내용|
    |------|------|
    |이름|사용할 가상머신의 이름|
    |머신 폴더|가상머신의 폴더 지정|
    |종류|Linux|
    |버전|Red Hat(64-bit)|
    |메모리|1024 MB 또는 2048 MB|
    |하드 디스크|지금 새 가상 하드 디스크 만들기|
    |하드 디스크 파일 종류|VDI(VirtualBox 디스크 이미지)|
    |물리적 하드 드라이브에 저장|동적 할당|
    |파일 위치 및 크기|파일 위치 : 가상머신의 폴더 지정<br>크기 : 최소 4GB 이상 지정|

2. 가상머신에 CentOS 7 설치

    - VirtualBox에서 생성한 새로운 가상머신을 실행한다.
    
    - 운영체제 설치를 위한 시동 디스크는 이전에 다운로드 받은 CentOS 7로 추가/선택한다.
    
    - `Install CentOS 7`을 선택하고 아래 표를 참고하여 설정 후 설치를 실행한다.
    
    |항목|내용|
    |------|------|
    |언어|한국어|
    |설치대상|로컬 표준 디스크 : 선택<br>파티션 설정 : 파티션을 자동으로 설정합니다.|
    |네트워크 & 호스트 이름|이더넷 : 켬|
    
    - ROOT 암호를 설정하여야 설치가 완료되므로 ROOT 암호를 설정한다. (사용자는 별도로 생성하지 않아도 된다.)
    
        
    
## CentOS 7 초기 설정 및 필수 패키지 설치
    
설치가 완료되면 재부팅 후 아래 표를 참고하여 CentOS 7 운영체제에 접속한다.

|항목|내용|
|------|------|
|localhost login|root|
|Password|초기 설정한 ROOT 비밀번호|

### 1. yum 업데이트

CentOS 7의 대부분 패키지는 yum을 통해 설치하므로 yum을 최신 버전으로 업데이트한다.
    
```commandline
[root@localhost ~]# yum update
   
    (생략)
   
Total download size: 236 M
Is this ok [y/d/N]: Y
   
    (생략)
   
Total
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7e
Importing GPG key 0xF4A80EB5:    
 Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>
 Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
 Package    : centos-release-7-9.2009.0.e17.centos.x86_64 (@anaconda)
 From       : /etc/pki/rpm-gpg/PRM-GPG-KEY-CentOS-7
Is this ok [y/N]: Y
```

### 2. net-tools 설치

- CentOS 7의 네트워크 정보에 접근하기 위해 `net-tools`를 설치한다.

```commandline
[root@localhost ~]# yum install net-tools
   
    (생략)

Total download size: 306 k
Installed size: 917 k
Is this ok [y/d/N]: Y
```

### 3. MariaDB 설치

- MariaDB를 설치하기 위하여 repo를 생성한다.

```commandline
[root@localhost ~]# vi /etc/yum.repos.d/MariaDB.repo
```

- 작성모드(`Alt + i`)를 통해 MariaDB 설치 정보를 입력하고, 중립모드(`Alt + ;`) + 명령모드(`Shift + ;`) + 저장 후 종료(`wq + Enter`)한다.

```commandline
[mariadb]
name=MariaDB
baseurl=http://yum.mariadb.org/10.4/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1

:wq
```

- MariaDB를 설치한다.

```commandline
[root@localhost ~]# yum install MariaDB
   
    (생략)

Total download size: 63 M
Is this ok [y/d/N]: Y
   
    (생략)

Total
Retrieving key from https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
Importing GPG key 0x1BB943DB:
 Userid     : "MariaDB Package Singing Key <package-signing-key@mariadb.org>"
 Fingerprint: 1993 69e5 404b d5fc 7d2f e43b cbcb 082a 1bb9 43db
 From       : https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
Is this ok [y/N]: Y
```

- MariaDB 버전 정보를 확인한다.
```commandline
[root@localhost ~]# rpm -qa | grep MariaDB
MariaDB-compat-10.4.19-1.el7.centos.x86_64
MariaDB-client-10.4.19-1.el7.centos.x86_64
MariaDB-common-10.4.19-1.el7.centos.x86_64
MariaDB-server-10.4.19-1.el7.centos.x86_64
```

### 4. MariaDB 초기 설정

- MariaDB 실행

```commandline
[root@localhost ~]# systemctl start mariadb
```

- 가상머신 부팅 시 MariaDB를 자동실행하도록 설정한다.

```commandline
[root@localhost ~]# systemctl enable mariadb
Created symlink from /etc/systemd/system/mysql.service to /usr/lib/systemd/syetem/mariadb.service.
Craeted symlink from /etc/systemd/system/mysqld/service to /usr/lib/systemd/syetem/mariadb.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/mariadb.service to /usr/lib/systemd/system/mariadb.service.
```

- MariaDB 자동 실행 상태를 확인한다.

```commandline
[root@localhost ~]# systemctl is-enabled mariadb
enabled
```

- MariaDB의 비밀번호를 변경한다.(본 예시에서는 `P@ssw0rd`로 변경하였음.)

```commandline
[root@localhost ~]# /usr/bin/mysqladmin -u root password 'P@ssw0rd'
```

### 5. MariaDB 외부 접속 설정

- MariaDB에 접속한다.

```commandline
[root@localhost ~]# mysql -u root -p
Enter password:

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 10.4.19-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for hele. Type '\c' to clear the current input statment.

MariaDB[(none)]>
```

- 새로운 데이베이스를 생성한다. (본 예시에서 새로운 데이터베이스명은 `main`으로 하였음.)

```commandline
MariaDB[(none)]>CREATE USER 'user'@'%' IDENTIFIED BY 'user';
```

- 외부 접속을 위해 관리자 계정을 추가한다.

```commandline
MariaDB[(none)]>CREATE USER 'root'@'%' IDENTIFIED BY 'P@ssw0rd';
```

- 관리자 계정에게 모든 데이터베이스의 접근 권한을 부여 후 새로고침하여 현재 서버에 반영한다.

```commandline
MariaDB[(none)]>GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
MariaDB[(none)]>FLUSH PRIVILEGES;
```

- 외부 접속을 허용할 새로운 사용자를 추가한다.

```commandline
MariaDB[(none)]>CREATE USER 'user'@'%' IDENTIFIED BY 'user';
```

- 새로운 사용자에게 데이터베이스 `main`의 접근 권한을 부여 후 새로고침하여 현재 서버에 반영한다.

```commandline
MariaDB[(none)]>GRANT ALL PRIVILEGES ON main.* TO 'user'@'%';
MariaDB[(none)]>FLUSH PRIVILEGES;
```

### 6. MariaDB 포트 방화벽 접근 허용 설정

- MariaDB의 기본 포트는 3306이고, 외부에서 해당 포트에 접근 가능하도록 방화벽 설정을 해주어야 한다.

```commandline
[root@localhost ~]# firewall-cmd --permanent --zone=public --add-port=3306/tcp
success
[root@localhost ~]# firewall-cmd --reload
success
[root@localhost ~]# firewall-cmd --list-ports
3306/tcp
```

## CentOS 7 원격접속 설정

- CentOS 7 원격접속을 위해 `openssh` 패키지를 설치한다.

```commandline
[root@localhost ~]# yum install -y openssh*
```

- ssh 서버를 실행한다.

```commandline
[root@localhost ~]# systemctl start sshd
```

- ssh 서버의 기본 포트는 22이고, 외부에서 해당 포트에 접근 가능하도록 방화벽 설정을 해주어야 한다.

```commandline
[root@localhost ~]# firewall-cmd --permanent --zone=public --add-port=22/tcp
success
[root@localhost ~]# firewall-cmd --reload
success
[root@localhost ~]# firewall-cmd --list-ports
3306/tcp 22/tcp
```

- 가상머신 부팅 시 ssh 서버를 자동실행하도록 설정한다.

```commandline
[root@localhost ~]# systemctl enable sshd
```

- ssh 서버 자동 실행 상태를 확인한다.

```commandline
[root@localhost ~]# systemctl is-enabled mariadb
enabled
```

- CentOS 7 IP, 포트 번호를 확인한다. (본 예시에서 IP는 `10.0.2.15`, 포트번호는 `24`이다.)

```commandline
[root@localhost ~]# ip address
   
    (생략)

2: enp0s3: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 1500 qdisc pfifo_fast stat UP
group default qlen 1000
    link/ether 08:00:27:bc:el:43 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.0.255 scope global noprefixroute dynmic enp0s3
        valid_lft 86058sec preferred_lft 86058sec
    inet6 fe80::8a99:f64c:3301:5b7d/64 scope link noprefixroute
        valid_lft forever preferred_lft forever
```

- 원격 접속을 위해서 포트포워딩을 해야 한다. VirtualBox에서 해당 가상머신에 마우스 우클릭을 하여 `설정`-`네트쿼크`-`고급`-`포트 포워딩` 화면을 열고 아래 표를 참고하여 포트포워딩 규칙을 추가한다.

|이름|프로토콜|호스트 IP|호스트 포트|게스트 IP|게스트 포트|
|---|------|:------:|------|------|------|
|MySQL|TCP|(공란)|3306|10.0.2.15|3306|
|SSH|TCP|(공란)|22|10.0.2.15|22|

- [여기](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.75-installer.msi) 를 클릭하여 원격 접속 소프트웨어인 Putty를 설치한다.

- Putty를 실행하고 아래 표를 참고하여 IP, 포트 번호를 입력 후 연결한다.

|Host Name (or IP address)|Port|Connection type|
|------|------|------|
|127.0.0.1|22|SSH|

## CentOS 7 기타 패키지 설치

### 1. Python 3 설치

- yum 업데이트 시 Python이 설치되었으므로 Python의 버전을 확인한다.

```commandline
[root@localhost ~]# python -V
python 2.7.5
[root@localhost ~]# pip -V
- bash: pip: command not found
[root@localhost ~]# python3 -V
- bash: python3: command not found
```

- Python 3가 설치되어 있지 않으므로 Python 3와 pip3를 설치한다.

```commandline
[root@localhost ~]# yum install python3
   
    (생략)

Total download size: 9.3 M
Installed size: 48 M
Is this ok [y/d/N]: Y
   
    (생략)

Complete!
[root@localhost ~]# python3 -V
Python 3.6.8
[root@localhost ~]# pip3 -V
pip 9.0.3 from /usr/lib/python3.6/site-packages (python 3.6)
```

### 2. Git 설치

- Github에 업로드한 코드를 불러오기 위하여 Git을 설치한다.

```commandline
[root@localhost ~]# yum install git
   
    (생략)

Total download size: 4.5 M
Installed size: 22 M
Is this ok [y/d/N]: y
   
    (생략)

Complete!
[root@localhost ~]# git --version
git version 1.8.3.1
```

### 3. Apache 설치

- 웹 서버를 구동하기 위한 기본적인 웹 데몬인 Apache를 설치한다.

```commandline
[root@localhost ~]# yum install httpd
   
    (생략)

Total download size: 3.0 M
installed size: 10 M
Is this ok [y/d/N]: Y

    (생략)

Complete!
[root@localhost ~]# httpd -v
Server version: Apache/2.4.6 (CentOS)
Server built: Nov 16 2020 16:18:20
```

- 외부 접속을 허용하기 위해 `httpd.conf` 파일을 아래와 같이 수정한다.

```commandline
[root@localhost ~]# vi /etc/httpd/conf/httpd.conf

    (생략)

<Directory />
    AllowOverride none
    Require all granted
</Directory>

    (생략)
```

- Apache를 실행한다.

```commandline
[root@localhost ~]# systemctl start httpd
```

- Apache 실행 상태를 확인한다.

```commandline
[root@localhost ~]# systemctl status httpd
- httpd.service - The Apache HTTP Server
    Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset
: disabled)
    Active: active (runnig) since 목  2021-06-03 15:38:48 KST; 3min 51s ago
      Docs: man:httpd(8)
            mad:apachectl(8)
 Main PID: 18094 (httpd)
    Status: "Total requests: 0; Current requests/sec: 0; Current traffic:  0 B/s
ec"
    CGroup: /system.slice/httpd.service
            -18094 /usr/sbin/httpd -DFOREGROUND
            -18095 /usr/sbin/httpd -DFOREGROUND
            -18096 /usr/sbin/httpd -DFOREGROUND
            -18097 /usr/sbin/httpd -DFOREGROUND
            -18098 /usr/sbin/httpd -DFOREGROUND
            -18099 /usr/sbin/httpd -DFOREGROUND

 6월  03 15:38:48 localhost.localdomain systemd[1]: Starting The Apache HTTP . . .
 6월  03 15:38:48 localhost.localdomain httpd[18094]: AHOO558: httpd: Could n. . .
 6월  03 15:38:48 localhost.localdomain systemd[1]: Started The Apache HTTP S. . .
Hint: Some lines were ellipsized, use -l to show in full.
```

- 가상머신 부팅 시 Apache 서버를 자동실행하도록 설정한다.

```commandline
[root@localhost ~]# systemctl enable httpd
Create syslink from /etc/systemd/system/multi-user.target.wants/httpd.service to /usr/lib/systemd/system/httpd.service.
```

- Apache 서버 자동 실행 상태를 확인한다.

```commandline
[root@localhost ~]# systemctl is-enabled httpd
enabled
```

- Apache 서버의 기본 포트는 80이고, 외부에서 해당 포트에 접근 가능하도록 방화벽 설정을 한 후 포트포워딩 규칙에 해당 포트를 추가한다.

```commandline
[root@localhost ~]# firewall-cmd --permanent --add-port=80/tcp
success

[root@localhost ~]# firewall-cmd --reload
success

[root@localhost ~]# firewall-cmd --list-ports
3306/tcp 22/tcp 80/tcp
```

- html 파일 작성 후 배포

```commandline
[root@localhost ~]# vi /var/www/html/index.html
<html>
    <body>Hello World</body>
</html>
```

### 4. Apache & Github 연동

- Github Repository Clone

```commandline
[root@localhost ~]# cd /var/www/website
[root@localhost website]# git clone https://github.com/choewy/website.git
```

- Apache 문서 폴더 변경
```commandline
[root@localhost website]# cd
[root@localhost ~]# vi /etc/httpd/conf/httpd.conf 

    (생략)

DocumentRoot "/var/www/website"

    (생략)
```
