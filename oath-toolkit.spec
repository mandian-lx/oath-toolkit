%define major 0

%define oathlibname %mklibname oath %{major}
%define oathdevname %mklibname oath -d

%define pskclibname %mklibname pskc %{major}
%define pskcdevname %mklibname pskc -d

Summary:	OATH Toolkit is a software toolkit for using HOTP/TOTP schemes
Name:		oath-toolkit
Version:	2.6.2
Release:	1
Group:		System/Base
License:	GPLv3+
URL:		http://www.nongnu.org/oath-toolkit
Source:		https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	gengetopt
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-mkpdf
BuildRequires:	help2man
BuildRequires:	libxml2-utils
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(xmlsec1)
BuildRequires:	pkgconfig(xmlsec1-openssl)

%description
The OATH Toolkit makes it easy to build one-time password authentication
systems. It contains shared libraries, command line tools and a PAM module.
Supported technologies include the event-based HOTP algorithm (RFC4226) and
the time-based TOTP algorithm (RFC6238). OATH stands for Open
AuTHentication, which is the organization that specify the algorithms. For
managing secret key files, the Portable Symmetric Key Container (PSKC)
format described in RFC6030 is supported.

The components included in the toolkit are:

  * liboath:  A C library for OATH handling.
  * oathtool: A command line tool for generating and validating OTPs.
  * pam_oath: A PAM module for pluggable login authentication for OATH.
  * libpskc:  A C library for PSKC handling.
  * pskctool: A command line tool for manipulating PSKC data.

This package contains the command line tools.

%files
%{_bindir}/oathtool
%{_bindir}/pskctool
%{_mandir}/man1/oathtool.1.*
%{_mandir}/man1/pskctool.1.*
%doc README
%doc ChangeLog
%doc oathtool/COPYING

#----------------------------------------------------------------------------

%package -n pam_oath
Summary:	A PAM module for pluggable login authentication for OATH
Group:		System/Libraries

%description -n pam_oath
The OATH Toolkit makes it easy to build one-time password authentication
systems. It contains shared libraries, command line tools and a PAM module.
Supported technologies include the event-based HOTP algorithm (RFC4226) and
the time-based TOTP algorithm (RFC6238). OATH stands for Open
AuTHentication, which is the organization that specify the algorithms. For
managing secret key files, the Portable Symmetric Key Container (PSKC)
format described in RFC6030 is supported.

The components included in the toolkit are:

  * liboath:  A C library for OATH handling.
  * oathtool: A command line tool for generating and validating OTPs.
  * pam_oath: A PAM module for pluggable login authentication for OATH.
  * libpskc:  A C library for PSKC handling.
  * pskctool: A command line tool for manipulating PSKC data.

This package contains the PAM module.

%files -n pam_oath
%{_libdir}/security/pam_oath.so
%doc pam_oath/README
%doc pam_oath/COPYING

#----------------------------------------------------------------------------

%package -n %{oathlibname}
Summary:	A library for OATH handling
License:	LGPLv2.1+
Group:		System/Libraries

%description -n %{oathlibname}
The OATH Toolkit makes it easy to build one-time password authentication
systems. It contains shared libraries, command line tools and a PAM module.
Supported technologies include the event-based HOTP algorithm (RFC4226) and
the time-based TOTP algorithm (RFC6238). OATH stands for Open
AuTHentication, which is the organization that specify the algorithms. For
managing secret key files, the Portable Symmetric Key Container (PSKC)
format described in RFC6030 is supported.

The components included in the toolkit are:

  * liboath:  A C library for OATH handling.
  * oathtool: A command line tool for generating and validating OTPs.
  * pam_oath: A PAM module for pluggable login authentication for OATH.
  * libpskc:  A C library for PSKC handling.
  * pskctool: A command line tool for manipulating PSKC data.

This package contains the library for OATH handling.

%files -n %{oathlibname}
%{_libdir}/liboath.so.%{major}*
%{_mandir}/man3/oath_*.3.*
%doc liboath/COPYING

#----------------------------------------------------------------------------

%package -n %{oathdevname}
Summary:	Development files and documentation for liboath
Group:		System/Libraries
Requires:	%{oathlibname} = %{version}

%description -n %{oathdevname}
Headers, development and documentation for libpoath.

%files -n %{oathdevname}
%dir %{_includedir}/liboath
%{_includedir}/liboath/oath.h
%{_libdir}/liboath.so
%{_libdir}/pkgconfig/liboath.pc
%dir %{_datadir}/gtk-doc/html/liboath
%doc %{_datadir}/gtk-doc/html/liboath/*
%doc liboath/COPYING

#----------------------------------------------------------------------------

%package -n %{pskclibname}
Summary:	A library for PSKC handling
License:	LGPLv2.1+
Group:		System/Libraries

%description -n %{pskclibname}
The OATH Toolkit makes it easy to build one-time password authentication
systems. It contains shared libraries, command line tools and a PAM module.
Supported technologies include the event-based HOTP algorithm (RFC4226) and
the time-based TOTP algorithm (RFC6238). OATH stands for Open
AuTHentication, which is the organization that specify the algorithms. For
managing secret key files, the Portable Symmetric Key Container (PSKC)
format described in RFC6030 is supported.

The components included in the toolkit are:

  * liboath:  A C library for OATH handling.
  * oathtool: A command line tool for generating and validating OTPs.
  * pam_oath: A PAM module for pluggable login authentication for OATH.
  * libpskc:  A C library for PSKC handling.
  * pskctool: A command line tool for manipulating PSKC data.

This package contains the library for PSKC handling.

%files -n %{pskclibname}
%{_libdir}/libpskc.so.%{major}*
%dir %{_datadir}/xml/pskc
%{_datadir}/xml/pskc/*
%{_mandir}/man3/pskc_*.3.*
%doc liboath/COPYING

#----------------------------------------------------------------------------

%package -n %{pskcdevname}
Summary:	Development files and documentation for libpskc
License:	LGPLv2.1+
Group:		System/Libraries
Requires:	%{pskclibname} = %{version}

%description -n %{pskcdevname}
Headers, development and documentation for libpskc.

%files -n %{pskcdevname}
%dir %{_includedir}/pskc
%{_includedir}/pskc/*
%{_libdir}/libpskc.so
%{_libdir}/pkgconfig/libpskc.pc
%dir %{_datadir}/gtk-doc/html/libpskc
%doc %{_datadir}/gtk-doc/html/libpskc/*
%doc libpskc/README
%doc liboath/COPYING

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --with-pam-dir=%{_libdir}/security --disable-static
#NOTE: parallel may break compilation
make

%install
%makeinstall_std

%check
%make check

%changelog
* Thu May 05 2011 Dimitri Teleguin <mitya@mandriva.org> 1.8.2-1mdv2011.0
+ Revision: 668019
- import oath-toolkit

