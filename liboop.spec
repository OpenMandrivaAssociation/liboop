%define _requires_exceptions devel(libadns\\|devel(libtcl

%define	major 4
%define libname %mklibname oop %{major}
%define develname %mklibname oop -d

Summary:	A low-level event loop management library for POSIX-based OS'es
Name:		liboop
Version:	1.0
Release:	11
License:	LGPL
Group:		System/Libraries
URL:		http://liboop.org/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		liboop-linkage_fix.diff
# Add 8.5 and 8.6 to tcl versions configure script detects - AdamW
# 2008/12
Patch1:		liboop-1.0-tcl86.patch
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	adns-devel
BuildRequires:	glib-devel
BuildRequires:	tcl-devel

%description
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application. 

%package -n	%{libname}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:          System/Libraries

%description -n	%{libname}
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application. 

%package -n	%{develname}
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	adns-devel
Requires:	glib-devel
Provides:	oop-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname oop 4 -d}

%description -n	%{develname}
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application. 

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p1 -b .tcl86

%build
# this bit is done with automake for good reason. If you use newer
# versions, it will run fine, but the final built libraries will have
# no .so extension. Quite bizarre. - AdamW 2008/12
export WANT_AUTOCONF_2_5=1
libtoolize --copy --force; aclocal; autoconf; automake
export CFLAGS="%{optflags} -fPIC"

%configure2_5x
make

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2011.0
+ Revision: 627790
- don't force the usage of automake1.7

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2011.0
+ Revision: 620169
- the mass rebuild of 2010.0 packages

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2010.0
+ Revision: 438723
- rebuild

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-7mdv2009.1
+ Revision: 311070
- rebuild for new tcl
- add tcl86.patch (make it detect tcl 8.5 and 8.6)

* Wed Jul 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2009.0
+ Revision: 232987
- fix build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-5mdv2008.1
+ Revision: 136557
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2008.0
+ Revision: 83684
- new devel naming


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2007.0
+ Revision: 85476
- Import liboop

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2007.1
- rebuild

* Sun Jan 01 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Sun Dec 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-2mdk
- use better catching in the _requires_exceptions macro (amd64 fix)

* Mon Aug 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-1mdk
- initial mandrake package

