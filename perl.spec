%define threading  1
%define largefiles 1
%define suidperl   1

%define multilib_64_archs x86_64 s390x ppc64 sparc64

%define perlver 5.8.0
%define perlrel 88.3
%define perlepoch 2
%define cpanver 1.61
%define dbfilever 1.804
%define cgiver 2.81

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
License: Artistic
Group: Development/Languages

Vendor       : Red Hat, Inc.
Distribution : Red Hat Linux

Source0: ftp://ftp.perl.org/pub/perl/CPAN/src/perl-%{perlver}.tar.bz2
Source1: clean-manifest.pl
Source5: MANIFEST.CPAN
Source6: MANIFEST.CGI
Source7: MANIFEST.DB_File
Source9: MANIFEST.suidperl
Source10: system-owned-directories
Source11: filter-depends.sh
Source12: perl-5.8.0-libnet.cfg

# Patch1: perl-5.6.0-installman.patch
# Patch2: perl5.005_03-db1.patch
# Patch3: perl-5.6.0-nodb.patch
Patch4: perl-5.6.1-prereq.patch
Patch5: perl-5.6.0-root.patch
Patch6: perl-5.8.0-fhs.patch
Patch7: perl-5.6.0-buildroot.patch
Patch8: perl-5.8.0-errno.patch
Patch9: perl-5.7.3-syslog.patch

%define __perl_requires %{SOURCE11}

Conflicts: perl-NDBM_File <= 1:1.75-34.99.6

Obsoletes: perl-Digest-MD5
Obsoletes: perl-MIME-Base64
Obsoletes: perl-libnet
Obsoletes: perl-Storable

# Configure doesn't listen well when we say no ndbm.  When it links in, it then conflicts with berkeley db.  oops.
Patch16: perl-5.8.0-nondbm.patch

# make sure we get the proper ldflags on libperl.so
Patch17: perl-5.8.0-sharedlinker.patch

# perl 5.8.0 likes to use man3ext for BOTH directories AND files.  not kosher.
Patch18: perl-5.8.0-manext.patch

# lynx is depracated, use links instead
Patch19: perl-5.8.0-links.patch

# work around annoying rpath issue
Patch21: perl-5.8.0-rpath-make.patch

# arch-specific patches
Patch100: perl-5.8.0-s390.patch
Patch101: perl-5.8.0-libdir64.patch

# module updates
Patch202: perl-5.8.0-Safe2.09.patch
Patch203: perl-5.8.0-CGI2.89.patch

# security patches
Patch1000: perl-5.8.0-cssfix.patch

# pseudo-official module updates (mostly from cvs, etc)
# Patch300: perl-5.8.0-makemaker-prefix.patch

