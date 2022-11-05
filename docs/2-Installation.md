# redpesk demo-n2k plugin installation

This part is only useful if you plan to build and install the package from source.
Do not forget that the environment where you want to run the plugin must have the **can_j1939** kernel modules loaded.

## Building from source

We advise you to use the [local builder]({% chapter_link local-builder-doc.installation %}) for building the plugin source. The local builder comes with everything setup to build natively and cross-build redpesk projects.

### Tools for native build

Add first the [redpesk SDK native repository]({% chapter_link host-configuration-doc.setup-your-build-host %}) to your package manager.

Install the building tools:

- gcc
- g++
- make
- cmake
- afb-cmake-modules

And then install the dependencies:

- json-c
- afb-binding
- afb-libhelpers
- afb-libcontroller
- signal-composer-binding

Fedora/OpenSuse:

```bash
sudo dnf install gcc-c++ make cmake afb-cmake-modules json-c-devel afb-binding-devel afb-libhelpers-devel afb-libcontroller-devel signal-composer-binding-devel
```

Ubuntu:

```bash
sudo apt install gcc g++ make cmake afb-cmake-modules libsystemd-dev libjson-c-dev afb-binding-dev afb-libhelpers-dev afb-libcontroller-dev signal-composer-binding-dev
```

### Build

```bash
git clone https://github.com/redpesk-samples/signal-composer-plugins-demo-n2k
cd signal-composer-plugins-demo-n2k
mkdir build
cd build
cmake ..
make demo-n2k -j
sudo make install_demo-n2k
```

From then, you have set up your environment to run the demo-n2k plugin. Go to the section [usage](./4-Usage.html) to see how to use it.
