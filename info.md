## Minimal configuration
```yaml
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
        qos: 2
        shelly1-001122-relay-0: 'light'
        shellyswitch-9900AA-relay-0: 'light'
        shellyswitch-9900AA-relay-1: 'fan'
        shellyswitch-334455: 'cover'
        shellyrgbw2-AABB22: 'white'
        shellyrgbw2-CC2211: 'rgbw'
```
## Script configuration
key | optional | type | default | description
-- | -- | -- | -- | --
`discovery_prefix` | True | string | `homeassistant` | MQTT discovery prefix
`temp_unit` | True | string | `C` | temperature unit, `C` for Celsius, `F` for Farenhait
`qos` | True | integer | `0` | MQTT QoS, you can use `0`, `1` or `2`
`relay_id`/`shelly_id` | True | string | `switch` | HA component to use with `relay_id`, for example: `shelly1-001122-relay-0: 'light'` means that relay 0 of shelly1-001122 will use light component in HA. You can use `switch`, `light` or `fan`. For Shelly2 and Shelly2.5 you can use `shellyswitch-334455: 'cover'` for roller mode. For ShellyRGBW2 you can use `shellyrgbw2-AABB22: 'white'` for wite mode.
