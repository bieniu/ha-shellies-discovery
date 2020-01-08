# Shellies Discovery
[![GitHub Release][releases-shield]][releases]
[![GitHub All Releases][downloads-total-shield]][releases]
[![hacs_badge][hacs-shield]][hacs]
[![Community Forum][forum-shield]][forum]
[![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]

![Screenshot](https://github.com/bieniu/ha-shellies-discovery/blob/master/images/shellies-integration.png?raw=true)

This script adds MQTT discovery support for Shellies in the [Home Assistant](https://home-assistant.io/).

This script use Home Assistant [python_script](https://www.home-assistant.io/components/python_script/) component and you have to add it to your `configuration.yaml` file:
```yaml
python_script:
```

You can install this script via [HACS](https://custom-components.github.io/hacs/) or just download `shellies_discovery.py` file and save it in `/config/python_scripts` folder.

After installing the script and adding automations, run `Shellies Announce` automation or restart Home Assistant twice.

Go to [HA community](https://community.home-assistant.io/t/shellies-discovery-script/94048) for support and help.

## Supported devices:
- Shelly1
- Shelly1PM
- Shelly2 (relays and roller mode)
- Shelly2.5 (relays and roller mode)
- Shelly4Pro
- Shelly Plug
- Shelly Plug S
- Shelly RGBW2 (color and white mode)
- Shelly Bulb
- Shelly H&T (with or without USB adapter)
- Shelly Smoke
- Shelly Sense
- ShellyEM
- Shelly Flood
- Shelly Dimmer
- Shelly Door/Window

## Troubleshooting checklist
- correct MQTT configuration in Home Assistant with `discovery` enabled
- same `discovery_prefix` in Home Assistant configuration and in script configuration
- Shellies firmware updated to current version
- Home Assistant updated to current version
- enabled MQTT in Shellies configuration
- default topics configuration in Shellies

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
        qos: 2
        shelly1-001122-relay-0: 'light'
        shellyswitch-9900AA-relay-0: 'light'
        shellyswitch-9900AA-relay-1: 'fan'
        shellyswitch25-334411-relay-1: 'light'
        shellyswitch-334455: 'cover'
        shellyrgbw2-AABB22: 'white'
        shellyrgbw2-CC2211: 'rgbw'
        shellyht-2200AA: 'ac_power'
```
## Script arguments
key | optional | type | default | description
-- | -- | -- | -- | --
`discovery_prefix` | True | string | `homeassistant` | MQTT discovery prefix
`qos` | True | integer | `0` | MQTT QoS, you can use `0`, `1` or `2`
`relay_id`/`shelly_id` | True | string | `switch` | HA component to use with `relay_id`, for example: `shelly1-001122-relay-0: 'light'` means that relay 0 of shelly1-001122 will use light component in HA. You can use `switch`, `light` or `fan`. For Shelly2 and Shelly2.5 you can use `shellyswitch-334455: 'cover'` for roller mode. For ShellyRGBW2 you can use `shellyrgbw2-AABB22: 'white'` for white mode.

[releases]: https://github.com/bieniu/ha-shellies-discovery/releases
[releases-shield]: https://img.shields.io/github/release/bieniu/ha-shellies-discovery.svg?style=popout
[downloads-total-shield]: https://img.shields.io/github/downloads/bieniu/ha-shellies-discovery/total
[forum]: https://community.home-assistant.io/t/shellies-discovery-script/94048
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=popout
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
[hacs-shield]: https://img.shields.io/badge/HACS-Default-orange.svg
[hacs]: https://hacs.xyz/docs/default_repositories