# upstream patches
Patch17649: perl-5.8.0-upstream-17649.patch
Patch18079: perl-5.8.0-upstream-18079.patch
Patch18080: perl-5.8.0-upstream-18080.patch
Patch18081: perl-5.8.0-upstream-18081.patch
Patch18082: perl-5.8.0-upstream-18082.patch
Patch18087: perl-5.8.0-upstream-18087.patch
Patch18089: perl-5.8.0-upstream-18089.patch
Patch18095: perl-5.8.0-upstream-18095.patch
Patch18096: perl-5.8.0-upstream-18096.patch
Patch18097: perl-5.8.0-upstream-18097.patch
Patch18098: perl-5.8.0-upstream-18098.patch
Patch18100: perl-5.8.0-upstream-18100.patch
Patch18101: perl-5.8.0-upstream-18101.patch
Patch18103: perl-5.8.0-upstream-18103.patch
Patch18104: perl-5.8.0-upstream-18104.patch
Patch18110: perl-5.8.0-upstream-18110.patch
Patch18111: perl-5.8.0-upstream-18111.patch
Patch18112: perl-5.8.0-upstream-18112.patch
Patch18126: perl-5.8.0-upstream-18126.patch
Patch18127: perl-5.8.0-upstream-18127.patch
Patch18128: perl-5.8.0-upstream-18128.patch
Patch18129: perl-5.8.0-upstream-18129.patch
Patch18130: perl-5.8.0-upstream-18130.patch
Patch18131: perl-5.8.0-upstream-18131.patch
Patch18132: perl-5.8.0-upstream-18132.patch
Patch18133: perl-5.8.0-upstream-18133.patch
Patch18134: perl-5.8.0-upstream-18134.patch
Patch18143: perl-5.8.0-upstream-18143.patch
Patch18144: perl-5.8.0-upstream-18144.patch
Patch18145: perl-5.8.0-upstream-18145.patch
Patch18146: perl-5.8.0-upstream-18146.patch
Patch18153: perl-5.8.0-upstream-18153.patch
Patch18155: perl-5.8.0-upstream-18155.patch
Patch18156: perl-5.8.0-upstream-18156.patch
Patch18173: perl-5.8.0-upstream-18173.patch
Patch18174: perl-5.8.0-upstream-18174.patch
Patch18187: perl-5.8.0-upstream-18187.patch
Patch18189: perl-5.8.0-upstream-18189.patch
Patch18190: perl-5.8.0-upstream-18190.patch
Patch18191: perl-5.8.0-upstream-18191.patch
Patch18192: perl-5.8.0-upstream-18192.patch
Patch18197: perl-5.8.0-upstream-18197.patch
Patch18202: perl-5.8.0-upstream-18202.patch
Patch18204: perl-5.8.0-upstream-18204.patch
Patch18205: perl-5.8.0-upstream-18205.patch
Patch18206: perl-5.8.0-upstream-18206.patch
Patch18207: perl-5.8.0-upstream-18207.patch
Patch18208: perl-5.8.0-upstream-18208.patch
Patch18209: perl-5.8.0-upstream-18209.patch
Patch18210: perl-5.8.0-upstream-18210.patch
Patch18211: perl-5.8.0-upstream-18211.patch
Patch18214: perl-5.8.0-upstream-18214.patch
Patch18215: perl-5.8.0-upstream-18215.patch
Patch18218: perl-5.8.0-upstream-18218.patch
Patch18219: perl-5.8.0-upstream-18219.patch
Patch18227: perl-5.8.0-upstream-18227.patch
Patch18234: perl-5.8.0-upstream-18234.patch
Patch18235: perl-5.8.0-upstream-18235.patch
Patch18236: perl-5.8.0-upstream-18236.patch
Patch18241: perl-5.8.0-upstream-18241.patch
Patch18242: perl-5.8.0-upstream-18242.patch
Patch18243: perl-5.8.0-upstream-18243.patch
Patch18247: perl-5.8.0-upstream-18247.patch
Patch18248: perl-5.8.0-upstream-18248.patch
Patch18252: perl-5.8.0-upstream-18252.patch
Patch18253: perl-5.8.0-upstream-18253.patch
Patch18254: perl-5.8.0-upstream-18254.patch
Patch18255: perl-5.8.0-upstream-18255.patch
Patch18256: perl-5.8.0-upstream-18256.patch
Patch18257: perl-5.8.0-upstream-18257.patch
Patch18258: perl-5.8.0-upstream-18258.patch
Patch18271: perl-5.8.0-upstream-18271.patch
Patch18273: perl-5.8.0-upstream-18273.patch
Patch18274: perl-5.8.0-upstream-18274.patch
Patch18275: perl-5.8.0-upstream-18275.patch
Patch18276: perl-5.8.0-upstream-18276.patch
Patch18286: perl-5.8.0-upstream-18286.patch
Patch18289: perl-5.8.0-upstream-18289.patch
Patch18290: perl-5.8.0-upstream-18290.patch
Patch18291: perl-5.8.0-upstream-18291.patch
Patch18293: perl-5.8.0-upstream-18293.patch
Patch18294: perl-5.8.0-upstream-18294.patch
Patch18295: perl-5.8.0-upstream-18295.patch
Patch18296: perl-5.8.0-upstream-18296.patch
Patch18297: perl-5.8.0-upstream-18297.patch
Patch18301: perl-5.8.0-upstream-18301.patch
Patch18322: perl-5.8.0-upstream-18322.patch
Patch18347: perl-5.8.0-upstream-18347.patch
Patch18348: perl-5.8.0-upstream-18348.patch
Patch18349: perl-5.8.0-upstream-18349.patch
Patch18352: perl-5.8.0-upstream-18352.patch
Patch18353: perl-5.8.0-upstream-18353.patch
Patch18359: perl-5.8.0-upstream-18359.patch
Patch18360: perl-5.8.0-upstream-18360.patch
Patch18361: perl-5.8.0-upstream-18361.patch
Patch18362: perl-5.8.0-upstream-18362.patch
Patch18363: perl-5.8.0-upstream-18363.patch
Patch18364: perl-5.8.0-upstream-18364.patch
Patch18365: perl-5.8.0-upstream-18365.patch
Patch18366: perl-5.8.0-upstream-18366.patch
Patch18367: perl-5.8.0-upstream-18367.patch
Patch18368: perl-5.8.0-upstream-18368.patch
Patch18369: perl-5.8.0-upstream-18369.patch
Patch18370: perl-5.8.0-upstream-18370.patch
Patch18375: perl-5.8.0-upstream-18375.patch
Patch18379: perl-5.8.0-upstream-18379.patch
Patch18380: perl-5.8.0-upstream-18380.patch

