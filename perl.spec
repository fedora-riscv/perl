%define multilib_64_archs x86_64 s390x ppc64 sparc64
%define perl_archname %{_arch}-%{_os}-thread-multi
%define perlmodcompat 5.8.7 5.8.6 5.8.5
%define new_perl_lib  $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}:$RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}
%define comp_perl_lib $RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}:$RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}
%define new_arch_lib  $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{perl_archname}
%define comp_arch_lib $RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}/%{perl_archname}
%define new_perl_flags LD_PRELOAD=/%{new_arch_lib}/CORE/libperl.so LD_LIBRARY_PATH=%{new_arch_lib}/CORE PERL5LIB=%{new_perl_lib}:%{comp_perl_lib}
%define new_perl %{new_perl_flags} $RPM_BUILD_ROOT/%{_bindir}/perl

%define perl_version    5.8.8
%define perl_epoch      4

# Use this for SUPER PERL DEBUGGING MODE.
%{?!perl_debugging:    %define perl_debugging 0}
%if %{perl_debugging}
%define debug_package %{nil}
# don't build debuginfo and disable stripping
%endif

Name:           perl
Version:        %{perl_version}
Release:        27%{?dist}
Epoch:          %{perl_epoch}
Summary:        The Perl programming language
Group:          Development/Languages
# Modules Tie::File and Getopt::Long are licenced under "GPLv2+ or Artistic,"
# we have to reflect that in the sub-package containing them.
# FIXME: Digest::MD5 has a must-advertise-RSA license with an exception,
# the tag does not reflect that (yet).
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic)
Url:            http://www.perl.org/
Source0:        http://www.cpan.org/authors/id/N/NW/NWCLARK/%{name}-%{perl_version}.tar.bz2
Source11:       filter-depends.sh
Source12:       perl-5.8.0-libnet.cfg
# Specific to Fedora/RHEL
Patch1:         perl-5.8.0-root.patch
# Upstream bug 41586
Patch2:         perl-5.8.8-incpush.patch
# Removes date check, Fedora/RHEL specific
Patch3:         perl-5.8.8-perlbug-tag.patch
# XXX: The next two patches appear to alter the order of @INC, but
# there isn't sufficient documentation as to why we do this.
Patch4:         perl-5.8.8-dashI.patch
Patch5:         perl-5.8.5-incorder.patch
# make sure we get the proper ldflags on libperl.so
# Upstream bug 41587
Patch6:         perl-5.8.0-sharedlinker.patch
# Fedora/RHEL use links instead of lynx
Patch7:         perl-5.8.8-links.patch
# work around annoying rpath issue
# This is only relevant for Fedora, as it is unlikely
# that upstream will assume the existence of a libperl.so
Patch8:         perl-5.8.8-rpath-make.patch
# Disable -DDEBUGGING and allow -g to do its job (#156113)
# Upstream bug 41588
Patch9:         perl-5.8.7-no-debugging.patch
# Upstream bug 41589
Patch10:        perl-5.8.1-fpic.patch
# Fedora/RHEL only (64bit only)
Patch11:        perl-5.8.0-libdir64.patch
# Upstream bug 41590
Patch12:        perl-5.8.0-nptlhint.patch
# Fedora/RHEL specific (use libresolv instead of libbind)
Patch13:        perl-5.8.6-libresolv.patch
# fix for bug 163958 / upstream bug 37056 :
# backport of perl-5.9's patch 25084 (bug still in 5.8.8!):
Patch14:        perl-5.8.7-25084.patch
# multi-threaded perl builds use localtime_r which does not call tzset
# bugzilla 172396
# Upstream bug 41591
Patch15:        perl-5.8.7-172396.patch
# Security fix
Patch16:        perl-5.8.8-CAN-2004-0976.patch
# XXX: Fixme
# Needs all the "Red Hat" references removed before upstreaming
Patch17:        perl-5.8.8-USE_MM_LD_RUN_PATH.patch
# Upstream bug 38385
Patch18:        perl-5.8.8-bz178343.patch
# Debian's fix for Net::NNTP:
# Upstream bug 41593
Patch19:        perl-5.8.8-debian_fix_net_nntp.patch
# Upstream patches 27133 and 27169 (27170):
Patch20:        perl-5.8.8-up27133_up27169.patch
# Upstream patch 27284:
Patch21:        perl-5.8.8-up27284.patch
# Fix for bug 183553 / upstream bug 38657:
Patch22:        perl-5.8.8-bz183553_ubz38657.patch
# http://rt.cpan.org/Ticket/Display.html?id=18692
Patch23:        perl-5.8.8-bz188441.patch
# Upstream bug 39130
Patch24:        perl-5.8.8-bz191416.patch
Patch25:        perl-5.8.8-U27116.patch
Patch26:        perl-5.8.8-U27391.patch
Patch27:        perl-5.8.8-U27426.patch
Patch28:        perl-5.8.8-U27509.patch
Patch29:        perl-5.8.8-U27512.patch
Patch30:        perl-5.8.8-U27604.patch
Patch31:        perl-5.8.8-U27605.patch
Patch32:        perl-5.8.8-U27914.patch
Patch33:        perl-5.8.8-U27329.patch
# XXX: Fixme
# Needs to be un-RedHatized before upstreaming
Patch34:        perl-5.8.8-R-switch.patch
# stop IPC/SysV.c including <asm/page.h> for getpagesize(), which
# is now declared by including <unistd.h> .
# Upstream bug 41594
Patch35:        perl-5.8.8-no_asm_page_h.patch
Patch36:        perl-5.8.8-U34297_C28006.patch
# Bugzilla 199372
# Upstream bug 41595
Patch37:        perl-5.8.8-useCFLAGSwithCC.patch
# Upstream bug 39903
Patch38:        perl-5.8.8-bz199736.patch
# Skip hostname tests, since hostname lookup isn't available in Fedora
# buildroots by design.
Patch39:        perl-5.8.8-disable_test_hosts.patch
# XXX: Fixme - Finish patch.
#Patch39:        perl-5.8.8-bz204679.patch
Patch40:	perl-5.8.8-U28775.patch
# Update DB_File to 1.815
Patch41:        perl-5.8.8-DB_File-1.815.patch
# Fix from perl bug #24254
Patch42:        perl-5.8.8-bug24254.patch
# Fix for CVE-2007-5116
Patch43:	perl-5.8.8-bz323571.patch
BuildRoot:      %{_tmppath}/%{name}-%{perl_version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  tcsh, dos2unix, man, groff
BuildRequires:  gdbm-devel, db4-devel

# The long line of Perl provides.

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

# Compat provides
Provides: perl(:MODULE_COMPAT_5.8.5)
Provides: perl(:MODULE_COMPAT_5.8.6)
Provides: perl(:MODULE_COMPAT_5.8.7)
Provides: perl(:MODULE_COMPAT_5.8.8)
# Threading provides
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
# Largefile provides
Provides: perl(:WITH_LARGEFILES)
# PerlIO provides
Provides: perl(:WITH_PERLIO)
# File provides
Provides: perl(abbrev.pl)
Provides: perl(assert.pl)
Provides: perl(bigfloat.pl)
Provides: perl(bigint.pl)
Provides: perl(bigrat.pl)
Provides: perl(bytes_heavy.pl)
Provides: perl(cacheout.pl)
Provides: perl(complete.pl)
Provides: perl(ctime.pl)
Provides: perl(dotsh.pl)
Provides: perl(dumpvar.pl)
Provides: perl(exceptions.pl)
Provides: perl(fastcwd.pl)
Provides: perl(find.pl)
Provides: perl(finddepth.pl)
Provides: perl(flush.pl)
Provides: perl(ftp.pl)
Provides: perl(getcwd.pl)
Provides: perl(getopt.pl)
Provides: perl(getopts.pl)
Provides: perl(hostname.pl)
Provides: perl(importenv.pl)
Provides: perl(look.pl)
Provides: perl(newgetopt.pl)
Provides: perl(open2.pl)
Provides: perl(open3.pl)
Provides: perl(perl5db.pl)
Provides: perl(pwd.pl)
Provides: perl(shellwords.pl)
Provides: perl(stat.pl)
Provides: perl(syslog.pl)
Provides: perl(tainted.pl)
Provides: perl(termcap.pl)
Provides: perl(timelocal.pl)
Provides: perl(utf8_heavy.pl)
Provides: perl(validate.pl)
Provides: perl(Carp::Heavy)
# Versioned Provides for our Obsoletes
Provides: perl-Filter-Simple = 0.82
Provides: perl-Time-HiRes = 1.86

# Last seen in Fedora Core 4
Obsoletes: perl-Filter-Simple
Obsoletes: perl-Time-HiRes

Requires: perl-libs = %{perl_epoch}:%{perl_version}-%{release}

# We need this to break the dependency loop, and ensure that perl-libs 
# gets installed before perl.
Requires(post): perl-libs

%define __perl_requires %{SOURCE11}


%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications are system
administration utilities and web programming.  A large proportion of
the CGI scripts on the web are written in Perl.  You need the perl
package installed on your system so that your system can handle Perl
scripts.

Install this package if you want to program in Perl or enable your
system to handle Perl scripts.

%package libs
Summary:        The libraries for the perl runtime
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description libs
The libraries for the perl runtime


%package devel
Summary:        Header files for use in perl development
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(CPAN), perl(ExtUtils::Embed), perl(ExtUtils::MakeMaker)
Requires:	perl(Test::Harness), perl(Test::Simple)

%description devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.


%package suidperl
Summary:        Suidperl, for use with setuid perl scripts
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description suidperl
Suidperl is a setuid binary copy of perl that allows for (hopefully)
more secure running of setuid perl scripts.

%package CPAN
Summary:        Query, download and build perl modules from CPAN sites
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        1.76_02
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Provides:       cpan = %{version}

%description CPAN
Query, download and build perl modules from CPAN sites.

%package ExtUtils-Embed
Summary:        Utilities for embedding Perl in C/C++ applications
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        1.26
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-Embed
Utilities for embedding Perl in C/C++ applications.

%package ExtUtils-MakeMaker
Summary:        Create a module Makefile
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        6.30
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Test::Harness)

%description ExtUtils-MakeMaker
Create a module Makefile.

%package Test-Harness
Summary:        Run Perl standard test scripts with statistics
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        2.56
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Harness
Run Perl standard test scripts with statistics.

%package Test-Simple
Summary:        Basic utilities for writing tests
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        0.62
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Simple
Basic utilities for writing tests.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%if !%{perl_debugging}
%patch9 -p1
%endif
%patch10 -p1
%ifarch %{multilib_64_archs}
%patch11 -p1
%endif
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
#
# Candidates for doc recoding (need case by case review):
# find . -name "*.pod" -o -name "README*" -o -name "*.pm" | xargs file -i | grep charset= | grep -v '\(us-ascii\|utf-8\)'
recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode README.cn euc-cn
recode README.jp euc-jp
recode README.ko euc-kr
recode README.tw big5
recode pod/perlebcdic.pod iso-8859-1
recode pod/perlhack.pod iso-8859-1
recode pod/perlhist.pod iso-8859-1
recode pod/perlothrtut.pod iso-8859-1
recode pod/perlthrtut.pod iso-8859-1
recode lib/Unicode/Collate.pm iso-8859-1

find . -name \*.orig -exec rm -fv {} \;

# Oh, the irony. Perl generates some non-versioned provides we don't need.
# Each of these has a versioned provide, which we keep.
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
    sed -e '/^perl(Carp)$/d' |\
    sed -e '/^perl(DynaLoader)$/d' |\
    sed -e '/^perl(Locale::Maketext)$/d' |\
    sed -e '/^perl(Math::BigInt)$/d' |\
    sed -e '/^perl(Net::Config)$/d' |\
    sed -e '/^perl(Tie::Hash)$/d' |\
    sed -e '/^perl(bigint)$/d' |\
    sed -e '/^perl(bigrat)$/d' |\
    sed -e '/^perl(bytes)$/d' |\
    sed -e '/^perl(utf8)$/d'
EOF
%define __perl_provides %{_builddir}/%{name}-%{perl_version}/%{name}-prov
chmod +x %{__perl_provides}


%build
echo "RPM Build arch: %{_arch}"

# yes; don't use %_libdir so that noarch packages from other OSs
# arches work correctly :\ the Configure lines below hardcode lib for
# similar reasons.

/bin/sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
        -Dversion=%{perl_version} \
        -Dmyhostname=localhost \
        -Dperladmin=root@localhost \
        -Dcc='%{__cc}' \
        -Dcf_by='Red Hat, Inc.' \
        -Dinstallprefix=%{_prefix} \
        -Dprefix=%{_prefix} \
%ifarch %{multilib_64_archs}
        -Dlibpth="/usr/local/lib64 /lib64 %{_prefix}/lib64" \
        -Dprivlib="%{_prefix}/lib/perl5/%{perl_version}" \
        -Dsitelib="%{_prefix}/lib/perl5/site_perl/%{perl_version}" \
        -Dvendorlib="%{_prefix}/lib/perl5/vendor_perl/%{perl_version}" \
        -Darchlib="%{_libdir}/perl5/%{perl_version}/%{perl_archname}" \
        -Dsitearch="%{_libdir}/perl5/site_perl/%{perl_version}/%{perl_archname}" \
        -Dvendorarch="%{_libdir}/perl5/vendor_perl/%{perl_version}/%{perl_archname}" \
%endif
        -Darchname=%{_arch}-%{_os} \
%ifarch sparc
        -Ud_longdbl \
%endif
        -Dvendorprefix=%{_prefix} \
        -Dsiteprefix=%{_prefix} \
        -Duseshrplib \
        -Dusethreads \
        -Duseithreads \
        -Duselargefiles \
        -Dd_dosuid \
        -Dd_semctl_semun \
        -Di_db \
        -Ui_ndbm \
        -Di_gdbm \
        -Di_shadow \
        -Di_syslog \
        -Dman3ext=3pm \
        -Duseperlio \
        -Dinstallusrbinperl=n \
        -Ubincompat5005 \
        -Uversiononly \
        -Dpager='/usr/bin/less -isr' \
        -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
        -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
        -Ud_endservent_r_proto -Ud_setservent_r_proto \
        -Dinc_version_list='%{perlmodcompat}' \
        -Dscriptdir='%{_bindir}'

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%ifarch %{multilib_64_archs}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{perl_version}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/site_perl/%{perl_version}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/vendor_perl/%{perl_version}
%endif

%ifarch %{multilib_64_archs}
mkdir -p -m 755 ${RPM_BUILD_ROOT}%{_prefix}/lib64/perl5/vendor_perl/%{perl_version}/%{_arch}-%{_os}
%endif

#
# Compatibility directories
#
pushd $RPM_BUILD_ROOT/%{_libdir}/perl5
for i in %{perlmodcompat}; do
    mkdir -pm 755 $i/%{perl_archname}/CORE
    mkdir -pm 755 $i/%{perl_archname}/auto
    pushd $i/%{perl_archname}/CORE
      ln -s ../../../%{perl_version}/%{perl_archname}/CORE/libperl.so libperl.so
    popd
  done
popd

install -p -m 755 utils/pl2pm ${RPM_BUILD_ROOT}%{_bindir}/pl2pm

for i in asm/termios.h syscall.h syslimits.h syslog.h sys/ioctl.h sys/socket.h sys/time.h wait.h
do
  %{new_perl} $RPM_BUILD_ROOT/%{_bindir}/h2ph -a \
              -d $RPM_BUILD_ROOT%{_libdir}/perl5/%{perl_version}/%{perl_archname} $i || /bin/true
done


for dir in $(%{new_perl} -le 'print join("\n", @INC)' | grep '^%{_prefix}/lib')
do
  mkdir -p $RPM_BUILD_ROOT/$dir
done

for dir in $(%{new_perl} -le 'print join("\n", @INC)' | grep '^%{_libdir}')
do
  mkdir -p $RPM_BUILD_ROOT/$dir
done

for i in %{perl_version} %{perlmodcompat} ; do
  mkdir -pm 755 $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl/$i/%{perl_archname}/auto
  mkdir -pm 755 $RPM_BUILD_ROOT%{_libdir}/perl5/vendor_perl/$i/%{perl_archname}/auto
done


#
# libnet configuration file
#
mkdir -p -m 755 $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perl_version}/Net
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perl_version}/Net/libnet.cfg

#
# Core modules removal
#
find $RPM_BUILD_ROOT -name '*NDBM*' | xargs rm -rfv

find $RPM_BUILD_ROOT -type f -name '*.bs' -a -empty -exec rm -f {} ';'

# Cleanup binary paths and make cgi files executable
pushd $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/CGI/eg/
  for i in *.cgi make_links.pl RunMeFirst ; do
    sed -i 's|/usr/local/bin/perl|%{_bindir}/perl|g' $i
    chmod +x $i
  done
popd

# miniperl? As an interpreter? How odd.
sed -i 's|./miniperl|%{_bindir}/perl|' $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/ExtUtils/xsubpp
chmod +x $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/ExtUtils/xsubpp

# Don't need the .packlist
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{perl_version}/%{perl_archname}/.packlist

# Fix some manpages to be UTF-8
pushd $RPM_BUILD_ROOT%{_mandir}/man1/
  for i in perl588delta.1 perldelta.1 ; do
    iconv -f MS-ANSI -t UTF-8 $i --output new-$i
    rm -rf $i
    mv new-$i $i
  done
popd

echo "%{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/libperl.so" > libs_filelist

for i in %{perlmodcompat} ; do
    if -d $RPM_BUILD_ROOT%{_libdir}/perl5/$i/%{perl_archname}/CORE ; then
       echo "%{_libdir}/perl5/$i/%{perl_archname}/CORE" >> libs_filelist
    fi
done

