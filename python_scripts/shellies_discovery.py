"""
This script adds MQTT discovery support for Shellies devices.
"""
ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_SHELLY = "Shelly"

ATTR_MODEL_SHELLY1 = "Shelly1"
ATTR_MODEL_SHELLY1PM = "Shelly1PM"
ATTR_MODEL_SHELLY2 = "Shelly2"
ATTR_MODEL_SHELLY25 = "Shelly2.5"
ATTR_MODEL_SHELLY4PRO = "Shelly4Pro"
ATTR_MODEL_SHELLYBULB = "Shelly Bulb"
ATTR_MODEL_SHELLYDIMMER = "Shelly Dimmer"
ATTR_MODEL_SHELLYDUO = "Shelly DUO"
ATTR_MODEL_SHELLYDW = "Shelly Door/Window"
ATTR_MODEL_SHELLYFLOOD = "Shelly Flood"
ATTR_MODEL_SHELLYHT = "Shelly H&T"
ATTR_MODEL_SHELLYPLUG = "Shelly Plug"
ATTR_MODEL_SHELLYPLUG_S = "Shelly Plug S"
ATTR_MODEL_SHELLYRGBW2 = "Shelly RGBW2"
ATTR_MODEL_SHELLYSENSE = "Shelly Sense"
ATTR_MODEL_SHELLYSMOKE = "Shelly Smoke"
ATTR_MODEL_SHELLY_3EM = "Shelly 3EM"
ATTR_MODEL_SHELLY_EM = "Shelly EM"

ATTR_BATTERY = "battery"
ATTR_CHARGER = "charger"
ATTR_COVER = "cover"
ATTR_CURRENT = "current"
ATTR_ENERGY = "energy"
ATTR_FAN = "fan"
ATTR_FLOOD = "flood"
ATTR_HEAT = "heat"
ATTR_HUMIDITY = "humidity"
ATTR_ILLUMINANCE = "illuminance"
ATTR_INPUT = "input"
ATTR_INPUT_0 = "input/0"
ATTR_INPUT_1 = "input/1"
ATTR_LIGHT = "light"
ATTR_LOADERROR = "loaderror"
ATTR_LONGPUSH = "longpush"
ATTR_LONGPUSH_0 = "longpush/0"
ATTR_LONGPUSH_1 = "longpush/1"
ATTR_LUX = "lux"
ATTR_MOISTURE = "moisture"
ATTR_MOTION = "motion"
ATTR_OPENING = "opening"
ATTR_OVERLOAD = "overload"
ATTR_OVERPOWER = "overpower"
ATTR_OVERTEMPERATURE = "overtemperature"
ATTR_POWER = "power"
ATTR_POWER_FACTOR = "pf"
ATTR_PROBLEM = "problem"
ATTR_REACTIVE_POWER = "reactive_power"
ATTR_RETURNED_ENERGY = "returned_energy"
ATTR_RGBW = "rgbw"
ATTR_SMOKE = "smoke"
ATTR_SWITCH = "switch"
ATTR_TEMPERATURE = "temperature"
ATTR_TOTAL = "total"
ATTR_TOTAL_RETURNED = "total_returned"
ATTR_VOLTAGE = "voltage"
ATTR_WHITE = "white"

ATTR_AC_POWER = "ac_power"

CONF_DEVELOP = "develop"
CONF_DISCOVERY_PREFIX = "discovery_prefix"
CONF_FORCE_UPDATE = "force_update"
CONF_FW_VER = "fw_ver"
CONF_ID = "id"
CONF_IGNORED_DEVICES = "ignored_devices"
CONF_MAC = "mac"
CONF_QOS = "qos"

DEFAULT_DISC_PREFIX = "homeassistant"

KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_COMMAND_TOPIC = "cmd_t"
KEY_DEVICE = "dev"
KEY_DEVICE_CLASS = "dev_cla"
KEY_EXPIRE_AFTER = "exp_aft"
KEY_FORCE_UPDATE = "frc_upd"
KEY_IDENTIFIERS = "ids"
KEY_MANUFACTURER = "mf"
KEY_MODEL = "mdl"
KEY_NAME = "name"
KEY_OFF_DELAY = "off_delay"
KEY_OPTIMISTIC = "opt"
KEY_PAYLOAD = "payload"
KEY_PAYLOAD_AVAILABLE = "pl_avail"
KEY_PAYLOAD_CLOSE = "pl_cls"
KEY_PAYLOAD_NOT_AVAILABLE = "pl_not_avail"
KEY_PAYLOAD_OFF = "pl_off"
KEY_PAYLOAD_ON = "pl_on"
KEY_PAYLOAD_OPEN = "pl_open"
KEY_PAYLOAD_STOP = "pl_stop"
KEY_POSITION_TOPIC = "pos_t"
KEY_QOS = "qos"
KEY_RETAIN = "retain"
KEY_SET_POSITION_TOPIC = "set_pos_t"
KEY_STATE_TOPIC = "stat_t"
KEY_SW_VERSION = "sw"
KEY_TOPIC = "topic"
KEY_UNIQUE_ID = "uniq_id"
KEY_UNIT = "unit_of_meas"
KEY_VALUE_TEMPLATE = "val_tpl"

TPL_BATTERY = "{{value|float|round}}"
TPL_CURRENT = "{{value|float|round(2)}}"
TPL_ENERGY_WH = "{{(value|float/1000)|round(2)}}"
TPL_ENERGY_WMIN = "{{(value|float/60/1000)|round(2)}}"
TPL_HUMIDITY = "{{value|float|round(1)}}"
TPL_LUX = "{{value|float|round}}"
TPL_OVERPOWER = "{% if value_json.overpower == true %}ON{% else %}OFF{% endif %}"
TPL_POWER = "{{value|float|round(1)}}"
TPL_POWER_FACTOR = "{{value|float*100|round}}"
TPL_TEMPERATURE = "{{value|float|round(1)}}"
TPL_TEMPERATURE_EXT = "{{value|replace(':','')|float|round(1)}}"
TPL_VOLTAGE = "{{value|float|round(1)}}"

UNIT_AMPERE = "A"
UNIT_CELSIUS = "°C"
UNIT_KWH = "kWh"
UNIT_LUX = "lx"
UNIT_PERCENT = "%"
UNIT_VAR = "VAR"
UNIT_VOLT = "V"
UNIT_WATT = "W"

VALUE_CLOSE = "close"
VALUE_FALSE = "false"
VALUE_OFF = "off"
VALUE_ON = "on"
VALUE_OPEN = "open"
VALUE_STOP = "stop"
VALUE_TRUE = "true"

PL_1_0 = {VALUE_ON: "1", VALUE_OFF: "0"}
PL_OPEN_CLOSE = {VALUE_ON: "open", VALUE_OFF: "close"}
PL_TRUE_FALSE = {VALUE_ON: "true", VALUE_OFF: "false"}