Patch32000: perl-5.8.0-protofix.patch
Patch32001: perl-5.8.0-pagerfix.patch


Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gawk, grep, tcsh, gdbm-devel, db4-devel, dos2unix

# By definition of 'do' (see 'man perlfunc') this package provides all
# versions of perl previous to it.
Provides: perl <= %{epoch}:%{version}

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

# XXX needed by perl-libnet
Provides: perl(Mac::Files)

# XXX needed by perl-CGI
Provides: perl(FCGI)

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

%package CPAN
Version: %{cpanver}
Release: %{perlrel}
Summary: CPAN module for Perl
Group: Development/Languages
Requires: perl >= %{perlepoch}:%{perlver}-%{perlrel}

%description CPAN
CPAN modules for Perl

%package CGI
Version: %{cgiver}
Release: %{perlrel}
Summary: CGI modules for Perl
Group: Development/Languages
Requires: perl >= %{perlepoch}:%{perlver}-%{perlrel}

%description CGI
CGI modules for Perl

%package DB_File
Version: %{dbfilever}
Release: %{perlrel}
Summary: DB_File module for Perl
Group: Development/Languages
Requires: perl >= %{perlepoch}:%{perlver}-%{perlrel}

%description DB_File
DB_File modules for Perl

%if %{suidperl}
%package suidperl
Version: %{perlver}
Release: %{perlrel}
Summary: suidperl, for use with setuid perl scripts
Group: Development/Languages
Requires: perl = %{perlepoch}:%{perlver}-%{perlrel}

%description suidperl
suidperl is a setuid binary copy of perl that allows for (hopefully)
more secure running of setuid perl scripts.
%endif

%prep
%setup -q
# %patch1 -p1 -b .instman
# Perl does not have a single entry point to define what db library to use
# so the patch below is mostly broken...
#%patch2 -p1
# %patch3 -p1 -b .nodb
#%patch4 -p1 -b .prereq
%patch5 -p1
%patch6 -p1
#%xpatch7 -p1 -b .buildroot
%patch8 -p1
%patch9 -p1
#%%patch10 -p1 -b .incs

# %xpatch16 -p1 -b .nondbm

%patch17 -p1

%patch18 -p1
%patch19 -p1
%patch21 -p1

%patch100 -p1

%ifarch %{multilib_64_archs}
%patch101 -p1
%endif

%patch202 -p1
%patch203 -p1

%patch1000 -p1

# this is ugly, but apparently necessary.
/usr/bin/dos2unix win32/Makefile win32/makefile.mk README.win32 README.dos jpl/JNI/JNI.xs jpl/JNI/Makefile.PL

