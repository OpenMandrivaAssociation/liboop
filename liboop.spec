%define major 4
%define major0 0
%define major3 3
%define libname %mklibname oop %{major}
%define libadns %mklibname oop-adns %{major3}
%define libglib %mklibname oop-glib %{major0}
%define libglib2 %mklibname oop-glib2 %{major0}
%define librl %mklibname oop-rl %{major0}
%define libtcl %mklibname oop-tcl %{major0}
%define devname %mklibname oop -d

Summary:	A low-level event loop management library for POSIX-based OS'es
Name:		liboop
Version:	1.0
Release:	12
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://liboop.org/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		liboop-linkage_fix.diff
# Add 8.5 and 8.6 to tcl versions configure script detects - AdamW 2008/12
Patch1:		liboop-1.0-tcl86.patch
BuildRequires:	libtool
BuildRequires:	adns-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(glib)
BuildRequires:	pkgconfig(glib-2.0)

%description
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:		System/Libraries

%description -n %{libname}
Liboop is a low-level event loop management library for POSIX-based
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application.

%files -n %{libname}
%{_libdir}/liboop.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libadns}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:		System/Libraries
Conflicts:	%{_lib}oop4 < 1.0-12

%description -n %{libadns}
Shared library for %{name}.

%files -n %{libadns}
%{_libdir}/liboop-adns.so.%{major3}*

#----------------------------------------------------------------------------

%package -n %{libglib}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:		System/Libraries
Conflicts:	%{_lib}oop4 < 1.0-12

%description -n %{libglib}
Shared library for %{name}.

%files -n %{libglib}
%{_libdir}/liboop-glib.so.%{major0}*

#----------------------------------------------------------------------------

%package -n %{libglib2}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:		System/Libraries
Conflicts:	%{_lib}oop4 < 1.0-12

%description -n %{libglib2}
Shared library for %{name}.

%files -n %{libglib2}
%{_libdir}/liboop-glib2.so.%{major0}*

#----------------------------------------------------------------------------

%package -n %{librl}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:		System/Libraries
Conflicts:	%{_lib}oop4 < 1.0-12

%description -n %{librl}
Shared library for %{name}.

%files -n %{librl}
%{_libdir}/liboop-rl.so.%{major0}*

#----------------------------------------------------------------------------

%package -n %{libtcl}
Summary:	A low-level event loop management library for POSIX-based OS'es
Group:		System/Libraries
Conflicts:	%{_lib}oop4 < 1.0-12

%description -n %{libtcl}
Shared library for %{name}.

%files -n %{libtcl}
%{_libdir}/liboop-tcl.so.%{major0}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libadns} = %{EVRD}
Requires:	%{libglib} = %{EVRD}
Requires:	%{libglib2} = %{EVRD}
Requires:	%{librl} = %{EVRD}
Requires:	%{libtcl} = %{EVRD}
Provides:	oop-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Liboop is a low-level event loop management library for POSIX-based
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application.

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .tcl86

%build
%global optflags %{optflags} -fPIC
libtoolize --copy --force; aclocal; autoconf; automake
%configure2_5x --disable-static
make

%install
%makeinstall_std

