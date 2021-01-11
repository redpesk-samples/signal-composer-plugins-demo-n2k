# redpesk® demo-n2k plugin installation

This part is only useful if you plan to build and install the package from source.  
Do not forget that the environment where you want to run the plugin must have the **can_j1939** kernel modules loaded.

## Using package manager

If you aren't planing to build it from source on your host, add the redpesk [repository](../developer-guides/host-configuration/docs/1-Setup-your-build-host.html)
to your package manager.


Then, to install the package and all its dependencies, install the package **signal-composer-plugins-demo-n2k**

## Building from source

We advise you to use the [local builder](../getting_started/local_builder/docs/1_installation.html) for building the plugin source. The local builder comes with everything setup to build redpesk projects.

### Tools

Install the building tools:
- gcc
- g++
- make
- cmake
- afb-cmake-modules

Install the dependencies:
- json-c
- afb-binding
- afb-libhelpers
- afb-libcontroller
- signal-composer-binding

Fedora/OpenSuse:
```bash
dnf install gcc-c++ make cmake afb-cmake-modules json-c-devel afb-binding-devel afb-libhelpers-devel afb-libcontroller-devel signal-composer-binding-devel
```

Ubuntu:
```bash
apt install gcc g++ make cmake afb-cmake-modules-bin libsystemd-dev libjson-c-dev afb-binding-dev afb-libhelpers-dev afb-libcontroller-dev signal-composer-binding-dev
```

### Build

```bash
git clone https://github.com/redpesk-samples/signal-composer-plugins-demo-n2k
cd signal-composer-plugins-demo-n2k
mkdir build
cd build
cmake ..
make demo-n2k -j
make install_demo-n2k
```

From then, you have set up your environment to run the demo-n2k plugin. Go to the section [usage](./4-Usage.html) to see how to use it.