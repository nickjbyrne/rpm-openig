# rpm-openig

An RPM spec file to build and install the is Forgerock OpenIG WAR file

To Build:

    sudo yum -y groupinstall "Development Tools"
    wget https://backstage.forgerock.com/downloads/enterprise/openig/3.1.0/OpenIG-3.1.0.war -P ~/rpmbuild/SOURCES/
    rpmbuild -bb  ~/rpmbuild/SPECS/openig.spec --define "release 1"
