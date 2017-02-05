%define major 0
%define libname %mklibname oath %{major}
%define develname %mklibname oath -d

Name:		oath-toolkit
Version:	2.6.2
Release:	1
License:	GPLv3+
Summary:	OATH Toolkit is a software toolkit for using HOTP/TOTP schemes
URL:		http://www.nongnu.org/oath-toolkit
Group:		System/Base
Source:		https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	gengetopt
BuildRequires:	gtk-doc-mkpdf
BuildRequires:	help2man
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(xmlsec1)
BuildRequires:	pkgconfig(xmlsec1-openssl)

%description
The OATH Toolkit contains a shared library, a command line tool and a PAM
module that makes it possible to implement one-time password authentication
systems. Supported technologies include the event-based HOTP algorithm and the
time-based TOTP algorithm. OATH stands for Open AuTHentication, a community
behind the specification. Please see RFC 4226 for further information.

The components included in the package are:

* liboath: A shared and static C library for OATH handling.
* oathtool: A command line tool for generating and validating OTPs.
* pam_oath: A PAM module for pluggable login authentication for OATH.

%files
%doc ChangeLog README COPYING
%{_bindir}/oathtool
%{_mandir}/man1/oathtool.*.*

#----------------------------------------------------------------------------

%package -n pam_oath
Summary:	A PAM module for HOTP/TOTP one-time password authentication
Group:		System/Libraries

%description -n pam_oath
A PAM module for HOTP/TOTP one-time password authentication.

%files -n pam_oath
%defattr(-,root,root)
/%{_lib}/security/pam_oath.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A library implementing HOTP/TOTP one-time password authentication schemes
Group:		System/Libraries

%description -n %{libname}
A library implementing HOTP/TOTP one-time password authentication schemes.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liboath.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files and documentation for liboath
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description -n %{develname}
Development files and documentation for liboath.

%files -n %{develname}
%{_libdir}/liboath.so
%dir %{_includedir}/liboath
%{_includedir}/liboath/oath.h
%{_libdir}/pkgconfig/liboath.pc
%dir %{_datadir}/gtk-doc/html/liboath
%doc %{_datadir}/gtk-doc/html/liboath/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
make

%install
%makeinstall_std

%check
%make check

%changelog
* Thu May 05 2011 Dimitri Teleguin <mitya@mandriva.org> 1.8.2-1mdv2011.0
+ Revision: 668019
- import oath-toolkit


