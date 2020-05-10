[![Community Forum][forum-shield]][forum]  [![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]

![Screenshot](https://github.com/bieniu/ha-shellies-discovery/blob/master/images/shellies-integration.png?raw=true)

This script use Home Assistant [python_script](https://www.home-assistant.io/components/python_script/) component and you have to add it to your `configuration.yaml` file:

```yaml
python_script:
```

## Supported devices

- Shelly1 (with external temperature sensors)
- Shelly1PM (with external temperature sensors)
- Shelly2 (relays and roller mode)
- Shely2.5 (relays and roller mode)
- Shelly4Pro
- Shelly Plug
- Shelly Plug S
- Shelly RGBW2 (color and white mode)
- Shelly Bulb
- Shelly DUO (experimental)
- Shelly H&T (with or without USB adapter)
- Shelly Smoke
- Shelly Sense
- Shelly EM
- Shelly 3EM
- Shelly Dimmer
- Shelly Door/Window

## How to debug

To debug the script add this to your `logger` configuration:

```yaml
# configuration.yaml file
logger:
  logs:
    homeassistant.components.python_script: debug
```

## Troubleshooting checklist

- correct MQTT configuration in Home Assistant with `discovery` enabled
- same `discovery_prefix` in Home Assistant configuration and in script configuration
- Shellies firmware updated to current version
- Home Assistant updated to current version
- enabled MQTT in Shellies configuration
- default topics configuration in Shellies
- default Shellies IDs

## Minimal configuration

```yaml
# configuration.yaml file
python_script:

# automations.yaml file
- id: shellies_announce
  alias: 'Shellies Announce'
  trigger:
    - platform: homeassistant
      event: start
  action:
    service: mqtt.publish
    data:
      topic: shellies/command
      payload: announce

- id: 'shellies_discovery'
  alias: 'Shellies Discovery'
  trigger:
    - platform: mqtt
      topic: shellies/announce
  action:
    service: python_script.shellies_discovery
    data_template:
      id: '{{ trigger.payload_json.id }}'
      mac: '{{ trigger.payload_json.mac }}'
      fw_ver: '{{ trigger.payload_json.fw_ver }}'
```

## Custom configuration example

```yaml
# in configuration.yaml file
python_script:

# in automation.yaml file
- id: shellies_announce
  alias: 'Shellies Announce'
  trigger:
    - platform: homeassistant
      event: start
  action:
    service: mqtt.publish
    data:
      topic: shellies/command
      payload: announce

- id: 'shellies_discovery'
  alias: 'Shellies Discovery'
  trigger:
    - platform: mqtt
      topic: shellies/announce
  action:
    service: python_script.shellies_discovery
    data_template:
      id: '{{ trigger.payload_json.id }}'
      mac: '{{ trigger.payload_json.mac }}'
      fw_ver: '{{ trigger.payload_json.fw_ver }}'
      discovery_prefix: 'hass'
      qos: 2
      shelly1-AABB9900:
        relay-0: "light"
        ext-0: "temperature"
        ext-1: "temperature"
        ext-2: "temperature"
        force_update_sensors: true
      shelly1pm-aabb9911:
        ext-0: "temperature"
        longpush_off_delay: false
        force_update_sensors: true
      shellyswitch-123409FF:
        relay-0: "fan"
        relay-1: "light"
      shellyswitch-123409cc:
        relay-1: "fan"
      shellyswitch25-334455AA:
        mode: "roller"
      shellyplug-s-CCBBCCAA:
        relay-0: "light"
        force_update_sensors: true
      shellyht-11AA00CCDD:
        force_update_sensors: true
      shellyht-11AA00CCEE:
        power: "battery"
      shellyht-11AA00CCFF:
        power: "ac"
      shellyrgbw2-AA123FF32:
        mode: "white"
      shellyrgbw2-AA123FF84:
        mode: "rgbw"
      shellyem-BB23CC45:
        force_update_sensors: true
      ignored_devices:
        - shelly1-DD0011
        - shellyem-EECC22
```

## Script arguments

key | optional | type | default | description
-- | -- | -- | -- | --
`discovery_prefix` | True | string | `homeassistant` | MQTT discovery prefix
`qos` | True | integer | `0` | MQTT QoS, you can use `0`, `1` or `2`
`ignored_devices` | True | list | None | list of devices to ignore

## Device arguments

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`relay-<NUM>` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay number <NUM>
`ext-<NUM>` | True | string | None | `temperature` | type of external sensor number <NUM>
`force_update_sensors` | True | boolean | `false` | `true`, `false` | [force update](https://www.home-assistant.io/integrations/sensor.mqtt/#force_update) sensors
`longpush_off_delay` | True | boolean | true | `true`, `false` | [off delay](https://www.home-assistant.io/integrations/binary_sensor.mqtt/#off_delay) (3 sec) for longpush binary sensors
`mode` | True | string | | `white`, `rgbw`, `relay`, `roller` | `white` or `rgbw` for ShellyRGBW2, `relay` or `roller` for Shelly2/Shelly2.5
`powered` | True | string | | `ac`, `battery` | `ac` or `battery` powered

[forum]: https://community.home-assistant.io/t/shellies-discovery-script/94048
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=popout
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
