Summary: qemu-dp storage datapath
Name: qemu-dp
Epoch: 2
Version: 2.10.2
Release: 1.2.0
License: GPL
Requires: jemalloc
Requires: xs-clipboardd
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Patch0: 0001-seccomp-changing-from-whitelist-to-blacklist.patch
Patch1: 0002-seccomp-add-obsolete-argument-to-command-line.patch
Patch2: 0003-seccomp-add-elevateprivileges-argument-to-command-li.patch
Patch3: 0004-seccomp-add-spawn-argument-to-command-line.patch
Patch4: 0005-seccomp-add-resourcecontrol-argument-to-command-line.patch
Patch5: 0006-buildsys-Move-seccomp-cflags-libs-to-per-object.patch
Patch6: 0001-vnc-use-QEMU_ALIGN_DOWN.patch
Patch7: 0002-vnc-use-DIV_ROUND_UP.patch
Patch8: 0004-ui-add-tracing-of-VNC-operations-related-to-QIOChann.patch
Patch9: 0005-ui-add-tracing-of-VNC-authentication-process.patch
Patch10: 0006-ui-Always-remove-an-old-VNC-channel-watch-before-add.patch
Patch11: 0004-vga-migration-Update-memory-map-in-post_load.patch
Patch12: 0007-vga-add-ram_addr_t-cast.patch
Patch13: 0008-cirrus-fix-oob-access-in-mode4and5-write-functions.patch
Patch14: 0009-vga-fix-region-checks-in-wraparound-case.patch
Patch15: 0001-xen-pt-allow-QEMU-to-request-MSI-unmasking-at-bind-t.patch
Patch16: 0007-vnc-fix-debug-spelling.patch
Patch17: 0008-ui-remove-sync-parameter-from-vnc_update_client.patch
Patch18: 0009-ui-remove-unreachable-code-in-vnc_update_client.patch
Patch19: 0010-ui-remove-redundant-indentation-in-vnc_client_update.patch
Patch20: 0011-ui-avoid-pointless-VNC-updates-if-framebuffer-isn-t-.patch
Patch21: 0012-ui-track-how-much-decoded-data-we-consumed-when-doin.patch
Patch22: 0013-ui-introduce-enum-to-track-VNC-client-framebuffer-up.patch
Patch23: 0014-ui-correctly-reset-framebuffer-update-state-after-pr.patch
Patch24: 0015-ui-refactor-code-for-determining-if-an-update-should.patch
Patch25: 0016-ui-fix-VNC-client-throttling-when-audio-capture-is-a.patch
Patch26: 0017-ui-fix-VNC-client-throttling-when-forced-update-is-r.patch
Patch27: 0018-ui-place-a-hard-cap-on-VNC-server-output-buffer-size.patch
Patch28: 0019-ui-add-trace-events-related-to-VNC-client-throttling.patch
Patch29: 0020-ui-mix-misleading-comments-return-types-of-VNC-I-O-h.patch
Patch30: 0021-ui-avoid-sign-extension-using-client-width-height.patch
Patch31: 0010-vga-check-the-validation-of-memory-addr-when-draw-te.patch
Patch32: 0001-block-let-blk_add-remove_aio_context_notifier-tolera.patch
Patch33: 0001-xen-disk-use-an-IOThread-per-instance.patch
Patch34: vga-fix-region-calculation.patch
Patch35: xen-platform-add-device-id-property.patch
Patch36: xen-platform-add-class-id-property.patch
Patch37: xen-platform-add-revision-property.patch
Patch38: 0001-xen-platform-Handle-write-of-four-byte-build-number-.patch
Patch39: 0002-xen-platform-Provide-QMP-query-commands-for-XEN-PV-d.patch
Patch40: 0003-xen-platform-Emit-XEN_PLATFORM_PV_DRIVER_INFO-after-.patch
Patch41: dont-set-a20-on-xen.patch
Patch42: dont-init-cpus-on-xen.patch
Patch43: 0001-xen-Emit-RTC_CHANGE-upon-TIMEOFFSET-ioreq.patch
Patch44: remove-ioapic.patch
Patch45: 0001-xen-pvdevice-Introduce-a-simplistic-xen-pvdevice-sav.patch
Patch46: 0001-pc-Do-not-expect-to-have-a-fw_cfg-device.patch
Patch47: 0003-xen-apic-Implement-unrealize.patch
Patch48: 0004-hotplug-Implement-legacy-CPU-hot-unplug.patch
Patch49: 0001-migration-Don-t-leak-IO-channels.patch
Patch50: 0002-io-Fix-QIOChannelFile-when-creating-and-opening-read.patch
Patch51: 0003-io-Don-t-call-close-multiple-times-in-QIOChannelFile.patch
Patch52: 0004-io-Add-dev-fdset-support-to-QIOChannelFile.patch
Patch53: save-device-check-return.patch
Patch54: 0001-xen-link-against-xentoolcore.patch
Patch55: 0002-xen-restrict-use-xentoolcore_restrict_all.patch
Patch56: 0003-xen-defer-call-to-xen_restrict-until-just-before-os_setup_post.patch
Patch57: 0004-xen-destroy_hvm_domain-Move-reason-into-a-variable.patch
Patch58: 0005-xen-move-xc_interface-compatibility-fallback-further-up-the-file.patch
Patch59: 0006-xen-destroy_hvm_domain-Try-xendevicemodel_shutdown.patch
Patch60: 0007-os-posix-Provide-new--runas-uid-.-gid-facility.patch
Patch61: use-new-dmops-for-vram.patch
Patch62: xenstore-ignore-state-write-error.patch
Patch63: igd-upt.patch
Patch64: 0001-CP-20436-Introduce-a-config-option-for-machines-comp.patch
Patch65: pci-add-subsystem-id-properties.patch
Patch66: pci-add-revision_id-property.patch
Patch67: force-lba-geometry.patch
Patch68: 0001-CP-21767-Don-t-accidently-unplug-ourselves-if-PCI_CL.patch
Patch69: 0001-CP-21434-Implement-VBE-LFB-physical-address-register.patch
Patch70: 0001-CA-256542-Workaround-unassigned-accesses-caused-by-b.patch
Patch71: ignore-rtc-century-changes.patch
Patch72: 0001-CP-17697-Initial-port-of-NVIDIA-VGPU-support-from-QEMU-trad.patch
Patch73: usb-batch-frames.patch
Patch74: 0001-CP-23753-Talk-to-new-clipboard-daemon.patch
Patch75: gvt-g.patch
Patch76: 0001-Update-fd-handlers-to-support-sysfs_notify.patch
Patch77: 0002-Fix-up-PCI-command-register-for-AMD-ATI-GPU-VFs.patch
Patch78: 0003-Add-interception-layer-for-BAR-ops.patch
Patch79: 0004-Add-AMD-code.patch
Patch80: rtc-no-ratelimit.patch
Patch81: pci-permissive-mode.patch
Patch82: 0001-CA-239469-Avoid-bind-listen-race-on-a-socket-with-SO.patch
Patch83: build-configuration.patch
Patch84: do_not_register_xen_backend_for_qdisk.patch
Patch85: added_xen-watch-domain_qmp_command.patch
Patch86: add-qemu-dp.patch
Patch87: make-blockdev-snapshot-use-same-node-name.patch
Patch88: use_existing_io_context.patch
Patch89: use_libaio_by_default.patch
Patch90: Use_the_legacy_grant_copy_ioctl

