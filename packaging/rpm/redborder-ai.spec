Name: redborder-ai
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Main package for redborder AI

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-ai
Source0: %{name}-%{version}.tar.gz

Requires: bash

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/etc/redborder
mkdir -p %{buildroot}/usr/lib/redborder/bin
cp resources/bin/* %{buildroot}/usr/lib/redborder/bin
cp llava* %{buildroot}/usr/lib/redborder/bin
chmod 0755 %{buildroot}/usr/lib/redborder/bin/*
install -D -m 0644 resources/systemd/llamafile.service %{buildroot}/usr/lib/systemd/system/llamafile.service

%pre

%post
firewall-cmd --zone=home --add-port=50505/tcp --permanent
firewall-cmd --reload
systemctl daemon-reload
systemctl enable llamafile.service
systemctl restart llamafile.service
mkdir -p /var/log/redborder-ai
[ -f /usr/lib/redborder/bin/rb_rubywrapper.sh ] && /usr/lib/redborder/bin/rb_rubywrapper.sh -c

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin
%defattr(0644,root,root)
/etc/redborder
/usr/lib/systemd/system/llamafile.service
%doc

%changelog
* Tue Jul 23 2024 Pablo Pérez <pperez@redborder.com> - 0.0.1-1
- first spec version