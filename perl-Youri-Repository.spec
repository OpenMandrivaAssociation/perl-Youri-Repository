%define module	Youri-Repository

Name:		perl-%{module}
Version:	0.1.1
Release:	5
Summary:	Packages repository abstraction layer
License:	GPL or Artistic
Group:		Development/Other
Source0:	http://youri.zarb.org/download/%{module}-%{version}.tar.gz
Url:		https://youri.zarb.org
BuildRequires:	perl-devel
BuildRequires:	perl(Youri::Package::RPM::Test)
BuildRequires:	perl(version)
BuildRequires:	perl-JSON-PP
Requires:		perl(version)
BuildArch:		noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This class provides an uniform view over various kind of packages repository.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc ChangeLog README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.0-5mdv2010.0
+ Revision: 430676
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.0-4mdv2009.0
+ Revision: 268888
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-3mdv2009.0
+ Revision: 210952
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-2mdv2008.0
+ Revision: 17202
- force dependency on perl-version

* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2008.0
+ Revision: 17079
- Import perl-Youri-Repository



* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2008.0
- first mdv release 
