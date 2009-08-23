# Sensible Perl-specific RPM build macros 
#
# Note that these depend on the generic filtering system being in place in
# rpm core.
#
# Chris Weyl <cweyl@alumni.drew.edu> 2009

# By default, for perl packages we want to filter all files in _docdir from 
# req/prov scanning, as well as filtering out any provides caused by private 
# libs in vendorarch/archlib (vendor/core)
#
# This should also give a good sense of how to use these macros.

%define perl_default_filter %{expand: \
%filter_provides_in %{perl_vendorarch}/.*\\.so$ \
%filter_provides_in -P %{perl_archlib}/(?!CORE/libperl).*\\.so$ \
%filter_provides_in %{_docdir} \
%filter_requires_in %{_docdir} \
%filter_setup \
}

