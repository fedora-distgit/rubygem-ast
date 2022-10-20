# Generated from ast-2.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ast

Name: rubygem-%{gem_name}
Version: 2.4.2
Release: 1%{?dist}
Summary: A library for working with Abstract Syntax Trees
License: MIT
URL: https://whitequark.github.io/ast/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bacon) >= 1.2
# BuildRequires: rubygem(bacon-colored_output)
# BuildRequires: rubygem(yard)
# BuildRequires: rubygem(kramdown)
BuildArch: noarch

%description
A library for working with Abstract Syntax Trees.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Tests are not shipped with the gem
# bacon -a
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.MIT
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.YARD.md

%changelog
* Thu Oct 20 2022 Pavel Valena <pvalena@redhat.com> - 2.4.2-1
- Initial package
