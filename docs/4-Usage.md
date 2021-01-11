# redpesk® demo-n2k plugin usage

This part will introduce you how you can start the demo that takes place late 2020 for the redpesk showcase, either with the pluging coming from your package manager, or the demo-n2k plugin you just build from source.

## Prerequesites

First of all you need to set up your CAN connection in order to get access to the CAN frame within your environment. Let's assume you use usb2can wire to plug your sensor in.  
Once plugged in you should see that a CAN interface has been created.
```bash
devel@redpesk: ~ ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
can0             DOWN
```

The sensor used during the demo is the Wired Wind WS310, which has a 250000 baud rate. In order to correctly set up the CAN interface, run the following commands:
```bash
ip link set can0 type can bitrate 250000
ip link set up can0
```
Then you should see the following state for your interface:
```bash
devel@redpesk: ~ ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
can0             UP
```

⚠️⚠️ If you do not have a sensor ⚠️⚠️  
Don't worry, the demo-n2k plugin install a CAN frame log file. It should be located in: `/var/local/lib/afm/applications/signal-composer/var/WS310.log`.  
Then install can-utils:
```bash
dnf install can-utils
```
Set up the CAN interface:
```bash
ip link add dev can0 type vcan
ip link set up can0
```

Play the logfile:
```bash
canplayer -li -I ${PATH_TO_THE_WS310_LOGS} can0=can0
```
Then you can check your sensor is correctly working by reading the frame it sends thanks to the **can-utils** package.
```bash
devel@redpesk: ~ candump can0
can0  09FD0202   [8]  86 D3 00 F2 C3 FA FF FF
can0  09FD0202   [8]  87 CF 00 ED CD FA FF FF
can0  09FD0202   [8]  88 CB 00 6C D7 FA FF FF
can0  09FD0202   [8]  89 C8 00 64 E0 FA FF FF
...
```

Don't forget that you need the can_j1939 kernel module loaded in your execution environment (Target/Host)

## Execution

Add the redpesk repository to your package manager.  
Here is the url for Redpesk and Fedora:
`download.redpesk.bzh`  
Then install the demo-n2k plugin:

Fedora/OpenSuse:
```bash
dnf install signal-composer-plugins-demo-n2k
```

Ubuntu:
```bash
apt install signal-composer-plugins-demo-n2k
```

Once the plugin and its dependencies are installed, you need to start the redis service. To do so, simply run:

```bash
systemctl start redis
```

### Target

Then start the demo services thanks to the afm-util tool:

```bash
afm-util start canbus-binding
afm-util start redis-tsdb-binding
afm-util start signal-composer-plugins-demo-n2k
```

### Host

The bindings should be located in `/var/local/lib/afm/applications` if not, find them on your machine and export it as `AFM_APP_PATH`

Start the demo services thanks to the afb-binder tool:

- canbus
```bash
afb-binder --name=afb-canbus-binding --workdir=${AFM_APP_PATH}/canbus-binding --binding=lib/afb-canbus-binding.so --port=9997 --ws-server unix://tmp/canbus
```

- redis-tsdb-binding
```bash
afb-binder --name=afbd-redis-tsdb-binding --workdir=${AFM_APP_PATH}/redis-tsdb-binding --binding=lib/redis-binding.so --port=9998 --ws-server unix:/tmp/redis
```

- signal-composer-binding
```bash
afb-binder --name=afbd-signal-composer-binding --workdir=${AFM_APP_PATH}/signal-composer-binding --binding=lib/afb-signal-composer-binding.so --port=9999 --ws-client=unix:/tmp/canbus --ws-client=unix:/tmp/redis
```

## Access

Then thanks to the redis client you can access to the data that are stored in your local redis database
```bash
devel@redpesk: ~ redis-cli -c TS.MGET FILTER class=WIRED_WIND_WS310
1) 1) "WIRED_WIND_WS310.angle.unit"
   2) (empty list or set)
   3) 1) (integer) 1607986220
      2) "rad"
2) 1) "WIRED_WIND_WS310.angle.value"
   2) (empty list or set)
   3) 1) (integer) 1607986220
      2) 4.127632
3) 1) "WIRED_WIND_WS310.speed.unit"
   2) (empty list or set)
   3) 1) (integer) 1607986220
      2) "m/s"
4) 1) "WIRED_WIND_WS310.speed.value"
   2) (empty list or set)
   3) 1) (integer) 1607986220
      2) 1.574502
```

## Monitoring

Thanks to [Binder Devtool](../ci-cd/monitoring.html), you can have a user friendly control of what is going on in your plugin.
You have access to basic signal-composer utilities such as the signals list, the config of your signal, and for the demo-n2k plugin, the data coming from the canbus-binding.

![afb-ui-dev-tool](./mov/ui_dev_tool.webm)
