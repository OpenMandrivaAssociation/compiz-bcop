%define shortname bcop
%define name compiz-bcop
%define version 0.6.99
%define rel 1
%define git 20080210

%if  %{git}
%define srcname %{shortname}-%{git}
%define distname %{shortname}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: BCOP: Compiz Fusion plugin build utility
Group: System/X11
URL: http://www.go-compiz.org/
Source: %{srcname}.tar.bz2 
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
