%include	/usr/lib/rpm/macros.perl
Summary:	Cflow perl module
Summary(pl):	Modu³ perla Cflow
Name:		perl-Cflow
Version:	1.051
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://net.doit.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.gz
URL:		http://net.doit.wisc.edu/~plonka/Cflow/
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cflow is a perl module providing an API for reading and analyzing raw
flow files written by freely-available software packages such as
CAIDA's cflowd, OSU flow-tools and lfapd which collect IP flow export
information from routers.

%description -l pl
Cflow to modu³ perla udostêpniaj±cy API do czytania i analizy surowych
plików przep³ywów, zapisanych przez takie wolnodostêpne programy, jak
cflowd CAIDA, flow-tools OSU i lfapd, zbieraj±cych dane o przep³ywie
pakietów IP z ruterów.

%prep
%setup -q -n Cflow-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/*.pm
%{perl_sitearch}/auto/Cflow
%{_mandir}/man?/*
