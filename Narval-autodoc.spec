%define short_name autodoc

Summary:	Autodoc extension for Narval
Summary(pl):	Rozszerzenie Autodoc dla Narvala
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

%description -l pl
Zestaw rozszerzeñ Autodoc jest recept± Narvala, która generuje
dokumentacje dla dzia³añ, przekszta³ceñ i recept Narvala.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps/%{short_name}-%{version}.npm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
