# Not noarch, but nothing to strip:
%define debug_package %{nil}

#for the gid creation
#%%bcond_without  fedora
%global username ctapiusers

Name:           ctapi-common
Version:        1.1
Release:        6.1%{?dist}
Summary:        Common files and packaging infrastructure for CT-API modules

Group:          System Environment/Libraries
License:        MIT
URL:            http://fedoraproject.org/
Requires(pre):	shadow-utils

Provides:       group(%username)

Source0:        %{name}.LICENSE
Source1:        %{name}.README
#BuildRequires:  fedora-usermgmt-devel
#%%{?FE_USERADD_REQ}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(pre):  shadow-utils

%description
%{summary}.


%prep
%setup -c -T
install -pm 644 %{SOURCE0} LICENSE
install -pm 644 %{SOURCE1} README


%build
echo %{_libdir}/ctapi > ctapi.conf


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 644 ctapi.conf \
    $RPM_BUILD_ROOT/etc/ld.so.conf.d/ctapi-%{_target_cpu}.conf
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/ctapi


%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent group %username >/dev/null || groupadd -r %username || :

%files
%defattr(-,root,root,-)
%doc LICENSE README
# Hardcoded /etc in README -> hardcoded here.
/etc/ld.so.conf.d/ctapi-%{_target_cpu}.conf
%{_libdir}/ctapi/


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-4
- Autorebuild for GCC 4.3

* Sat Aug 04 2007 Frank Büttner <frank-buettner@gmx.net> - 1.1-3
 - fix creation of the group and don't remove it

* Mon Jul 23 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.1-2
- Change group to ctapiusers.
- Don't hardcode a static gid.
- Don't remove the group at all.
- Require shadow-utils for group creation.

* Sat Jul 21 2007 Frank Büttner <frank-buettner@gmx.net> - 1.1-1
 - set version to 1.1 so that other packages can require it

* Sat Jul 21 2007 Frank Büttner <frank-buettner@gmx.net> - 1.0-5
 - fix for #220767 all users that will use card readers must be
   in the new group cardusers.

* Fri Sep 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-4
- Rebuild.

* Mon Jul 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-3
- Ensure proper doc file permissions.

* Sat May  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-2
- Encourage dir based dependency on %%{_libdir}/ctapi in packages (#190911).
- Split contents of README into a separate file.
- Change license to MIT, include license text.
- Add URL.

* Sat May  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-1
- First build.
