Summary:	GTK+ music client for MPD
Summary(pl.UTF-8):	Oparty na GTK+ klient muzyki dla MPD
Name:		sonata
Version:	1.5.3
Release:	1
License:	GPLv2?
Group:		Applications
Source0:	http://download.berlios.de/sonata/%{name}-%{version}.tar.bz2
# Source0-md5:	447e46f24005de797ebc11131db1bd82
Patch0:		%{name}-el.patch
URL:		http://sonata.berlios.de/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.6.0
BuildRequires:	rpm-pythonprov
Requires:	python-mpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sonata is an elegant GTK+ music client for the Music Player Daemon
(MPD).

%description -l pl.UTF-8
Sonata to elegancki, oparty na GTK+ klient muzyki dla demona MPD
(Music Player Daemon).

%prep
%setup -q
%patch0 -p1 -b .wiget
%{__mv} po/el_GR.po po/el.po

%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT

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
%{py_sitedir}/Sonata-%{version}-py*.egg-info
%attr(755,root,root) %{py_sitedir}/mmkeys.so
%dir %{py_sitedir}/sonata
%{py_sitedir}/sonata/__init__.py[co]
%{py_sitedir}/sonata/audioscrobbler.py[co]
%{py_sitedir}/sonata/img.py[co]
%{py_sitedir}/sonata/main.py[co]
%{py_sitedir}/sonata/misc.py[co]
%{py_sitedir}/sonata/mpdhelper.py[co]
%{py_sitedir}/sonata/tray.py[co]
%{py_sitedir}/sonata/ui.py[co]
%{_desktopdir}/sonata.desktop
%{_pixmapsdir}/sonata-album.png
%{_pixmapsdir}/sonata-artist.png
%{_pixmapsdir}/sonata-case.png
%{_pixmapsdir}/sonata-stock_volume-max.png
%{_pixmapsdir}/sonata-stock_volume-med.png
%{_pixmapsdir}/sonata-stock_volume-min.png
%{_pixmapsdir}/sonata-stock_volume-mute.png
%{_pixmapsdir}/sonata.png
%{_pixmapsdir}/sonata_disconnect.png
%{_pixmapsdir}/sonata_large.png
%{_pixmapsdir}/sonata_pause.png
%{_pixmapsdir}/sonata_play.png
%{_pixmapsdir}/sonatacd.png
%{_pixmapsdir}/sonatacd_large.png
