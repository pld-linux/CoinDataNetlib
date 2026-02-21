Summary:	COIN-OR Netlib models
Summary(pl.UTF-8):	Modele Netlib z projektu COIN-OR
Name:		CoinDataNetlib
Version:	1.2.9
Release:	1
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://www.coin-or.org/download/source/Data/Data-Netlib-%{version}.tgz
# Source0-md5:	5850144bede2cd9187197a90e8d8d3a8
URL:		https://projects.coin-or.org/svn/Data/Netlib
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	zlib-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
COIN-OR Netlib models.

%description -l pl.UTF-8
Modele Netlib z projektu COIN-OR.

%prep
%setup -q -n Data-Netlib-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfiglibdir=%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/coin/Data/Netlib
%{_npkgconfigdir}/coindatanetlib.pc
