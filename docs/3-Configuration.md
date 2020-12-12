# redpesk® demo-n2k plugin configuration

You can find down below the configuration obtained after compiling the demo-n2k plugin and a brief descritpion of several concept introduced.

```json
{
  "$schema": "http://iot.bzh/download/public/schema/json/signal-composer-schema.json",
  "metadata": {
		"uid": "signal-composer-binding",
		"version": "10.0",
		"api": "signal-composer",
		"info": "Signal composer API connected to low level services",
    "require": ["canbus", "redis"]
  },
  "plugins":
    {
      "uid":"demo-n2k-plugin",
      "info": "A signal composer plugin meant to collect, process and push NMEA200 data coming from the low-can binding, to a redis TSDB",
      "libs":"demo-n2k.ctlso"
    },
  "sources":
  {
    "uid":"canbus-binding",
    "api":"canbus",
    "info":"Low level binding to handle CAN bus communications",
    "getSignals":
      {"action": "api://canbus#subscribe"}
  },
  "signals" :
  [
    {
      "uid":"demo-n2k-speed",
      "event": "canbus/messages.Wind.Data.Wind.Speed",
      "unit": "m/s",
      "retention": 1,
      "getSignalsArgs":
        {"event": "messages.Wind.Data.Wind.Speed"},
      "onReceived":
        {"action":"plugin://demo-n2k-plugin#pushData"}
    },
    {
      "uid":"demo-n2k-angle",
      "event": "canbus/messages.Wind.Data.Wind.Angle",
      "unit": "rad",
      "retention": 1,
      "getSignalsArgs":
        {"event": "messages.Wind.Data.Wind.Angle"},
      "onReceived":
        {"action":"plugin://demo-n2k-plugin#pushData"}
    }
  ]
}
```

## Metadata

```json
"metadata":
{
    "uid": "signal-composer-binding",
    "version": "10.0",
    "api": "signal-composer",
    "info": "Signal composer API connected to low level services",
    "require": ["canbus", "redis"]
}
```
The metadata if the first block of the json configuration. It gathered basic statement regarding the signal-composer. The most interesting part to notice here is the key `require` that notice the signal-composer, which *api* the plugin needs to behave correctly.

## Plugins

```json
"plugins":
{
    "uid":"demo-n2k-plugin",
    "info": "A signal composer plugin meant to collect, process and push NMEA200 data coming from the low-can binding, to a redis TSDB",
    "libs":"demo-n2k.ctlso"
}
```

Here is the basic statement regarding your plugin. It presents the virtual name of your plugin within the signal-composer (key `uid`) and the real name (key `libs`) of your plugin, which can be obtained after the compilation of the project.

## Sources

```json
"sources":
{
    "uid":"canbus-binding",
    "api":"canbus",
    "info":"Low level binding to handle CAN bus communications",
    "getSignals":
        {"action": "api://canbus#subscribe"}
}
```

Here are defined from which source your entry signal are coming from. Notice here the key `getSignals`, which notice the signal composer to launch a request towards the source during its initialization. Here we want to perform a subscription to the canbus-binding in order to receive events which gathered the data.

## Signals

```json
"signals" :
{
    "uid":"demo-n2k-speed",
    "event": "canbus/messages.Wind.Data.Wind.Speed",
    "unit": "m/s",
    "retention": 1,
    "getSignalsArgs":
    {"event": "messages.Wind.Data.Wind.Speed"},
    "onReceived":
    {"action":"plugin://demo-n2k-plugin#pushData"}
}
```

This section defines the name of the output signal of the signal-composer-binding.  
This example present a signal named *demo-n2k-speed* that is linked to the source *canbus*, invoked when the event *messages.Wind.Data.Wind.Speed* and which perform the function *pushData* implementing by the plugin *demo-n2k-plugin*.

Last but not least, the signal's retention represents how long the signal-composer keep in memory one of the signal's value. The value is expressed in second and, for demo-n2k plugin, is directly link to the database push frequency. Indeed, if you want the plugin to push every 5 seconds, then you can set the signal's retention to 5 in order for the signal-composer to keep the values in memory and so processed an average on them.