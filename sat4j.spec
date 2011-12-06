%define eclipse_base %{_libdir}/eclipse
# We want the version to match that shipped in Eclipse's Orbit project
%define qualifier 20090825

Name:           sat4j
Version:        2.1.1
Release:        1.2%{?dist}
Summary:        A library of SAT solvers written in Java

Group:          Development/Libraries
License:        EPL or LGPLv2
URL:            http://www.sat4j.org/
# Created by sh %{name}-fetch.sh
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-fetch.sh
Patch0:         %{name}-classpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  java-devel >= 1:1.6
BuildRequires:  ant
BuildRequires:  ecj
Requires:       java >= 1:1.6
Requires:       jpackage-utils

BuildArch:      noarch

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q
%patch0

# Only used for the tests
rm lib/commons-cli.jar

%build
ant -Dbuild.compiler=modern -Drelease=%{version} -DBUILD_DATE=%{qualifier} p2 

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -rp dist/%{version}/org.sat4j.core.jar \
 $RPM_BUILD_ROOT%{_javadir}
cp -rp dist/%{version}/org.sat4j.pb.jar \
 $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
# No %%doc files as the about.html is in the jar
%{_javadir}/org.sat4j*

%changelog
* Tue Mar 30 2010 Andrew Overholt <overholt@redhat.com> 2.1.1-1.2
- Patch out main-in-manifest (akurtakov).
- Fix license tag.

* Fri Mar 19 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-1.1
- Update to 2.1.1.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.0-1.1
- Rebuilt for RHEL 6

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 final.

* Wed Apr 8 2009 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-0.1.rc2
- Update to 2.1.0.RC2.

* Thu Feb 26 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.3-1
- Update to 2.0.3.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-7
- eclipse_base is now libdir/eclipse

* Tue Jul 15 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-6
- Build with OpenJDK (java.util.Scanner)

* Tue Jul 15 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-5
- Use sed instead of dos2unix

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-4
- Remove jmock JARs
- Don't run tests as part of build

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-3
- Remove Class-Path from pb MANIFEST.MF

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-2
- Add eclipse-pde BR for pdebuild script

* Fri Jun 27 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-1
- 2.0.0
- Run tests

* Thu Mar 13 2008 Andrew Overholt <overholt@redhat.com> 2.0-0.1.RC5
- Initial version
