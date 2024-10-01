# ewn-box-opener

Box Opener client for mining EWN tokens.

## How to run

There are two ways to run the the Box Opener:

### 1. Docker (recommended)

The easiest way to run the Box Opener is to use Docker. [Find out more on how to run with Docker](https://docs.erwin.lol/docs/box-openers/box-opener-node).

### 2. Standalone (advanced)

Another way to run the Box Opener is to run the Python script standalone. Docs will follow.
=======
- linux/amd64 (64-bit x86 systems)
- linux/arm64 (64-bit ARM systems)
- linux/arm/v7 (32-bit ARM systems, like older Raspberry Pi models)

This means you can run the Box Opener on a variety of devices, from standard PCs to Raspberry Pis and other ARM-based systems.

## How to Run

There are two ways to run the Box Opener:

1. **Docker (recommended)**  
   The easiest way to run the Box Opener is to use Docker. [Find out more on how to run with Docker](http://docs.erwin.lol/docs/box-openers/box-opener-node/).

2. **Standalone (advanced)**  
   Another way to run the Box Opener is to run the Python script standalone. Documentation for this method will be available soon.

### Usage Notes

When running the Box Opener with Docker, use the following commands:

- Standard run command (may show a warning on non-AMD64 systems, but will run correctly):

    ```bash
    docker run -it -e API_KEY=<your_api_key> ghcr.io/erwin-schrodinger-token/ewn-box-opener:latest
    ```

- To suppress the platform mismatch warning, explicitly specify the platform:
 
    ```bash
    docker run -it --platform linux/amd64 -e API_KEY=<your_api_key> ghcr.io/erwin-schrodinger-token/ewn-box-opener:latest
    ```

- To run the container in the background, add the -d flag:
 
    ```bash
    docker run -d -e API_KEY=<your_api_key> ghcr.io/erwin-schrodinger-token/ewn-box-opener:latest
    ```

- To run in the background and suppress platform mismatch warning:
 
    ```bash
    docker run -d --platform linux/amd64 -e API_KEY=<your_api_key> ghcr.io/erwin-schrodinger-token/ewn-box-opener:latest
    ```

Replace `linux/amd64` with `linux/arm64` or `linux/arm/v7` as appropriate for your system.

**Note:** The warning message "The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8)" can be safely ignored when running without the --platform flag, as QEMU will handle the emulation automatically.

These enhancements ensure that the Box Opener can run efficiently on a wide range of hardware, from powerful servers to small, energy-efficient ARM devices.