expire_after = 43200
off_delay = 3


def mqtt_publish(topic, payload, retain, qos):
    service_data = {
        KEY_TOPIC: topic,
        KEY_PAYLOAD: payload,
        KEY_RETAIN: retain,
        KEY_QOS: qos,
    }
    logger.debug("Send to MQTT broker: %s %s", topic, payload)
    hass.services.call("mqtt", "publish", service_data, False)


if data.get(CONF_FORCE_UPDATE, False) in [True, False]:
    force_update = data.get(CONF_FORCE_UPDATE, False)
else:
    logger.error("Wrong force_update argument, the default value false was used")

retain = True
qos = 0
roller_mode = False

no_battery_sensor = False

id = data.get(CONF_ID)
mac = data.get(CONF_MAC)
fw_ver = data.get(CONF_FW_VER)
ignored = [element.lower() for element in data.get(CONF_IGNORED_DEVICES, [])]

if not id:
    raise ValueError(f"{id} is wrong id argument")
if not mac:
    raise ValueError(f"{mac} is wrong mac argument")
if not fw_ver:
    raise ValueError(f"{fw_ver} is wrong mac argument")

logger.debug("id: %s, mac: %s, fw_ver: %s", id, mac, fw_ver)

try:
    if int(data.get(CONF_QOS, 0)) in [0, 1, 2]:
        qos = int(data.get(CONF_QOS, 0))
    else:
        raise ValueError()
except ValueError:
    logger.error("Wrong qos argument, the default value 0 was used")

disc_prefix = data.get(CONF_DISCOVERY_PREFIX, DEFAULT_DISC_PREFIX)

develop = data.get(CONF_DEVELOP, False)
if develop:
    disc_prefix = "develop"
    retain = False
    logger.error("DEVELOP MODE !!!")


relays = 0
rollers = 0
meters = 0
relay_components = [ATTR_SWITCH, ATTR_LIGHT, ATTR_FAN]
relays_sensors = []
relays_sensors_units = []
relays_sensors_tpls = []
relays_sensors_classes = []
relays_bin_sensors = []
relays_bin_sensors_pl = []
lights_bin_sensors = []
lights_bin_sensors_pl = []
lights_sensors = []
lights_sensors_classes = []
lights_sensors_units = []
lights_sensors_tpls = []
sensors = []
sensors_units = []
sensors_tpls = []
sensors_classes = []
bin_sensors = []
bin_sensors_classes = []
rgbw_lights = 0
white_lights = 0
ext_sensors = 0
battery_powered = False
ext_sensor_type = None

if id.rsplit("-", 1)[0] == "shelly1":
    model = ATTR_MODEL_SHELLY1
    relays = 1
    relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0]
    ext_sensors = 3

if id.rsplit("-", 1)[0] == "shelly1pm":
    model = ATTR_MODEL_SHELLY1PM
    relays = 1
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0]
    sensors = [ATTR_TEMPERATURE]
    sensors_classes = sensors
    sensors_units = [UNIT_CELSIUS]
    sensors_tpls = [TPL_TEMPERATURE]
    bin_sensors = [ATTR_OVERTEMPERATURE]
    bin_sensors_classes = [ATTR_HEAT]
    bin_sensors_pl = [PL_1_0]
    ext_sensors = 3

if id.rsplit("-", 1)[0] == "shellyswitch":
    model = ATTR_MODEL_SHELLY2
    relays = 2
    rollers = 1
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0]

if id.rsplit("-", 1)[0] == "shellyswitch25":
    model = ATTR_MODEL_SHELLY25
    relays = 2
    rollers = 1
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0]
    sensors = [ATTR_TEMPERATURE]
    sensors_classes = sensors
    sensors_units = [UNIT_CELSIUS]
    sensors_tpls = [TPL_TEMPERATURE]
    bin_sensors = [ATTR_OVERTEMPERATURE]
    bin_sensors_classes = [ATTR_HEAT]
    bin_sensors_pl = [PL_1_0]

if id.rsplit("-", 1)[0] == "shellyplug":
    model = ATTR_MODEL_SHELLYPLUG
    relays = 1
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]

if id.rsplit("-", 1)[0] == "shellyplug-s":
    model = ATTR_MODEL_SHELLYPLUG_S
    relays = 1
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    sensors = [ATTR_TEMPERATURE]
    sensors_classes = [ATTR_TEMPERATURE]
    sensors_units = [UNIT_CELSIUS]
    sensors_tpls = [TPL_TEMPERATURE]
    bin_sensors = [ATTR_OVERTEMPERATURE]
    bin_sensors_classes = [ATTR_HEAT]
    bin_sensors_pl = [PL_1_0]

if id.rsplit("-", 1)[0] == "shelly4pro":
    model = ATTR_MODEL_SHELLY4PRO
    relays = 4
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]

if id.rsplit("-", 1)[0] == "shellyht":
    model = ATTR_MODEL_SHELLYHT
    sensors = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_BATTERY]
    sensors_classes = sensors
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_HUMIDITY, TPL_BATTERY]
    battery_powered = True

if id.rsplit("-", 1)[0] == "shellydw":
    model = ATTR_MODEL_SHELLYDW
    sensors = [ATTR_LUX, ATTR_BATTERY]
    sensors_classes = [ATTR_ILLUMINANCE, ATTR_BATTERY]
    sensors_units = [UNIT_LUX, UNIT_PERCENT]
    sensors_tpls = [TPL_LUX, TPL_BATTERY]
    bin_sensors = [ATTR_OPENING]
    bin_sensors_classes = bin_sensors
    bin_sensors_pl = [PL_OPEN_CLOSE]
    battery_powered = True

if id.rsplit("-", 1)[0] == "shellysmoke":
    model = ATTR_MODEL_SHELLYSMOKE
    sensors = [ATTR_TEMPERATURE, ATTR_BATTERY]
    sensors_classes = sensors
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_BATTERY]
    bin_sensors = [ATTR_SMOKE]
    bin_sensors_classes = bin_sensors
    bin_sensors_pl = [PL_TRUE_FALSE]
    battery_powered = True

if id.rsplit("-", 1)[0] == "shellysense":
    model = ATTR_MODEL_SHELLYSENSE
    sensors = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_LUX, ATTR_BATTERY]
    sensors_classes = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_ILLUMINANCE, ATTR_BATTERY]
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT, UNIT_LUX, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_HUMIDITY, TPL_LUX, TPL_BATTERY]
    bin_sensors = [ATTR_MOTION, ATTR_CHARGER]
    bin_sensors_classes = [ATTR_MOTION, ATTR_POWER]
    bin_sensors_pl = [PL_TRUE_FALSE, PL_TRUE_FALSE]
    battery_powered = True

