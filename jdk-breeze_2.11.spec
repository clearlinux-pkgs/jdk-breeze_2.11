Name     : jdk-breeze_2.11
Version  : 0.11.2
Release  : 1
URL      : http://repo2.maven.org/maven2/org/scalanlp/breeze_2.11/0.11.2/breeze_2.11-0.11.2.jar
Source0  : http://repo2.maven.org/maven2/org/scalanlp/breeze_2.11/0.11.2/breeze_2.11-0.11.2.jar
Source1  : http://repo2.maven.org/maven2/org/scalanlp/breeze_2.11/0.11.2/breeze_2.11-0.11.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-breeze_2.11-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-breeze_2.11 package.
Group: Data

%description data
data components for the jdk-breeze_2.11 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/breeze_2.11.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/breeze_2.11.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/breeze_2.11.xml \
%{buildroot}/usr/share/maven-poms/breeze_2.11.pom \
%{buildroot}/usr/share/java/breeze_2.11.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/breeze_2.11.jar
/usr/share/maven-metadata/breeze_2.11.xml
/usr/share/maven-poms/breeze_2.11.pom
