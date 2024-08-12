%global package_speccommit f6a955254753ba1d72e2573e399de4a7dc80b11e
%global usver 7.0.0
%global xsver 15
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit v7.0.0

# submodule ui/keycodemapdb
%define keycodemapdb_cset e15649b83a78f89f57205927022115536d2c1698
%define keycodemapdb_path ui/keycodemapdb

Summary: qemu-dp storage datapath
Name: qemu-dp
Epoch: 2
Version: 7.0.0
Release: %{?xsrel}%{?dist}
License: GPL
Requires: kernel >= 4.19.19-5.0.0
Source0: qemu-dp-7.0.0.tar.gz
Source1: keycodemapdb-e15649b83a78f89f57205927022115536d2c1698.tar.gz
Patch0: hw-xen-avoid-crash-when
Patch1: ensure_ring_drained_on_stop
Patch2: increase-size-of-node_name
Patch3: include_sched_h
Patch4: add-service-and-trace-events
Patch5: with_xen_datapath_only
Patch6: update_coverity_model
Patch7: amend_max_events
Patch8: reduce_watch_load
Patch9: backport_eb6ae7a682
Patch10: cancel_all_jobs_on_dataplane_stop
Patch11: cancel_all_jobs_on_dataplane_start
Patch12: drain_section_in_dataplane_start
Patch13: mirror_job_can_be_null
BuildRequires: libaio-devel
BuildRequires: glib2-devel
# This doesn't look like it should be necessary but the configure isn't clever enough to not require it
BuildRequires: pixman-devel
BuildRequires: xen-libs-devel
BuildRequires: libseccomp-devel
BuildRequires: zlib-devel
BuildRequires: python3 >= 3.6
BuildRequires: meson
BuildRequires: libfdt-devel
BuildRequires: devtoolset-11-gcc
BuildRequires: devtoolset-11-binutils
Conflicts: xapi-storage-plugins-libs < 3.5.0-1
%{?_cov_buildrequires}

%description
This package contains Qemu, but builds only tools and a limited qemu-dp which handles
the storage datapath.

%prep
%autosetup -p1
%{?_cov_prepare}
# submodule ui/keymapcodedb
tar xzf %{SOURCE1}

%build
source /opt/rh/devtoolset-11/enable

%{?_cov_make_model:%{_cov_make_model scripts/coverity-scan/model.c}}
./configure --cc=gcc --cxx=/dev/null --enable-xen --target-list=i386-softmmu \
    --prefix=%{_prefix} --libdir=%{_libdir} --bindir=%{_libdir}/qemu-dp/bin --datadir=%{_datarootdir} \
    --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --sysconfdir=%{_sysconfdir} \
    --enable-werror --enable-libusb --enable-trace-backend=log \
    --disable-kvm --disable-docs --disable-guest-agent --disable-sdl \
    --disable-curses --disable-curl --disable-gtk --disable-bzip2 \
    --disable-strip --disable-gnutls --disable-nettle --disable-gcrypt \
    --disable-vhost-net --disable-vhost-scsi --disable-vhost-vsock --disable-vhost-user \
    --disable-lzo --disable-tpm --disable-virtfs --disable-tcg --disable-tcg-interpreter \
    --disable-replication --disable-qom-cast-debug --disable-slirp \
    --audio-drv-list= --disable-live-block-migration \
    --disable-bochs --disable-cloop --disable-dmg --disable-vvfat --disable-qed \
    --disable-parallels --disable-libusb --with-xen-datapath-only \
    --disable-xen-pci-passthrough \
    --without-default-devices --with-git-submodules=ignore \
    --disable-vnc --disable-oss \
    --enable-seccomp --meson=/usr/bin/meson

##CONFIGEND
%{?_cov_wrap} %{__make} %{?_smp_mflags} V=1 all

%install
source /opt/rh/devtoolset-11/enable

