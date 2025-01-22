#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-HTTP-Request-AsCGI
Version  : 1.2
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-1.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-1.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-request-ascgi-perl/libhttp-request-ascgi-perl_1.2-3.debian.tar.xz
Summary  : 'Set up a CGI environment from an HTTP::Request'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Request-AsCGI-license = %{version}-%{release}
Requires: perl-HTTP-Request-AsCGI-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(URI::Escape)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution HTTP-Request-AsCGI, version
1.2:
Set up a CGI environment from an HTTP::Request

%package dev
Summary: dev components for the perl-HTTP-Request-AsCGI package.
Group: Development
Provides: perl-HTTP-Request-AsCGI-devel = %{version}-%{release}
Requires: perl-HTTP-Request-AsCGI = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Request-AsCGI package.


%package license
Summary: license components for the perl-HTTP-Request-AsCGI package.
Group: Default

%description license
license components for the perl-HTTP-Request-AsCGI package.


%package perl
Summary: perl components for the perl-HTTP-Request-AsCGI package.
Group: Default
Requires: perl-HTTP-Request-AsCGI = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Request-AsCGI package.


%prep
%setup -q -n HTTP-Request-AsCGI-1.2
cd %{_builddir}
tar xf %{_sourcedir}/libhttp-request-ascgi-perl_1.2-3.debian.tar.xz
cd %{_builddir}/HTTP-Request-AsCGI-1.2
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTTP-Request-AsCGI-1.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Request-AsCGI
cp %{_builddir}/HTTP-Request-AsCGI-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Request-AsCGI/674378819f8d4b269c32274d072b0b0757529b27 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-Request-AsCGI/4734ab822a897959b2ebefd74ad5fdd31b7b54fc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Request::AsCGI.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Request-AsCGI/4734ab822a897959b2ebefd74ad5fdd31b7b54fc
/usr/share/package-licenses/perl-HTTP-Request-AsCGI/674378819f8d4b269c32274d072b0b0757529b27

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
