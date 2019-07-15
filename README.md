# Shellies Discovery
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

![Screenshot](https://github.com/bieniu/ha-shellies-discovery/blob/master/images/shellies-integration.png?raw=true)

This script adds MQTT discovery support for Shellies in the [Home Assistant](https://home-assistant.io/).

This script use Home Assistant [python_script](https://www.home-assistant.io/components/python_script/) component.

You can install this script via [HACS](https://custom-components.github.io/hacs/) or just download `shellies_discovery.py` file and save it in `/config/python_scripts` folder.

After installing the script and adding automations, run `Shellies Announce` automation or restart Home Assistant twice.

Go to [HA community](https://community.home-assistant.io/t/shellies-discovery-script/94048) for support and help.

## Supported devices:
- Shelly1
- Shelly1PM
- Shelly2 (relays and roller mode)
- Shely2.5 (relays and roller mode)
- Shelly4Pro
- Shelly Plug
- Shelly Plug S
- Shelly RGBW2 (color and white mode)
- Shelly H&T
- Shelly Smoke
- Shelly Sense

## Minimal configuration
```yaml
python_script:

automation:
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
python_script:

automation:
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
        temp_unit: 'F'
        qos: 2
        shelly1-001122-relay-0: 'light'
        shellyswitch-9900AA-relay-0: 'light'
        shellyswitch-9900AA-relay-1: 'fan'
        shellyswitch-334455: 'cover'
        shellyrgbw2-AABB22: 'white'
        shellyrgbw2-CC2211: 'rgbw'
```
## Script arguments
key | optional | type | default | description
-- | -- | -- | -- | --
`discovery_prefix` | True | string | `homeassistant` | MQTT discovery prefix
`temp_unit` | True | string | `C` | temperature unit, `C` for Celsius, `F` for Farenhait
`qos` | True | integer | `0` | MQTT QoS, you can use `0`, `1` or `2`
`relay_id`/`shelly_id` | True | string | `switch` | HA component to use with `relay_id`, for example: `shelly1-001122-relay-0: 'light'` means that relay 0 of shelly1-001122 will use light component in HA. You can use `switch`, `light` or `fan`. For Shelly2 and Shelly2.5 you can use `shellyswitch-334455: 'cover'` for roller mode. For ShellyRGBW2 you can use `shellyrgbw2-AABB22: 'white'` for wite mode.
