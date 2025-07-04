**SIMD** (Single Instruction Multiple Data)  allows a single instruction to operate on multiple elements of data at the same time.
This lends itself well to processing media, with sequentially ordered data.
SIMD is also referred to as vector programming.
SIMD procedures are also sometimes referred to as assembly functions or assembly kernels.
By contrast, programming languages that operate on a single instruction at a time are known as scalar programming.

**Intrinsics** are C-like functions that map to assembly instructions.

Human readable instructions like `mov` and `inc` are known as **mnemonics**.

There are two flavors of 64-bit x86 assembly syntax (amd64): Intel (preferred) and AT&T which is older and harder to read.

**x86inc.asm** is a "header" developed in the x264, ffmpeg, and dav1d communities to provide helpers, predefined names, and macros to simplify writing assembly.