%patch17649 -p1
%patch18079 -p1
%patch18080 -p1
%patch18081 -p1
%patch18082 -p1
%patch18087 -p1
%patch18089 -p1
%patch18095 -p1
%patch18096 -p1
%patch18097 -p1
%patch18098 -p1 
%patch18100 -p1
%patch18101 -p1
%patch18103 -p1
%patch18104 -p1
%patch18110 -p1
%patch18111 -p1
%patch18112 -p1
%patch18126 -p1
%patch18127 -p1
%patch18128 -p1
%patch18129 -p1
%patch18130 -p1
%patch18131 -p1
%patch18132 -p1
%patch18133 -p1
%patch18134 -p1
%patch18143 -p1
%patch18144 -p1
%patch18145 -p1
%patch18146 -p1
%patch18153 -p1
%patch18155 -p1
%patch18156 -p1
%patch18173 -p1
%patch18174 -p1
%patch18187 -p1
%patch18189 -p1
%patch18190 -p1
%patch18191 -p1
%patch18192 -p1
%patch18197 -p1
%patch18202 -p1
%patch18204 -p1
%patch18205 -p1
%patch18206 -p1
%patch18207 -p1
%patch18208 -p1
%patch18209 -p1
%patch18210 -p1
%patch18211 -p1
%patch18214 -p1
%patch18215 -p1
%patch18218 -p1
%patch18219 -p1
%patch18227 -p1
%patch18234 -p1
%patch18235 -p1
%patch18236 -p1
%patch18241 -p1
%patch18242 -p1
%patch18243 -p1
%patch18247 -p1
%patch18248 -p1
%patch18252 -p1
%patch18253 -p1
%patch18254 -p1
%patch18255 -p1
%patch18256 -p1
%patch18257 -p1
%patch18258 -p1
%patch18271 -p1
%patch18273 -p1
%patch18274 -p1
%patch18275 -p1
%patch18276 -p1
%patch18286 -p1
%patch18289 -p1
%patch18290 -p1
%patch18291 -p1
%patch18293 -p1
%patch18294 -p1
%patch18295 -p1
%patch18296 -p1
%patch18297 -p1
%patch18301 -p1
%patch18322 -p1
%patch18347 -p1
%patch18348 -p1
%patch18349 -p1
%patch18352 -p1
%patch18353 -p1
%patch18359 -p1
%patch18360 -p1
%patch18361 -p1
%patch18362 -p1
%patch18363 -p1
%patch18364 -p1
%patch18365 -p1
%patch18366 -p1
%patch18367 -p1
%patch18368 -p1
%patch18369 -p1
%patch18370 -p1
%patch18375 -p1
%patch18379 -p1
%patch18380 -p1

%patch32000 -p1
%patch32001 -p1

find . -name \*.orig -exec rm -fv {} \;

%build

echo "RPM Build arch: %{_arch}"

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# yes; don't use %_libdir so that noarch packages from other OSs
# arches work correctly :\ the Configure lines below hardcode lib for
# similar reasons.

%ifarch %{multilib_64_archs}
	mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}
	mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/%{perlver}
	mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/vendor_perl/%{perlver}
%endif

sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
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
	-Dsitearch="%{_libdir}/perl5/site_perl/%{perlver}" \
	-Dvendorarch="%{_libdir}/perl5/vendor_perl/%{perlver}/%{_arch}-%{_os}%{thread_arch}" \
%endif
	-Darchname=%{_arch}-%{_os} \
%ifarch sparc
	-Ud_longdbl \
%endif
	-Dvendorprefix=%{_prefix} \
	-Dsiteprefix=%{_prefix} \
	-Dotherlibdirs=/usr/lib/perl5/%{perlver} \
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
	-Dinstallusrbinperl \
	-Ubincompat5005 \
	-Uversiononly \
	-Dpager='/usr/bin/less -isr'

make -f Makefile

make -f Makefile test || /bin/true

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install -f Makefile

%ifarch %{multilib_64_archs}
mkdir -p ${RPM_BUILD_ROOT}/usr/lib64/perl5/vendor_perl/%{perlver}/%{_arch}-%{_os}
%endif

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 utils/pl2pm ${RPM_BUILD_ROOT}%{_bindir}/pl2pm

# Generate *.ph files with a trick. Is this sick or what ?
make all -f - <<EOF
PKGS	= glibc-devel gdbm-devel gpm-devel libgr-devel libjpeg-devel \
	  libpng-devel libtiff-devel ncurses-devel popt \
	  zlib-devel binutils libelf e2fsprogs-devel pam pwdb \
	  rpm-devel
