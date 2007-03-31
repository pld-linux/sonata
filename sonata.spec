#
Summary:	GTK2 for MPD
Name:		sonata
Version:	1.0.1
Release:	1
License:	GPLv2?
Group:		Applications
Source0:	http://download.berlios.de/sonata/%{name}-%{version}.tar.bz2
# Source0-md5:	aa7dd98cf31d719328adf7afba4c0c83
URL:		http://sonata.berlios.de/
BuildRequires:	python-pygtk-devel >= 2:2.6.0
Requires:	python-SOPE
#Requires:	python-taglib # NFY
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO CHANGELOG TRANSLATORS
%attr(755,root,root) %{_bindir}/sonata
%{py_sitedir}/Sonata-1.0.1-py2.5.egg-info
%{py_sitedir}/mmkeys.so
%{py_sitedir}/mpdclient3.py
%{py_sitedir}/mpdclient3.pyc
%{py_sitedir}/mpdclient3.pyo
%{py_sitedir}/sonata.py
%{py_sitedir}/sonata.pyc
%{py_sitedir}/sonata.pyo
%{_desktopdir}/sonata.desktop
%{_pixmapsdir}/sonata-album.png
%{_pixmapsdir}/sonata-artist.png
%{_pixmapsdir}/sonata.png
%{_pixmapsdir}/sonata_large.png
%{_pixmapsdir}/sonatacd.png
%{_pixmapsdir}/sonatacd_large.png
