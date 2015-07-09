%define version 3.1.0
%{!?release: %{!?release: %define release 1}}

Summary: The Open Identity Gateway is a high-performance reverse proxy server with specialized session management and credential replay functionality.
Name: openig
Version: %{version}
Release: %{release}%{?dist}
License: CDDL
Group: Applications/System
URL: http://openig.forgerock.org/
Source0: https://backstage.forgerock.com/downloads/enterprise/openig/3.1.0/OpenIG-3.1.0.war
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: tomcat6

%description
The Open Identity Gateway is a high-performance reverse proxy server with specialized session management and credential replay functionality. OpenIG works together with OpenAM to integrate Web applications without the need to modify the target application or the container that it runs in.

%prep

# We don't want any perl dependecies in this RPM:
%define __perl_requires /bin/true

%build

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}/var/lib/tomcat6/webapps
cp %{_sourcedir}/OpenIG-3.1.0.war %{buildroot}/var/lib/tomcat6/webapps/ROOT.war

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%pre

%post

%preun

%postun

%files

%attr(750, tomcat, tomcat) /var/lib/tomcat6/webapps/ROOT.war

%changelog
* Thu Jul 09 2015 Nick Byrne <nick@incension.com
- Initial version of openig 3.1.0