if id.rsplit("-", 1)[0] == "shellyrgbw2":
    model = ATTR_MODEL_SHELLYRGBW2
    rgbw_lights = 1
    white_lights = 4
    lights_sensors = [ATTR_POWER]
    lights_sensors_classes = [ATTR_POWER]
    lights_sensors_units = [UNIT_WATT]
    lights_sensors_tpls = ["{{value_json.power|float|round(1)}}"]
    lights_bin_sensors = [ATTR_OVERPOWER, ATTR_INPUT]
    lights_bin_sensors_classes = [ATTR_POWER, None]
    lights_bin_sensors_tpls = [TPL_OVERPOWER, None]
    lights_bin_sensors_pl = [None, PL_1_0]

if id.rsplit("-", 1)[0] == "shellydimmer":
    model = ATTR_MODEL_SHELLYDIMMER
    white_lights = 1
    sensors = [ATTR_TEMPERATURE]
    sensors_classes = [ATTR_TEMPERATURE]
    sensors_units = [UNIT_CELSIUS]
    sensors_tpls = [TPL_TEMPERATURE]
    bin_sensors = [
        ATTR_OVERTEMPERATURE,
        ATTR_OVERLOAD,
        ATTR_LOADERROR,
        ATTR_INPUT_0,
        ATTR_INPUT_1,
        ATTR_LONGPUSH_0,
        ATTR_LONGPUSH_1,
    ]
    bin_sensors_classes = [ATTR_HEAT, ATTR_POWER, ATTR_PROBLEM, None, None, None, None]
    bin_sensors_pl = [PL_1_0, PL_1_0, PL_1_0, PL_1_0, PL_1_0, PL_1_0, PL_1_0]
    lights_sensors = [ATTR_POWER, ATTR_ENERGY]
    lights_sensors_units = [UNIT_WATT, UNIT_KWH]
    lights_sensors_classes = [ATTR_POWER, ATTR_POWER]
    lights_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]

if id.rsplit("-", 1)[0] == "shellybulb":
    model = ATTR_MODEL_SHELLYBULB
    rgbw_lights = 1

if id.rsplit("-", 1)[0] == "ShellyBulbDuo":
    model = ATTR_MODEL_SHELLYDUO
    white_lights = 1
    lights_sensors = [ATTR_ENERGY, ATTR_POWER]
    lights_sensors_units = [UNIT_KWH, UNIT_WATT]
    lights_sensors_classes = [ATTR_POWER, ATTR_POWER]
    lights_sensors_tpls = [TPL_ENERGY_WMIN, TPL_POWER]

if id.rsplit("-", 1)[0] == "shellyem":
    model = ATTR_MODEL_SHELLY_EM
    relays = 1
    relays_sensors = [ATTR_POWER, ATTR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    meters = 2
    meters_sensors = [
        ATTR_POWER,
        ATTR_REACTIVE_POWER,
        ATTR_VOLTAGE,
        ATTR_ENERGY,
        ATTR_RETURNED_ENERGY,
        ATTR_TOTAL,
        ATTR_TOTAL_RETURNED,
    ]
    meters_sensors_units = [
        UNIT_WATT,
        UNIT_VAR,
        UNIT_VOLT,
        UNIT_KWH,
        UNIT_KWH,
        UNIT_KWH,
        UNIT_KWH,
    ]
    meters_sensors_classes = [
        ATTR_POWER,
        None,
        None,
        ATTR_POWER,
        ATTR_POWER,
        ATTR_POWER,
        ATTR_POWER,
    ]
    meters_sensors_tpls = [
        TPL_POWER,
        TPL_POWER,
        TPL_VOLTAGE,
        TPL_ENERGY_WMIN,
        TPL_ENERGY_WMIN,
        TPL_ENERGY_WH,
        TPL_ENERGY_WH,
    ]

if id.rsplit("-", 1)[0] == "shellyem3":
    model = ATTR_MODEL_SHELLY_3EM
    relays = 1
    meters = 3
    meters_sensors = [
        ATTR_CURRENT,
        ATTR_POWER,
        ATTR_POWER_FACTOR,
        ATTR_VOLTAGE,
        ATTR_ENERGY,
        ATTR_RETURNED_ENERGY,
        ATTR_TOTAL,
        ATTR_TOTAL_RETURNED,
    ]
    meters_sensors_units = [
        UNIT_AMPERE,
        UNIT_WATT,
        UNIT_PERCENT,
        UNIT_VOLT,
        UNIT_KWH,
        UNIT_KWH,
        UNIT_KWH,
        UNIT_KWH,
    ]
    meters_sensors_classes = [
        None,
        ATTR_POWER,
        None,
        None,
        ATTR_POWER,
        ATTR_POWER,
        ATTR_POWER,
        ATTR_POWER,
    ]
    meters_sensors_tpls = [
        TPL_CURRENT,
        TPL_POWER,
        TPL_POWER_FACTOR,
        TPL_VOLTAGE,
        TPL_ENERGY_WMIN,
        TPL_ENERGY_WMIN,
        TPL_ENERGY_WH,
        TPL_ENERGY_WH,
    ]

if id.rsplit("-", 1)[0] == "shellyflood":
    model = ATTR_MODEL_SHELLYFLOOD
    sensors = [ATTR_TEMPERATURE, ATTR_BATTERY]
    sensors_classes = sensors
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_BATTERY]
    bin_sensors = [ATTR_FLOOD]
    bin_sensors_classes = [ATTR_MOISTURE]
    bin_sensors_pl = [PL_TRUE_FALSE]
    battery_powered = True

# rollers
for roller_id in range(0, rollers):
    device_name = f"{model} {id.split('-')[-1]}"
    roller_name = f"{device_name} Roller {roller_id}"
    default_topic = f"shellies/{id}/"
    state_topic = f"~roller/{roller_id}"
    command_topic = f"{state_topic}/command"
    position_topic = f"{state_topic}/pos"
    set_position_topic = f"{state_topic}/command/pos"
    availability_topic = "~online"
    unique_id = f"{id}-roller-{roller_id}"
    config_component = data.get(id, data.get(id.lower()))
    component = ATTR_COVER
    config_topic = f"{disc_prefix}/{component}/{id}-roller-{roller_id}/config"
    if config_component == component:
        roller_mode = True
        payload = {
            KEY_NAME: roller_name,
            KEY_COMMAND_TOPIC: command_topic,
            KEY_POSITION_TOPIC: position_topic,
            KEY_SET_POSITION_TOPIC: set_position_topic,
            KEY_PAYLOAD_OPEN: VALUE_OPEN,
            KEY_PAYLOAD_CLOSE: VALUE_CLOSE,
            KEY_PAYLOAD_STOP: VALUE_STOP,
            KEY_OPTIMISTIC: VALUE_FALSE,
            KEY_AVAILABILITY_TOPIC: availability_topic,
            KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
            KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
            KEY_UNIQUE_ID: unique_id,
            KEY_QOS: qos,
            KEY_DEVICE: {
                KEY_IDENTIFIERS: [mac],
                KEY_NAME: device_name,
                KEY_MODEL: model,
                KEY_SW_VERSION: fw_ver,
                KEY_MANUFACTURER: ATTR_MANUFACTURER,
            },
            "~": default_topic,
        }
    else:
        payload = ""
    if id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# relays
