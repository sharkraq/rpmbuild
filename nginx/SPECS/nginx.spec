%define _topdir     /var/lib/jenkins/workspace/Nginx-Linux-RPM/nginx
%define name        nginx 
%define release        1
%define version     1.16.0
%define buildroot %{_topdir}/%{name}‑%{version}‑root

BuildRoot:    %{buildroot}
Summary:         AIR nginx
License:         GPL
Name:             %{name}
Version:         %{version}
Release:         %{release}
Source0:	nginx-1.16.0.tar.gz 
Source1:	openssl-1.1.1.tar.gz
Source2:	pcre-8.43.tar.gz
Source3:	zlib-1.2.11.tar.gz
Prefix:         /usr
Group:          AIR Development



#Requires: screen nmap openvpn PyYAML python-pycurl dialog jwhois bind-utils hping tcptraceroute       

%description
Nginx Reverse Proxy

%prep 
%setup -q

tar zxvf %{SOURCE0} -C %{_topdir}/BUILD
tar zxvf %{SOURCE1} -C %{_topdir}/BUILD
tar zxvf %{SOURCE2} -C %{_topdir}/BUILD
tar zxvf %{SOURCE3} -C %{_topdir}/BUILD

%build
./configure \
    --with-http_ssl_module \
    --with-openssl=%{_topdir}/BUILD/openssl-1.1.1 \
    --with-pcre=%{_topdir}/BUILD/pcre-8.43 \
    --with-zlib=%{_topdir}/BUILD/zlib-1.2.11
    make

%pre
#if [[ $1 = 1 ]]; then
#echo "Initial Install"  
#elif [[ $1 = 2 ]]; then
#echo "Starting update"
# Check if scans are running.
#SCANSDIR="/scanner/tmp/reports"
#if [ "$(ls -A $SCANSDIR)" ]; then
#echo "Scan in progress...Exiting Update"
#exit 1
#else
#echo "No scans detected"
#fi

%install
make install prefix=%{buildroot}/usr

%files
%defattr(‑,root,root)
/usr/local/nginx/sbin/nginx

%doc

%clean

%post


%preun
#if [[ $1 = 0 ]]; then
#echo "Removing rpm"  
#mv %{prefix}
#service  nexposeengine.rc stop
#/opt/rapid7/nexpose/.install4j/uninstall << EOF
#y
#EOF
#fi
%postun

#%changelog
#* Thursday May 16 2019 <malvarenga@air-worldwide.com> 
#- Initial Build.

