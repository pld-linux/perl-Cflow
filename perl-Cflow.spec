%include	/usr/lib/rpm/macros.perl
Summary:	Cflow perl module
Summary(pl):	Modu³ perla Cflow
Name:		perl-Cflow
Version:	1.040
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	http://net.doit.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.gz
URL:		http://net.doit.wisc.edu/~plonka/Cflow/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cflow is a perl module providing an API for reading and analyzing raw
flow files written by freely-available software packages such as
CAIDA's cflowd, OSU flow-tools and lfapd which collect IP flow export
information from routers.

%description -l pl
Modu³ perla Cflow.

%prep
%setup -q -n Cflow-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/*.pm
%dir %{perl_sitearch}/auto/Cflow
%attr(755,root,root) %{perl_sitearch}/auto/Cflow/Cflow.so
%{_mandir}/man?/*
