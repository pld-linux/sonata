Summary:	GTK+ music client for MPD
Summary(pl.UTF-8):	Oparty na GTK+ klient muzyki dla MPD
Name:		sonata
Version:	1.6.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Sound
Source0:	http://download.berlios.de/sonata/%{name}-%{version}.tar.bz2
# Source0-md5:	f2bca0855fd2eb3d199f62fbd88af62f
Patch0:		%{name}-el.patch
URL:		http://sonata.berlios.de/
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygobject-devel
BuildRequires:	python-pygtk-devel >= 2:2.6.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-mpd
Requires:	python-modules
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-pygtk-pango
Requires:	python-pygobject
Suggests:	python-dbus
Suggests:	python-gnome
Suggests:	python-gnome-ui
Suggests:	python-ZSI
Suggests:	python-tagpy
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
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
%{_mandir}/man1/sonata.1*
%dir %{py_sitedir}/sonata
%dir %{py_sitedir}/sonata/plugins
%{py_sitedir}/sonata/__init__.py[co]
%{py_sitedir}/sonata/about.py[co]
%{py_sitedir}/sonata/artwork.py[co]
%{py_sitedir}/sonata/audioscrobbler.py[co]
%{py_sitedir}/sonata/breadcrumbs.py[co]
%{py_sitedir}/sonata/cli.py[co]
%{py_sitedir}/sonata/config.py[co]
%{py_sitedir}/sonata/consts.py[co]
%{py_sitedir}/sonata/current.py[co]
%{py_sitedir}/sonata/dbus_plugin.py[co]
%{py_sitedir}/sonata/img.py[co]
%{py_sitedir}/sonata/info.py[co]
%{py_sitedir}/sonata/library.py[co]
%{py_sitedir}/sonata/main.py[co]
%{py_sitedir}/sonata/misc.py[co]
%{py_sitedir}/sonata/mpdhelper.py[co]
%{py_sitedir}/sonata/playlists.py[co]
%{py_sitedir}/sonata/pluginsystem.py[co]
%{py_sitedir}/sonata/preferences.py[co]
%{py_sitedir}/sonata/scrobbler.py[co]
%{py_sitedir}/sonata/streams.py[co]
%{py_sitedir}/sonata/svnversion.py[co]
%{py_sitedir}/sonata/tagedit.py[co]
%{py_sitedir}/sonata/tray.py[co]
%{py_sitedir}/sonata/ui.py[co]
%{py_sitedir}/sonata/version.py[co]
%{py_sitedir}/sonata/plugins/__init__.py[co]
%{py_sitedir}/sonata/plugins/localmpd.py[co]
%{py_sitedir}/sonata/plugins/test.py[co]
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
