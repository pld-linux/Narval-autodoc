%define short_name autodoc

Summary:	Autodoc extension for Narval
Summary(pl.UTF-8):   Rozszerzenie Autodoc dla Narvala
Name:		Narval-%{short_name}
Version:	20020220
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	1a415d413564387aaef72106a9f3f2ae
URL:		http://www.logilab.org/narval/app.html
Requires:	Narval
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Autodoc extension set is a Narval recipe that generates
documentation for Narval actions, transformations and recipe.

%description -l pl.UTF-8
Zestaw rozszerzeń Autodoc jest receptą Narvala, która generuje
dokumentacje dla działań, przekształceń i recept Narvala.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps/%{short_name}-%{version}.npm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
