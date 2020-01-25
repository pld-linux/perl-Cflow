#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Cflow
Summary:	Cflow - find "interesting" flows in raw IP flow files
Summary(pl.UTF-8):	Cflow - znajdywanie "interesujących" przepływów w surowych plikach przepływów IP
Name:		perl-Cflow
Version:	1.053
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://net.doit.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.gz
# Source0-md5:	4d868045636cbda9b775e8d9e27b44e7
Patch0:		%{name}-link.patch
URL:		http://net.doit.wisc.edu/~plonka/Cflow/
BuildRequires:	flow-tools-devel >= 0.67-2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cflow is a perl module providing an API for reading and analyzing raw
flow files written by freely-available software packages such as
CAIDA's cflowd, OSU flow-tools and lfapd which collect IP flow export
information from routers.

%description -l pl.UTF-8
Cflow to moduł Perla udostępniający API do czytania i analizy surowych
plików przepływów, zapisanych przez takie wolnodostępne programy, jak
cflowd CAIDA, flow-tools OSU i lfapd, zbierających dane o przepływie
pakietów IP z ruterów.

%prep
%setup -q -n Cflow-%{version}
%patch0 -p1

%{__perl} -pi -e 's#\.\./\.\./lib/#%{_libdir}/#g' Makefile*

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Cflow
%{perl_vendorarch}/auto/Cflow/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Cflow/Cflow.so
%{_mandir}/man?/*
