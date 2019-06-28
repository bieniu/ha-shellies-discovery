"""
This script adds MQTT discovery support for Shellies. Shelly1, Shelly1PM,
Shelly2, Shely2.5, Shelly4Pro, Shelly Plug, Shelly Plug S, Shelly RGBW2 (color
and white mode), Shelly H&T, Shelly Smoke and Shelly Sense are supported.

Arguments:
 - discovery_prefix:    - discovery prefix in HA, default 'homeassistant',
                          optional
 - id                   - Shelly ID (required)
 - mac                  - Shelly MAC address (required)
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

Script supports custom_updater and HACS components. Add this to your configuration and
stay up-to-date.

custom_updater:
  track:
    - python_scripts
  python_script_urls:
    - https://raw.githubusercontent.com/bieniu/home-assistant-config/master/python_scripts/python_scripts.json
"""

VERSION = '0.9.7'

ATTR_DEVELOP = 'develop'

ATTR_ID = 'id'
ATTR_MAC = 'mac'
ATTR_FW_VER = 'fw_ver'
ATTR_DISCOVERY_PREFIX = 'discovery_prefix'
ATTR_TEMP_UNIT = 'temp_unit'
ATTR_QOS = 'qos'

ATTR_TEMPLATE_TEMPERATURE = '{{ value | float | round(1) }}'
ATTR_TEMPLATE_HUMIDITY = '{{ value | float | round(1) }}'
ATTR_TEMPLATE_LUX = '{{ value | float | round }}'
ATTR_TEMPLATE_POWER = '{{ value | float | round(1) }}'
ATTR_TEMPLATE_ENERGY = '{{ (value | float / 60 / 1000) | round(2) }}'
ATTR_TEMPLATE_BATTERY = '{{ value | float | round }}'

ATTR_MANUFACTURER = 'Allterco Robotics'
ATTR_MODEL_SHELLY1 = 'Shelly1'
ATTR_MODEL_SHELLY1PM = 'Shelly1PM'
ATTR_MODEL_SHELLY2 = 'Shelly2'
ATTR_MODEL_SHELLY25 = 'Shelly2.5'
ATTR_MODEL_SHELLYPLUG = 'Shelly Plug'
ATTR_MODEL_SHELLYPLUG_S = 'Shelly Plug S'
ATTR_MODEL_SHELLY4PRO = 'Shelly4Pro'
ATTR_MODEL_SHELLYHT = 'Shelly H&T'
ATTR_MODEL_SHELLYSMOKE = 'Shelly Smoke'
ATTR_MODEL_SHELLYSENSE = 'Shelly Sense'
ATTR_MODEL_SHELLYRGBW2 = 'Shelly RGBW2'
ATTR_SHELLY = 'Shelly'
ATTR_TEMPERATURE = 'temperature'
ATTR_HUMIDITY = 'humidity'
ATTR_BATTERY = 'battery'
ATTR_LUX = 'lux'
ATTR_ILLUMINANCE = 'illuminance'
ATTR_POWER = 'power'
ATTR_ENERGY = 'energy'
ATTR_SWITCH = 'switch'
ATTR_LIGHT = 'light'
ATTR_RGBW = 'rgbw'
ATTR_WHITE = 'white'
ATTR_FAN = 'fan'
ATTR_SMOKE = 'smoke'
ATTR_MOTION = 'motion'
ATTR_CHARGER = 'charger'
ATTR_INPUT = 'input'
ATTR_LONGPUSH = 'longpush'
ATTR_OVERTEMPERATURE = 'overtemperature'
ATTR_HEAT = 'heat'
ATTR_COVER = 'cover'
ATTR_UNIT_W = 'W'
ATTR_UNIT_KWH = 'kWh'
ATTR_UNIT_PERCENT = '%'
ATTR_UNIT_LUX = 'lx'
ATTR_UNIT_CELSIUS = '°C'
ATTR_UNIT_FARENHEIT = '°F'
ATTR_ON = 'on'
ATTR_OFF = 'off'
ATTR_TRUE_FALSE_PAYLOAD = {ATTR_ON: 'true', ATTR_OFF: 'false'}
ATTR_1_0_PAYLOAD = {ATTR_ON: '1', ATTR_OFF: '0'}
ATTR_EXPIRE_AFTER = '7200'

