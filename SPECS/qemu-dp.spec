%global package_speccommit 70b2940b038dbb66bae0f7fee55236ca2eb6d138
%global usver 2.12.0
%global xsver 2.0.12
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit v2.12.0-rc2
Summary: qemu-dp storage datapath
Name: qemu-dp
Epoch: 2
Version: 2.12.0
Release: %{?xsrel}%{?dist}
License: GPL
Requires: jemalloc
Requires: kernel >= 4.19.19-5.0.0
Source0: qemu-dp-2.12.0.tar.gz
Patch0: update_coverity_model
Patch1: 01-make-a-qemu-dp-build.patch
Patch2: 02-do-not-register-xen-backends.patch
Patch3: 03-added-xen-watch-domain-qmp.patch
Patch4: 04-make-blockdev-snapshot-use.patch
Patch5: 05-send-stdout-and-stderr-to.patch
Patch6: 06-add-a-trace-file-to-control.patch
Patch7: 07-do-not-use-iothread-for.patch
Patch8: 08-remove-unwanted-crypto.patch
Patch9: 09-use-libaio-by-default-and.patch
Patch10: 10-add-qmp_relink_chain-command.patch
Patch11: 11-log-errno-on-ioctl-failure.patch
Patch12: 12-improve-xen_disk-batching.patch
Patch13: 13-improve-xen_disk-response.patch
Patch14: 14-adjust-qcow2-default-cache.patch
Patch15: 15-avoid-repeated-memory.patch
Patch16: 16-add-xen-unwatch-domain-qmp.patch
Patch17: 17-detach-aio-context-before-bs-free.patch
Patch18: 18-fix-file-and-filename.patch
Patch19: 19-xen-add-a-meaningful.patch
Patch20: 20-xen_backend-add-grant-table.patch
Patch21: 21-xen_disk-remove-open-coded-use.patch
Patch22: 22-xen_backend-add-an-emulation.patch
Patch23: 23-xen_disk-remove-use-of-grant.patch
Patch24: 24-avoid-trying-to-clean-an-empty.patch
Patch25: 25-flush-all-block-drivers-on.patch
Patch26: 26-speed-up-nbd_cmd_block_status.patch
Patch27: 27-limit-logging-of-ioreq_parse.patch
Patch28: CA-320100__drain_pv_ring_on_unwatch
Patch29: backport_query_anonymous_BBs
Patch30: no-dom0-libs.patch
BuildRequires: libaio-devel glib2-devel
# This doesn't look like it should be necessary but the configure isn't clever enough to not require it
BuildRequires: pixman-devel
BuildRequires: xen-libs-devel
BuildRequires: libseccomp-devel zlib-devel
%{?_cov_buildrequires}

%description
This package contains Qemu, but builds only tools and a limited qemu-dp which handles
the storage datapath.

%prep
%autosetup -p1
%{?_cov_prepare}

%build
%{?_cov_make_model:%{_cov_make_model scripts/coverity-model.c}}
./configure --cc=gcc --cxx=/dev/null --enable-xen --target-list=i386-softmmu --source-path=. \
    --prefix=%{_prefix} --libdir=%{_libdir} --bindir=%{_libdir}/qemu-dp/bin --datadir=%{_datarootdir} \
    --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --sysconfdir=%{_sysconfdir} \
    --enable-werror --enable-libusb --enable-trace-backend=syslog \
    --disable-kvm --disable-docs --disable-guest-agent --disable-sdl \
    --disable-curses --disable-curl --disable-gtk --disable-bzip2 \
    --disable-strip --disable-gnutls --disable-nettle --disable-gcrypt \
    --disable-vhost-net --disable-vhost-scsi --disable-vhost-vsock --disable-vhost-user \
    --disable-lzo --disable-tpm --disable-virtfs --disable-tcg --disable-tcg-interpreter \
    --disable-replication --disable-qom-cast-debug --disable-slirp \
    --audio-drv-list= --disable-live-block-migration \
    --disable-libusb \
    --enable-seccomp --enable-qemudp
%{?_cov_wrap} %{__make} %{?_smp_mflags} V=1 all

%install
mkdir -p %{buildroot}%{_libdir}/qemu-dp/bin

rm -rf %{buildroot}
%{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/include %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/libcacard.*a \
       %{buildroot}/usr/share/locale %{buildroot}%{_datarootdir} %{buildroot}%{_libexecdir} \
       %{buildroot}%{_libdir}/qemu-dp/bin/ivshmem-* %{buildroot}%{_libdir}/qemu-dp/bin/qemu-system-i386
install -m 644 qemu-dp-tracing "%{buildroot}%{_libdir}/qemu-dp/bin/qemu-dp-tracing"
%{?_cov_install}

%files
%dir %{_libdir}/qemu-dp/
%{_libdir}/qemu-dp/bin

%{?_cov_results_package}

%changelog
* Wed Nov 17 2021 Mark Syms <mark.syms@citrix.com> - 2.12.0-2.0.12
- Rebuild

* Tue Mar 30 2021 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.11
- Reduce dependencies on Xen libraries

* Tue Dec  8 2020 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.10
- Configure static analysis

* Wed Nov 25 2020 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.9
- Rebase koji build

* Thu Nov  5 2020 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.8
- Remove unnecessary BuildRequires

* Wed Sep 16 2020 Mark Syms <mark.syms@citrix.com> - 2.12.0-2.0.7
- CP-34899: Update coverity model with g_hash_table_insert
- CP-34899: Add g_array_append_vals to model

* Thu Jul  2 2020 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.6
- Remove unnecessary Xen dependencies

* Fri Mar 13 2020 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.5
- CP-33183: Backport "block/qapi: Include anonymous BBs in query-blockstats"

* Mon Jun  3 2019 Mark Syms <mark.syms@citrix.com> - 2:2.12.0-2.0.4
- Drain the PV ring as part of unwatch

* Fri Apr 05 2019 Tim Smith <tim.smith@citrix.com> - 2:2.12.0-2.0.3
- CA-314386 limit ioreq_parse() errors to avoid log storm

* Thu Mar 21 2019 Tim Smith <tim.smith@citrix.com> - 2:2.12.0-2.0.2
- CA-312853 drop background cache cleaner

* Wed Feb 27 2019 Tim Smith <tim.smith@citrix.com> - 2:2.12.0-2.0.1
- CA-311595 Improve defence against cleaning dead caches

* Wed Feb  6 2019 Tim Smith <tim.smith@citrix.com> - 2:2.12.0-2.0.0
- CA-308852 Speed up NBD_CMD_BLOCK_STATUS
- CA-307294 QCow2 cache clean timers called with null cache
- CA-300339 backport patches to remove grant map/unmap
- Drop qemu_trad_image.py as it's device model related

* Thu Aug 16 2018 Mark Syms <mark.syms@citrix.com> - 2.12.0-1.10.0
- CA-295665 More problems with relink_chain

* Mon Aug 06 2018 Mark Syms <mark.syms@citrix.com> - 2.12.0-1.9.0
- CA-294291 Improve the xen_disk responsiveness patch
- CA-294961 Set up QCOW2 default cache sizes
- CA-294963 Clear base parents list during relink-chain

* Wed Jul 25 2018 Mark Syms <mark.syms@citrix.com> - 2.12.0-1.8.0
- CA-294291 Drop MMAP_THRESHOLD patch and fix xen_disk memory allocation

* Tue Jun 12 2018 Mark Syms <mark.syms@citrix.com> - 2.12.0-1.7.0
- CA-290361 Fix "Can't specify 'file' and 'filename'" error

* Mon Jun 04 2018 Mark Syms <mark.syms@citrix.com> - 2.12.0-1.6.0
- CA-290361 Patch use-after-free and add check

* Tue May 29 2018 marksy <mark.syms@citrix.com> - 2.12.0-1.5.0
- CA-290505 correct double-insert when renaming BS

* Fri May 18 2018 marksy <mark.syms@citrix.com> - 2.12.0-1.4.0
- CP-28012: Correct some documentation
- [CP-28077 CP-28099] Update patch series for unwatch-domain
- CP-28099 Don't try to unplug in qemu-dp
- CP-28099 fix xen-watch-domain bug

* Fri Apr 27 2018 Tim Smith <tim.smith@citrix.com> - 2:2.12.0-1.3.0
- Updated to v2.12.0-rc2 (Announces as 2.12.0)
- Reinstate coroutine pools
- Install qemu-dp-tracing file

* Wed Mar 28 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.10.2-3.0.0
- Adjust dmops patch after backporting final version
- CA-266841: Improve VNC performance over long, thin pipes
- migration: Check return value of qemu_fclose
- CP-25629: Don't record QEMU's state in xenstore
- CA-267326: Backport VGA fixes including CVE-2018-5683
- CP-26998: Reintroduce QEMU vCPU hot-(un)plug patches
- CA-283664: Fix using QEMU upstream with libxl
- CP-23325: GVT-g: Save errno earlier
- CP-23325: Fix error handling issues in AMD GPU patch
- CP-23325: GVT-g: Check for allocation failure
- CP-23325: vgpu: Log sendto errors
- CP-24243: GVT-d: Use UPT instead of legacy mode
- CA-284366: Fix use of MSI-X with passthrough devices
- CP-23969 Introduce xen-pvdevice save state and upgrade into it
- CA-267326: Fix cirrus crash found by fuzzing
- CA-285409: Fix Windows RTC issues
- Enable e1000 device model for debug purposes
- CP-27303: Change QEMU vGPU communication with DEMU to fifo
- CA-285385: Backport qemu-trad vgpu-migrate patch, to allow vgpu migration
- CA-285493: Turn on PCI passthrough permissive mode

* Thu Aug 31 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.10.0-1
- Update to QEMU v2.10.0.

* Tue Jun 16 2015 Ross Lagerwall <ross.lagerwall@citrix.com>
- Update for Xen 4.5.

* Tue Apr 8 2014 Frediano Ziglio <frediano.ziglio@citrix.com>
- First packaging
