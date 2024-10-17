%define upstream_name    IO-Capture-Extended
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	IO::Capture::Extended - Extend functionality of IO::Capture


License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Capture)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes 
%dir %{perl_vendorlib}/IO/Capture/Stdout
%dir %{perl_vendorlib}/IO/Capture/Extended
%dir %{perl_vendorlib}/IO/Capture/Stderr
%{perl_vendorlib}/IO/Capture/Extended.pm
%{perl_vendorlib}/IO/Capture/Stdout/*pm
%{perl_vendorlib}/IO/Capture/Extended/*pm
%{perl_vendorlib}/IO/Capture/Stderr/*pm
%{_mandir}/*/*




