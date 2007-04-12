%define _requires_exceptions devel(libadns\\|devel(libtcl

%define	major 4
%define libname	%mklibname oop %{major}

Summary:	A low-level event loop management library for POSIX-based OS'es
Name:		liboop
Version:	1.0
Release:	%mkrel 4
URL:		http://liboop.org/
License:	LGPL
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Libraries
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	adns-devel
BuildRequires:	glib-devel
BuildRequires:	tcl tcl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Obsoletes:	%{name}
Provides:	%{name}

%description -n	%{libname}
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application. 

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
Obsoletes:	oop-devel %{name}-devel
Provides:	oop-devel %{name}-devel
Requires:	adns-devel
Requires:	glib-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
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

%build
export WANT_AUTOCONF_2_5=1
libtoolize --copy --force; aclocal-1.7; autoconf; automake-1.7

export CFLAGS="%{optflags} -fPIC"

%configure2_5x

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc


