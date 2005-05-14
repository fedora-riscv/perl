%define threading  1
%define largefiles 1
%define suidperl   1

%define multilib_64_archs x86_64 s390x ppc64 sparc64

%define perlver 5.8.6
%define perlrel 12
%define perlepoch 3

Provides: perl(:WITH_PERLIO)

%if %{threading}
%define thread_arch -thread-multi
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
%else
%define thread_arch %{nil}
Provides: perl(:WITHOUT_ITHREADS)
Provides: perl(:WITHOUT_THREADS)
%endif

%define perlmodcompat 5.8.5 5.8.4 5.8.3
Provides: perl(:MODULE_COMPAT_5.8.3)
Provides: perl(:MODULE_COMPAT_5.8.4)
Provides: perl(:MODULE_COMPAT_5.8.5)
Provides: perl(:MODULE_COMPAT_5.8.6)

%if %{largefiles}
Provides: perl(:WITH_LARGEFILES)
%else
Provides: perl(:WITHOUT_LARGEFILES)
%endif

Summary: The Perl programming language.
Name: perl
Version: %{perlver}
Release: %{perlrel}
Epoch: %{perlepoch}
License: Artistic or GPL
Group: Development/Languages
Url: http://www.perl.org/

Source0: perl-5.8.6.tar.gz
Source1: clean-manifest.pl
Source9: MANIFEST.suidperl
Source10: system-owned-directories
Source11: filter-depends.sh
Source12: perl-5.8.0-libnet.cfg

Patch5: perl-5.8.0-root.patch
# Patch6: perl-5.8.0-fhs.patch
Patch7: perl-5.6.0-buildroot.patch
# Patch8: perl-5.8.0-errno.patch
Patch9: perl-5.7.3-syslog.patch
# Patch10: perl-5.8.0-notty.patch
Patch11: perl-5.8.3-fullinc.patch
Patch12: perl-5.8.6-incpush.patch
Patch13: perl-5.8.3-perlbug-tag.patch
Patch14: perl-5.8.5-dashI.patch
Patch15: perl-5.8.5-incorder.patch

%define __perl_requires %{SOURCE11}

Conflicts: perl-NDBM_File <= 1:1.75-34.99.6

Obsoletes: perl-Digest-MD5
Obsoletes: perl-MIME-Base64
Obsoletes: perl-libnet
Obsoletes: perl-Storable
Obsoletes: perl-CGI
Obsoletes: perl-CPAN
Obsoletes: perl-DB_File

# Configure doesn't listen well when we say no ndbm.  When it links in, it then conflicts with berkeley db.  oops.
Patch16: perl-5.8.0-nondbm.patch

# make sure we get the proper ldflags on libperl.so
Patch17: perl-5.8.0-sharedlinker.patch

# perl 5.8.0 likes to use man3ext for BOTH directories AND files.  not kosher.
# Patch18: perl-5.8.0-manext.patch

# lynx is depracated, use links instead
Patch19: perl-5.8.0-links.patch

# work around annoying rpath issue
Patch21: perl-5.8.0-rpath-make.patch

# bugzilla 101767, make sure threads.so links directly to -lpthread
Patch22: perl-5.8.1-lpthread-link.patch

# fix empty RPATH security issue
Patch24: perl-5.8.3-empty-rpath.patch

# mod_perl 2.0.0 RC5 requires CGI.pm 3.08
Patch25: perl-5.8.6-CGI-3.08.patch

# CAN-2004-0452 fix
Patch26: perl-5.8.0-rmtree.patch

# CAN-2005-0155 and CAN-2005-0156 fix
Patch27: perl-5.8.5-CAN-2005-0155+0156.patch

# bugzilla 118877, 127023
Patch28: perl-5.8.6-findbin-selinux.patch

# arch-specific patches
Patch100: perl-5.8.1-fpic.patch
Patch101: perl-5.8.0-libdir64.patch

Patch32002: perl-5.8.0-nptlhint.patch

Patch32003: perl-5.8.6-libresolv.patch

# module updatesd
# Patch202: perl-5.8.0-Safe2.09.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gawk, grep, tcsh, gdbm-devel, db4-devel, dos2unix, man, groff

# By definition of 'do' (see 'man perlfunc') this package provides all
# versions of perl previous to it.
Provides: perl <= %{epoch}:%{version}

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

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

# These modules appear to be missing or break assumptions made by the
# dependency analysis tools.  Typical problems include refering to
# CGI::Apache as Apache and having no package line in CPAN::Nox.pm. I
# hope that the perl people fix these to work with our dependency
# engine or give us better dependency tools.
#
# Provides: perl(Apache)
# Provides: perl(ExtUtils::MM_Mac)
# Provides: perl(ExtUtils::XSSymSet)
# Provides: perl(LWP::UserAgent)
# Provides: perl(URI::URL)

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

%if %{suidperl}
%package suidperl
Summary: suidperl, for use with setuid perl scripts
Group: Development/Languages
Requires: perl = %{perlepoch}:%{perlver}-%{perlrel}

%description suidperl
suidperl is a setuid binary copy of perl that allows for (hopefully)
more secure running of setuid perl scripts.
%endif

%prep
%setup -q -n perl-5.8.6
%patch5 -p1
# %%patch8 -p1 
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%patch17 -p1

%patch19 -p1
%patch21 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p0
%patch28 -p1

%patch100 -p1

%ifarch %{multilib_64_archs}
%patch101 -p1
%endif

%patch32002 -p1

%patch32003 -p1

find . -name \*.orig -exec rm -fv {} \;

%build

echo "RPM Build arch: %{_arch}"

rm -rf $RPM_BUILD_ROOT

# yes; don't use %_libdir so that noarch packages from other OSs
# arches work correctly :\ the Configure lines below hardcode lib for
# similar reasons.

%ifarch %{multilib_64_archs}
	mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}
	mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/%{perlver}
	mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/vendor_perl/%{perlver}
%endif

sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
	-Dversion=5.8.6 \
	-Dmyhostname=localhost \
	-Dperladmin=root@localhost \
	-Dcc='%{__cc}' \
        -Dcf_by='Red Hat, Inc.' \
	-Dinstallprefix=$RPM_BUILD_ROOT%{_prefix} \
	-Dprefix=%{_prefix} \
%ifarch %{multilib_64_archs}
	-Dlibpth="/usr/local/lib64 /lib64 /usr/lib64" \
	-Dprivlib="/usr/lib/perl5/%{version}" \
	-Dsitelib="/usr/lib/perl5/site_perl/%{version}" \
	-Dvendorlib="/usr/lib/perl5/vendor_perl/%{version}" \
	-Darchlib="%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}" \
	-Dsitearch="%{_libdir}/perl5/site_perl/%{perlver}/%{_arch}-%{_os}%{thread_arch}" \
	-Dvendorarch="%{_libdir}/perl5/vendor_perl/%{perlver}/%{_arch}-%{_os}%{thread_arch}" \
%endif
	-Darchname=%{_arch}-%{_os} \
%ifarch sparc
	-Ud_longdbl \
%endif
	-Dvendorprefix=%{_prefix} \
	-Dsiteprefix=%{_prefix} \
	-Duseshrplib \
%if %threading
	-Dusethreads \
        -Duseithreads \
%else
	-Uusethreads \
        -Uuseithreads \
%endif
%if %largefiles
        -Duselargefiles \
%else
        -Uuselargefiles \
%endif
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
	-Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_endprotoent_r_proto -Ud_endservent_r_proto \
	-Ud_sethostent_r_proto -Ud_setprotoent_r_proto -Ud_setservent_r_proto \
	-Dinc_version_list='%{perlmodcompat}' 

make

make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install -f Makefile

pushd $RPM_BUILD_ROOT/%{_libdir}/perl5
for i in %{perlmodcompat}; do
    mkdir -pm 755 $i/%{_arch}-%{_os}%{thread_arch}/CORE
    mkdir -pm 755 $i/%{_arch}-%{_os}%{thread_arch}/auto
    pushd $i/%{_arch}-%{_os}%{thread_arch}/CORE
      ln -s ../../../%{perlver}/%{_arch}-%{_os}%{thread_arch}/CORE/libperl.so libperl.so
    popd
  done
popd

%ifarch %{multilib_64_archs}
mkdir -p ${RPM_BUILD_ROOT}/usr/lib64/perl5/vendor_perl/%{perlver}/%{_arch}-%{_os}
%endif

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 utils/pl2pm ${RPM_BUILD_ROOT}%{_bindir}/pl2pm

# build MANIFEST.all

%define new_perl_lib  $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}:$RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}
%define comp_perl_lib $RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}:$RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}
%define new_arch_lib  $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}
%define comp_arch_lib $RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}

%define new_perl_flags LD_PRELOAD=/%{new_arch_lib}/CORE/libperl.so LD_LIBRARY_PATH=%{new_arch_lib}/CORE PERL5LIB=%{new_perl_lib}:%{comp_perl_lib}
%define new_perl %{new_perl_flags} $RPM_BUILD_ROOT/%{_bindir}/perl

for i in asm/termios.h syscall.h syslimits.h syslog.h sys/ioctl.h sys/socket.h sys/time.h wait.h
do
  %{new_perl} $RPM_BUILD_ROOT/%{_bindir}/h2ph -a \
              -d $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch} $i || /bin/true
done

%{new_perl} -p -i -e "s|$RPM_BUILD_ROOT||g;" %{new_arch_lib}/Config.pm

for dir in $(%{new_perl} -le 'print join("\n", @INC)' | grep '^/usr/lib')
do
  mkdir -p $RPM_BUILD_ROOT/$dir
done

for dir in $(%{new_perl} -le 'print join("\n", @INC)' | grep '^%{_libdir}')
do
  mkdir -p $RPM_BUILD_ROOT/$dir
done

for i in %{perlver} %{perlmodcompat} ; do
  mkdir -pm 755 $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl/$i/%{_arch}-%{_os}%{thread_arch}/auto
  mkdir -pm 755 $RPM_BUILD_ROOT%{_libdir}/perl5/vendor_perl/$i/%{_arch}-%{_os}%{thread_arch}/auto
done


%ifarch %{multilib_64_archs}
mkdir -pm 755 $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/%{perlver}
mkdir -pm 755 $RPM_BUILD_ROOT/usr/lib/perl5/vendor_perl/%{perlver}
%endif

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perlver}/Net
install -m 0644 %{SOURCE12} $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perlver}/Net/libnet.cfg

find $RPM_BUILD_ROOT -name '*HiRes*' | xargs rm -rfv
find $RPM_BUILD_ROOT -name '*Filter*' | xargs rm -rfv
find $RPM_BUILD_ROOT -name '*NDBM*' | xargs rm -rfv

find $RPM_BUILD_ROOT -type f -name '*.bs' -a -empty -exec rm -f {} ';'

find $RPM_BUILD_ROOT -type f -or -type l > MANIFEST.all
find $RPM_BUILD_ROOT -type d -printf "%%%%dir %p\n" >> MANIFEST.all

%{new_perl} -i -p -e "s|$RPM_BUILD_ROOT||g;" MANIFEST.all

# add .gz to all the entries in the man directories.  necessary since
# brp-compress takes place after the manifest is built but the %files
# section must match what it ends up renaming files into
%{new_perl} -i -p -e 's((^/usr/share/man/.*))($1.gz)g' MANIFEST.all

cp MANIFEST.all /tmp

for i in  %{SOURCE10} 
do
  %{new_perl} %{SOURCE1} %{_arch} $i MANIFEST.all MANIFEST.all.tmp %{_libdir} %{thread_arch}
  mv MANIFEST.all.tmp MANIFEST.all
done

%if %{suidperl}
  %{new_perl} %{SOURCE1} %{_arch} %{SOURCE9} MANIFEST.all MANIFEST.all.tmp %{_libdir} %{thread_arch}
  mv MANIFEST.all.tmp MANIFEST.all
%endif

# fix the rest of the stuff
find $RPM_BUILD_ROOT%{_libdir}/perl* \
  -name .packlist -o -name perllocal.pod -o -name config.h | \
    %{new_perl_flags} xargs $RPM_BUILD_ROOT/%{_bindir}/perl -I lib/ -i -p -e "s|$RPM_BUILD_ROOT||g;" MANIFEST.all

chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files -f MANIFEST.all
%defattr(-,root,root,-)

%if %{suidperl}
%files -f %{SOURCE9} suidperl
%defattr(-,root,root,-)
%endif

%changelog
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
- make sure multilib boxes also own the entries in @INC that are in /usr/lib, not just %_libdir

* Tue Mar  9 2004 Chip Turner <cturner@redhat.com> 3:5.8.3-%{perlrel}.1
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

* Mon Jul  7 2003 Chip Turner <cturner@redhat.com> 3:5.8.0-89.pre%{PRELEVEL}.0
- integrate another pre-5.8.1 release

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Chip Turner <cturner@redhat.com> 3:5.8.0-89.pre%{PRELEVEL}.0
- bump epoch since we went from perl 5.8.1-pre to 5.8.0-pre (ie,
  changed what version perl thought of itself as)

* Mon May  5 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%{PRELEVEL}.3
- rebuild

* Thu May  1 2003 Chip Turner <cturner@redhat.com>
- bump for rebuilg

* Sun Apr 27 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%{PRELEVEL}.1
- fix the fix for RPM_BUILD_ROOT substitution

* Tue Apr 22 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%{PRELEVEL}.3
- fix Config.pm; lost when h2ph changes made

* Thu Apr 17 2003 Chip Turner <cturner@redhat.com> 2:5.8.1-0.pre%{PRELEVEL}
- move to latest snapshot, 19261

* Tue Feb 18 2003 Chip Turner <cturner@redhat.com>
- fix MANIFEST.DB_File handling for #83410; problem was unsubstituted
  %{_libdir} that crept in with multilib

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
- specify cc=%{__cc}; continue to let cpp sort itself out
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
