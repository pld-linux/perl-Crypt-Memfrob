%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Memfrob
Summary:	Crypt::Memfrob Perl module - memfrob implementation in pure Perl
Summary(pl):	Modu³ Perla Crypt::Memfrob - implementacja memfrob w samym Perlu
Name:		perl-Crypt-Memfrob
Version:	1.00
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	488dd2a4bb7bdef63615d40a73ebf21b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides one function 'memfrob.' This is equivalent to
the memfrob function included in glibc. With this library, you can
generate glibc-compatible frobnicated (encrypted) strings, and
defrobnicate glibc-generated strings, in Perl.

%description -l pl
Ten pakiet zawiera jedn± funkcjê: memfrob. Jest to odpowiednik funkcji
memfrob z biblioteki glibc. Przy pomocy tej biblioteki mo¿na z poziomu
Perla generowaæ zgodne z glibc "zakodowane" ³añcuchy oraz rozkodowywaæ
³añcuchy wygenerowane przez funkcjê glibc.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/Memfrob.pm
%{_mandir}/man3/*
