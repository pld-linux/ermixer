
Summary:	Audio mixer.
Summary(pl):	Mixer audio, konkurencja dla aumix'a.
Name:		ermixer
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://erevan.cuore.org/files/ermixer/%{name}-%{version}.tar.gz
Patch0:		%{name}-curses.patch
URL:		http://ermixer.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a OSS mixer with a lot of usefull features like the handling
of multiple profiles files, real time support, it offers a complete
interface to the mixer capatibilities. You can use it with a nice
curses interface or with a command line interface (usefull for use it
in scripts).

%description -l pl
Mikser muzyczny z masa uzytecznych opcji, konkurencja dla aumix'a.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure
%{__make} CC="%{__cc} %{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
