%define short_name autodoc

Summary:	Autodoc extension for Narval
Summary(pl):	Rozszerzenie Autodoc dla Narvala
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
License:	GPL
Group:		Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
The Autodoc extension set is a Narval recipe that generates
documentation for Narval actions, transformations and recipe.

%description -l pl
Zestaw rozszerzeñ Autodoc jest recept± Narvala, która generuje
dokumentacje dla dzia³añ, przekszta³ceñ i recept Narvala.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