STDH	= \$(filter %{_includedir}/include/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' \$(PKGS)))
STDH	+=\$(wildcard %{_includedir}/linux/*.h) \
	  \$(wildcard %{_includedir}/bits/*.h)  \
	  \$(wildcard %{_includedir}/sys/*.h)  \
	  \$(wildcard %{_includedir}/scsi/*.h) 
# \$(wildcard %{_includedir}/asm/*.h)
GCCDIR	= \$(shell gcc --print-file-name include)
GCCH	= \$(filter \$(GCCDIR)/%%, \$(shell rpm -q --queryformat '[%%{FILEMODES} %%{FILENAMES}\n]' gcc | grep -v ^4 | awk '{print $NF}'))

PERLLIB = \$(RPM_BUILD_ROOT)%{_libdir}/perl5/%{perlver}
ARCHLIB = \$(RPM_BUILD_ROOT)%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}
PERL	= LD_PRELOAD=\$(RPM_BUILD_DIR)/perl-%{perlver}/libperl.so LD_LIBRARY_PATH=\$(ARCHLIB)/CORE PERL5LIB=\$(PERLLIB) \$(RPM_BUILD_ROOT)%{_bindir}/perl
PHDIR	= \$(PERLLIB)/\${RPM_ARCH}-linux*
H2PH	= \$(PERL) \$(RPM_BUILD_ROOT)%{_bindir}/h2ph -d \$(PHDIR)/

all: std-headers gcc-headers fix-config

std-headers: \$(STDH)
	cd %{_includedir} && \$(H2PH) \$(STDH:%{_includedir}/%%=%%)

gcc-headers: \$(GCCH)
	cd \$(GCCDIR) && \$(H2PH) \$(GCCH:\$(GCCDIR)/%%=%%) || true

fix-config: \$(PHDIR)/Config.pm
	\$(PERL) -i -p -e "s|\$(RPM_BUILD_ROOT)||g;" \$<

EOF

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

# build MANIFEST.all

%define new_perl_lib $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}
%define new_arch_lib $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}
%define new_perl_flags LD_LIBRARY_PATH=%{new_arch_lib}/CORE PERL5LIB=%{new_perl_lib}
%define new_perl %{new_perl_flags} $RPM_BUILD_ROOT/%{_bindir}/perl

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/perl5/5.8.0/Net
install -m 0644 %{SOURCE12} $RPM_BUILD_ROOT/%{_libdir}/perl5/5.8.0/Net/libnet.cfg

find $RPM_BUILD_ROOT -name '*HiRes*' | xargs rm -rfv
find $RPM_BUILD_ROOT -name '*Filter*' | xargs rm -rfv
find $RPM_BUILD_ROOT -name '*NDBM*' | xargs rm -rfv

find $RPM_BUILD_ROOT -type f -or -type l > MANIFEST.all
find $RPM_BUILD_ROOT -type d -printf "%%%%dir %p\n" >> MANIFEST.all

%{new_perl} -i -p -e "s|$RPM_BUILD_ROOT||g;" MANIFEST.all
cp MANIFEST.all /tmp

for i in  %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE10} 
do
  %{new_perl} %{SOURCE1} %{_arch} $i MANIFEST.all MANIFEST.all.tmp %{_libdir} %{thread_arch}
  mv MANIFEST.all.tmp MANIFEST.all
done

%if %{suidperl}
  %{new_perl} %{SOURCE1} %{_arch} %{SOURCE9} MANIFEST.all MANIFEST.all.tmp %{_libdir} %{thread_arch}
  mv MANIFEST.all.tmp MANIFEST.all
%endif

# fix the rest of the stuff
find $RPM_BUILD_ROOT%{_libdir}/perl* -name .packlist -o -name perllocal.pod | \
%{new_perl_flags} xargs $RPM_BUILD_ROOT/%{_bindir}/perl -I lib/ -i -p -e "s|$RPM_BUILD_ROOT||g;" MANIFEST.all

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files -f MANIFEST.all
%defattr(-,root,root)
%config %{_libdir}/perl5/5.8.0/Net/libnet.cfg

%files -f %{SOURCE5} CPAN
%defattr(-,root,root)

%files -f %{SOURCE6} CGI
%defattr(-,root,root)

%files -f %{SOURCE7} DB_File
%defattr(-,root,root)

%if %{suidperl}
%files -f %{SOURCE9} suidperl
%defattr(-,root,root)
%endif

%changelog
* Tue Aug 12 2003 Chip Turner <cturner@redhat.com> 2:5.8.0-88.1
- fix for CAN-2003-0615

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
