%{?scl:%scl_package %{vagrant_plugin_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from vagrant-registration-0.0.7.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-registration

Name: %{?scl_prefix}%{vagrant_plugin_name}
Version: 0.0.19
Release: 5%{?dist}
Summary: Automatic guest registration for Vagrant
Group: Development/Languages
License: GPLv2
URL: https://rubygems.org/gems/vagrant-registration 
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires(pre): shadow-utils
Requires(posttrans): %{?scl_prefix}vagrant
Requires(preun): %{?scl_prefix}vagrant
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix}vagrant
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.6
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}vagrant
BuildArch: noarch
Provides: %{?scl_prefix}vagrant(%{vagrant_plugin_name}) = %{version}

%description
Enables guests to be registered automatically which is especially useful
for RHEL or SLES guests.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{vagrant_plugin_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{vagrant_plugin_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{vagrant_plugin_name}.gemspec
%vagrant_plugin_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

# We can't run test suite because it requires virtualization

%check
pushd .%{vagrant_plugin_instdir}

popd

%pre
getent group vagrant >/dev/null || groupadd -r vagrant

%posttrans
%{?scl:scl enable %{scl} - << \EOF}
%vagrant_plugin_register %{vagrant_plugin_name}
%{?scl:EOF}

%preun
%{?scl:scl enable %{scl} - << \EOF}
%vagrant_plugin_unregister %{vagrant_plugin_name}
%{?scl:EOF}

%files
%license %{vagrant_plugin_instdir}/LICENSE.md
%{vagrant_plugin_instdir}/plugins/*
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_instdir}/README.md
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%doc %{vagrant_plugin_docdir}
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/vagrant-registration.gemspec
%{vagrant_plugin_instdir}/tests

%changelog
* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-5
- Fix %posttrans and %preun scripts

* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-4
- Properly require SCL version of vagrant

* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-3
- Change to SCL

* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-2
- Fix virtual provide (rhbz#1243417)

* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-1
- Update to 0.0.19

* Wed Jun 24 2015 Josef Stribny <jstribny@redhat.com> - 0.0.16-1
- Update to 0.0.16

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Josef Stribny <jstribny@redhat.com> - 0.0.15-1
- Update to 0.0.15

* Wed Jun 10 2015 Josef Stribny <jstribny@redhat.com> - 0.0.14-1
- Update to 0.0.14

* Thu May 28 2015 Josef Stribny <jstribny@redhat.com> - 0.0.13-1
- Update to 0.0.13

* Mon May 18 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.12-1
- New upstream release

* Thu Feb 19 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-3
- Changed license string to GPLv2
- Split description to two lines

* Wed Feb 18 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-2
- Move README and CHANGELOG to %doc subpackage
- Re-word description
- Add upstream URL
- Require vagrant at build time

* Wed Feb 18 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-1
- Initial package
