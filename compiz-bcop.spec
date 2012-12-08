%define shortname bcop
%define name compiz-bcop
%define version 0.8.4
%define rel 4
%define git 0

%if  %{git}
%define srcname %{shortname}-%{git}.tar.lzma
%define distname %{shortname}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: BCOP: Compiz Fusion plugin build utility
Group: System/X11
URL: http://www.go-compiz.org/
Source: %{srcname}
License: GPL
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxslt-devel
Requires: libxslt-proc
Obsoletes: %{shortname}

%description
BCOP: Compiz Fusion plugin build utility

%prep
%setup -q -n %{distname}

%build
%if %{git}
  # This is a CVS snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{shortname}
%dir %{_datadir}/%{shortname}
%{_datadir}/%{shortname}/%{shortname}.xslt
%{_datadir}/pkgconfig/%{shortname}.pc


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-4mdv2011.0
+ Revision: 663394
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-3mdv2011.0
+ Revision: 603844
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-2mdv2010.1
+ Revision: 522390
- rebuilt for 2010.1

* Thu Oct 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-1mdv2010.0
+ Revision: 457725
- New version: 0.8.4

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2010.0
+ Revision: 413261
- rebuild

* Sun Mar 15 2009 Emmanuel Andry <eandry@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 355361
- New version 0.8.2

* Sun Feb 08 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-0.20090208.1mdv2009.1
+ Revision: 338484
- 0.8 pre-release snapshot

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.8-0.20080713.1mdv2009.0
+ Revision: 284295
- Bump version in anticipation of full release

* Sun Jul 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.7-0.20080713.1mdv2009.0
+ Revision: 234338
- New snapshot
- New version: 0.7.6

* Tue Apr 08 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.4-1mdv2009.0
+ Revision: 192366
- New version 0.7.4

* Fri Mar 07 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 181114
- New version 0.7.2

* Mon Feb 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.99-0.20080210.1mdv2008.1
+ Revision: 172290
- Update to git master for new Compiz Fusion

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 100719
- New upstream release: 0.6.0

* Mon Aug 13 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 62610
- Rename package to compiz-bcop
- Renamed to match upstream
- First official release: 0.5.4

* Thu Jun 28 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.3-0.20070627.1mdv2008.0
+ Revision: 45277
- Import bcop