for relay_id in range(0, relays):
    device_name = f"{model} {id.split('-')[-1]}"
    relay_name = f"{device_name} Relay {relay_id}"
    default_topic = f"shellies/{id}/"
    state_topic = f"~relay/{relay_id}"
    command_topic = f"{state_topic}/command"
    availability_topic = "~online"
    unique_id = f"{id}-relay-{relay_id}"
    config_component = data.get(unique_id, data.get(unique_id.lower(), ATTR_SWITCH))
    for component in relay_components:
        config_topic = f"{disc_prefix}/{component}/{id}-relay-{relay_id}/config"
        if component == config_component and not roller_mode:
            payload = {
                KEY_NAME: relay_name,
                KEY_COMMAND_TOPIC: command_topic,
                KEY_STATE_TOPIC: state_topic,
                KEY_PAYLOAD_OFF: VALUE_OFF,
                KEY_PAYLOAD_ON: VALUE_ON,
                KEY_AVAILABILITY_TOPIC: availability_topic,
                KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                KEY_UNIQUE_ID: unique_id,
                KEY_QOS: qos,
                KEY_DEVICE: {
                    KEY_IDENTIFIERS: [mac],
                    KEY_NAME: device_name,
                    KEY_MODEL: model,
                    KEY_SW_VERSION: fw_ver,
                    KEY_MANUFACTURER: ATTR_MANUFACTURER,
                },
                "~": default_topic,
            }
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # relay's sensors
    if relay_id == relays - 1:
        for sensor_id in range(0, len(relays_sensors)):
            unique_id = f"{id}-relay-{relays_sensors[sensor_id]}"
            config_topic = (
                f"{disc_prefix}/sensor/{id}-{relays_sensors[sensor_id]}/config"
            )
            sensor_name = f"{device_name} {relays_sensors[sensor_id].capitalize()}"
            state_topic = f"~relay/{relays_sensors[sensor_id]}"
            if model == ATTR_MODEL_SHELLY2 or roller_mode:
                payload = {
                    KEY_NAME: sensor_name,
                    KEY_STATE_TOPIC: state_topic,
                    KEY_UNIT: relays_sensors_units[sensor_id],
                    KEY_VALUE_TEMPLATE: relays_sensors_tpls[sensor_id],
                    KEY_DEVICE_CLASS: relays_sensors_classes[sensor_id],
                    KEY_AVAILABILITY_TOPIC: availability_topic,
                    KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                    KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                    KEY_FORCE_UPDATE: str(force_update),
                    KEY_UNIQUE_ID: unique_id,
                    KEY_QOS: qos,
                    KEY_DEVICE: {
                        KEY_IDENTIFIERS: [mac],
                        KEY_NAME: device_name,
                        KEY_MODEL: model,
                        KEY_SW_VERSION: fw_ver,
                        KEY_MANUFACTURER: ATTR_MANUFACTURER,
                    },
                    "~": default_topic,
                }
            else:
                payload = ""
            if id.lower() in ignored:
                payload = ""
            mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # relay's sensors
    for sensor_id in range(0, len(relays_sensors)):
        unique_id = f"{id}-relay-{relays_sensors[sensor_id]}-{relay_id}"
        config_topic = (
            f"{disc_prefix}/sensor/{id}-{relays_sensors[sensor_id]}-{relay_id}/config"
        )
        sensor_name = (
            f"{device_name} {relays_sensors[sensor_id].capitalize()} {relay_id}"
        )
        state_topic = f"~relay/{relay_id}/{relays_sensors[sensor_id]}"
        if model != ATTR_MODEL_SHELLY2 and not roller_mode:
            payload = {
                KEY_NAME: sensor_name,
                KEY_STATE_TOPIC: state_topic,
                KEY_UNIT: relays_sensors_units[sensor_id],
                KEY_VALUE_TEMPLATE: relays_sensors_tpls[sensor_id],
                KEY_DEVICE_CLASS: relays_sensors_classes[sensor_id],
                KEY_AVAILABILITY_TOPIC: availability_topic,
                KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                KEY_FORCE_UPDATE: str(force_update),
                KEY_UNIQUE_ID: unique_id,
                KEY_QOS: qos,
                KEY_DEVICE: {
                    KEY_IDENTIFIERS: [mac],
                    KEY_NAME: device_name,
                    KEY_MODEL: model,
                    KEY_SW_VERSION: fw_ver,
                    KEY_MANUFACTURER: ATTR_MANUFACTURER,
                },
                "~": default_topic,
            }
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # relay's binary sensors
    for bin_sensor_id in range(0, len(relays_bin_sensors)):
        unique_id = f"{id}-{relays_bin_sensors[bin_sensor_id]}-{relay_id}"
        config_topic = f"{disc_prefix}/binary_sensor/{id}-{relays_bin_sensors[bin_sensor_id]}-{relay_id}/config"
        sensor_name = (
            f"{device_name} {relays_bin_sensors[bin_sensor_id].capitalize()} {relay_id}"
        )
        state_topic = f"~{relays_bin_sensors[bin_sensor_id]}/{relay_id}"
        if not roller_mode:
            payload = {
                KEY_NAME: sensor_name,
                KEY_STATE_TOPIC: state_topic,
                KEY_PAYLOAD_ON: relays_bin_sensors_pl[bin_sensor_id][VALUE_ON],
                KEY_PAYLOAD_OFF: relays_bin_sensors_pl[bin_sensor_id][VALUE_OFF],
                KEY_AVAILABILITY_TOPIC: availability_topic,
                KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                KEY_UNIQUE_ID: unique_id,
                KEY_QOS: qos,
                KEY_DEVICE: {
                    KEY_IDENTIFIERS: [mac],
                    KEY_NAME: device_name,
                    KEY_MODEL: model,
                    KEY_SW_VERSION: fw_ver,
                    KEY_MANUFACTURER: ATTR_MANUFACTURER,
                },
                "~": default_topic,
            }
            if relays_bin_sensors[bin_sensor_id] == ATTR_LONGPUSH:
                payload[KEY_OFF_DELAY] = off_delay
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# sensors
for sensor_id in range(0, len(sensors)):
    device_name = f"{model} {id.split('-')[-1]}"
    unique_id = f"{id}-{sensors[sensor_id]}"
    config_topic = f"{disc_prefix}/sensor/{id}-{sensors[sensor_id]}/config"
    default_topic = f"shellies/{id}/"
    availability_topic = "~online"
    sensor_name = f"{device_name} {sensors[sensor_id].capitalize()}"
    if relays > 0 or white_lights > 0:
        state_topic = f"~{sensors[sensor_id]}"
    else:
        state_topic = f"~sensor/{sensors[sensor_id]}"
    if data.get(id, data.get(id.lower())) == ATTR_AC_POWER:
        no_battery_sensor = True
        expire_after = 7200
    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: state_topic,
        KEY_UNIT: sensors_units[sensor_id],
        KEY_DEVICE_CLASS: sensors_classes[sensor_id],
        KEY_VALUE_TEMPLATE: sensors_tpls[sensor_id],
        KEY_EXPIRE_AFTER: expire_after,
        KEY_FORCE_UPDATE: str(force_update),
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: {
            KEY_IDENTIFIERS: [mac],
            KEY_NAME: device_name,
            KEY_MODEL: model,
            KEY_SW_VERSION: fw_ver,
            KEY_MANUFACTURER: ATTR_MANUFACTURER,
        },
        "~": default_topic,
    }
    if not battery_powered:
        payload[KEY_AVAILABILITY_TOPIC] = availability_topic
        payload[KEY_PAYLOAD_AVAILABLE] = VALUE_TRUE
        payload[KEY_PAYLOAD_NOT_AVAILABLE] = VALUE_FALSE
    if no_battery_sensor and sensors[sensor_id] == ATTR_BATTERY:
        payload = ""
    if id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# external sensors
