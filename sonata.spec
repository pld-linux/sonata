Summary:	GTK+ music client for MPD
Summary(pl.UTF-8):	Oparty na GTK+ klient muzyki dla MPD
Name:		sonata
Version:	1.0.1
Release:	1
License:	GPLv2?
Group:		Applications
Source0:	http://download.berlios.de/sonata/%{name}-%{version}.tar.bz2
# Source0-md5:	aa7dd98cf31d719328adf7afba4c0c83
URL:		http://sonata.berlios.de/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.6.0
BuildRequires:	rpm-pythonprov
Requires:	python-SOPE
#Requires:	python-taglib # NFY
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sonata is an elegant GTK+ music client for the Music Player Daemon
(MPD).

%description -l pl.UTF-8
Sonata to elegancki, oparty na GTK+ klient muzyki dla demona MPD
(Music Player Daemon).

%prep
%setup -q

%build
python setup.py build

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO CHANGELOG TRANSLATORS
%attr(755,root,root) %{_bindir}/sonata
%{py_sitedir}/Sonata-1.0.1-py*.egg-info
%attr(755,root,root) %{py_sitedir}/mmkeys.so
%{py_sitedir}/mpdclient3.py[co]
%{py_sitedir}/sonata.py
%{py_sitedir}/sonata.py[co]
%{_desktopdir}/sonata.desktop
%{_pixmapsdir}/sonata-album.png
%{_pixmapsdir}/sonata-artist.png
%{_pixmapsdir}/sonata.png
%{_pixmapsdir}/sonata_large.png
%{_pixmapsdir}/sonatacd.png
%{_pixmapsdir}/sonatacd_large.png
