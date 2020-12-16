# signal-composer-plugins-demo-n2k

## Goal

The main purpose of this project is to provide a signal-composer plugin, built as a showcase of what a user can achieve thanks to the application framework binder.

This project is a part of a demo which implies:
- sensor which emits can frames
- [canbus-binding](https://docs.redpesk.bzh/docs/en/master/redpesk-core/canbus/1-Architecture.html)
- [signal-composer-binding](https://docs.redpesk.bzh/docs/en/master/redpesk-core/signal-composer/part-1/1-Architecture.html)
- [redis-tsdb-binding](http://docs.redpesk.bzh/docs/en/master/redpesk-core/redis/1-Architecture.html)
- [cloud-publication-binding](https://docs.redpesk.bzh/docs/en/master/redpesk-core/cloud-pub/1-Architecture.html)

The full documentation can be found under the [docs](./docs/) directory.

As a quick sum up, once loded by the signal-composer, this plugin will collect, process and push data coming from the canbus-binding, to a redis time series database.

# Fast build procedure

Just use autobuild script:

```bash
./autobuild/linux/autobuild build
```
