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
      force_update: true
      shelly1-001122-relay-0: 'light'
      shellyswitch-9900AA-relay-0: 'light'
      shellyswitch-9900AA-relay-1: 'fan'
      shellyswitch25-334411-relay-1: 'light'
      shellyswitch-334455: 'cover'
      shellyrgbw2-AABB22: 'white'
      shellyht-2200AA: 'ac_power'
      shelly1-001122-ext-0: 'temperature'
      shelly1-001122-ext-1: 'temperature'
      shelly1-001122-ext-2: 'temperature'
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
`force_update` | True | boolean | False | force update sensors

## Arguments for Shelly1

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shelly1-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay
`shelly1-<ID>-ext-0` | True | string | None | `temperature` | type of external sensor 0
`shelly1-<ID>-ext-1` | True | string | None | `temperature` | type of external sensor 1
`shelly1-<ID>-ext-2` | True | string | None | `temperature` | type of external sensor 2

## Arguments for Shelly1PM

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shelly1pm-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay
`shelly1pm-<ID>-ext-0` | True | string | None | `temperature` | type of external sensor 0
`shelly1pm-<ID>-ext-1` | True | string | None | `temperature` | type of external sensor 1
`shelly1pm-<ID>-ext-2` | True | string | None | `temperature` | type of external sensor 2

## Arguments for Shelly2

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shellyswitch-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 0
`shellyswitch-<ID>-relay-1` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 1
`shellyswitch-<ID>` | True | string | None | `cover` | use `roller mode`

## Arguments for Shelly2.5

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shellyswitch25-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 0
`shellyswitch25-<ID>-relay-1` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 1
`shellyswitch25-<ID>` | True | string | None | `cover` | use `roller mode`

## Arguments for Shelly4Pro

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shelly4pro-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 0
`shelly4pro-<ID>-relay-1` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 1
`shelly4pro-<ID>-relay-2` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 2
`shelly4pro-<ID>-relay-3` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay 3

## Arguments for Shelly EM

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shellyem-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay

## Arguments for Shelly 3EM

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shellyem3-<ID>-relay-0` | True | string | `switch` | `switch`, `light`, `fan` | component to use with the relay

## Arguments for Shelly RGBW2

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shellyrgbw2-<ID>` | True | string | None | `white` | use `white mode`

## Arguments for Shelly H&T

key | optional | type | default | possible values | description
-- | -- | -- | -- | -- | --
`shellyht-<ID>` | True | string | None | `ac_power` | use when your H&T sensor is powered via USB adapter

[forum]: https://community.home-assistant.io/t/shellies-discovery-script/94048
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=popout
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
