# Shellies Discovery

This script adds MQTT discovery support for Shellies.

Supported devices:
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

Arguments:
 - discovery_prefix:    - discovery prefix in HA, default 'homeassistant',
                          optional
 - id                   - Shelly ID (required)
 - mac                  - Shelly MAC address (required)
 - sensor               - sensor entity_id (required)
 - fw_ver               - Shelly firmware version (optional)
 - temp_unit            - C for Celsius, F for Farenhait, default C (optional)
 - list of shelies relays and components for them, only for devices with relays
                          (optional), by default all relays are added as
                          switches.

Default configuration
Automations:
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

If you want the relay to be a other component than the switch in the Home
Assistant, you have to add a description of the relay and its function to the
script configuration.
For example:
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
      shellyswitch-334455: 'cover'
      shellyrgbw2-AABB22: 'white'
      shellyrgbw2-CC2211: 'rgbw'

qos - maximum QoS level of the topics, this is optional argument, default is 0
      (integer)

shelly1-001122-relay-0: 'light' - means that relay 0 of shelly1-001122 will use
light component in Home Assistant. You can use switch, light or fan.

shellyswitch-334455: 'cover' - means that Shelly2 works in roller mode and use
cover component in Home Assistant.

shellyrgbw2-AABB22: 'white' - means that Shelly RGBW2 works in white-mode

shellyrgbw2-CC2211: 'rgbw' - means that Shelly RGBW2 works in color-mode
(default)
