%{?_javapackages_macros:%_javapackages_macros}
%global vertag M4

Name:           sisu-maven-plugin
Epoch:          1
Version:        0.0.0
Release:        0.1.%{vertag}.0%{?dist}
Summary:        Sisu plugin for Apache Maven
BuildArch:      noarch
License:        EPL
URL:            http://eclipse.org/sisu
Source:         http://git.eclipse.org/c/sisu/org.eclipse.sisu.mojos.git/snapshot/milestones/%{version}.%{vertag}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(org.sonatype.oss:oss-parent)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice)


%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -c -T
tar xf %{SOURCE0} && mv milestones/*/* . && rm -rf milestones
%mvn_alias : org.sonatype.plugins:
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Thu Jul 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.1.M4
- Update to upstream version 0.0.0.M4

* Mon May 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-6
- Fix license tag

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 1.1-3
- Build with xmvn

* Wed Aug  8 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Added parent POM dependency

* Tue Jul 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Initial packaging