%{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/include %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/libcacard.*a \
       %{buildroot}/usr/share/locale %{buildroot}%{_datarootdir} %{buildroot}%{_libexecdir} \
       %{buildroot}%{_libdir}/qemu-dp/bin/ivshmem-*
# Install qemu-dp script
install -D -m 644 qemu-datapath@.service %{buildroot}%{_unitdir}/qemu-datapath@.service
install -D -m 755 qemu-dp %{buildroot}%{_libdir}/qemu-dp/bin/qemu-dp
# Install trace events
install -D -m 644 dp-trace-events %{buildroot}%{_libdir}/qemu-dp/bin/trace-events
# Rename qemu-system-i386 binary to qemu-datapath
mv %{buildroot}%{_libdir}/qemu-dp/bin/qemu-system-i386 %{buildroot}%{_libdir}/qemu-dp/bin/qemu-datapath
%{?_cov_install}

%files
%dir %{_libdir}/qemu-dp/
%{_libdir}/qemu-dp/bin
%{_unitdir}/qemu-datapath@.service

%{?_cov_results_package}

%changelog
* Fri Jul 05 2024 Tim Smith <tim.smith@cloud.com> - 7.0.0-15
- CA-394742 Improve robustness on ring connect/disconnect

* Tue Jun 11 2024 Tim Smith <tim.smith@cloud.com> - 7.0.0-14
- CA-393844 Replace previous job cancelation with drained section

* Thu May 23 2024 Tim Smith <tim.smith@cloud.com> - 7.0.0-13
- CA-393131 Cancel all block jobs on NBD export/unexport

* Tue May 07 2024 Tim Smith <tim.smith@cloud.com> - 7.0.0-12
- CA-392001 Cancel all jobs on datapath stop
- CA-392022 Cancel all jobs on dataplane start
- CA-392022 Add conflict for older xapi storage-plugins-libs

* Fri Feb 02 2024 Tim Smith <tim.smith@cloud.com> - 7.0.0-11
- Use vm.slice for datapath

* Fri Jan 26 2024 Mark Syms <mark.syms@citrix.com> - 7.0.0-10
- Rebuild against libxenstore.so.4

* Thu Jan 25 2024 Tim Smith <tim.smith@cloud.com> - 7.0.0-9
- CA-382742 Avoid SEGV on deactivating last disk

* Wed Aug 09 2023 Tim Smith <tim.smith@citrix.com> - 7.0.0-8
- CA-379219 adjust patch to drain the ring on dataplane stop
- Re-enable coroutine pool

* Wed Jun 21 2023 Mark Syms <mark.syms@citrix.com> - 7.0.0-7
- Adjust ring-drain patch to stop acting on post-shutdown events

* Thu Apr 20 2023 Tim Smith <tim.smith@citrix.com> - 7.0.0-6
- CA-376355 Prevent segfaults on datapath shutdown/restart

* Wed Mar 29 2023 Tim Smith <tim.smith@citrix.com> - 7.0.0-5
- Trace Xen backend
- Backport: Avoid crash when backend watch fires too early
- Reinstate ensure_ring_drained_on_stop patch

* Fri Mar 17 2023 Mark Syms <mark.syms@citrix.com> - 7.0.0-4
- Disable VNC

* Mon Mar 06 2023 Tim Smith <tim.smith@citrix.com> - 7.0.0-3
- CA-375614 Reduce the amount of xenstore watch activity

* Wed Mar 01 2023 Tim Smith <tim.smith@citrix.com> - 7.0.0-2
- CA-375417 reduce MAX_EVENTS for Linux AIO
- CA-375469 Increase FD limit for datapath service

* Fri Feb 03 2023 Tim Smith <tim.smith@citrix.com> - 7.0.0-1
- CP-31202 Rebase on 4.2.1 and switch to instanced service
- CP-36590 Update to build using Qemu v7.0.0
- CP-36590 Update coverity model

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