chmod -R u+w $RPM_BUILD_ROOT/*
%if %{perl_debugging}
exit 0
# disable brp-strip
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc Copying README
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*
%{_libdir}/perl5/
%ifarch %{multilib_64_archs}
%{_prefix}/lib/perl5/
%endif

# libs
%exclude %{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/libperl.so
%exclude %{_libdir}/perl5/5.8.5/%{perl_archname}/CORE
%exclude %{_libdir}/perl5/5.8.6/%{perl_archname}/CORE
%exclude %{_libdir}/perl5/5.8.7/%{perl_archname}/CORE


# devel
%exclude %{_bindir}/enc2xs
%exclude %{_mandir}/man1/enc2xs*
%exclude %{_bindir}/h2xs
%exclude %{_mandir}/man1/h2xs*
%exclude %{_bindir}/libnetcfg
%exclude %{_mandir}/man1/libnetcfg*
%exclude %{_bindir}/perlcc
%exclude %{_mandir}/man1/perlcc*
%exclude %{_bindir}/perlivp
%exclude %{_mandir}/man1/perlivp*
%exclude %{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/*.h

# suidperl
%exclude %{_bindir}/suidperl
%exclude %{_bindir}/sperl%{perl_version}

# CPAN
%exclude %{_bindir}/cpan
%exclude %{_prefix}/lib/perl5/%{perl_version}/CPAN/
%exclude %{_prefix}/lib/perl5/%{perl_version}/CPAN.pm
%exclude %{_mandir}/man1/cpan.1*
%exclude %{_mandir}/man3/CPAN*

# ExtUtils-Embed
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Embed.pm
%exclude %{_mandir}/man3/ExtUtils::Embed*

# ExtUtils-MakeMaker
%exclude %{_bindir}/instmodsh
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Command/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Install.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Installed.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MANIFEST.SKIP
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MM*.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MY.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Manifest.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mkbootstrap.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mksymlists.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/NOTES
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Packlist.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/PATCHING
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/testlib.pm
%exclude %{_mandir}/man1/instmodsh.1*
%exclude %{_mandir}/man3/ExtUtils::Command::MM*
%exclude %{_mandir}/man3/ExtUtils::Install.3*
%exclude %{_mandir}/man3/ExtUtils::Installed.3*
%exclude %{_mandir}/man3/ExtUtils::Liblist.3*
%exclude %{_mandir}/man3/ExtUtils::MM*
%exclude %{_mandir}/man3/ExtUtils::MY.3*
%exclude %{_mandir}/man3/ExtUtils::MakeMaker*
%exclude %{_mandir}/man3/ExtUtils::Manifest.3*
%exclude %{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%exclude %{_mandir}/man3/ExtUtils::Mksymlists.3*
%exclude %{_mandir}/man3/ExtUtils::Packlist.3*
%exclude %{_mandir}/man3/ExtUtils::testlib.3*

# Test::Harness
%exclude %{_bindir}/prove
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Harness*
%exclude %{_mandir}/man1/prove.1*
%exclude %{_mandir}/man3/Test::Harness*

# Test::Simple
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/More*
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Builder*
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Simple*
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Tutorial*
%exclude %{_mandir}/man3/Test::More*
%exclude %{_mandir}/man3/Test::Builder*
%exclude %{_mandir}/man3/Test::Simple*
%exclude %{_mandir}/man3/Test::Tutorial*

%files libs -f libs_filelist
%defattr(-,root,root)

%files devel
%defattr(-,root,root,-)
%{_bindir}/enc2xs
%{_mandir}/man1/enc2xs*
%{_bindir}/h2xs
%{_mandir}/man1/h2xs*
%{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg*
%{_bindir}/perlcc
%{_mandir}/man1/perlcc*
%{_bindir}/perlivp
%{_mandir}/man1/perlivp*
%{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/*.h

%files suidperl
%defattr(-,root,root,-)
%{_bindir}/suidperl
%{_bindir}/sperl%{perl_version}

%files CPAN
%defattr(-,root,root,-)
%{_bindir}/cpan
%{_prefix}/lib/perl5/%{perl_version}/CPAN/
%{_prefix}/lib/perl5/%{perl_version}/CPAN.pm
%{_mandir}/man1/cpan.1*
%{_mandir}/man3/CPAN*

%files ExtUtils-Embed
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Embed.pm
%{_mandir}/man3/ExtUtils::Embed*

%files ExtUtils-MakeMaker
%defattr(-,root,root,-)
%{_bindir}/instmodsh
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Command/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Install.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Installed.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MANIFEST.SKIP
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MM*.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MY.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Manifest.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mkbootstrap.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mksymlists.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/NOTES
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Packlist.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/PATCHING
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/testlib.pm
%{_mandir}/man1/instmodsh.1*
%{_mandir}/man3/ExtUtils::Command::MM*
%{_mandir}/man3/ExtUtils::Install.3*
%{_mandir}/man3/ExtUtils::Installed.3*
%{_mandir}/man3/ExtUtils::Liblist.3*
%{_mandir}/man3/ExtUtils::MM*
%{_mandir}/man3/ExtUtils::MY.3*
%{_mandir}/man3/ExtUtils::MakeMaker*
%{_mandir}/man3/ExtUtils::Manifest.3*
%{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%{_mandir}/man3/ExtUtils::Mksymlists.3*
%{_mandir}/man3/ExtUtils::Packlist.3*
%{_mandir}/man3/ExtUtils::testlib.3*

%files Test-Harness
%defattr(-,root,root,-)
%{_bindir}/prove
%{_prefix}/lib/perl5/%{perl_version}/Test/Harness*
%{_mandir}/man1/prove.1*
%{_mandir}/man3/Test::Harness*

%files Test-Simple
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Test/More*
%{_prefix}/lib/perl5/%{perl_version}/Test/Builder*
%{_prefix}/lib/perl5/%{perl_version}/Test/Simple*
%{_prefix}/lib/perl5/%{perl_version}/Test/Tutorial*
%{_mandir}/man3/Test::More*
%{_mandir}/man3/Test::Builder*
%{_mandir}/man3/Test::Simple*
%{_mandir}/man3/Test::Tutorial*

%changelog
* Mon Nov 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.8.8-27
- break dep loop, fix bugzilla 397881

* Mon Nov 12 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.8.8-26
- fix for CVE-2007-5116

* Thu Oct 25 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.8.8-25
- patch from perl bug 24254, fix for RH bz 114271

* Mon Oct  1 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.8.8-24
- update DB_File to 1.815

* Sat Aug 18 2007 Stepan Kasal <skasal@redhat.com> - 4:5.8.8-23
- Remove unnnecessary parens from the License tags.

* Sat Aug 18 2007 Stepan Kasal <skasal@redhat.com> - 4:5.8.8-22
- Fix the License: tags.

* Fri Aug 17 2007 Stepan Kasal <skasal@redhat.com> - 4:5.8.8-21
- Apply patch to skip hostname tests, since hostname lookup isn't
  available in Fedora buildroots by design.

* Fri Aug 17 2007 Stepan Kasal <skasal@redhat.com> - 4:5.8.8-20
- perl rpm requires the corresponding version of perl-libs rpm
- Resolves: rhbz#240540

* Fri Jun 22 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-19
- Resolves: rhbz#196836
- Apply upstream patch #28775, which fixes an issue where reblessing
  overloaded objects incurs significant performance penalty

* Wed May 16 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-18
- Have perl-devel Require the other development/build related modules for simplicity.

* Fri May  4 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-17
- Includes patch from Ralf Corsepius to split out some more perl modules.
- Further split out development related perl modules.
- Remove Requires: perl-devel from perl
- Move libperl.so -> perl-libs
- Patch39 to disable test_hosts in Net::Config

* Fri Mar  9 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-15
- Incorporate fixes from spot and others on fedora-perl-devel
- The main perl package will temporarily Require perl-devel
- move ExtUtils::MakeMaker, ExtUtils::Embed, CPAN, Test::Harness into devel
- also move perlcc, perlivp, h2xs, libnetcfg to devel

* Tue Feb 27 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-14
- Add a description for most of the patches, to reflect Spot's work to
  report said patches upstream.

* Sat Feb  3 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.8.8-13
- massive cleanups

* Wed Jan 24 2007 Jindrich Novy <jnovy@redhat.com> - 4:5.8.8-12
- put dist tag directly to perlrel to fix dependency to suidperl

* Tue Jan 23 2007 Jindrich Novy <jnovy@redhat.com> - 4:5.8.8-11
- rebuild against new db4
- use dist tag

* Sat Sep 30 2006 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-10
- bugzilla: 208731 - remove directory support for old perl versions

* Fri Sep 15 2006 Robin Norwood <rnorwood@redhat.com> - 4:5.8.8-9
- fix bug 204679: add Unicode 5.0.0 support

* Fri Jul 21 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-8
- fix bug 199736: make perlcc handle floating point values

* Wed Jul 19 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-8
- fix bug 199372: add .so cflags for sparc64

* Fri Jul 14 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-8
- Fix upstream perl bug #34297:
  'utf8 overload stringify bug (utf8 caching maybe)'
  upstream patch #28006 applied

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4:5.8.8-6.1
- rebuild

* Thu Jun 01 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-6
- Fix upstream perl bug #38454:
  'rindex corrects for $[ on bytes rather than UTF-8'
  apply upstream patch #27116
- Fix upstream perl bug 24816:
  'Magic vars seem unsure if they are purely numeric' 
  ( perl -wle 'print $? = $? ^ "3"' -> 'Argument "^C" isn't numeric' )
  apply upstream patch #27391
- Avoid writing over the input string in the case 'F' in moreswitches.
  apply upstream patch #27426
- Fix upstream perl bug 34925 - 'overload and rebless' -
  apply upstream patches #27509, #27512
- Fix upstream perl bug 3038 - '$qr = qr/^a$/m; $x =~ $qr; fails'
  apply upstream patch #27604
- apply upstream patch #27605 - 'Fix off-by-one in $0 set magic.'
- Fix upstream perl bug 23141 - '($_) = () fails to set $_ to undef'
  apply upstream patch #27914
- Fix upstream perl bug #38619 - 
  'Bug in lc and uc (interaction between UTF-8, substr, and lc/uc)'
  apply upstream patch #27329
- Give users the '-R' option to disable the Red Hat
  module compatibility default search path extension (incpush.patch).

* Thu May 11 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-6
- Fix bug 191416: make h2ph generate correct code for cpp statements
  like: '#if defined A || defined B'
- Fix 172396.patch for non-threaded builds

* Wed Apr 12 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-6
- Fix bug 188841: make CGI.pm's url(-relative) handle rewrites

* Tue Mar 01 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-4
- Fix bug 183553 / upstream bug 38657: fix -d:Foo=bar processing
- rebuild with new gcc-4.1.0-1, released today

* Mon Feb 27 2006 Jason Vas Dias <jvdias@redhat.com>
- Apply upstream patch #28284

* Mon Feb 13 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-3
- Apply upstream bugfix patch 27170

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4:5.8.8-2.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-2
- Rebuild again
- Debian released 5.8.8 patches today; apply only relevant difference:
  03_fix_net_nntp : fix precedence in Net::NNTP::article 
                    from Brendan O'Dea<bod@debian.org>

* Mon Feb 06 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-1.2
- Rebuild with new gcc, glibc, and glibc-kernheaders

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-1.1
- Rebuild with new gcc and glibc

* Wed Feb 01 2006 Jason Vas Dias <jvdias@redhat.com> - 4:5.8.8-1
- Upgrade to new upstream release 5.8.8, officially released today

* Tue Jan 31 2006 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.8-0.1_RC1
- fix bug 178343: h2ph must include cpp "predefined macros" in _h2ph_pre.ph
- Add perl(:MODULE_COMPAT_5.8.8) to Provides
- Fix perlbug patch

* Fri Jan 20 2006 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.8-0_RC1
- Upgrade to new upstream release candidate 5.8.8-RC1

* Wed Dec 14 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-8.1
- Updated upstream patches for CVE-2005-3962: 26322 , 26331, 26333

* Thu Dec 08 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-8
- Apply upstream patches 26283 and 26284 : complete, revised fixes
  for CVE-2005-3962 and CVE-2005-3912 and 
  "Sys::Syslog security vulnerabilities" issues.
- Fix bug 136009 / MakeMaker LD_RUN_PATH issue: 
  restore previous default Red Hat behavior of removing the MakeMaker
  generated LD_RUN_PATH setting from the link command .
  Document this removal, as it contravenes upstream default behavior, and 
  provide a USE_MM_LD_RUN_PATH MakeMaker member to enable use of the 
  MakeMaker generated LD_RUN_PATH .

* Thu Dec 01 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.8
- fix bug 174684 / CVE-2005-3962: sprintf integer overflow vulnerability
  backport upstream patch #26240

* Wed Nov 09 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.7
- fix bug 136009: restore MakeMaker support for LD_RUN_PATH, 
  while removing empty LD_RUN_PATH

* Tue Nov 08 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.7
- fix bug 172739: upstream bug 36521 : deep recursion and segfault
  in CGI::Carp::warn with 'use diagnostics' : applied patch 25160.
- fix CAN-2004-0976: insecure use of temp files (ala Debian)

* Mon Nov 07 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.7
- fix bug 172587: apply upstream patches 26009, 26011

* Thu Nov 03 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.7
- fix bug 172396 / upstream bug 26136: insert tzset() call before localtime_r() calls

* Wed Nov 02 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.7
- fix bug 172336 / upstream bug 37056: reentr ERANGE realloc recursion

* Tue Nov 01 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.7
- fix bug 172236 : missing C standard headers -
  use gcc4's '-print-search-path' option in h2ph

* Tue Oct 25 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.7-0.6
- fix bug 171111 : define ioctl length macro IOCPARM_LEN(x)
  macro to be _IOC_SIZE(x), not 256 - upstream bug #37535 raised.
- provide 'perl_debugging' .spec file option to enable -DDEBUGGING
  and disable stripping / debuginfo generation - default: 0

* Sun Oct 09 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.7-0.4
- rebuild for db4 (#170235)

* Mon Sep 05 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.7-0.3
- convert docs to UTF-8 (#140871)

* Sat Sep 03 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.7-0.2
- scriptdir to /usr/bin (#167205)

* Sun Aug 28 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.7-0.1
- patch12 from Marius Feraru (#165907)
  TODO: patch11, patch26 and patch27 clash and need verification
- Build without -DDEBUGGING (#156113)

* Sun Aug 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3:5.8.7-0
- 5.8.7
- Dropped the CGI.pm update patches (patch25 and patch29).

* Fri Aug 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3:5.8.6-17
- Don't remove the core modules:
    Filter::Util::Call, Filter::Simple, and Time::HiRes.
- Obsoletes perl-{Filter,Filter-Simple,Time-HiRes}.

* Tue Aug  9 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3:5.8.6-16
- Reformatted the specfile.
- Added the Source0 URL.
- Dropped the MANIFEST.all file for the perl package.
- Dropped the MANIFEST.suidperl file for the suidperl subpackage.

* Wed May 18 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.6-15
- remove unused /tmp/MANIFEST.all (#151801)

* Tue May 17 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.6-14
- CGI.pm 3.10 fixes mod_perl problems (#158036)

* Sun May 15 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.6-13
- Better patch for FindBin.pm (#127023#c37)

* Sat May 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3:5.8.6-12
- New findbin-selinux patch: it now passes the FindBin.t tests
  (patch28 replaces patch23). #118877 #127023
- Remove 5.8.2 ABI compat (#154295 comments 6 and 7).

* Thu Apr 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 3:5.8.6-10
- Apply fixes for CAN-2004-0452, CAN-2005-0155 and CAN-2005-0156 (#156128).

* Tue Apr 26 2005 Warren Togami <wtogami@redhat.com. - 3:5.8.6-8
- -Dinstallusrbinperl=n (#141182 Aaron Sherman)
- remove 5.8.0 and 5.8.1 ABI compat (#154295)

* Sun Apr 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3:5.8.6-7
- Updating CGI.pm from version 3.05 to 3.08 (mod_perl 2.0.0 RC5). (#155839)

* Wed Apr 20 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3:5.8.6-6
- FCGI is not provided by perl (#148847).
- Drop the '.1' suffix from the perl-suidperl subpackage.

* Thu Mar 17 2005 Jason Vas Dias <jvdias@redhat.com> - 3:5.8.6-5
- bug 151127: fix to use libresolv instead of libbind (perl-5.8.6-libresolv.patch).

* Tue Mar  8 2005 Chip Turner <cturner@redhat.com> - 3:5.8.6-4
- add patch to put site_perl and vendor_perl before core perl dirs, to
  allow for overriding modules

* Sat Jan 29 2005 Warren Togami <wtogami@redhat.com> - 3:5.8.6-3
- bugzilla: 127025, fix strip warnings

* Tue Jan 18 2005 Chip Turner <cturner@redhat.com> - 3:5.8.6-2
- bugzilla: 145448, fix invalid utf8 in changelog

* Tue Jan 18 2005 Chip Turner <cturner@redhat.com> - 3:5.8.6-1
- bugzilla: 145447, add 5.8.5 to perlmodcompat list

* Mon Jan 17 2005 Chip Turner <cturner@redhat.com> - 3:5.8.6-1
- update to 5.8.6

* Wed Dec  1 2004 Chip Turner <cturner@redhat.com> 3:5.8.5-13
- rebuild

* Wed Dec  1 2004 Chip Turner <cturner@redhat.com> 3:5.8.5-11
- bugzilla: 140563, nptl doesn't act like linuxthreads; threads have no PIDs

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 3:5.8.5-10
- rebuild against db-4.3.21.

* Tue Oct 12 2004 Jose Pedro Oliveira <jpo@di.uminho.pt>
- Corrected the license information (missing GPL).
- Added the URL tag.
- Removed empty .bs files.
- Eliminated several strip generated messages (bug 127025).
- Corrected problems mentioned in bug 120772
  (updated Ville Skytta)

* Tue Oct 12 2004 Chip Turner <cturner@redhat.com>
- bugzilla: 135303, add more missing 5.8.4 paths

* Mon Oct 11 2004 Tim Waugh <twaugh@redhat.com>
- Build requires groff (bug #135101).

* Tue Oct  5 2004 Chip Turner <cturner@redhat.com> 3:5.8.5-7
- update perlbug patch to strip build date as well

* Mon Aug 23 2004 Chip Turner <cturner@redhat.com> 3:5.8.5-2
- fix conflicting file when building on x86_64 and i386

* Sat Jul 24 2004 Chip Turner <cturner@redhat.com> 3:5.8.5-1
- Add Provides: Carp::Heavy to fix new dep error (bz 128507)

* Thu Jul 22 2004 Chip Turner <cturner@redhat.com> 3:5.8.5-1
- update to 5.8.5

* Mon Jun 28 2004 Chip Turner <cturner@redhat.com> 3:5.8.4-1
- update to 5.8.4, remove patch 8

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr 15 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-18
- add patch to fix empty RPATH issue on perl module compile

* Sat Apr 03 2004 Colin Walters <walters@redhat.com> 3:5.8.3-17
- Apply patch to fix FindBin module when access to cwd is disallowed,
  should solve the MRTG/SELinux cron spam issue

* Tue Mar 23 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-14
- make sure multilib boxes also own the entries in @INC that are in /usr/lib, not just %%_libdir

* Tue Mar  9 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-%%{perlrel}.1
- fix i386-specifics in %%install to arch generic

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-10
- add perl(:MODULE_COMPAT_*) provides; make sure all of @INC is owned by perl package

* Thu Feb 19 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-8
- rebuild

* Thu Feb 19 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-7.9.rhl9
- rebuild

 patch for perl 5.8.4).

* Thu Feb 19 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-7.10.fc1
- rebuild

* Sun Feb 15 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-6
- fix very broken @INC calculations with slightly less broken @INC
  calculations (not perfectly handled but the result is correct)
- fix broken -Dsitearch declaration

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-5
- update incpush patch to better handle multilib

* Fri Jan 23 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-2
- add a dependency filter on perl(Tie::RangeHash)

* Thu Jan 22 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-7
- upgrade to 5.8.3

* Mon Dec 15 2003 Chip Turner <cturner@redhat.com> 3:5.8.2-7
- fix @INC so that all dirs go into it, not just those that exist at buildtime in the build system

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 3:5.8.2-4
- rebuild against db-4.2.52.

* Sun Dec  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 3:5.8.2-3
- Own site and vendor auto directories (#73970).

* Wed Dec  3 2003 Chip Turner <cturner@redhat.com> 3:5.8.2-2
- upgrade to 5.8.2

* Fri Oct 31 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-92
- remove Vendor and Distribution macros from specfile (#108567)

* Wed Oct 15 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-92
- add srand on fork patch from upstream, as well as test case

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 3:5.8.1-91.1
- rebuild against db-4.2.42.

* Thu Sep 25 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-91
- perl 5.8.1 final

* Mon Sep 22 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-90.rc5.3
- ensure inc_version_list is always set properly

* Mon Sep 22 2003 Chip Turner <cturner@redhat.com>
- update to RC5

* Wed Aug 20 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-90.rc4.2
- rebuild

* Wed Aug  6 2003 Chip Turner <cturner@redhat.com>
- bugzilla 101767, make sure threads.so links directly to -lpthread

* Fri Aug  1 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-90.rc2.1
- RC4
- remove perl-5.8.0-fhs.patch since it is integrated now
- remove perl-5.8.0-Safe2.09.patch, unnecessary now

* Fri Jul 11 2003 Chip Turner <cturner@redhat.com> 3:5.8.1-90.rc2.1
- rc2 snapshot

* Thu Jul 10 2003 Chip Turner <cturner@redhat.com> 3:5.8.0-90.rc1
- upgrade to 5.8.1 RC1

* Mon Jul  7 2003 Chip Turner <cturner@redhat.com> 3:5.8.0-89.pre%%{PRELEVEL}.0
- integrate another pre-5.8.1 release

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Chip Turner <cturner@redhat.com> 3:5.8.0-89.pre%%{PRELEVEL}.0
- bump epoch since we went from perl 5.8.1-pre to 5.8.0-pre (ie,
  changed what version perl thought of itself as)

* Mon May  5 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%%{PRELEVEL}.3
- rebuild

* Thu May  1 2003 Chip Turner <cturner@redhat.com>
- bump for rebuilg

* Sun Apr 27 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%%{PRELEVEL}.1
- fix the fix for RPM_BUILD_ROOT substitution

* Tue Apr 22 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%%{PRELEVEL}.3
- fix Config.pm; lost when h2ph changes made

* Thu Apr 17 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%%{PRELEVEL}
- move to latest snapshot, 19261

* Tue Feb 18 2003 Chip Turner <cturner@redhat.com>
- fix MANIFEST.DB_File handling for #83410; problem was unsubstituted
  %%{_libdir} that crept in with multilib

* Tue Feb 18 2003 Bill Nottingham <notting@redhat.com> 5.8.0-87
- clean up backup files from patches (#82838)

* Wed Feb 05 2003 Elliot Lee <sopwith@redhat.com> 5.8.0-86
- Fix up multilib handling to use multilib_64_archs macro, add ppc64.
- Patch100 probably makes sense on all archs, and ifarch'd patches are Bad(tm).

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version the Obsoleted on perl-NDBM_File so users can install newer
- change the Obsoletes on NDBM_File to a Conflicts
  ones than what shipped with 7.3, yet still keep anaconda happy

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan  9 2003 Chip Turner <cturner@redhat.com>
- rebuild

* Sat Jan  4 2003 Jeff Johnson <jbj@redhat.com> 5.8.0-82
- use internal dep generator.

* Thu Jan  2 2003 Chip Turner <cturner@redhat.com>
- fix issue with -Dpager in Pod::Perldoc.pm to properly respect setting once more

* Tue Dec 31 2002 Chip Turner <cturner@redhat.com>
- add rpath fix to prevent building perl from using installed system perl
- massive re-integration of upstream patches to come to common basis (head of perl-maint branch)

* Mon Dec 16 2002 Chip Turner <cturner@redhat.com>
- rebuild

* Sun Dec 15 2002 Chip Turner <cturner@redhat.com>
- add numerous upstream patches to fix utf8/perlio issues
- upgrade Storable, Safe, and Encoding to latest CPAN versions

* Thu Nov  7 2002 Chip Turner <cturner@redhat.com>
- multilib support when building noarch perl modules
- integrate upstream bugfix patches

* Tue Sep 10 2002 Chip Turner <cturner@redhat.com>
- integrate patch for /usr/lib64 instead of /usr/lib from Than Ngo

* Mon Sep  9 2002 Chip Turner <cturner@redhat.com>
- integrate s390/s390x patch from Florian La Roche

* Sun Sep  1 2002 Chip Turner <cturner@redhat.com>
- fix pager issues; default to /usr/bin/less -isr
- more work on pager bug (72125)

* Thu Aug 29 2002 Chip Turner <cturner@redhat.com>
- add a few new directories to h2ph to produce better .ph files

* Thu Aug 15 2002 Chip Turner <cturner@redhat.com>
- change from lynx to links in CPAN.pm

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build
- remove Filter packages and use CPAN ones

* Fri Jul 19 2002 Chip Turner <cturner@redhat.com>
- move to final perl 5.8.0, huzzah!

* Tue Jul 16 2002 Chip Turner <cturner@redhat.com>
- update CPAN, CGI, and DB_File versions; obsolete perl-libnet
- libnet.cfg supplied, default to passive ftp in all cases

* Tue Jun 18 2002 Chip Turner <cturner@redhat.com>
- add patch to ensire libperl.so is linked properly

* Mon May 20 2002 Nalin Dahyabhai <nalin@redhat.com>
- always build with -fPIC

* Thu May  9 2002 Jeff Johnson <jbj@redhat.com>
- rebuild in rawhide

* Sun Mar 31 2002 Chip Turner <cturner@redhat.com>
- split suidperl back out (bug #62215)

* Tue Mar 26 2002 Chip Turner <cturner@redhat.com>
- restructuring of some directories, alteration of @INC

* Thu Dec 20 2001 Chip Turner <cturner@redhat.com>
- remove ndbm completely

* Sun Dec 16 2001 Chip Turner <cturner@redhat.com>
- make rpmlint happy, split out NDBM_File, clean up other spots
- stopped doing grep -v etc in favor of custom script

* Wed Dec 12 2001 Chip Turner <cturner@redhat.com>
- cleaning up of ia64 issues, as well as compatibility with gcc 3.1
  and glibc 2.2.4

* Mon Sep 24 2001 Chip Turner <cturner@redhat.com>
- changing building of extra modules out of the core perl rpm

* Mon Sep 17 2001 Chip Turner <cturner@redhat.com>
- upgrade to 5.6.1, added old INC dirs to maintain compat

* Fri Mar 23 2001 Preston Brown <pbrown@redhat.com>
- bzip2 source, save some space.

* Thu Dec  7 2000 Crutcher Dunnavant <crutcher@redhat.com>
- initial rebuild for 7.1

* Tue Sep 12 2000 Bill Nottingham <notting@redhat.com>
- fix dependencies on ia64/sparc64

* Mon Aug  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- replace the deprecated MD5 with Digest::MD5 (has to be here for cleanfeed)
- obsolete: perl-Digest-MD5
- use syslog instead of mail to report possible attempts to break into suidperl
- force syslog on at build-time

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add Owen's fix for #14779/#14863
- specify cc=%%{__cc}; continue to let cpp sort itself out
- switch shadow support on (#8646)
- release 7

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- strip buildroot from perl pods (#14040)
- release 6

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild (release 5)

* Wed Jun 21 2000 Preston Brown <pbrown@redhat.com>
- don't require tcsh to install, only to build
- release 4

* Mon Jun 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild against new db3 package
- release 3

* Sat Jun 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable 64-bit file support
- change name of package that Perl expects gcc to be in from "egcs" to "gcc"
- move man pages to /usr/share via hints/linux.sh and MM_Unix.pm
- fix problems prefixifying with empty prefixes
- disable long doubles on sparc (they're the same as doubles anyway)
- add an Epoch to make sure we can upgrade from perl-5.00503
- release 2

* Thu Mar 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.6.0

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Fri Jan 14 2000 Jeff Johnson <jbj@redhat.com>
- add provides for perl modules (from kestes@staff.mail.com).

* Mon Oct 04 1999 Cristian Gafton <gafton@redhat.com>
- fix the %%install so that the MD5 module gets actually installed correctly

* Mon Aug 30 1999 Cristian Gafton <gafton@redhat.com>
- make sure the package builds even when we don't have perl installed on the
  system

* Fri Aug 06 1999 Cristian Gafton <gafton@redhat.com>
- merged with perl-MD5
- get rid of the annoying $RPM_BUILD_ROOT paths in the installed tree

* Mon Jul 26 1999 Cristian Gafton <gafton@redhat.com>
- do not link anymore against the system db library (and make each module
  link against it separately, so that we can have Berkeley db1 and db2 mixed
  up)

* Wed Jun 16 1999 Cristian Gafton <gafton@redhat.com>
- use wildcards for files in /usr/bin and /usr/man

* Tue Apr 06 1999 Cristian Gafton <gafton@redhat.com>
- version 5.00503
- make the default man3 install dir be release independent
- try to link against db1 to preserve compatibility with older databases;
  abandoned idea because perl is too broken to allow such an easy change
  (hardcoded names *everywhere* !!!)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- guilty of the inlined Makefile in the spec file
- adapted for the arm build

* Wed Sep 09 1998 Preston Brown <pbrown@redhat.com>
- added newer CGI.pm to the build
- changed the version naming scheme around to work with RPM

* Sun Jul 19 1998 Jeff Johnson <jbj@redhat.com>
- attempt to generate *.ph files reproducibly

* Mon Jun 15 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.004_04-m4 (pre-5.005 maintenance release)

* Tue Jun 12 1998 Christopher McCrory <chrismcc@netus.com
- need stdarg.h from gcc shadow to fix "use Sys::Syslog" (problem #635)

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to correct the .ph constructs unless defined (foo) to read
  unless(defined(foo))

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- fixed strftime problem

* Sun Mar 08 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to fix a security race
- do not use setres[ug]id - those are not implemented on 2.0.3x kernels

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 5.004_04 - 5.004_01 had some nasty memory leaks.
- fixed the spec file to be version-independent

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- Config.pm wasn't right do to the builtrooting

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- fixed arch-specfic part of spec file

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to perl 5.004_01
- users a build root

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Incorporated security patch from Chip Salzenberg <salzench@nielsenmedia.com>

* Fri Feb 07 1997 Erik Troan <ewt@redhat.com>
- Use -Darchname=i386-linux 
- Require csh (for glob)
- Use RPM_ARCH during configuration and installation for arch independence
