Summary:	Audio mixer
Summary(pl):	Mikser audio, konkurencja dla aumiksa
Name:		ermixer
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://erevan.cuore.org/files/ermixer/%{name}-%{version}.tar.gz
# Source0-md5:	ce6e896c7c2678c98ff9d841d3504003
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
Mikser muzyczny z mas± u¿ytecznych opcji, takich jak profile, obs³uga
w czasie rzeczywistym, oferuje pe³ny interfejs mixerski. Mo¿esz u¿ywaæ
go z linii komend (przydatne w skryptach) lub skorzystaæ z interfejsu
ncurses.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

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