for sensor_id in range(0, ext_sensors):
    device_name = f"{model} {id.split('-')[-1]}"
    unique_id = f"{id}-ext-{sensor_id}"
    ext_sensor_type = data.get(unique_id, data.get(unique_id.lower()))
    if ext_sensor_type:
        config_topic = f"{disc_prefix}/sensor/{id}-ext-{sensor_id}/config"
        default_topic = f"shellies/{id}/"
        availability_topic = "~online"
        sensor_name = (
            f"{device_name} External {sensor_id} {ext_sensor_type.capitalize()}"
        )
        state_topic = f"~ext_{ext_sensor_type}/{sensor_id}"
        if ext_sensor_type == ATTR_TEMPERATURE:
            payload = (
                '{"name":"' + sensor_name + '",'
                '"stat_t":"' + state_topic + '",'
                '"unit_of_meas":"' + UNIT_CELSIUS + '",'
                '"dev_cla":"' + ATTR_TEMPERATURE + '",'
                '"val_tpl":"' + TPL_TEMPERATURE_EXT + '",'
                '"frc_upd":"' + str(force_update) + '",'
                '"avty_t":"' + availability_topic + '",'
                '"pl_avail":"true",'
                '"pl_not_avail":"false",'
                '"uniq_id":"' + unique_id + '",'
                '"qos":"' + str(qos) + '",'
                '"dev": {"ids": ["' + mac + '"],'
                '"name":"' + device_name + '",'
                '"mdl":"' + model + '",'
                '"sw":"' + fw_ver + '",'
                '"mf":"' + ATTR_MANUFACTURER + '"},'
                '"~":"' + default_topic + '"}'
            )
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, payload, retain, qos)

# binary sensors
for bin_sensor_id in range(0, len(bin_sensors)):
    device_name = f"{model} {id.split('-')[-1]}"
    unique_id = f"{id}-{bin_sensors[bin_sensor_id].replace('/', '-')}"
    config_topic = f"{disc_prefix}/binary_sensor/{id}-{bin_sensors[bin_sensor_id].replace('/', '-')}/config"
    default_topic = f"shellies/{id}/"
    availability_topic = "~online"
    sensor_name = (
        f"{device_name} {bin_sensors[bin_sensor_id].replace('/', ' ').capitalize()}"
    )
    if relays > 0 or white_lights > 0:
        state_topic = f"~{bin_sensors[bin_sensor_id]}"
    elif bin_sensors[bin_sensor_id] == ATTR_OPENING:
        state_topic = "~sensor/state"
    else:
        state_topic = f"~sensor/{bin_sensors[bin_sensor_id]}"
    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: state_topic,
        KEY_PAYLOAD_ON: bin_sensors_pl[bin_sensor_id][VALUE_ON],
        KEY_PAYLOAD_OFF: bin_sensors_pl[bin_sensor_id][VALUE_OFF],
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: {
            KEY_IDENTIFIERS: [mac],
            KEY_NAME: device_name,
            KEY_MODEL: model,
            KEY_SW_VERSION: fw_ver,
            KEY_MANUFACTURER: ATTR_MANUFACTURER,
        },
        "~": default_topic,
    }
    if battery_powered:
        payload[KEY_EXPIRE_AFTER] = expire_after
    else:
        payload[KEY_AVAILABILITY_TOPIC] = availability_topic
        payload[KEY_PAYLOAD_AVAILABLE] = VALUE_TRUE
        payload[KEY_PAYLOAD_NOT_AVAILABLE] = VALUE_FALSE
    if bin_sensors_classes[bin_sensor_id]:
        payload[KEY_DEVICE_CLASS] = bin_sensors_classes[bin_sensor_id]
    if bin_sensors[bin_sensor_id] in [ATTR_LONGPUSH_0, ATTR_LONGPUSH_1]:
        payload[KEY_OFF_DELAY] = off_delay
    if id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# color lights
