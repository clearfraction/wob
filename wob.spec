Name     : wob
Version  : 0.15.1
Release  : 1
URL      : https://github.com/francma/wob
Source0  : https://github.com/francma/wob/archive/refs/tags/%{version}.tar.gz
Summary  : A lightweight overlay volume/backlight/progress/anything bar for Wayland
Group    : Development/Tools
License  : ISC
BuildRequires : meson
BuildRequires : gcc
BuildRequires : systemd-dev
BuildRequires : wayland-dev
BuildRequires : wayland-protocols-dev
BuildRequires : inih-dev

%description
A lighcklight/progress/anything b
%prep
%setup -q

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/wob
