#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Request-AsCGI
Version  : 1.2
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-1.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-1.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-request-ascgi-perl/libhttp-request-ascgi-perl_1.2-3.debian.tar.xz
Summary  : 'Set up a CGI environment from an HTTP::Request'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Request-AsCGI-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(URI::Escape)

%description
This archive contains the distribution HTTP-Request-AsCGI, version
1.2:
Set up a CGI environment from an HTTP::Request

%package dev
Summary: dev components for the perl-HTTP-Request-AsCGI package.
Group: Development
Provides: perl-HTTP-Request-AsCGI-devel = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Request-AsCGI package.


%package license
Summary: license components for the perl-HTTP-Request-AsCGI package.
Group: Default

%description license
license components for the perl-HTTP-Request-AsCGI package.


%prep
%setup -q -n HTTP-Request-AsCGI-1.2
cd ..
%setup -q -T -D -n HTTP-Request-AsCGI-1.2 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTTP-Request-AsCGI-1.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Request-AsCGI
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Request-AsCGI/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/HTTP/Request/AsCGI.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Request::AsCGI.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Request-AsCGI/LICENSE
