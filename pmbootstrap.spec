Summary:	Tool to develop and install postmarketOS
Name:		pmbootstrap
Version:	1.51.0
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://gitlab.com/postmarketOS/pmbootstrap/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	aa1513b049282ce6d4e58c563e3933ae
URL:		https://wiki.postmarketos.org/wiki/Pmbootstrap
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	git-core
Requires:	python3 >= 1:3.6
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sophisticated chroot/build/flash tool to develop and install
postmarketOS.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/pmbootstrap
%{py3_sitescriptdir}/pmb
%{py3_sitescriptdir}/pmbootstrap-%{version}-py3*.egg-info