develop = False
retain = True
qos = 0
roller_mode = False

id = data.get(ATTR_ID)
mac = data.get(ATTR_MAC)
fw_ver = data.get(ATTR_FW_VER)
try:
    if data.get(ATTR_QOS):
        if int(data.get(ATTR_QOS)) in [0, 1, 2]:
            qos = int(data.get(ATTR_QOS))
        else:
            raise ValueError
except ValueError:
    logger.error("Wrong qos argument! Should be 0, 1 or 2. The default \
                        value 0 was used.")
temp_unit = ATTR_UNIT_CELSIUS
if data.get(ATTR_TEMP_UNIT) is not None:
    if data.get(ATTR_TEMP_UNIT) == 'F':
        temp_unit = ATTR_UNIT_FARENHEIT
disc_prefix = 'homeassistant'
if data.get(ATTR_DISCOVERY_PREFIX) is not None:
    disc_prefix = data.get(ATTR_DISCOVERY_PREFIX)

if data.get(ATTR_DEVELOP) is not None:
    develop = data.get(ATTR_DEVELOP)
if develop:
    disc_prefix = 'develop'
    retain = False
    logger.error("DEVELOP MODE !!!")

if id == '' or mac == '':
    logger.error("Expected id and mac as arguments.")
else:
    relays = 0
    rollers = 0
    relay_components = [ATTR_SWITCH, ATTR_LIGHT, ATTR_FAN]
    config_component = ATTR_SWITCH
    config_light = ATTR_RGBW
    relays_sensors = []
    relays_sensors_units = []
    relays_sensors_templates = []
    relays_sensors_classes = []
    relays_bin_sensors = []
    relays_bin_sensors_payload = []
    sensors = []
    sensors_units = []
    sensors_templates = []
    sensors_classes = []
    bin_sensors = []
    bin_sensors_classes = []
    rgbw_lights = 0
    white_lights = 0
    battery_powered = False

    if id[:-7] == 'shelly1':
        model = ATTR_MODEL_SHELLY1
        relays = 1
        relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
        relays_bin_sensors_payload = [ATTR_1_0_PAYLOAD, ATTR_1_0_PAYLOAD]

    if id[:-7] == 'shelly1pm':
        model = ATTR_MODEL_SHELLY1PM
        relays = 1
        relays_sensors = [ATTR_POWER, ATTR_ENERGY]
        relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
        relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
        relays_sensors_templates = [
            ATTR_TEMPLATE_POWER,
            ATTR_TEMPLATE_ENERGY
        ]
        relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
        relays_bin_sensors_payload = [ATTR_1_0_PAYLOAD, ATTR_1_0_PAYLOAD]
        sensors = [ATTR_TEMPERATURE]
        sensors_classes = sensors
        sensors_units = [temp_unit]
        sensors_templates = [ATTR_TEMPLATE_TEMPERATURE]
        bin_sensors = [ATTR_OVERTEMPERATURE]
        bin_sensors_classes = [ATTR_HEAT]
        bin_sensors_payload = [ATTR_1_0_PAYLOAD]

    if id[:-7] == 'shellyswitch':
        model = ATTR_MODEL_SHELLY2
        relays = 2
        rollers = 1
        relays_sensors = [ATTR_POWER, ATTR_ENERGY]
        relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
        relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
        relays_sensors_templates = [
            ATTR_TEMPLATE_POWER,
            ATTR_TEMPLATE_ENERGY
        ]
        relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
        relays_bin_sensors_payload = [ATTR_1_0_PAYLOAD, ATTR_1_0_PAYLOAD]

    if id[:-7] == 'shellyswitch25':
        model = ATTR_MODEL_SHELLY25
        relays = 2
        rollers = 1
        relays_sensors = [ATTR_POWER, ATTR_ENERGY]
        relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
        relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
        relays_sensors_templates = [
            ATTR_TEMPLATE_POWER,
            ATTR_TEMPLATE_ENERGY
        ]
        relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
        relays_bin_sensors_payload = [ATTR_1_0_PAYLOAD, ATTR_1_0_PAYLOAD]
        sensors = [ATTR_TEMPERATURE]
        sensors_classes = sensors
        sensors_units = [temp_unit]
        sensors_templates = [ATTR_TEMPLATE_TEMPERATURE]
        bin_sensors = [ATTR_OVERTEMPERATURE]
        bin_sensors_classes = [ATTR_HEAT]
        bin_sensors_payload = [ATTR_1_0_PAYLOAD]

    if id[:-7] == 'shellyplug':
        model = ATTR_MODEL_SHELLYPLUG
        relays = 1
        relays_sensors = [ATTR_POWER, ATTR_ENERGY]
        relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
        relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
        relays_sensors_templates = [
            ATTR_TEMPLATE_POWER,
            ATTR_TEMPLATE_ENERGY
        ]

    if id[:-7] == 'shellyplug-s':
        model = ATTR_MODEL_SHELLYPLUG_S
        relays = 1
        relays_sensors = [ATTR_POWER, ATTR_ENERGY]
        relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
        relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
        relays_sensors_templates = [
            ATTR_TEMPLATE_POWER,
            ATTR_TEMPLATE_ENERGY
        ]
        sensors = [ATTR_TEMPERATURE]
        sensors_classes = sensors
        sensors_units = [temp_unit]
        sensors_templates = [ATTR_TEMPLATE_TEMPERATURE]
        bin_sensors = [ATTR_OVERTEMPERATURE]
        bin_sensors_classes = [ATTR_HEAT]
        bin_sensors_payload = [ATTR_1_0_PAYLOAD]

    if id[:-7] == 'shelly4pro':
        model = ATTR_MODEL_SHELLY4PRO
        relays = 4
        relays_sensors = [ATTR_POWER, ATTR_ENERGY]
        relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
        relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
        relays_sensors_templates = [
            ATTR_TEMPLATE_POWER,
            ATTR_TEMPLATE_ENERGY
        ]

    if id[:-7] == 'shellyht':
        model = ATTR_MODEL_SHELLYHT
        sensors = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_BATTERY]
        sensors_classes = sensors
        sensors_units = [temp_unit, ATTR_UNIT_PERCENT, ATTR_UNIT_PERCENT]
        sensors_templates = [
            ATTR_TEMPLATE_TEMPERATURE,
            ATTR_TEMPLATE_HUMIDITY,
            ATTR_TEMPLATE_BATTERY
        ]
        battery_powered = True

    if id[:-7] == 'shellysmoke':
        model = ATTR_MODEL_SHELLYSMOKE
        sensors = [ATTR_TEMPERATURE, ATTR_BATTERY]
        sensors_classes = sensors
        sensors_units = [temp_unit, ATTR_UNIT_PERCENT]
        sensors_templates = [
            ATTR_TEMPLATE_TEMPERATURE,
            ATTR_TEMPLATE_BATTERY
        ]
        bin_sensors = [ATTR_SMOKE]
        bin_sensors_classes = bin_sensors
        bin_sensors_payload = [ATTR_TRUE_FALSE_PAYLOAD]
        battery_powered = True

    if id[:-7] == 'shellysense':
        model = ATTR_MODEL_SHELLYSENSE
        sensors = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_LUX, ATTR_BATTERY]
        sensors_classes = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_ILLUMINANCE,
                           ATTR_BATTERY]
        sensors_units = [temp_unit, ATTR_UNIT_PERCENT, ATTR_UNIT_LUX,
                         ATTR_UNIT_PERCENT]
        sensors_templates = [
            ATTR_TEMPLATE_TEMPERATURE,
            ATTR_TEMPLATE_HUMIDITY,
            ATTR_TEMPLATE_LUX,
            ATTR_TEMPLATE_BATTERY
        ]
        bin_sensors = [ATTR_MOTION, ATTR_CHARGER]
        bin_sensors_classes = [ATTR_MOTION, ATTR_POWER]
        bin_sensors_payload = [
            ATTR_TRUE_FALSE_PAYLOAD,
            ATTR_TRUE_FALSE_PAYLOAD
        ]
        battery_powered = True

    if id[:-7] == 'shellyrgbw2':
        model = ATTR_MODEL_SHELLYRGBW2
        rgbw_lights = 1
        white_lights = 4

    for roller_id in range(0, rollers):
        device_name = '{} {}'.format(model, id.split('-')[-1])
        roller_name = '{} Roller {}'.format(device_name, roller_id)
        default_topic = 'shellies/{}/'.format(id)
        state_topic = '~roller/{}'.format(roller_id)
        command_topic = '{}/command'.format(state_topic)
        position_topic = '{}/pos'.format(state_topic)
        set_position_topic = '{}/command/pos'.format(state_topic)
        availability_topic = '~online'
        unique_id = '{}-roller-{}'.format(id, roller_id)
        if data.get(id):
            config_component = data.get(id)
        elif data.get(id.lower()):
            config_component = data.get(id.lower())
        component = ATTR_COVER
        config_topic = '{}/{}/{}-roller-{}/config'.format(disc_prefix,
                                                          component, id,
                                                          roller_id)
        if config_component == component:
            roller_mode = True
            payload = '{\"name\":\"' + roller_name + '\",' \
                '\"cmd_t\":\"' + command_topic + '\",' \
                '\"pos_t\":\"' + position_topic + '\",' \
                '\"set_pos_t\":\"' + set_position_topic + '\",' \
                '\"pl_open\":\"open\",' \
                '\"pl_cls\":\"close\",' \
                '\"pl_stop\":\"stop\",' \
                '\"opt\":\"false\",' \
                '\"avty_t\":\"' + availability_topic + '\",' \
                '\"pl_avail\":\"true\",' \
                '\"pl_not_avail\":\"false\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        else:
            payload = ''
        service_data = {
            'topic': config_topic,
            'payload': payload,
            'retain': retain,
            'qos': qos
        }
        hass.services.call('mqtt', 'publish', service_data, False)

    for relay_id in range(0, relays):
        device_name = '{} {}'.format(model, id.split('-')[-1])
        relay_name = '{} Relay {}'.format(device_name, relay_id)
        default_topic = 'shellies/{}/'.format(id)
        state_topic = '~relay/{}'.format(relay_id)
        command_topic = '{}/command'.format(state_topic)
        availability_topic = '~online'
        unique_id = '{}-relay-{}'.format(id, relay_id)
        if data.get(unique_id):
            config_component = data.get(unique_id)
        elif data.get(unique_id.lower()):
            config_component = data.get(unique_id.lower())
        for component in relay_components:
            config_topic = '{}/{}/{}-relay-{}/config'.format(disc_prefix,
                                                             component, id,
                                                             relay_id)
            if component == config_component and not roller_mode:
                payload = '{\"name\":\"' + relay_name + '\",' \
                    '\"cmd_t\":\"' + command_topic + '\",' \
                    '\"stat_t\":\"' + state_topic + '\",' \
                    '\"pl_off\":\"off\",' \
                    '\"pl_on\":\"on\",' \
                    '\"avty_t\":\"' + availability_topic + '\",' \
                    '\"pl_avail\":\"true\",' \
                    '\"pl_not_avail\":\"false\",' \
                    '\"uniq_id\":\"' + unique_id + '\",' \
                    '\"qos\":\"' + str(qos) + '\",' \
                    '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                    '\"name\":\"' + device_name + '\",' \
                    '\"mdl\":\"' + model + '\",' \
                    '\"sw\":\"' + fw_ver + '\",' \
                    '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                    '\"~\":\"' + default_topic + '\"}'
            else:
                payload = ''
            service_data = {
                'topic': config_topic,
                'payload': payload,
                'retain': retain,
                'qos': qos
            }
            hass.services.call('mqtt', 'publish', service_data, False)

        if relay_id == relays-1:
            for sensor_id in range(0, len(relays_sensors)):
                unique_id = '{}-relay-{}'.format(id,
                                                 relays_sensors[sensor_id])
                config_topic = '{}/sensor/{}-{}/config'.format(disc_prefix, id,
                                                               relays_sensors[sensor_id])
                sensor_name = '{} {}'.format(device_name,
                                             relays_sensors[sensor_id].capitalize())
                state_topic = '~relay/{}'.format(relays_sensors[sensor_id])
                if model == ATTR_MODEL_SHELLY2 or roller_mode:
                    payload = '{\"name\":\"' + sensor_name + '\",' \
                        '\"stat_t\":\"' + state_topic + '\",' \
                        '\"unit_of_meas\":\"' + relays_sensors_units[sensor_id] + '\",' \
                        '\"dev_cla\":\"' + relays_sensors_classes[sensor_id] + '\",' \
                        '\"val_tpl\":\"' + relays_sensors_templates[sensor_id] + '\",' \
                        '\"avty_t\":\"' + availability_topic + '\",' \
                        '\"pl_avail\":\"true\",' \
                        '\"pl_not_avail\":\"false\",' \
                        '\"uniq_id\":\"' + unique_id + '\",' \
                        '\"qos\":\"' + str(qos) + '\",' \
                        '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                        '\"name\":\"' + device_name + '\",' \
                        '\"mdl\":\"' + model + '\",' \
                        '\"sw\":\"' + fw_ver + '\",' \
                        '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                        '\"~\":\"' + default_topic + '\"}'
                else:
                    payload = ''
                service_data = {
                    'topic': config_topic,
                    'payload': payload,
                    'retain': retain,
                    'qos': qos
                }
                hass.services.call('mqtt', 'publish', service_data, False)
        for sensor_id in range(0, len(relays_sensors)):
            unique_id = '{}-relay-{}-{}'.format(id, relays_sensors[sensor_id],
                                                relay_id)
            config_topic = '{}/sensor/{}-{}-{}/config'.format(disc_prefix, id,
                                                              relays_sensors[sensor_id],
                                                              relay_id)
            sensor_name = '{} {} {}'.format(device_name,
                                            relays_sensors[sensor_id].capitalize(
                                            ),
                                            relay_id)
            state_topic = '~relay/{}/{}'.format(relay_id,
                                                relays_sensors[sensor_id])
            if model != ATTR_MODEL_SHELLY2 and not roller_mode:
                payload = '{\"name\":\"' + sensor_name + '\",' \
                    '\"stat_t\":\"' + state_topic + '\",' \
                    '\"unit_of_meas\":\"' + relays_sensors_units[sensor_id] + '\",' \
                    '\"dev_cla\":\"' + relays_sensors_classes[sensor_id] + '\",' \
                    '\"val_tpl\":\"' + relays_sensors_templates[sensor_id] + '\",' \
                    '\"avty_t\":\"' + availability_topic + '\",' \
                    '\"pl_avail\":\"true\",' \
                    '\"pl_not_avail\":\"false\",' \
                    '\"uniq_id\":\"' + unique_id + '\",' \
                    '\"qos\":\"' + str(qos) + '\",' \
                    '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                    '\"name\":\"' + device_name + '\",' \
                    '\"mdl\":\"' + model + '\",' \
                    '\"sw\":\"' + fw_ver + '\",' \
                    '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                    '\"~\":\"' + default_topic + '\"}'
            else:
                payload = ''
            service_data = {
                'topic': config_topic,
                'payload': payload,
                'retain': retain,
                'qos': qos
            }
            hass.services.call('mqtt', 'publish', service_data, False)

        for bin_sensor_id in range(0, len(relays_bin_sensors)):
            unique_id = '{}-{}-{}'.format(id, relays_bin_sensors[bin_sensor_id],
                                          relay_id)
            config_topic = '{}/binary_sensor/{}-{}-{}/config'.format(disc_prefix,
                                            id,
                                            relays_bin_sensors[bin_sensor_id],
                                            relay_id)
            sensor_name = '{} {} {}'.format(device_name,
                                relays_bin_sensors[bin_sensor_id].capitalize(),
                                relay_id)
            state_topic = '~{}/{}'.format(relays_bin_sensors[bin_sensor_id],
                                          relay_id)
            if not roller_mode:
                payload = '{\"name\":\"' + sensor_name + '\",' \
                    '\"stat_t\":\"' + state_topic + '\",' \
                    '\"pl_on\":\"' + relays_bin_sensors_payload[bin_sensor_id][ATTR_ON] + '\",' \
                    '\"pl_off\":\"' + relays_bin_sensors_payload[bin_sensor_id][ATTR_OFF] + '\",' \
                    '\"avty_t\":\"' + availability_topic + '\",' \
                    '\"pl_avail\":\"true\",' \
                    '\"pl_not_avail\":\"false\",' \
                    '\"uniq_id\":\"' + unique_id + '\",' \
                    '\"qos\":\"' + str(qos) + '\",' \
                    '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                    '\"name\":\"' + device_name + '\",' \
                    '\"mdl\":\"' + model + '\",' \
                    '\"sw\":\"' + fw_ver + '\",' \
                    '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                    '\"~\":\"' + default_topic + '\"}'
            else:
                payload = ''
            service_data = {
                'topic': config_topic,
                'payload': payload,
                'retain': retain,
                'qos': qos
            }
            hass.services.call('mqtt', 'publish', service_data, False)

    for sensor_id in range(0, len(sensors)):
        device_name = '{} {}'.format(model, id.split('-')[-1])
        unique_id = '{}-{}'.format(id, sensors[sensor_id])
        config_topic = '{}/sensor/{}-{}/config'.format(disc_prefix, id,
                                                       sensors[sensor_id])
        default_topic = 'shellies/{}/'.format(id)
        availability_topic = '~online'
        sensor_name = '{} {}'.format(device_name,
                                     sensors[sensor_id].capitalize())
        if relays != 0:
            state_topic = '~{}'.format(sensors[sensor_id])
        else:
            state_topic = '~sensor/{}'.format(sensors[sensor_id])
        if battery_powered:
            payload = '{\"name\":\"' + sensor_name + '\",' \
                '\"stat_t\":\"' + state_topic + '\",' \
                '\"unit_of_meas\":\"' + sensors_units[sensor_id] + '\",' \
                '\"dev_cla\":\"' + sensors_classes[sensor_id] + '\",' \
                '\"val_tpl\":\"' + sensors_templates[sensor_id] + '\",' \
                '\"exp_aft\":\"' + ATTR_EXPIRE_AFTER + '\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        else:
            payload = '{\"name\":\"' + sensor_name + '\",' \
                '\"stat_t\":\"' + state_topic + '\",' \
                '\"unit_of_meas\":\"' + sensors_units[sensor_id] + '\",' \
                '\"dev_cla\":\"' + sensors_classes[sensor_id] + '\",' \
                '\"val_tpl\":\"' + sensors_templates[sensor_id] + '\",' \
                '\"avty_t\":\"' + availability_topic + '\",' \
                '\"pl_avail\":\"true\",' \
                '\"pl_not_avail\":\"false\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        service_data = {
            'topic': config_topic,
            'payload': payload,
            'retain': retain,
            'qos': qos
        }
        hass.services.call('mqtt', 'publish', service_data, False)

    for bin_sensor_id in range(0, len(bin_sensors)):
        device_name = '{} {}'.format(model, id.split('-')[-1])
        unique_id = '{}-{}'.format(id, bin_sensors[bin_sensor_id])
        config_topic = '{}/binary_sensor/{}-{}/config'.format(disc_prefix, id,
                                                              bin_sensors[bin_sensor_id])
        default_topic = 'shellies/{}/'.format(id)
        availability_topic = '~online'
        sensor_name = '{} {}'.format(device_name,
                                     bin_sensors[bin_sensor_id].capitalize())
        if relays != 0:
            state_topic = '~{}'.format(bin_sensors[bin_sensor_id])
        else:
            state_topic = '~sensor/{}'.format(bin_sensors[bin_sensor_id])
        if battery_powered:
            payload = '{\"name\":\"' + sensor_name + '\",' \
                '\"stat_t\":\"' + state_topic + '\",' \
                '\"pl_on\":\"' + bin_sensors_payload[bin_sensor_id][ATTR_ON] + '\",' \
                '\"pl_off\":\"' + bin_sensors_payload[bin_sensor_id][ATTR_OFF] + '\",' \
                '\"dev_cla\":\"' + bin_sensors_classes[bin_sensor_id] + '\",' \
                '\"exp_aft\":\"' + ATTR_EXPIRE_AFTER + '\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        else:
            payload = '{\"name\":\"' + sensor_name + '\",' \
                '\"stat_t\":\"' + state_topic + '\",' \
                '\"pl_on\":\"' + bin_sensors_payload[bin_sensor_id][ATTR_ON] + '\",' \
                '\"pl_off\":\"' + bin_sensors_payload[bin_sensor_id][ATTR_OFF] + '\",' \
                '\"avty_t\":\"' + availability_topic + '\",' \
                '\"pl_avail\":\"true\",' \
                '\"pl_not_avail\":\"false\",' \
                '\"dev_cla\":\"' + bin_sensors_classes[bin_sensor_id] + '\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        service_data = {
            'topic': config_topic,
            'payload': payload,
            'retain': retain,
            'qos': qos
        }
        hass.services.call('mqtt', 'publish', service_data, False)

    for light_id in range(0, rgbw_lights):
        device_name = '{} {}'.format(model, id.split('-')[-1])
        light_name = '{} Light {}'.format(device_name, light_id)
        default_topic = 'shellies/{}/'.format(id)
        state_topic = '~color/{}/status'.format(light_id)
        command_topic = '~color/{}/set'.format(light_id)
        availability_topic = '~online'
        unique_id = '{}-light-{}'.format(id, light_id)
        config_topic = '{}/light/{}-{}/config'.format(
            disc_prefix, id, light_id)
        if data.get(id):
            config_light = data.get(id)
        elif data.get(id.lower()):
            config_light = data.get(id.lower())
        if config_light == ATTR_RGBW:
            payload = '{\"schema\":\"template\",' \
                '\"name\":\"' + light_name + '\",' \
                '\"cmd_t\":\"' + command_topic + '\",' \
                '\"stat_t\":\"' + state_topic + '\",' \
                '\"avty_t\":\"' + availability_topic + '\",' \
                '\"pl_avail\":\"true\",' \
                '\"pl_not_avail\":\"false\",' \
                '\"fx_list\":[0, 1, 2, 3, 4, 5, 5],' \
                '\"cmd_on_tpl\":\"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"gain\\":{{ brightness | float | multiply(0.3922) | round(0) }}{% endif %}{% if red is defined and green is defined and blue is defined %},\\"red\\":{{ red }},\\"green\\":{{ green }},\\"blue\\":{{ blue }}{% endif %}{% if white_value is defined %},\\"white\\":{{ white_value }}{% endif %}{% if effect is defined %},\\"effect\\":{{ effect }}{% endif %}}\",' \
                '\"cmd_off_tpl\":\"{\\"turn\\":\\"off\\"}\",' \
                '\"stat_tpl\":\"{% if value_json.ison %}on{% else %}off{% endif %}\",' \
                '\"bri_tpl\":\"{{ value_json.gain | float | multiply(2.55) | round(0) }}\",' \
                '\"r_tpl\":\"{{ value_json.red }}\",' \
                '\"g_tpl\":\"{{ value_json.green }}\",' \
                '\"b_tpl\":\"{{ value_json.blue }}\",' \
                '\"whit_val_tpl\":\"{{ value_json.white }}\",' \
                '\"fx_tpl\":\"{{ value_json.effect }}\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        else:
            payload = ''
        service_data = {
            'topic': config_topic,
            'payload': payload,
            'retain': retain,
            'qos': qos
        }
        hass.services.call('mqtt', 'publish', service_data, False)

    for light_id in range(0, white_lights):
        device_name = '{} {}'.format(model, id.split('-')[-1])
        light_name = '{} Light {}'.format(device_name, light_id)
        default_topic = 'shellies/{}/'.format(id)
        state_topic = '~white/{}/status'.format(light_id)
        command_topic = '~white/{}/set'.format(light_id)
        availability_topic = '~online'
        unique_id = '{}-light-white-{}'.format(id, light_id)
        config_topic = '{}/light/{}-white-{}/config'.format(
            disc_prefix, id, light_id)
        if data.get(id):
            config_light = data.get(id)
        elif data.get(id.lower()):
            config_light = data.get(id.lower())
        if config_light == ATTR_WHITE:
            payload = '{\"schema\":\"template\",' \
                '\"name\":\"' + light_name + '\",' \
                '\"cmd_t\":\"' + command_topic + '\",' \
                '\"stat_t\":\"' + state_topic + '\",' \
                '\"avty_t\":\"' + availability_topic + '\",' \
                '\"pl_avail\":\"true\",' \
                '\"pl_not_avail\":\"false\",' \
                '\"cmd_on_tpl\":\"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"brightness\\":{{brightness | float | multiply(0.3922) | round(0)}}{% endif %}{% if red is defined and green is defined and blue is defined %},\\"red\\":{{ red }},\\"green\\":{{ green }},\\"blue\\":{{ blue }}{% endif %}{% if white_value is defined %},\\"white\\":{{ white_value }}{% endif %}{% if effect is defined %},\\"effect\\":{{ effect }}{% endif %}}\",' \
                '\"cmd_off_tpl\":\"{\\"turn\\":\\"off\\"}\",' \
                '\"stat_tpl\":\"{% if value_json.ison %}on{% else %}off{% endif %}\",' \
                '\"bri_tpl\":\"{{ value_json.brightness | float | multiply(2.55) | round(0) }}\",' \
                '\"uniq_id\":\"' + unique_id + '\",' \
                '\"qos\":\"' + str(qos) + '\",' \
                '\"dev\": {\"ids\": [\"' + mac + '\"],' \
                '\"name\":\"' + device_name + '\",' \
                '\"mdl\":\"' + model + '\",' \
                '\"sw\":\"' + fw_ver + '\",' \
                '\"mf\":\"' + ATTR_MANUFACTURER + '\"},' \
                '\"~\":\"' + default_topic + '\"}'
        else:
            payload = ''
        service_data = {
            'topic': config_topic,
            'payload': payload,
            'retain': retain,
            'qos': qos
        }
        hass.services.call('mqtt', 'publish', service_data, False)
