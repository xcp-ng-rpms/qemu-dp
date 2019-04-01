Summary: qemu-dp storage datapath
Name: qemu-dp
Epoch: 2
Version: 2.12.0
Release: 1.10.0.3%{dist}
License: GPL
Requires: jemalloc
Requires: xcp-clipboardd
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v2.12.0-rc2&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Patch0: 01-make-a-qemu-dp-build.patch
Patch1: 02-do-not-register-xen-backend.patch
Patch2: 03-added-xen-watch-domain-qmp.patch
Patch3: 04-make-blockdev-snapshot-use.patch
Patch4: 05-use-the-legacy-grant-copy.patch
Patch5: 06-send-stdout-and-stderr-to.patch
Patch6: 07-add-a-trace-file-to-control.patch
Patch7: 08-do-not-use-iothread-for.patch
Patch8: 09-remove-unwanted-crypto.patch
Patch9: 10-use-libaio-by-default-and.patch
Patch10: 11-add-qmp_relink_chain-command.patch
Patch11: 12-log-errno-on-ioctl-failure.patch
Patch12: 13-improve-xen_disk-batching.patch
Patch13: 14-improve-xen_disk-response.patch
Patch14: 15-memory-usage-experiments.patch
Patch15: 16-adjust-qcow2-default-cache.patch
Patch16: 17-avoid-repeated-memory.patch
Patch17: 18-add-xen-unwatch-domain-qmp.patch
Patch18: 19-detach-aio-context-before-bs-free.patch
Patch19: 20-fix-file-and-filename.patch
BuildRequires: gcc
BuildRequires: libaio-devel glib2-devel
BuildRequires: libjpeg-devel libpng-devel pixman-devel libdrm-devel
BuildRequires: xen-dom0-devel xen-libs-devel libusbx-devel
BuildRequires: libseccomp-devel zlib-devel

%description
This package contains Qemu, but builds only tools and a limited qemu-dp which handles
the storage datapath.

%prep
%autosetup -p1

%build
./configure --cc=gcc --cxx=/dev/null --enable-xen --target-list=i386-softmmu --source-path=. \
    --prefix=%{_prefix} --bindir=%{_libdir}/qemu-dp/bin --datadir=%{_datarootdir} \
    --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --sysconfdir=%{_sysconfdir} \
    --enable-werror --enable-libusb --enable-trace-backend=syslog \
    --disable-kvm --disable-docs --disable-guest-agent --disable-sdl \
    --disable-curses --disable-curl --disable-gtk --disable-bzip2 \
    --disable-strip --disable-gnutls --disable-nettle --disable-gcrypt \
    --disable-vhost-net --disable-vhost-scsi --disable-vhost-vsock --disable-vhost-user \
    --disable-lzo --disable-tpm --disable-virtfs --disable-tcg --disable-tcg-interpreter \
    --disable-replication --disable-qom-cast-debug --disable-slirp \
    --audio-drv-list= --disable-live-block-migration \
    --enable-seccomp --enable-qemudp
%{?cov_wrap} %{__make} %{?_smp_mflags} V=1 all

%install
mkdir -p %{buildroot}%{_libdir}/qemu-dp/bin

rm -rf %{buildroot}
%{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/include %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/libcacard.*a \
       %{buildroot}/usr/share/locale %{buildroot}%{_datarootdir} %{buildroot}%{_libexecdir} \
       %{buildroot}%{_libdir}/qemu-dp/bin/ivshmem-* %{buildroot}%{_libdir}/qemu-dp/bin/qemu-system-i386
install -m 644 qemu-dp-tracing "%{buildroot}%{_libdir}/qemu-dp/bin/qemu-dp-tracing"

%files
%{_libdir}/qemu-dp/bin

%changelog
* Mon Apr 01 2019 Ronan Abhamon <ronan.abhamon@vates.fr> - 2.12.0-1.10.0.3
- xcp-clipboardd is now required instead of xs-clipboardd

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