# XCP-ng patches
Patch1000: qemu-dp-2.10.2-add-rbd-support.XCP-ng.patch
Patch1001: qemu-dp-2.10.2-add_x-blockdev-suspend_x-blockdev-resume_qmp_commands.XCP-ng.patch

BuildRequires: libaio-devel glib2-devel
BuildRequires: libjpeg-devel libpng-devel pixman-devel libdrm-devel
BuildRequires: xen-dom0-devel xen-libs-devel libusbx-devel
BuildRequires: libseccomp-devel
BuildRequires: librbd1-devel

%description
This package contains Qemu.

%prep
%autosetup -p1

%build
./configure --cc=gcc --cxx=/dev/null --enable-xen --target-list=i386-softmmu --source-path=. \
    --prefix=%{_prefix} --bindir=%{_libdir}/qemu-dp/bin --datadir=%{_datarootdir} \
    --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --sysconfdir=%{_sysconfdir} \
    --enable-werror --enable-libusb --enable-trace-backend=log \
    --disable-kvm --disable-docs --disable-guest-agent --disable-sdl \
    --disable-curses --disable-curl --disable-gtk --disable-bzip2 \
    --disable-strip --disable-gnutls --disable-nettle --disable-gcrypt \
    --disable-vhost-net --disable-vhost-scsi --disable-vhost-vsock --disable-vhost-user \
    --disable-lzo --disable-tpm --disable-virtfs --disable-tcg --disable-tcg-interpreter \
    --disable-replication --disable-qom-cast-debug --disable-slirp \
    --audio-drv-list= --disable-coroutine-pool --disable-live-block-migration \
    --enable-seccomp
%{?cov_wrap} %{__make} %{?_smp_mflags} all

%install
mkdir -p %{buildroot}%{_libdir}/qemu-dp/bin

rm -rf %{buildroot}
%{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/include %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/libcacard.*a \
       %{buildroot}/usr/share/locale %{buildroot}%{_datarootdir} %{buildroot}%{_libexecdir} \
       %{buildroot}%{_libdir}/qemu-dp/bin/ivshmem-* %{buildroot}%{_libdir}/qemu-dp/bin/qemu-system-i386

%files
%{_libdir}/qemu-dp/bin

%changelog
* Thu Jul 21 2018 rposudnevskiy <ramzes_r@yahoo.com> - 2.10.2-1.2.0
- Add new QMP commands x-blockdev-suspend and x-blockdev-resume

* Thu Jul 05 2018 rposudnevskiy <ramzes_r@yahoo.com> - 2.10.2-1.2.0
- Enable support of Ceph RBD

* Tue Apr 24 2018 marksy <mark.syms@citrix.com> - 2.10.2-1.2.0
- CA-288288: Avoid built-in QEMU crypto

* Tue Apr 17 2018 marksy <mark.syms@citrix.com> - 2.10.2-1.1.0
- Fix segfault on disconnect and enable read caching
- CA-287872: Use the legacy grant copy ioctl

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
