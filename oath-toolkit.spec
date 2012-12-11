%define major 0
%define libname %mklibname oath %{major}
%define develname %mklibname oath -d

Name:		oath-toolkit
Version:	1.8.2
Release:	%mkrel 1
License:	GPLv3
Summary:	OATH Toolkit is a software toolkit for using HOTP/TOTP schemes
URL:		http://www.nongnu.org/oath-toolkit
Group:		System/Base
Source:		http://download.savannah.nongnu.org/releases/oath-toolkit/oath-toolkit-%{version}.tar.gz
BuildRequires:	pam-devel pkgconfig

%description
The OATH Toolkit contains a shared library, a command line tool and a PAM module
that makes it possible to implement one-time password authentication systems.
Supported technologies include the event-based HOTP algorithm and the
time-based TOTP algorithm. OATH stands for Open AuTHentication, a community
behind the specification. Please see RFC 4226 for further information.

The components included in the package are:

* liboath: A shared and static C library for OATH handling.
* oathtool: A command line tool for generating and validating OTPs.
* pam_oath: A PAM module for pluggable login authentication for OATH.

%package -n pam_oath
Summary:	A PAM module for HOTP/TOTP one-time password authentication
Group:		System/Libraries

%description -n pam_oath
A PAM module for HOTP/TOTP one-time password authentication.

%package -n %{libname}
Summary:	A library implementing HOTP/TOTP one-time password authentication schemes
Group:		System/Libraries

%description -n %{libname}
A library implementing HOTP/TOTP one-time password authentication schemes.

%package -n %{develname}
Summary:	Development files and documentation for liboath
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description -n %{develname}
Development files and documentation for liboath.

%prep
%setup -q

%build
%configure2_5x --with-pam-dir=/%{_lib}/security \
	    --disable-static \
	    --with-pic

%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std
%{__rm} -rf %{buildroot}/%{_libdir}/liboath.la

%check
make check

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_bindir}/oathtool
%{_mandir}/man1/oathtool.*.*

%files -n pam_oath
%defattr(-,root,root)
/%{_lib}/security/pam_oath.so

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liboath.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/liboath.so
%dir %{_includedir}/liboath
%{_includedir}/liboath/oath.h
%{_libdir}/pkgconfig/liboath.pc
%dir %{_datadir}/gtk-doc/html/liboath
%doc %{_datadir}/gtk-doc/html/liboath/*



%changelog
* Thu May 05 2011 Dimitri Teleguin <mitya@mandriva.org> 1.8.2-1mdv2011.0
+ Revision: 668019
- import oath-toolkit


