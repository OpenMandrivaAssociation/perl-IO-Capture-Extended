%define upstream_name    IO-Capture-Extended
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	IO::Capture::Extended - Extend functionality of IO::Capture
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-IO-Capture
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
IO::Capture::Extended is a distribution consisting of two
classes, each of which is a collection of subroutines which are
useful in extending the functionality of CPAN modules 
IO::Capture::Stdout and IO::Capture::Stderr, particularly when
used in a testing context such as that provided by Test::Simple,
Test::More or other modules built on Test::Builder.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/IO/Capture/Stdout
%dir %{perl_vendorlib}/IO/Capture/Extended
%dir %{perl_vendorlib}/IO/Capture/Stderr
%{perl_vendorlib}/IO/Capture/Extended.pm
%{perl_vendorlib}/IO/Capture/Stdout/*pm
%{perl_vendorlib}/IO/Capture/Extended/*pm
%{perl_vendorlib}/IO/Capture/Stderr/*pm
%{_mandir}/*/*