for light_id in range(0, rgbw_lights):
    device_name = f"{model} {id.split('-')[-1]}"
    light_name = f"{device_name} Light {light_id}"
    default_topic = f"shellies/{id}/"
    state_topic = f"~color/{light_id}/status"
    command_topic = f"~color/{light_id}/set"
    availability_topic = "~online"
    unique_id = f"{id}-light-{light_id}"
    config_topic = f"{disc_prefix}/light/{id}-{light_id}/config"
    config_light = data.get(id, data.get(id.lower(), ATTR_RGBW))
    if config_light == ATTR_RGBW and model == ATTR_MODEL_SHELLYRGBW2:
        payload = (
            '{"schema":"template",'
            '"name":"' + light_name + '",'
            '"cmd_t":"' + command_topic + '",'
            '"stat_t":"' + state_topic + '",'
            '"avty_t":"' + availability_topic + '",'
            '"pl_avail":"true",'
            '"pl_not_avail":"false",'
            '"fx_list":["Off", "Meteor Shower", "Gradual Change", "Flash"],'
            '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"gain\\":{{brightness|float|multiply(0.3922)|round}}{% endif %}{% if red is defined and green is defined and blue is defined %},\\"red\\":{{red}},\\"green\\":{{green}},\\"blue\\":{{blue}}{% endif %}{% if white_value is defined %},\\"white\\":{{white_value}}{% endif %}{% if effect is defined %}{% if effect == \\"Meteor Shower\\" %}\\"effect\\":1{% elif effect == \\"Gradual Change\\" %}\\"effect\\":2{% elif effect == \\"Flash\\" %}\\"effect\\":3{% else %}\\"effect\\":0{% endif %}{% else %}\\"effect\\":0{% endif %}}",'
            '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
            '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
            '"bri_tpl":"{{value_json.gain|float|multiply(2.55)|round}}",'
            '"r_tpl":"{{value_json.red}}",'
            '"g_tpl":"{{value_json.green}}",'
            '"b_tpl":"{{value_json.blue}}",'
            '"whit_val_tpl":"{{value_json.white}}",'
            '"fx_tpl":"{% if value_json.effect == 1 %}Meteor Shower{% elif value_json.effect == 2 %}Gradual Change{% elif value_json.effect == 3 %}Flash{% else %}Off{% endif %}",'
            '"uniq_id":"' + unique_id + '",'
            '"qos":"' + str(qos) + '",'
            '"dev": {"ids": ["' + mac + '"],'
            '"name":"' + device_name + '",'
            '"mdl":"' + model + '",'
            '"sw":"' + fw_ver + '",'
            '"mf":"' + ATTR_MANUFACTURER + '"},'
            '"~":"' + default_topic + '"}'
        )
    elif config_light == ATTR_RGBW and model == ATTR_MODEL_SHELLYBULB:
        payload = (
            '{"schema":"template",'
            '"name":"' + light_name + '",'
            '"cmd_t":"' + command_topic + '",'
            '"stat_t":"' + state_topic + '",'
            '"avty_t":"' + availability_topic + '",'
            '"pl_avail":"true",'
            '"pl_not_avail":"false",'
            '"fx_list":["Off", "Meteor Shower", "Gradual Change", "Breath", "Flash", "On/Off Gradual", "Red/Green Change"],'
            '"cmd_on_tpl":"{\\"turn\\":\\"on\\",\\"mode\\":\\"color\\",{% if red is defined and green is defined and blue is defined %}\\"red\\":{{red}},\\"green\\":{{green}},\\"blue\\":{{blue}},{% endif %}{% if white_value is defined %}\\"white\\":{{white_value}},{% endif %}{% if brightness is defined %}\\"gain\\":{{brightness|float|multiply(0.3922)|round}},{% endif %}{% if effect is defined %}{% if effect == \\"Meteor Shower\\" %}\\"effect\\":1{% elif effect == \\"Gradual Change\\" %}\\"effect\\":2{% elif effect == \\"Breath\\" %}\\"effect\\":3{% elif effect == \\"Flash\\" %}\\"effect\\":4{% elif effect == \\"On/Off Gradual\\" %}\\"effect\\":5{% elif effect == \\"Red/Green Change\\" %}\\"effect\\":6{% else %}\\"effect\\":0{% endif %}{% else %}\\"effect\\":0{% endif %}}",'
            '"cmd_off_tpl":"{\\"turn\\":\\"off\\",\\"mode\\":\\"color\\",\\"effect\\": 0}",'
            '"stat_tpl":"{% if value_json.ison == true and value_json.mode == \\"color\\" %}on{% else %}off{% endif %}",'
            '"bri_tpl":"{{value_json.gain|float|multiply(2.55)|round}}",'
            '"r_tpl":"{{value_json.red}}",'
            '"g_tpl":"{{value_json.green}}",'
            '"b_tpl":"{{value_json.blue}}",'
            '"whit_val_tpl":"{{value_json.white}}",'
            '"fx_tpl":"{% if value_json.effect == 1 %}Meteor Shower{% elif value_json.effect == 2 %}Gradual Change{% elif value_json.effect == 3 %}Breath{% elif value_json.effect == 4 %}Flash{% elif value_json.effect == 5 %}On/Off Gradual{% elif value_json.effect == 6 %}Red/Green Change{% else %}Off{% endif %}",'
            '"uniq_id":"' + unique_id + '",'
            '"qos":"' + str(qos) + '",'
            '"dev": {"ids": ["' + mac + '"],'
            '"name":"' + device_name + '",'
            '"mdl":"' + model + '",'
            '"sw":"' + fw_ver + '",'
            '"mf":"' + ATTR_MANUFACTURER + '"},'
            '"~":"' + default_topic + '"}'
        )
    else:
        payload = ""
    if id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, payload, retain, qos)

    # color light's binary sensors
    for bin_sensor_id in range(0, len(lights_bin_sensors)):

        # fix for RGBW2 input binary sensor issue
        if lights_bin_sensors[bin_sensor_id] == ATTR_INPUT and light_id == 0:
            unique_id = f"{id}-{lights_bin_sensors[bin_sensor_id]}-{light_id}"
            config_topic = f"{disc_prefix}/binary_sensor/{id}-{lights_bin_sensors[bin_sensor_id]}-{light_id}/config"
            state_topic = f"~{lights_bin_sensors[bin_sensor_id]}/{light_id}"
            sensor_name = f"{device_name} {lights_bin_sensors[bin_sensor_id].capitalize()} {light_id}"
            payload = ""
            service_data = {
                KEY_TOPIC: config_topic,
                KEY_PAYLOAD: str(payload).replace("'", '"'),
                KEY_RETAIN: retain,
                KEY_QOS: qos,
            }
            logger.debug("Send to MQTT broker: %s %s", config_topic, payload)
            hass.services.call("mqtt", "publish", service_data, False)
        # end of fix

        sensor_name = (
            f"{device_name} {lights_bin_sensors[bin_sensor_id].capitalize()} {light_id}"
        )
        config_topic = f"{disc_prefix}/binary_sensor/{id}-color-{lights_bin_sensors[bin_sensor_id]}-{light_id}/config"
        unique_id = f"{id}-color-{lights_bin_sensors[bin_sensor_id]}-{light_id}"
        if lights_bin_sensors[bin_sensor_id] == ATTR_INPUT:
            state_topic = f"~{lights_bin_sensors[bin_sensor_id]}/{light_id}"
        else:
            state_topic = f"~color/{light_id}/status"
        if config_light == ATTR_RGBW:
            payload = {
                KEY_NAME: sensor_name,
                KEY_STATE_TOPIC: state_topic,
                KEY_AVAILABILITY_TOPIC: availability_topic,
                KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                KEY_UNIQUE_ID: unique_id,
                KEY_QOS: qos,
                KEY_DEVICE: {
                    KEY_IDENTIFIERS: [mac],
                    KEY_NAME: device_name,
                    KEY_MODEL: model,
                    KEY_SW_VERSION: fw_ver,
                    KEY_MANUFACTURER: ATTR_MANUFACTURER,
                },
                "~": default_topic,
            }
            if lights_bin_sensors_classes[bin_sensor_id]:
                payload[KEY_DEVICE_CLASS] = lights_bin_sensors_classes[bin_sensor_id]
            if lights_bin_sensors_tpls[bin_sensor_id]:
                payload[KEY_VALUE_TEMPLATE] = lights_bin_sensors_tpls[bin_sensor_id]
            else:
                payload[KEY_PAYLOAD_ON] = lights_bin_sensors_pl[bin_sensor_id][VALUE_ON]
                payload[KEY_PAYLOAD_OFF] = lights_bin_sensors_pl[bin_sensor_id][VALUE_OFF]
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # color light's sensors
    for sensor_id in range(0, len(lights_sensors)):
        unique_id = f"{id}-color-{lights_sensors[sensor_id]}-{light_id}"
        config_topic = f"{disc_prefix}/sensor/{id}-color-{lights_sensors[sensor_id]}-{light_id}/config"
        sensor_name = (
            f"{device_name} {lights_sensors[sensor_id].capitalize()} {light_id}"
        )
        state_topic = f"~color/{light_id}/status"
        if config_light == ATTR_RGBW:
            payload = {
                KEY_NAME: sensor_name,
                KEY_STATE_TOPIC: state_topic,
                KEY_UNIT: lights_sensors_units[sensor_id],
                KEY_VALUE_TEMPLATE: lights_sensors_tpls[sensor_id],
                KEY_DEVICE_CLASS: lights_sensors_classes[sensor_id],
                KEY_AVAILABILITY_TOPIC: availability_topic,
                KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                KEY_FORCE_UPDATE: str(force_update),
                KEY_UNIQUE_ID: unique_id,
                KEY_QOS: qos,
                KEY_DEVICE: {
                    KEY_IDENTIFIERS: [mac],
                    KEY_NAME: device_name,
                    KEY_MODEL: model,
                    KEY_SW_VERSION: fw_ver,
                    KEY_MANUFACTURER: ATTR_MANUFACTURER,
                },
                "~": default_topic,
            }
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# white lights
for light_id in range(0, white_lights):
    device_name = f"{model} {id.split('-')[-1]}"
    light_name = f"{device_name} Light {light_id}"
    default_topic = f"shellies/{id}/"
    if model == ATTR_MODEL_SHELLYDIMMER or model == ATTR_MODEL_SHELLYDUO:
        state_topic = f"~light/{light_id}/status"
        command_topic = f"~light/{light_id}/set"
        unique_id = f"{id}-light-{light_id}"
        config_topic = f"{disc_prefix}/light/{id}-{light_id}/config"
    else:
        state_topic = f"~white/{light_id}/status"
        command_topic = f"~white/{light_id}/set"
        unique_id = f"{id}-light-white-{light_id}"
        config_topic = f"{disc_prefix}/light/{id}-white-{light_id}/config"
    availability_topic = "~online"
    config_light = data.get(id, data.get(id.lower(), ATTR_RGBW))
    if config_light == ATTR_WHITE and model == ATTR_MODEL_SHELLYRGBW2:
        payload = (
            '{"schema":"template",'
            '"name":"' + light_name + '",'
            '"cmd_t":"' + command_topic + '",'
            '"stat_t":"' + state_topic + '",'
            '"avty_t":"' + availability_topic + '",'
            '"pl_avail":"true",'
            '"pl_not_avail":"false",'
            '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"brightness\\":{{brightness|float|multiply(0.3922)|round}}{% endif %}{% if white_value is defined %},\\"white\\":{{white_value}}{% endif %}{% if effect is defined %},\\"effect\\":{{effect}}{% endif %}}",'
            '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
            '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
            '"bri_tpl":"{{value_json.brightness|float|multiply(2.55)|round}}",'
            '"uniq_id":"' + unique_id + '",'
            '"qos":"' + str(qos) + '",'
            '"dev": {"ids": ["' + mac + '"],'
            '"name":"' + device_name + '",'
            '"mdl":"' + model + '",'
            '"sw":"' + fw_ver + '",'
            '"mf":"' + ATTR_MANUFACTURER + '"},'
            '"~":"' + default_topic + '"}'
        )
    elif model == ATTR_MODEL_SHELLYDIMMER:
        payload = (
            '{"schema":"template",'
            '"name":"' + light_name + '",'
            '"cmd_t":"' + command_topic + '",'
            '"stat_t":"' + state_topic + '",'
            '"avty_t":"' + availability_topic + '",'
            '"pl_avail":"true",'
            '"pl_not_avail":"false",'
            '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"brightness\\":{{brightness|float|multiply(0.3922)|round}}{% endif %}}",'
            '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
            '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
            '"bri_tpl":"{{value_json.brightness|float|multiply(2.55)|round}}",'
            '"uniq_id":"' + unique_id + '",'
            '"qos":"' + str(qos) + '",'
            '"dev": {"ids": ["' + mac + '"],'
            '"name":"' + device_name + '",'
            '"mdl":"' + model + '",'
            '"sw":"' + fw_ver + '",'
            '"mf":"' + ATTR_MANUFACTURER + '"},'
            '"~":"' + default_topic + '"}'
        )
    elif model == ATTR_MODEL_SHELLYDUO:
        payload = (
            '{"schema":"template",'
            '"name":"' + light_name + '",'
            '"cmd_t":"' + command_topic + '",'
            '"stat_t":"' + state_topic + '",'
            '"avty_t":"' + availability_topic + '",'
            '"pl_avail":"true",'
            '"pl_not_avail":"false",'
            '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"brightness\\":{{brightness|float|multiply(0.3922)|round}}{% endif %}{% if color_temp is defined %},\\"temp\\":{{[([((1000000/(color_temp|int))|round(0,\\"floor\\")),6500]|min),2700]|max}}{% endif %}}",'
            '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
            '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
            '"bri_tpl":"{{value_json.brightness|float|multiply(2.55)|round}}",'
            '"clr_temp_tpl":"{{((1000000/(value_json.temp|int))|round(0,\\"floor\\"))}}",'
            '"uniq_id":"' + unique_id + '",'
            '"qos":"' + str(qos) + '",'
            '"dev": {"ids": ["' + mac + '"],'
            '"name":"' + device_name + '",'
            '"mdl":"' + model + '",'
            '"sw":"' + fw_ver + '",'
            '"mf":"' + ATTR_MANUFACTURER + '"},'
            '"~":"' + default_topic + '"}'
        )
    else:
        payload = ""
    if id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, payload, retain, qos)

    # white light's binary sensors
    for bin_sensor_id in range(0, len(lights_bin_sensors)):

        # fix for RGBW2 input binary sensor issue
        if lights_bin_sensors[bin_sensor_id] == ATTR_INPUT and light_id == 0:
            unique_id = f"{id}-{lights_bin_sensors[bin_sensor_id]}-{light_id}"
            config_topic = f"{disc_prefix}/binary_sensor/{id}-{lights_bin_sensors[bin_sensor_id]}-{light_id}/config"
            state_topic = f"~{lights_bin_sensors[bin_sensor_id]}/{light_id}"
            sensor_name = f"{device_name} {lights_bin_sensors[bin_sensor_id].capitalize()} {light_id}"
            payload = ""
            service_data = {
                KEY_TOPIC: config_topic,
                KEY_PAYLOAD: str(payload).replace("'", '"'),
                KEY_RETAIN: retain,
                KEY_QOS: qos,
            }
            logger.debug("Send to MQTT broker: %s %s", config_topic, payload)
            hass.services.call("mqtt", "publish", service_data, False)
        # end of fix

        if (
            lights_bin_sensors[bin_sensor_id] == ATTR_INPUT and light_id == 0
        ) or lights_bin_sensors[bin_sensor_id] != ATTR_INPUT:
            unique_id = f"{id}-white-{lights_bin_sensors[bin_sensor_id]}-{light_id}"
            config_topic = f"{disc_prefix}/binary_sensor/{id}-white-{lights_bin_sensors[bin_sensor_id]}-{light_id}/config"
            if lights_bin_sensors[bin_sensor_id] == ATTR_INPUT:
                state_topic = f"~{lights_bin_sensors[bin_sensor_id]}/{light_id}"
            else:
                state_topic = f"~white/{light_id}/status"
            sensor_name = f"{device_name} {lights_bin_sensors[bin_sensor_id].capitalize()} {light_id}"

            if config_light != ATTR_RGBW:
                payload = {
                    KEY_NAME: sensor_name,
                    KEY_STATE_TOPIC: state_topic,
                    KEY_AVAILABILITY_TOPIC: availability_topic,
                    KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                    KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                    KEY_UNIQUE_ID: unique_id,
                    KEY_QOS: qos,
                    KEY_DEVICE: {
                        KEY_IDENTIFIERS: [mac],
                        KEY_NAME: device_name,
                        KEY_MODEL: model,
                        KEY_SW_VERSION: fw_ver,
                        KEY_MANUFACTURER: ATTR_MANUFACTURER,
                    },
                    "~": default_topic,
                }
                if lights_bin_sensors_classes[bin_sensor_id]:
                    payload[KEY_DEVICE_CLASS] = lights_bin_sensors_classes[
                        bin_sensor_id
                    ]
                if lights_bin_sensors_tpls[bin_sensor_id]:
                    payload[KEY_VALUE_TEMPLATE] = lights_bin_sensors_tpls[bin_sensor_id]
                else:
                    payload[KEY_PAYLOAD_ON] = lights_bin_sensors_pl[bin_sensor_id][VALUE_ON]
                    payload[KEY_PAYLOAD_OFF] = lights_bin_sensors_pl[bin_sensor_id][VALUE_OFF]

            else:
                payload = ""
            if id.lower() in ignored:
                payload = ""
            mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # white light's sensors
    for sensor_id in range(0, len(lights_sensors)):
        unique_id = f"{id}-white-{lights_sensors[sensor_id]}-{light_id}"
        config_topic = f"{disc_prefix}/sensor/{id}-white-{lights_sensors[sensor_id]}-{light_id}/config"
        sensor_name = (
            f"{device_name} {lights_sensors[sensor_id].capitalize()} {light_id}"
        )
        if model == ATTR_MODEL_SHELLYDIMMER or model == ATTR_MODEL_SHELLYDUO:
            state_topic = f"~light/{light_id}/{lights_sensors[sensor_id]}"
        else:
            state_topic = f"~white/{light_id}/status"
        if (
            config_light != ATTR_RGBW
            or model == ATTR_MODEL_SHELLYDIMMER
            or model == ATTR_MODEL_SHELLYDUO
        ):
            payload = {
                KEY_NAME: sensor_name,
                KEY_STATE_TOPIC: state_topic,
                KEY_UNIT: lights_sensors_units[sensor_id],
                KEY_VALUE_TEMPLATE: lights_sensors_tpls[sensor_id],
                KEY_DEVICE_CLASS: lights_sensors_classes[sensor_id],
                KEY_AVAILABILITY_TOPIC: availability_topic,
                KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
                KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
                KEY_FORCE_UPDATE: str(force_update),
                KEY_UNIQUE_ID: unique_id,
                KEY_QOS: qos,
                KEY_DEVICE: {
                    KEY_IDENTIFIERS: [mac],
                    KEY_NAME: device_name,
                    KEY_MODEL: model,
                    KEY_SW_VERSION: fw_ver,
                    KEY_MANUFACTURER: ATTR_MANUFACTURER,
                },
                "~": default_topic,
            }
        else:
            payload = ""
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# meters
for meter_id in range(0, meters):
    device_name = f"{model} {id.split('-')[-1]}"
    default_topic = f"shellies/{id}/"
    availability_topic = "~online"
    for sensor_id in range(0, len(meters_sensors)):
        unique_id = f"{id}-emeter-{meters_sensors[sensor_id]}-{meter_id}"
        config_topic = f"{disc_prefix}/sensor/{id}-emeter-{meters_sensors[sensor_id]}-{meter_id}/config"
        sensor_name = (
            f"{device_name} Meter {meters_sensors[sensor_id].capitalize()} {meter_id}"
        )
        state_topic = f"~emeter/{meter_id}/{meters_sensors[sensor_id]}"
        payload = {
            KEY_NAME: sensor_name,
            KEY_STATE_TOPIC: state_topic,
            KEY_UNIT: meters_sensors_units[sensor_id],
            KEY_VALUE_TEMPLATE: meters_sensors_tpls[sensor_id],
            KEY_AVAILABILITY_TOPIC: availability_topic,
            KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
            KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
            KEY_FORCE_UPDATE: str(force_update),
            KEY_UNIQUE_ID: unique_id,
            KEY_QOS: qos,
            KEY_DEVICE: {
                KEY_IDENTIFIERS: [mac],
                KEY_NAME: device_name,
                KEY_MODEL: model,
                KEY_SW_VERSION: fw_ver,
                KEY_MANUFACTURER: ATTR_MANUFACTURER,
            },
            "~": default_topic,
        }
        if meters_sensors_classes[sensor_id]:
            payload[KEY_DEVICE_CLASS] = meters_sensors_classes[sensor_id]
        if id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)
