%global _empty_manifest_terminate_build 0
Name:		python-exif
Version:	1.3.5
Release:	1
Summary:	Read and modify image EXIF metadata using Python.
License:	MIT 
URL:		https://gitlab.com/TNThieding/exif
Source0:	https://files.pythonhosted.org/packages/f2/8d/0db23fa243abfd71246df00550663a1b0e23542368d1040d55fc5ef3cbe8/exif-1.3.5.tar.gz
BuildArch:	noarch

Requires:	python3-plum-py

%description
Read and modify image EXIF metadata using Python without any third-party software
dependencies. For example, batch process image metadata using a Python script.

%package -n python3-exif
Summary:	Read and modify image EXIF metadata using Python.
Provides:	python-exif
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-exif
Read and modify image EXIF metadata using Python without any third-party software
dependencies. For example, batch process image metadata using a Python script.

%package help
Summary:	Development documents and examples for exif
Provides:	python3-exif-doc
%description help
Read and modify image EXIF metadata using Python without any third-party software
dependencies. For example, batch process image metadata using a Python script.

%prep
%autosetup -n exif-1.3.5

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-exif -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Sep 09 2022 hkgy <kaguyahatu@outlook.com> - 1.3.5-1
- Update to 1.3.5

* Tue Dec 14 2021 Python_Bot <Python_Bot@openeuler.org> - 1.3.4-1
- Package Init
