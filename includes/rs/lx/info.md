Kconfig is the kernel's build system and is associated with Kconfig files found throughout the kernel source tree.

Enabling Rust in the Linux kernel depends on setting the RUST variable.

```sh
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- bcm2711_defconfig
./scripts/config --disable "MODVERSIONS"
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- rust.config
```
