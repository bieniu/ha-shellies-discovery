"""
This script adds MQTT discovery support for Shellies devices.
"""
ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_POWER_AC = "ac"
ATTR_RELAY = "relay"
ATTR_ROLLER = "roller"
ATTR_SHELLY = "Shelly"
ATTR_TEMPLATE = "template"

COMP_FAN = "fan"
COMP_LIGHT = "light"
COMP_SWITCH = "switch"

CONF_DEVELOP = "develop"
CONF_DISCOVERY_PREFIX = "discovery_prefix"
CONF_FORCE_UPDATE_SENSORS = "force_update_sensors"
CONF_FRIENDLY_NAME = "friendly_name"
CONF_FW_VER = "fw_ver"
CONF_ID = "id"
CONF_IGNORED_DEVICES = "ignored_devices"
CONF_MAC = "mac"
CONF_MODE = "mode"
CONF_POWERED = "powered"
CONF_PUSH_OFF_DELAY = "push_off_delay"
CONF_QOS = "qos"

DEFAULT_DISC_PREFIX = "homeassistant"

DEVICE_CLASS_AWNING = "awning"
DEVICE_CLASS_BATTERY = "battery"
DEVICE_CLASS_BATTERY_CHARGING = "battery_charging"
DEVICE_CLASS_BLIND = "blind"
DEVICE_CLASS_COLD = "cold"
DEVICE_CLASS_CONNECTIVITY = "connectivity"
DEVICE_CLASS_CURRENT = "current"  # Home Assistant 0.115
DEVICE_CLASS_CURTAIN = "curtain"
DEVICE_CLASS_DAMPER = "damper"
DEVICE_CLASS_DOOR = "door"
DEVICE_CLASS_ENERGY = "energy"  # Home Assistant 0.115
DEVICE_CLASS_GARAGE = "garage"
DEVICE_CLASS_GARAGE_DOOR = "garage_door"
DEVICE_CLASS_GAS = "gas"
DEVICE_CLASS_GATE = "gate"
DEVICE_CLASS_HEAT = "heat"
DEVICE_CLASS_HUMIDITY = "humidity"
DEVICE_CLASS_ILLUMINANCE = "illuminance"
DEVICE_CLASS_LIGHT = "light"
DEVICE_CLASS_LOCK = "lock"
DEVICE_CLASS_MOISTURE = "moisture"
DEVICE_CLASS_MOTION = "motion"
DEVICE_CLASS_MOVING = "moving"
DEVICE_CLASS_OCCUPANCY = "occupancy"
DEVICE_CLASS_OPENING = "opening"
DEVICE_CLASS_PLUG = "plug"
DEVICE_CLASS_POWER = "power"
DEVICE_CLASS_POWER_FACTOR = "power_factor"  # Home Assistant 0.115
DEVICE_CLASS_PRESENCE = "presence"
DEVICE_CLASS_PRESSURE = "pressure"
DEVICE_CLASS_PROBLEM = "problem"
DEVICE_CLASS_SAFETY = "safety"
DEVICE_CLASS_SHADE = "shade"
DEVICE_CLASS_SHUTTER = "shutter"
DEVICE_CLASS_SIGNAL_STRENGTH = "signal_strength"
DEVICE_CLASS_SMOKE = "smoke"
DEVICE_CLASS_SOUND = "sound"
DEVICE_CLASS_TEMPERATURE = "temperature"
DEVICE_CLASS_VIBRATION = "vibration"
DEVICE_CLASS_VOLTAGE = "voltage"  # Home Assistant 0.115
DEVICE_CLASS_WINDOW = "window"

EXPIRE_AFTER_FOR_BATTERY_POWERED = 43200
EXPIRE_AFTER_FOR_AC_POWERED = 7200

KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_BLUE_TEMPLATE = "b_tpl"
KEY_BRIGHTNESS_TEMPLATE = "bri_tpl"
KEY_COLOR_TEMP_TEMPLATE = "clr_temp_tpl"
KEY_COMMAND_OFF_TEMPLATE = "cmd_off_tpl"
KEY_COMMAND_ON_TEMPLATE = "cmd_on_tpl"
KEY_COMMAND_TOPIC = "cmd_t"
KEY_DEVICE = "dev"
KEY_DEVICE_CLASS = "dev_cla"
KEY_EFFECT_LIST = "fx_list"
KEY_EFFECT_TEMPLATE = "fx_tpl"
KEY_EXPIRE_AFTER = "exp_aft"
KEY_FORCE_UPDATE = "frc_upd"
KEY_GREEN_TEMPLATE = "g_tpl"
KEY_ICON = "icon"
KEY_IDENTIFIERS = "ids"
KEY_JSON_ATTRIBUTES_TEMPLATE = "json_attr_tpl"
KEY_JSON_ATTRIBUTE_TOPIC = "json_attr_t"
KEY_MANUFACTURER = "mf"
KEY_MAX_MIREDS = "max_mireds"
KEY_MIN_MIREDS = "min_mireds"
KEY_MODEL = "mdl"
KEY_NAME = "name"
KEY_OFF_DELAY = "off_dly"
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
KEY_RED_TEMPLATE = "r_tpl"
KEY_RETAIN = "retain"
KEY_SCHEMA = "schema"
KEY_SET_POSITION_TOPIC = "set_pos_t"
KEY_STATE_TEMPLATE = "stat_tpl"
KEY_STATE_TOPIC = "stat_t"
KEY_SW_VERSION = "sw"
KEY_TOPIC = "topic"
KEY_UNIQUE_ID = "uniq_id"
KEY_UNIT = "unit_of_meas"
KEY_VALUE_TEMPLATE = "val_tpl"
KEY_WHITE_VALUE_TEMPLATE = "whit_val_tpl"

LIGHT_RGBW = "rgbw"
LIGHT_WHITE = "white"

MIN_FIRMWARE_VERSION = "1.8.0"

MODEL_SHELLY1 = "Shelly 1"
MODEL_SHELLY1PM = "Shelly 1PM"
MODEL_SHELLY2 = "Shelly 2"
MODEL_SHELLY25 = "Shelly 2.5"
MODEL_SHELLY3EM = "Shelly 3EM"
MODEL_SHELLY4PRO = "Shelly 4Pro"
MODEL_SHELLYAIR = "Shelly Air"
MODEL_SHELLYBULB = "Shelly Bulb"
MODEL_SHELLYBUTTON1 = "Shelly Button1"
MODEL_SHELLYDIMMER = "Shelly Dimmer"
MODEL_SHELLYDIMMER2 = "Shelly Dimmer 2"
MODEL_SHELLYDUO = "Shelly DUO"
MODEL_SHELLYDW = "Shelly Door/Window"
MODEL_SHELLYDW2 = "Shelly Door/Window 2"
MODEL_SHELLYEM = "Shelly EM"
MODEL_SHELLYFLOOD = "Shelly Flood"
MODEL_SHELLYGAS = "Shelly Gas"
MODEL_SHELLYHT = "Shelly H&T"
MODEL_SHELLYI3 = "Shelly i3"
MODEL_SHELLYPLUG = "Shelly Plug"
MODEL_SHELLYPLUG_S = "Shelly Plug S"
MODEL_SHELLYRGBW2 = "Shelly RGBW2"
MODEL_SHELLYSENSE = "Shelly Sense"
MODEL_SHELLYSMOKE = "Shelly Smoke"
MODEL_SHELLYVINTAGE = "Shelly Vintage"

OFF_DELAY = 2

SENSOR_BATTERY = "battery"
SENSOR_CHARGER = "charger"
SENSOR_CONCENTRATION = "concentration"
SENSOR_CURRENT = "current"
SENSOR_DOUBLE_SHORTPUSH = "double shortpush"
SENSOR_DOUBLE_SHORTPUSH_0 = "double shortpush 0"
SENSOR_DOUBLE_SHORTPUSH_1 = "double shortpush 1"
SENSOR_DOUBLE_SHORTPUSH_2 = "double shortpush 2"
SENSOR_ENERGY = "energy"
SENSOR_EXT_HUMIDITY = "ext_humidity"
SENSOR_EXT_TEMPERATURE = "ext_temperature"
SENSOR_FIRMWARE_UPDATE = "firmware update"
SENSOR_FLOOD = "flood"
SENSOR_GAS = "gas"
SENSOR_HUMIDITY = "humidity"
SENSOR_ILLUMINATION = "illumination"
SENSOR_INPUT = "input"
SENSOR_INPUT_0 = "input 0"
SENSOR_INPUT_1 = "input 1"
SENSOR_INPUT_2 = "input 2"
SENSOR_LOADERROR = "loaderror"
SENSOR_LONGPUSH = "longpush"
SENSOR_LONGPUSH_0 = "longpush 0"
SENSOR_LONGPUSH_1 = "longpush 1"
SENSOR_LONGPUSH_2 = "longpush 2"
SENSOR_LONGPUSH_SHORTPUSH_0 = "longpush shortpush 0"
SENSOR_LONGPUSH_SHORTPUSH_1 = "longpush shortpush 1"
SENSOR_LONGPUSH_SHORTPUSH_2 = "longpush shortpush 2"
SENSOR_LUX = "lux"
SENSOR_MOTION = "motion"
SENSOR_OPENING = "opening"
SENSOR_OPERATION = "operation"
SENSOR_OVERLOAD = "overload"
SENSOR_OVERPOWER = "overpower"
SENSOR_OVERTEMPERATURE = "overtemperature"
SENSOR_POWER = "power"
SENSOR_POWER_FACTOR = "pf"
SENSOR_REACTIVE_POWER = "reactive_power"
SENSOR_RETURNED_ENERGY = "returned_energy"
SENSOR_RSSI = "rssi"
SENSOR_SELF_TEST = "self_test"
SENSOR_SHORTPUSH = "shortpush"
SENSOR_SHORTPUSH_0 = "shortpush/0"
SENSOR_SHORTPUSH_1 = "shortpush/1"
SENSOR_SHORTPUSH_2 = "shortpush/2"
SENSOR_SHORTPUSH_LONGPUSH_0 = "shortpush longpush 0"
SENSOR_SHORTPUSH_LONGPUSH_1 = "shortpush longpush 1"
SENSOR_SHORTPUSH_LONGPUSH_2 = "shortpush longpush 2"
SENSOR_SMOKE = "smoke"
SENSOR_SSID = "ssid"
SENSOR_TEMPERATURE = "temperature"
SENSOR_TILT = "tilt"
SENSOR_TOTAL = "total"
SENSOR_TOTALWORKTIME = "totalworktime"
SENSOR_TOTAL_RETURNED = "total_returned"
SENSOR_TRIPLE_SHORTPUSH = "triple shortpush"
SENSOR_TRIPLE_SHORTPUSH_0 = "triple shortpush 0"
SENSOR_TRIPLE_SHORTPUSH_1 = "triple shortpush 1"
SENSOR_TRIPLE_SHORTPUSH_2 = "triple shortpush 2"
SENSOR_VIBRATION = "vibration"
SENSOR_VOLTAGE = "voltage"

TOPIC_ANNOUNCE = "announce"
TOPIC_COLOR_0_STATUS = "color/0/status"
TOPIC_INFO = "info"
TOPIC_INPUT_0 = "input/0"
TOPIC_INPUT_1 = "input/1"
TOPIC_INPUT_2 = "input/2"
TOPIC_INPUT_EVENT_0 = "input_event/0"
TOPIC_INPUT_EVENT_1 = "input_event/1"
TOPIC_INPUT_EVENT_2 = "input_event/2"
TOPIC_LONGPUSH = "longpush"
TOPIC_LONGPUSH_0 = "longpush/0"
TOPIC_LONGPUSH_1 = "longpush/1"
TOPIC_LONGPUSH_2 = "longpush/2"
TOPIC_RELAY = "relay"

TPL_BATTERY = "{{value|float|round}}"
TPL_CURRENT = "{{value|float|round(2)}}"
TPL_DOUBLE_SHORTPUSH = "{% if value_json.event == ^SS^ %}ON{% else %}OFF{% endif %}"
TPL_ENERGY_WH = "{{(value|float/1000)|round(2)}}"
TPL_ENERGY_WMIN = "{{(value|float/60/1000)|round(2)}}"
TPL_HUMIDITY = "{{value|float|round(1)}}"
TPL_ILLUMINATION_TO_JSON = "{{{^illumination^:value}|tojson}}"
TPL_LONGPUSH = "{% if value_json.event == ^L^ %}ON{% else %}OFF{% endif %}"
TPL_LONGPUSH_SHORTPUSH = "{% if value_json.event == ^LS^ %}ON{% else %}OFF{% endif %}"
TPL_LUX = "{{value|float|round}}"
TPL_NEW_FIRMWARE_FROM_ANNOUNCE = (
    "{% if value_json.new_fw == true %}ON{% else %}OFF{% endif %}"
)
TPL_NEW_FIRMWARE_FROM_INFO = (
    "{% if value_json[^update^].has_update == true %}ON{% else %}OFF{% endif %}"
)
TPL_OVERPOWER = "{% if value_json.overpower == true %}ON{% else %}OFF{% endif %}"
TPL_OVERPOWER_RELAY = "{% if value == ^overpower^ %}ON{% else %}OFF{% endif %}"
TPL_POWER = "{{value|float|round(1)}}"
TPL_POWER_FACTOR = "{{value|float*100|round}}"
TPL_RSSI = "{{value_json[^wifi_sta^].rssi}}"
TPL_SHORTPUSH = "{% if value_json.event == ^S^ %}ON{% else %}OFF{% endif %}"
TPL_SHORTPUSH_LONGPUSH = "{% if value_json.event == ^SL^ %}ON{% else %}OFF{% endif %}"
TPL_SSID = "{{value_json[^wifi_sta^].ssid}}"
TPL_TEMPERATURE = "{{value|float|round(1)}}"
TPL_TILT = "{{value|float}}"
TPL_TRIPLE_SHORTPUSH = "{% if value_json.event == ^SSS^ %}ON{% else %}OFF{% endif %}"
TPL_VOLTAGE = "{{value|float|round(1)}}"

UNIT_AMPERE = "A"
UNIT_CELSIUS = "°C"
UNIT_DB = "dB"
UNIT_DEGREE = "°"
UNIT_KWH = "kWh"
UNIT_LUX = "lx"
UNIT_PERCENT = "%"
UNIT_PPM = "ppm"
UNIT_SECOND = "s"
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

PL_0_1 = {VALUE_ON: "0", VALUE_OFF: "1"}
PL_1_0 = {VALUE_ON: "1", VALUE_OFF: "0"}
PL_OPEN_CLOSE = {VALUE_ON: VALUE_OPEN, VALUE_OFF: VALUE_CLOSE}
PL_TRUE_FALSE = {VALUE_ON: VALUE_TRUE, VALUE_OFF: VALUE_FALSE}

ROLLER_DEVICE_CLASSES = [
    DEVICE_CLASS_AWNING,
    DEVICE_CLASS_BLIND,
    DEVICE_CLASS_CURTAIN,
    DEVICE_CLASS_DAMPER,
    DEVICE_CLASS_DOOR,
    DEVICE_CLASS_GARAGE,
    DEVICE_CLASS_GATE,
    DEVICE_CLASS_SHADE,
    DEVICE_CLASS_SHUTTER,
    DEVICE_CLASS_WINDOW,
]


def get_device_config(dev_id):
    """Get device configuration."""
    result = data.get(dev_id, data.get(dev_id.lower(), {}))  # noqa: F821
    if not result:
        result = {}
    try:
        if isinstance(result, list):
            raise TypeError
        if len(result) > 0:
            result[0]
    except TypeError:
        logger.error("Wrong configuration for %s", dev_id)  # noqa: F821
        result = {}
    finally:
        return result


def mqtt_publish(topic, payload, retain, qos):
    """Publish data to MQTT broker."""
    service_data = {
        KEY_TOPIC: topic,
        KEY_PAYLOAD: payload,
        KEY_RETAIN: retain,
        KEY_QOS: qos,
    }
    logger.debug("Sending to MQTT broker: %s %s", topic, payload)  # noqa: F821
    hass.services.call("mqtt", "publish", service_data, False)  # noqa: F821


expire_after = EXPIRE_AFTER_FOR_BATTERY_POWERED

qos = 0
retain = True
roller_mode = False

no_battery_sensor = False

fw_ver = data.get(CONF_FW_VER)  # noqa: F821
dev_id = data.get(CONF_ID)  # noqa: F821
ignored = [
    element.lower() for element in data.get(CONF_IGNORED_DEVICES, [])
]  # noqa: F821
mac = data.get(CONF_MAC).lower()  # noqa: F821

if not dev_id:
    raise ValueError(f"{dev_id} is wrong dev_id argument")
if not mac:
    raise ValueError(f"{mac} is wrong mac argument")
if not fw_ver:
    raise ValueError(f"{fw_ver} is wrong fvw_ver argument")

cur_ver = fw_ver.split("/v")[1].split("@")[0].rsplit(".", 1)
cur_ver = float(cur_ver[0]) + float(cur_ver[1]) / 100

min_ver = MIN_FIRMWARE_VERSION.rsplit(".", 1)
min_ver = float(min_ver[0]) + float(min_ver[1]) / 100

if cur_ver < min_ver:
    raise ValueError(
        f"Firmware version {MIN_FIRMWARE_VERSION} is required, please update your device {dev_id}"
    )

logger.debug("dev_id: %s, mac: %s, fw_ver: %s", dev_id, mac, fw_ver)  # noqa: F821

try:
    if int(data.get(CONF_QOS, 0)) in [0, 1, 2]:  # noqa: F821
        qos = int(data.get(CONF_QOS, 0))  # noqa: F821
    else:
        raise ValueError()
except ValueError:
    logger.error("Wrong qos argument, the default value 0 was used")  # noqa: F821

disc_prefix = data.get(CONF_DISCOVERY_PREFIX, DEFAULT_DISC_PREFIX)  # noqa: F821

develop = data.get(CONF_DEVELOP, False)  # noqa: F821
if develop:
    disc_prefix = "develop"
    retain = False
    logger.error("DEVELOP MODE !!!")  # noqa: F821

battery_powered = False
bin_sensors = []
bin_sensors_classes = []
bin_sensors_pl = []
bin_sensors_topics = []
bin_sensors_tpls = []
ext_humi_sensors = 0
ext_sensors = 0  # to remove
ext_temp_sensors = 0
lights_bin_sensors = []
lights_bin_sensors_classes = []
lights_bin_sensors_pl = []
lights_bin_sensors_tpls = []
lights_sensors = []
lights_sensors_classes = []
lights_sensors_tpls = []
lights_sensors_units = []
meters = 0
meters_sensors = []
meters_sensors_classes = []
meters_sensors_tpls = []
meters_sensors_units = []
meters_sensors_units = []
model = None
relay_components = [COMP_SWITCH, COMP_LIGHT, COMP_FAN]
relays = 0
relays_bin_sensors = []
relays_bin_sensors_classes = []
relays_bin_sensors_pl = []
relays_bin_sensors_topics = []
relays_bin_sensors_tpls = []
relays_sensors = []
relays_sensors_classes = []
relays_sensors_tpls = []
relays_sensors_units = []
rgbw_lights = 0
rollers = 0
sensors = []
sensors_classes = []
sensors_tpls = []
sensors_units = []
white_lights = 0

if dev_id.rsplit("-", 1)[0] == "shelly1":
    model = MODEL_SHELLY1
    relays = 1
    relays_bin_sensors = [SENSOR_INPUT, SENSOR_LONGPUSH, SENSOR_SHORTPUSH]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0, PL_0_1]
    relays_bin_sensors_topics = [None, TOPIC_LONGPUSH, TOPIC_LONGPUSH]
    relays_bin_sensors_tpls = [None, None, None]
    relays_bin_sensors_classes = [None, None, None]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]
    ext_humi_sensors = 1
    ext_temp_sensors = 3
    ext_sensors = 3  # to remove

if dev_id.rsplit("-", 1)[0] == "shelly1pm":
    model = MODEL_SHELLY1PM
    relays = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [
        SENSOR_INPUT,
        SENSOR_LONGPUSH,
        SENSOR_SHORTPUSH,
        SENSOR_OVERPOWER,
    ]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0, PL_0_1, None]
    relays_bin_sensors_topics = [None, TOPIC_LONGPUSH, TOPIC_LONGPUSH, TOPIC_RELAY]
    relays_bin_sensors_tpls = [None, None, None, TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [None, None, None, DEVICE_CLASS_PROBLEM]
    sensors = [SENSOR_TEMPERATURE, SENSOR_RSSI, SENSOR_SSID]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_units = [UNIT_CELSIUS, UNIT_DB, None]
    sensors_tpls = [TPL_TEMPERATURE, TPL_RSSI, TPL_SSID]
    bin_sensors = [SENSOR_OVERTEMPERATURE, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_HEAT, None]
    bin_sensors_pl = [PL_1_0, None]
    bin_sensors_tpls = [None, TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [None, TOPIC_INFO]
    ext_humi_sensors = 1
    ext_temp_sensors = 3
    ext_sensors = 3  # to remove

if dev_id.rsplit("-", 1)[0] == "shellyair":
    model = MODEL_SHELLYAIR
    relays = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [SENSOR_INPUT]
    relays_bin_sensors_pl = [PL_1_0]
    relays_bin_sensors_tpls = [None]
    relays_bin_sensors_classes = [None]
    sensors = [SENSOR_TEMPERATURE, SENSOR_TOTALWORKTIME, SENSOR_RSSI, SENSOR_SSID]
    sensors_classes = [
        DEVICE_CLASS_TEMPERATURE,
        None,
        DEVICE_CLASS_SIGNAL_STRENGTH,
        None,
    ]
    sensors_units = [UNIT_CELSIUS, UNIT_SECOND, UNIT_DB, None]
    sensors_tpls = [TPL_TEMPERATURE, None, TPL_RSSI, TPL_SSID]
    bin_sensors = [SENSOR_OVERTEMPERATURE, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_HEAT, None]
    bin_sensors_pl = [PL_1_0, None]
    bin_sensors_tpls = [None, TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [None, TOPIC_INFO]
    ext_temp_sensors = 1
    ext_sensors = 1  # to remove

if dev_id.rsplit("-", 1)[0] == "shellyswitch":
    model = MODEL_SHELLY2
    relays = 2
    rollers = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [
        SENSOR_INPUT,
        SENSOR_LONGPUSH,
        SENSOR_SHORTPUSH,
        SENSOR_OVERPOWER,
    ]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0, PL_0_1, None]
    relays_bin_sensors_topics = [None, TOPIC_LONGPUSH, TOPIC_LONGPUSH, TOPIC_RELAY]
    relays_bin_sensors_tpls = [None, None, None, TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [None, None, None, DEVICE_CLASS_PROBLEM]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellyswitch25":
    model = MODEL_SHELLY25
    relays = 2
    rollers = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [
        SENSOR_INPUT,
        SENSOR_LONGPUSH,
        SENSOR_SHORTPUSH,
        SENSOR_OVERPOWER,
    ]
    relays_bin_sensors_pl = [PL_1_0, PL_1_0, PL_0_1, None]
    relays_bin_sensors_topics = [None, TOPIC_LONGPUSH, TOPIC_LONGPUSH, TOPIC_RELAY]
    relays_bin_sensors_tpls = [None, None, None, TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [None, None, None, DEVICE_CLASS_PROBLEM]
    sensors = [SENSOR_TEMPERATURE, SENSOR_RSSI, SENSOR_SSID]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_units = [UNIT_CELSIUS, UNIT_DB, None]
    sensors_tpls = [TPL_TEMPERATURE, TPL_RSSI, TPL_SSID]
    bin_sensors = [SENSOR_OVERTEMPERATURE, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_HEAT, None]
    bin_sensors_pl = [PL_1_0, None]
    bin_sensors_tpls = [None, TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [None, TOPIC_INFO]

if dev_id.rsplit("-", 1)[0] == "shellyplug":
    model = MODEL_SHELLYPLUG
    relays = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [SENSOR_OVERPOWER]
    relays_bin_sensors_pl = [None]
    relays_bin_sensors_topics = [TOPIC_RELAY]
    relays_bin_sensors_tpls = [TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [DEVICE_CLASS_PROBLEM]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellyplug-s":
    model = MODEL_SHELLYPLUG_S
    relays = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [SENSOR_OVERPOWER]
    relays_bin_sensors_pl = [None]
    relays_bin_sensors_topics = [TOPIC_RELAY]
    relays_bin_sensors_tpls = [TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [DEVICE_CLASS_PROBLEM]
    sensors = [SENSOR_TEMPERATURE, SENSOR_RSSI, SENSOR_SSID]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_units = [UNIT_CELSIUS, UNIT_DB, None]
    sensors_tpls = [TPL_TEMPERATURE, TPL_RSSI, TPL_SSID]
    bin_sensors = [SENSOR_OVERTEMPERATURE, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_HEAT, None]
    bin_sensors_pl = [PL_1_0, None]
    bin_sensors_tpls = [None, TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [None, TOPIC_INFO]

if dev_id.rsplit("-", 1)[0] == "shelly4pro":
    model = MODEL_SHELLY4PRO
    relays = 4
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [SENSOR_OVERPOWER]
    relays_bin_sensors_pl = [None]
    relays_bin_sensors_topics = [TOPIC_RELAY]
    relays_bin_sensors_tpls = [TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [DEVICE_CLASS_PROBLEM]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellyht":
    model = MODEL_SHELLYHT
    sensors = [SENSOR_TEMPERATURE, SENSOR_HUMIDITY, SENSOR_BATTERY]
    sensors_classes = [
        DEVICE_CLASS_TEMPERATURE,
        DEVICE_CLASS_HUMIDITY,
        DEVICE_CLASS_BATTERY,
    ]
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_HUMIDITY, TPL_BATTERY]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_ANNOUNCE]
    bin_sensors_topics = [TOPIC_ANNOUNCE]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellygas":
    model = MODEL_SHELLYGAS
    sensors = [
        SENSOR_OPERATION,
        SENSOR_GAS,
        SENSOR_SELF_TEST,
        SENSOR_CONCENTRATION,
        SENSOR_RSSI,
        SENSOR_SSID,
    ]
    sensors_classes = [None, None, None, None, DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [None, None, None, None, TPL_RSSI, TPL_SSID]
    sensors_units = [None, None, None, UNIT_PPM, UNIT_DB, None]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]

if dev_id.rsplit("-", 1)[0] == "shellybutton1":
    model = MODEL_SHELLYBUTTON1
    sensors = [SENSOR_BATTERY]
    sensors_classes = [DEVICE_CLASS_BATTERY]
    sensors_units = [UNIT_PERCENT]
    sensors_tpls = [TPL_BATTERY]
    bin_sensors = [
        SENSOR_INPUT_0,
        SENSOR_SHORTPUSH,
        SENSOR_DOUBLE_SHORTPUSH,
        SENSOR_TRIPLE_SHORTPUSH,
        SENSOR_LONGPUSH,
        SENSOR_FIRMWARE_UPDATE,
    ]
    bin_sensors_classes = [None, None, None, None, None, None]
    bin_sensors_tpls = [
        None,
        TPL_SHORTPUSH,
        TPL_DOUBLE_SHORTPUSH,
        TPL_TRIPLE_SHORTPUSH,
        TPL_LONGPUSH,
        TPL_NEW_FIRMWARE_FROM_ANNOUNCE,
    ]
    bin_sensors_pl = [PL_1_0, None, None, None, None, None]
    bin_sensors_topics = [
        None,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_0,
        TOPIC_ANNOUNCE,
    ]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellydw":
    model = MODEL_SHELLYDW
    sensors = [SENSOR_LUX, SENSOR_BATTERY, SENSOR_TILT]
    sensors_classes = [DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_BATTERY, None]
    sensors_units = [UNIT_LUX, UNIT_PERCENT, UNIT_DEGREE]
    sensors_tpls = [TPL_LUX, TPL_BATTERY, TPL_TILT]
    bin_sensors = [SENSOR_OPENING, SENSOR_VIBRATION, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_OPENING, DEVICE_CLASS_VIBRATION, None]
    bin_sensors_pl = [PL_OPEN_CLOSE, PL_1_0, None]
    bin_sensors_tpls = [None, None, TPL_NEW_FIRMWARE_FROM_ANNOUNCE]
    bin_sensors_topics = [None, None, TOPIC_ANNOUNCE]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellydw2":
    model = MODEL_SHELLYDW2
    sensors = [SENSOR_LUX, SENSOR_BATTERY, SENSOR_TILT, SENSOR_TEMPERATURE]
    sensors_classes = [
        DEVICE_CLASS_ILLUMINANCE,
        DEVICE_CLASS_BATTERY,
        None,
        DEVICE_CLASS_TEMPERATURE,
    ]
    sensors_units = [UNIT_LUX, UNIT_PERCENT, UNIT_DEGREE, UNIT_CELSIUS]
    sensors_tpls = [TPL_LUX, TPL_BATTERY, TPL_TILT, TPL_TEMPERATURE]
    bin_sensors = [SENSOR_OPENING, SENSOR_VIBRATION, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_OPENING, DEVICE_CLASS_VIBRATION, None]
    bin_sensors_pl = [PL_OPEN_CLOSE, PL_1_0, None]
    bin_sensors_tpls = [None, None, TPL_NEW_FIRMWARE_FROM_ANNOUNCE]
    bin_sensors_topics = [None, None, TOPIC_ANNOUNCE]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellysmoke":
    model = MODEL_SHELLYSMOKE
    sensors = [SENSOR_TEMPERATURE, SENSOR_BATTERY]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_BATTERY]
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_BATTERY]
    bin_sensors = [SENSOR_SMOKE, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_SMOKE, None]
    bin_sensors_pl = [PL_TRUE_FALSE, None]
    bin_sensors_tpls = [None, TPL_NEW_FIRMWARE_FROM_ANNOUNCE]
    bin_sensors_topics = [None, TOPIC_ANNOUNCE]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellysense":
    model = MODEL_SHELLYSENSE
    sensors = [SENSOR_TEMPERATURE, SENSOR_HUMIDITY, SENSOR_LUX, SENSOR_BATTERY]
    sensors_classes = [
        DEVICE_CLASS_TEMPERATURE,
        DEVICE_CLASS_HUMIDITY,
        DEVICE_CLASS_ILLUMINANCE,
        DEVICE_CLASS_BATTERY,
    ]
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT, UNIT_LUX, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_HUMIDITY, TPL_LUX, TPL_BATTERY]
    bin_sensors = [SENSOR_MOTION, SENSOR_CHARGER, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_MOTION, DEVICE_CLASS_BATTERY_CHARGING, None]
    bin_sensors_pl = [PL_TRUE_FALSE, PL_TRUE_FALSE, None]
    bin_sensors_tpls = [None, None, TPL_NEW_FIRMWARE_FROM_ANNOUNCE]
    bin_sensors_topics = [None, None, TOPIC_ANNOUNCE]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellyrgbw2":
    model = MODEL_SHELLYRGBW2
    rgbw_lights = 1
    white_lights = 4
    lights_sensors = [SENSOR_POWER]
    lights_sensors_classes = [DEVICE_CLASS_POWER]
    lights_sensors_units = [UNIT_WATT]
    lights_sensors_tpls = ["{{value_json.power|float|round(1)}}"]
    bin_sensors = [
        SENSOR_OVERPOWER,
        SENSOR_INPUT_0,
        SENSOR_LONGPUSH_0,
        SENSOR_SHORTPUSH_0,
        SENSOR_FIRMWARE_UPDATE,
    ]
    bin_sensors_classes = [DEVICE_CLASS_PROBLEM, None, None, None, None]
    bin_sensors_tpls = [TPL_OVERPOWER, None, None, None, TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_pl = [None, PL_1_0, PL_1_0, PL_0_1, None]
    bin_sensors_topics = [
        TOPIC_COLOR_0_STATUS,
        TOPIC_INPUT_0,
        TOPIC_LONGPUSH_0,
        TOPIC_LONGPUSH_0,
        TOPIC_INFO,
    ]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellydimmer":
    model = MODEL_SHELLYDIMMER
    white_lights = 1
    sensors = [SENSOR_TEMPERATURE, SENSOR_RSSI, SENSOR_SSID]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_units = [UNIT_CELSIUS, UNIT_DB, None]
    sensors_tpls = [TPL_TEMPERATURE, TPL_RSSI, TPL_SSID]
    bin_sensors = [
        SENSOR_OVERTEMPERATURE,
        SENSOR_OVERLOAD,
        SENSOR_LOADERROR,
        SENSOR_INPUT_0,
        SENSOR_INPUT_1,
        SENSOR_LONGPUSH_0,
        SENSOR_LONGPUSH_1,
        SENSOR_SHORTPUSH_0,
        SENSOR_SHORTPUSH_1,
        SENSOR_FIRMWARE_UPDATE,
    ]
    bin_sensors_classes = [
        DEVICE_CLASS_HEAT,
        DEVICE_CLASS_PROBLEM,
        DEVICE_CLASS_PROBLEM,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    bin_sensors_pl = [
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_0_1,
        PL_0_1,
        None,
    ]
    bin_sensors_tpls = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        TPL_NEW_FIRMWARE_FROM_INFO,
    ]
    bin_sensors_topics = [
        None,
        None,
        None,
        TOPIC_INPUT_0,
        TOPIC_INPUT_1,
        TOPIC_LONGPUSH_0,
        TOPIC_LONGPUSH_1,
        TOPIC_LONGPUSH_0,
        TOPIC_LONGPUSH_1,
        TOPIC_INFO,
    ]
    lights_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    lights_sensors_units = [UNIT_WATT, UNIT_KWH]
    lights_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    lights_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]

if dev_id.rsplit("-", 1)[0] == "shellydimmer2":
    model = MODEL_SHELLYDIMMER2
    white_lights = 1
    sensors = [SENSOR_TEMPERATURE, SENSOR_RSSI, SENSOR_SSID]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_units = [UNIT_CELSIUS, UNIT_DB, None]
    sensors_tpls = [TPL_TEMPERATURE, TPL_RSSI, TPL_SSID]
    bin_sensors = [
        SENSOR_OVERTEMPERATURE,
        SENSOR_OVERLOAD,
        SENSOR_LOADERROR,
        SENSOR_INPUT_0,
        SENSOR_INPUT_1,
        SENSOR_LONGPUSH_0,
        SENSOR_LONGPUSH_1,
        SENSOR_SHORTPUSH_0,
        SENSOR_SHORTPUSH_1,
        SENSOR_FIRMWARE_UPDATE,
    ]
    bin_sensors_classes = [
        DEVICE_CLASS_HEAT,
        DEVICE_CLASS_PROBLEM,
        DEVICE_CLASS_PROBLEM,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    bin_sensors_pl = [
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_1_0,
        PL_0_1,
        PL_0_1,
        None,
    ]
    bin_sensors_tpls = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        TPL_NEW_FIRMWARE_FROM_INFO,
    ]
    bin_sensors_topics = [
        None,
        None,
        None,
        TOPIC_INPUT_0,
        TOPIC_INPUT_1,
        TOPIC_LONGPUSH_0,
        TOPIC_LONGPUSH_1,
        TOPIC_LONGPUSH_0,
        TOPIC_LONGPUSH_1,
        TOPIC_INFO,
    ]
    lights_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    lights_sensors_units = [UNIT_WATT, UNIT_KWH]
    lights_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    lights_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]

if dev_id.rsplit("-", 1)[0] == "shellybulb":
    model = MODEL_SHELLYBULB
    rgbw_lights = 1
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0].lower() == "shellybulbduo":
    model = MODEL_SHELLYDUO
    white_lights = 1
    lights_sensors = [SENSOR_ENERGY, SENSOR_POWER]
    lights_sensors_units = [UNIT_KWH, UNIT_WATT]
    lights_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    lights_sensors_tpls = [TPL_ENERGY_WMIN, TPL_POWER]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0].lower() == "shellyvintage":
    model = MODEL_SHELLYVINTAGE
    white_lights = 1
    lights_sensors = [SENSOR_ENERGY, SENSOR_POWER]
    lights_sensors_units = [UNIT_KWH, UNIT_WATT]
    lights_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    lights_sensors_tpls = [TPL_ENERGY_WMIN, TPL_POWER]
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellyem":
    model = MODEL_SHELLYEM
    relays = 1
    relays_sensors = [SENSOR_POWER, SENSOR_ENERGY]
    relays_sensors_units = [UNIT_WATT, UNIT_KWH]
    relays_sensors_classes = [DEVICE_CLASS_POWER, DEVICE_CLASS_POWER]
    relays_sensors_tpls = [TPL_POWER, TPL_ENERGY_WMIN]
    relays_bin_sensors = [SENSOR_OVERPOWER]
    relays_bin_sensors_pl = [None]
    relays_bin_sensors_topics = [TOPIC_RELAY]
    relays_bin_sensors_tpls = [TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [DEVICE_CLASS_PROBLEM]
    meters = 2
    meters_sensors = [
        SENSOR_POWER,
        SENSOR_REACTIVE_POWER,
        SENSOR_VOLTAGE,
        SENSOR_ENERGY,
        SENSOR_RETURNED_ENERGY,
        SENSOR_TOTAL,
        SENSOR_TOTAL_RETURNED,
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
        DEVICE_CLASS_POWER,
        None,
        None,
        DEVICE_CLASS_POWER,
        DEVICE_CLASS_POWER,
        DEVICE_CLASS_POWER,
        DEVICE_CLASS_POWER,
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
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellyem3":
    model = MODEL_SHELLY3EM
    relays = 1
    meters = 3
    relays_bin_sensors = [SENSOR_OVERPOWER]
    relays_bin_sensors_pl = [None]
    relays_bin_sensors_topics = [TOPIC_RELAY]
    relays_bin_sensors_tpls = [TPL_OVERPOWER_RELAY]
    relays_bin_sensors_classes = [DEVICE_CLASS_PROBLEM]
    meters_sensors = [
        SENSOR_CURRENT,
        SENSOR_POWER,
        SENSOR_POWER_FACTOR,
        SENSOR_VOLTAGE,
        SENSOR_ENERGY,
        SENSOR_RETURNED_ENERGY,
        SENSOR_TOTAL,
        SENSOR_TOTAL_RETURNED,
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
        DEVICE_CLASS_POWER,
        None,
        None,
        DEVICE_CLASS_POWER,
        DEVICE_CLASS_POWER,
        DEVICE_CLASS_POWER,
        DEVICE_CLASS_POWER,
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
    bin_sensors = [SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [None]
    bin_sensors_tpls = [TPL_NEW_FIRMWARE_FROM_INFO]
    bin_sensors_topics = [TOPIC_INFO]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

if dev_id.rsplit("-", 1)[0] == "shellyflood":
    model = MODEL_SHELLYFLOOD
    sensors = [SENSOR_TEMPERATURE, SENSOR_BATTERY]
    sensors_classes = [DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_BATTERY]
    sensors_units = [UNIT_CELSIUS, UNIT_PERCENT]
    sensors_tpls = [TPL_TEMPERATURE, TPL_BATTERY]
    bin_sensors = [SENSOR_FLOOD, SENSOR_FIRMWARE_UPDATE]
    bin_sensors_classes = [DEVICE_CLASS_MOISTURE, None]
    bin_sensors_pl = [PL_TRUE_FALSE, None]
    bin_sensors_tpls = [None, TPL_NEW_FIRMWARE_FROM_ANNOUNCE]
    bin_sensors_topics = [None, TOPIC_ANNOUNCE]
    battery_powered = True

if dev_id.rsplit("-", 1)[0] == "shellyix3":
    model = MODEL_SHELLYI3
    bin_sensors = [
        SENSOR_INPUT_0,
        SENSOR_INPUT_1,
        SENSOR_INPUT_2,
        SENSOR_SHORTPUSH_0,
        SENSOR_DOUBLE_SHORTPUSH_0,
        SENSOR_TRIPLE_SHORTPUSH_0,
        SENSOR_LONGPUSH_0,
        SENSOR_SHORTPUSH_1,
        SENSOR_DOUBLE_SHORTPUSH_1,
        SENSOR_TRIPLE_SHORTPUSH_1,
        SENSOR_LONGPUSH_1,
        SENSOR_SHORTPUSH_2,
        SENSOR_DOUBLE_SHORTPUSH_2,
        SENSOR_TRIPLE_SHORTPUSH_2,
        SENSOR_LONGPUSH_2,
        SENSOR_SHORTPUSH_LONGPUSH_0,
        SENSOR_SHORTPUSH_LONGPUSH_1,
        SENSOR_SHORTPUSH_LONGPUSH_2,
        SENSOR_LONGPUSH_SHORTPUSH_0,
        SENSOR_LONGPUSH_SHORTPUSH_1,
        SENSOR_LONGPUSH_SHORTPUSH_2,
        SENSOR_FIRMWARE_UPDATE,
    ]
    bin_sensors_classes = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    bin_sensors_tpls = [
        None,
        None,
        None,
        TPL_SHORTPUSH,
        TPL_DOUBLE_SHORTPUSH,
        TPL_TRIPLE_SHORTPUSH,
        TPL_LONGPUSH,
        TPL_SHORTPUSH,
        TPL_DOUBLE_SHORTPUSH,
        TPL_TRIPLE_SHORTPUSH,
        TPL_LONGPUSH,
        TPL_SHORTPUSH,
        TPL_DOUBLE_SHORTPUSH,
        TPL_TRIPLE_SHORTPUSH,
        TPL_LONGPUSH,
        TPL_SHORTPUSH_LONGPUSH,
        TPL_SHORTPUSH_LONGPUSH,
        TPL_SHORTPUSH_LONGPUSH,
        TPL_LONGPUSH_SHORTPUSH,
        TPL_LONGPUSH_SHORTPUSH,
        TPL_LONGPUSH_SHORTPUSH,
        TPL_NEW_FIRMWARE_FROM_INFO,
    ]
    bin_sensors_topics = [
        TOPIC_INPUT_0,
        TOPIC_INPUT_1,
        TOPIC_INPUT_2,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_1,
        TOPIC_INPUT_EVENT_1,
        TOPIC_INPUT_EVENT_1,
        TOPIC_INPUT_EVENT_1,
        TOPIC_INPUT_EVENT_2,
        TOPIC_INPUT_EVENT_2,
        TOPIC_INPUT_EVENT_2,
        TOPIC_INPUT_EVENT_2,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_1,
        TOPIC_INPUT_EVENT_2,
        TOPIC_INPUT_EVENT_0,
        TOPIC_INPUT_EVENT_1,
        TOPIC_INPUT_EVENT_2,
        TOPIC_INFO,
    ]
    bin_sensors_pl = [
        PL_1_0,
        PL_1_0,
        PL_0_1,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    sensors = [SENSOR_RSSI, SENSOR_SSID]
    sensors_units = [UNIT_DB, None]
    sensors_classes = [DEVICE_CLASS_SIGNAL_STRENGTH, None]
    sensors_tpls = [TPL_RSSI, TPL_SSID]

# rollers
for roller_id in range(rollers):
    device_config = get_device_config(dev_id)
    config_mode = ATTR_RELAY
    if device_config.get(CONF_MODE):
        config_mode = device_config[CONF_MODE]
    device_name = f"{model} {dev_id.split('-')[-1]}"
    if device_config.get(f"roller-{roller_id}-name"):
        roller_name = device_config[f"roller-{roller_id}-name"]
    else:
        roller_name = f"{device_name} Roller {roller_id}"
    device_class = None
    if device_config.get(f"roller-{roller_id}-class"):
        if device_config[f"roller-{roller_id}-class"] in ROLLER_DEVICE_CLASSES:
            device_class = device_config[f"roller-{roller_id}-class"]
        else:
            logger.error(
                "Wrong roller class, the default value None was used"
            )  # noqa: F821
    default_topic = f"shellies/{dev_id}/"
    state_topic = f"~roller/{roller_id}"
    command_topic = f"{state_topic}/command"
    position_topic = f"{state_topic}/pos"
    set_position_topic = f"{state_topic}/command/pos"
    availability_topic = "~online"
    unique_id = f"{dev_id}-roller-{roller_id}".lower()
    config_topic = f"{disc_prefix}/cover/{dev_id}-roller-{roller_id}/config"
    if config_mode == ATTR_ROLLER:
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
    if device_class:
        payload[KEY_DEVICE_CLASS] = device_class
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# relays
for relay_id in range(relays):
    device_config = get_device_config(dev_id)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    if device_config.get(f"relay-{relay_id}-name"):
        relay_name = device_config[f"relay-{relay_id}-name"]
    else:
        relay_name = f"{device_name} Relay {relay_id}"
    default_topic = f"shellies/{dev_id}/"
    state_topic = f"~relay/{relay_id}"
    command_topic = f"{state_topic}/command"
    availability_topic = "~online"
    unique_id = f"{dev_id}-relay-{relay_id}".lower()
    config_component = COMP_SWITCH
    if device_config.get(f"relay-{relay_id}"):
        config_component = device_config[f"relay-{relay_id}"]
    for component in relay_components:
        config_topic = f"{disc_prefix}/{component}/{dev_id}-relay-{relay_id}/config"
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
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # relay's sensors
    if relay_id == relays - 1:
        for sensor_id in range(len(relays_sensors)):
            device_config = get_device_config(dev_id)
            force_update = False
            if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
                force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
            unique_id = f"{dev_id}-relay-{relays_sensors[sensor_id]}".lower()
            config_topic = (
                f"{disc_prefix}/sensor/{dev_id}-{relays_sensors[sensor_id]}/config"
            )
            if device_config.get(f"relay-{relay_id}-name"):
                sensor_name = f"{device_config[f'relay-{relay_id}-name']} {relays_sensors[sensor_id].title()}"
            else:
                sensor_name = f"{device_name} {relays_sensors[sensor_id].title()}"
            state_topic = f"~relay/{relays_sensors[sensor_id]}"
            if model == MODEL_SHELLY2 or roller_mode:
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
            if dev_id.lower() in ignored:
                payload = ""
            mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # relay's sensors
    for sensor_id in range(len(relays_sensors)):
        device_config = get_device_config(dev_id)
        force_update = False
        if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
            force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
        unique_id = f"{dev_id}-relay-{relays_sensors[sensor_id]}-{relay_id}".lower()
        config_topic = f"{disc_prefix}/sensor/{dev_id}-{relays_sensors[sensor_id]}-{relay_id}/config"
        if device_config.get(f"relay-{relay_id}-name"):
            sensor_name = f"{device_config[f'relay-{relay_id}-name']} {relays_sensors[sensor_id].title()}"
        else:
            sensor_name = (
                f"{device_name} {relays_sensors[sensor_id].title()} {relay_id}"
            )
        state_topic = f"~relay/{relay_id}/{relays_sensors[sensor_id]}"
        if model != MODEL_SHELLY2 and not roller_mode:
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
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # relay's binary sensors
    for bin_sensor_id in range(len(relays_bin_sensors)):
        device_config = get_device_config(dev_id)
        push_off_delay = True
        if isinstance(device_config.get(CONF_PUSH_OFF_DELAY), bool):
            push_off_delay = device_config.get(CONF_PUSH_OFF_DELAY)
        unique_id = f"{dev_id}-{relays_bin_sensors[bin_sensor_id]}-{relay_id}".lower()
        config_topic = f"{disc_prefix}/binary_sensor/{dev_id}-{relays_bin_sensors[bin_sensor_id]}-{relay_id}/config"
        if device_config.get(f"relay-{relay_id}-name"):
            sensor_name = f"{device_config[f'relay-{relay_id}-name']} {relays_bin_sensors[bin_sensor_id].title()}"
        else:
            sensor_name = (
                f"{device_name} {relays_bin_sensors[bin_sensor_id].title()} {relay_id}"
            )
        if relays_bin_sensors_topics and relays_bin_sensors_topics[bin_sensor_id]:
            state_topic = f"~{relays_bin_sensors_topics[bin_sensor_id]}/{relay_id}"
        else:
            state_topic = f"~{relays_bin_sensors[bin_sensor_id]}/{relay_id}"
        if not roller_mode:
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
            if (
                relays_bin_sensors[bin_sensor_id]
                in [
                    SENSOR_LONGPUSH,
                    SENSOR_LONGPUSH_0,
                    SENSOR_LONGPUSH_1,
                    SENSOR_LONGPUSH_2,
                    SENSOR_SHORTPUSH,
                    SENSOR_SHORTPUSH_0,
                    SENSOR_SHORTPUSH_1,
                    SENSOR_SHORTPUSH_2,
                    SENSOR_DOUBLE_SHORTPUSH,
                    SENSOR_DOUBLE_SHORTPUSH_0,
                    SENSOR_DOUBLE_SHORTPUSH_1,
                    SENSOR_DOUBLE_SHORTPUSH_2,
                    SENSOR_TRIPLE_SHORTPUSH,
                    SENSOR_TRIPLE_SHORTPUSH_0,
                    SENSOR_TRIPLE_SHORTPUSH_1,
                    SENSOR_TRIPLE_SHORTPUSH_2,
                ]
                and push_off_delay
            ):
                payload[KEY_OFF_DELAY] = OFF_DELAY
            if relays_bin_sensors_tpls[bin_sensor_id]:
                payload[KEY_VALUE_TEMPLATE] = relays_bin_sensors_tpls[bin_sensor_id]
            else:
                payload[KEY_PAYLOAD_ON] = relays_bin_sensors_pl[bin_sensor_id][VALUE_ON]
                payload[KEY_PAYLOAD_OFF] = relays_bin_sensors_pl[bin_sensor_id][
                    VALUE_OFF
                ]
            if relays_bin_sensors_classes[bin_sensor_id]:
                payload[KEY_DEVICE_CLASS] = relays_bin_sensors_classes[bin_sensor_id]
        else:
            payload = ""
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(
            config_topic, str(payload).replace("'", '"').replace("^", "'"), retain, qos
        )

# sensors
for sensor_id in range(len(sensors)):
    device_config = get_device_config(dev_id)
    force_update = False
    if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
        force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    unique_id = f"{dev_id}-{sensors[sensor_id]}".lower()
    config_topic = f"{disc_prefix}/sensor/{dev_id}-{sensors[sensor_id]}/config"
    default_topic = f"shellies/{dev_id}/"
    availability_topic = "~online"
    if sensors[sensor_id] in [SENSOR_RSSI, SENSOR_SSID]:
        sensor_name = f"{device_name} {sensors[sensor_id].upper()}"
    else:
        sensor_name = f"{device_name} {sensors[sensor_id].title()}"
    if sensors[sensor_id] in [SENSOR_RSSI, SENSOR_SSID]:
        state_topic = "~info"
    elif relays > 0 or white_lights > 0:
        state_topic = f"~{sensors[sensor_id]}"
    else:
        state_topic = f"~sensor/{sensors[sensor_id]}"

    config_component = COMP_SWITCH
    if device_config.get(CONF_POWERED) == ATTR_POWER_AC:
        no_battery_sensor = True
        expire_after = EXPIRE_AFTER_FOR_AC_POWERED
    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: state_topic,
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
    if model == MODEL_SHELLYDW2 and sensors[sensor_id] == SENSOR_LUX:
        payload[KEY_JSON_ATTRIBUTE_TOPIC] = f"~sensor/{SENSOR_ILLUMINATION}"
        payload[KEY_JSON_ATTRIBUTES_TEMPLATE] = TPL_ILLUMINATION_TO_JSON
    if sensors_units[sensor_id]:
        payload[KEY_UNIT] = sensors_units[sensor_id]
    if sensors_classes[sensor_id]:
        payload[KEY_DEVICE_CLASS] = sensors_classes[sensor_id]
    if not battery_powered:
        payload[KEY_AVAILABILITY_TOPIC] = availability_topic
        payload[KEY_PAYLOAD_AVAILABLE] = VALUE_TRUE
        payload[KEY_PAYLOAD_NOT_AVAILABLE] = VALUE_FALSE
    if sensors_tpls[sensor_id]:
        payload[KEY_VALUE_TEMPLATE] = sensors_tpls[sensor_id]
    if sensors[sensor_id] == SENSOR_SSID:
        payload[KEY_ICON] = "mdi:wifi"
    if no_battery_sensor and sensors[sensor_id] == SENSOR_BATTERY:
        payload = ""
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(
        config_topic, str(payload).replace("'", '"').replace("^", "'"), retain, qos
    )

# external sensors, to remove
for sensor_id in range(ext_sensors):
    config_topic = f"{disc_prefix}/sensor/{dev_id}-ext-{sensor_id}/config"
    payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# external temperature sensors
for sensor_id in range(ext_temp_sensors):
    device_config = get_device_config(dev_id)
    force_update = False
    if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
        force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    unique_id = f"{dev_id}-ext-temperature-{sensor_id}".lower()
    config_topic = f"{disc_prefix}/sensor/{dev_id}-ext-temperature-{sensor_id}/config"
    default_topic = f"shellies/{dev_id}/"
    availability_topic = "~online"
    sensor_name = f"{device_name} External Temperature {sensor_id}"
    state_topic = f"~{SENSOR_EXT_TEMPERATURE}/{sensor_id}"
    if device_config.get(f"ext-temperature-{sensor_id}"):
        payload = {
            KEY_NAME: sensor_name,
            KEY_STATE_TOPIC: state_topic,
            KEY_UNIT: UNIT_CELSIUS,
            KEY_DEVICE_CLASS: SENSOR_TEMPERATURE,
            KEY_EXPIRE_AFTER: expire_after,
            KEY_FORCE_UPDATE: str(force_update),
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
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# external humidity sensors
for sensor_id in range(ext_humi_sensors):
    device_config = get_device_config(dev_id)
    force_update = False
    if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
        force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    unique_id = f"{dev_id}-ext-humidity-{sensor_id}".lower()
    config_topic = f"{disc_prefix}/sensor/{dev_id}-ext-humidity-{sensor_id}/config"
    default_topic = f"shellies/{dev_id}/"
    availability_topic = "~online"
    sensor_name = f"{device_name} External Humidity {sensor_id}"
    state_topic = f"~{SENSOR_EXT_HUMIDITY}/{sensor_id}"
    if device_config.get(f"ext-temperature-{sensor_id}"):
        payload = {
            KEY_NAME: sensor_name,
            KEY_STATE_TOPIC: state_topic,
            KEY_UNIT: UNIT_PERCENT,
            KEY_DEVICE_CLASS: SENSOR_HUMIDITY,
            KEY_EXPIRE_AFTER: expire_after,
            KEY_FORCE_UPDATE: str(force_update),
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
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# binary sensors
for bin_sensor_id in range(len(bin_sensors)):
    device_config = get_device_config(dev_id)
    push_off_delay = True
    if isinstance(device_config.get(CONF_PUSH_OFF_DELAY), bool):
        push_off_delay = device_config.get(CONF_PUSH_OFF_DELAY)
    config_mode = LIGHT_RGBW
    if device_config.get(CONF_MODE):
        config_mode = device_config[CONF_MODE]
    device_name = f"{model} {dev_id.split('-')[-1]}"
    unique_id = f"{dev_id}-{bin_sensors[bin_sensor_id].replace(' ', '-').replace('/', '-')}".lower()
    config_topic = f"{disc_prefix}/binary_sensor/{dev_id}-{bin_sensors[bin_sensor_id].replace(' ', '-').replace('/', '-')}/config"
    default_topic = f"shellies/{dev_id}/"
    availability_topic = "~online"
    sensor_name = (
        f"{device_name} {bin_sensors[bin_sensor_id].replace('/', ' ').title()}"
    )
    if bin_sensors_topics and bin_sensors_topics[bin_sensor_id]:
        state_topic = f"~{bin_sensors_topics[bin_sensor_id]}"
    elif relays > 0 or white_lights > 0:
        state_topic = f"~{bin_sensors[bin_sensor_id]}"
    elif bin_sensors[bin_sensor_id] == SENSOR_OPENING:
        state_topic = "~sensor/state"
    else:
        state_topic = f"~sensor/{bin_sensors[bin_sensor_id]}"
    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: state_topic,
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
    if bin_sensors_tpls[bin_sensor_id]:
        payload[KEY_VALUE_TEMPLATE] = bin_sensors_tpls[bin_sensor_id]
    else:
        payload[KEY_PAYLOAD_ON] = bin_sensors_pl[bin_sensor_id][VALUE_ON]
        payload[KEY_PAYLOAD_OFF] = bin_sensors_pl[bin_sensor_id][VALUE_OFF]
    if battery_powered:
        payload[KEY_EXPIRE_AFTER] = expire_after
    else:
        payload[KEY_AVAILABILITY_TOPIC] = availability_topic
        payload[KEY_PAYLOAD_AVAILABLE] = VALUE_TRUE
        payload[KEY_PAYLOAD_NOT_AVAILABLE] = VALUE_FALSE
    if bin_sensors_classes[bin_sensor_id]:
        payload[KEY_DEVICE_CLASS] = bin_sensors_classes[bin_sensor_id]
    if (
        bin_sensors[bin_sensor_id]
        in [
            SENSOR_LONGPUSH,
            SENSOR_LONGPUSH_0,
            SENSOR_LONGPUSH_1,
            SENSOR_LONGPUSH_2,
            SENSOR_SHORTPUSH,
            SENSOR_SHORTPUSH_0,
            SENSOR_SHORTPUSH_1,
            SENSOR_SHORTPUSH_2,
            SENSOR_DOUBLE_SHORTPUSH,
            SENSOR_DOUBLE_SHORTPUSH_0,
            SENSOR_DOUBLE_SHORTPUSH_1,
            SENSOR_DOUBLE_SHORTPUSH_2,
            SENSOR_TRIPLE_SHORTPUSH,
            SENSOR_TRIPLE_SHORTPUSH_0,
            SENSOR_TRIPLE_SHORTPUSH_1,
            SENSOR_TRIPLE_SHORTPUSH_2,
        ]
        and push_off_delay
    ):
        payload[KEY_OFF_DELAY] = OFF_DELAY
    if (
        model == MODEL_SHELLYRGBW2
        and config_mode == LIGHT_WHITE
        and bin_sensors[bin_sensor_id] == SENSOR_OVERPOWER
    ):
        payload = ""
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(
        config_topic, str(payload).replace("'", '"').replace("^", "'"), retain, qos
    )

# color lights
for light_id in range(rgbw_lights):
    device_config = get_device_config(dev_id)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    if device_config.get(f"light-{light_id}-name"):
        light_name = device_config[f"light-{light_id}-name"]
    else:
        light_name = f"{device_name} Light {light_id}"
    default_topic = f"shellies/{dev_id}/"
    state_topic = f"~color/{light_id}/status"
    command_topic = f"~color/{light_id}/set"
    availability_topic = "~online"
    unique_id = f"{dev_id}-light-{light_id}".lower()
    config_topic = f"{disc_prefix}/light/{dev_id}-{light_id}/config"
    config_mode = LIGHT_RGBW
    if device_config.get(CONF_MODE):
        config_mode = device_config[CONF_MODE]
    payload = {
        KEY_SCHEMA: ATTR_TEMPLATE,
        KEY_NAME: light_name,
        KEY_COMMAND_TOPIC: command_topic,
        KEY_STATE_TOPIC: state_topic,
        KEY_AVAILABILITY_TOPIC: availability_topic,
        KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_COMMAND_OFF_TEMPLATE: "{^turn^:^off^}",
        KEY_BRIGHTNESS_TEMPLATE: "{{value_json.gain|float|multiply(2.55)|round}}",
        KEY_RED_TEMPLATE: "{{value_json.red}}",
        KEY_GREEN_TEMPLATE: "{{value_json.green}}",
        KEY_BLUE_TEMPLATE: "{{value_json.blue}}",
        KEY_WHITE_VALUE_TEMPLATE: "{{value_json.white}}",
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
    if config_mode == LIGHT_RGBW and model == MODEL_SHELLYRGBW2:
        payload[KEY_EFFECT_LIST] = ["Off", "Meteor Shower", "Gradual Change", "Flash"]
        payload[
            KEY_COMMAND_ON_TEMPLATE
        ] = "{^turn^:^on^{% if brightness is defined %},^gain^:{{brightness|float|multiply(0.3922)|round}}{% endif %}{% if red is defined and green is defined and blue is defined %},^red^:{{red}},^green^:{{green}},^blue^:{{blue}}{% endif %}{% if white_value is defined %},^white^:{{white_value}}{% endif %}{% if effect is defined %}{% if effect == ^Meteor Shower^ %}^effect^:1{% elif effect == ^Gradual Change^ %}^effect^:2{% elif effect == ^Flash^ %}^effect^:3{% else %}^effect^:0{% endif %}{% else %}^effect^:0{% endif %}}"
        payload[
            KEY_STATE_TEMPLATE
        ] = "{% if value_json.ison %}on{% else %}off{% endif %}"
        payload[
            KEY_EFFECT_TEMPLATE
        ] = "{% if value_json.effect == 1 %}Meteor Shower{% elif value_json.effect == 2 %}Gradual Change{% elif value_json.effect == 3 %}Flash{% else %}Off{% endif %}"
    elif config_mode == LIGHT_RGBW and model == MODEL_SHELLYBULB:
        payload[KEY_EFFECT_LIST] = [
            "Off",
            "Meteor Shower",
            "Gradual Change",
            "Breath",
            "Flash",
            "On/Off Gradual",
            "Red/Green Change",
        ]
        payload[
            KEY_COMMAND_ON_TEMPLATE
        ] = "{^turn^:^on^,^mode^:^color^,{% if red is defined and green is defined and blue is defined %}^red^:{{red}},^green^:{{green}},^blue^:{{blue}},{% endif %}{% if white_value is defined %}^white^:{{white_value}},{% endif %}{% if brightness is defined %}^gain^:{{brightness|float|multiply(0.3922)|round}},{% endif %}{% if effect is defined %}{% if effect == ^Meteor Shower^ %}^effect^:1{% elif effect == ^Gradual Change^ %}^effect^:2{% elif effect == ^Breath^ %}^effect^:3{% elif effect == ^Flash^ %}^effect^:4{% elif effect == ^On/Off Gradual^ %}^effect^:5{% elif effect == ^Red/Green Change^ %}^effect^:6{% else %}^effect^:0{% endif %}{% else %}^effect^:0{% endif %}}"
        payload[
            KEY_STATE_TEMPLATE
        ] = "{% if value_json.ison == true and value_json.mode == ^color^ %}on{% else %}off{% endif %}"
        payload[
            KEY_EFFECT_TEMPLATE
        ] = "{% if value_json.effect == 1 %}Meteor Shower{% elif value_json.effect == 2 %}Gradual Change{% elif value_json.effect == 3 %}Breath{% elif value_json.effect == 4 %}Flash{% elif value_json.effect == 5 %}On/Off Gradual{% elif value_json.effect == 6 %}Red/Green Change{% else %}Off{% endif %}"
    else:
        payload = ""
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(
        config_topic, str(payload).replace("'", '"').replace("^", "'"), retain, qos
    )

    # color light's binary sensors
    for bin_sensor_id in range(len(lights_bin_sensors)):
        sensor_name = (
            f"{device_name} {lights_bin_sensors[bin_sensor_id].title()} {light_id}"
        )
        config_topic = f"{disc_prefix}/binary_sensor/{dev_id}-color-{lights_bin_sensors[bin_sensor_id]}-{light_id}/config"
        unique_id = (
            f"{dev_id}-color-{lights_bin_sensors[bin_sensor_id]}-{light_id}".lower()
        )
        if lights_bin_sensors[bin_sensor_id] == SENSOR_INPUT:
            state_topic = f"~{lights_bin_sensors[bin_sensor_id]}/{light_id}"
        else:
            state_topic = f"~color/{light_id}/status"
        if config_mode == LIGHT_RGBW:
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
            if lights_bin_sensors_classes and lights_bin_sensors_classes[bin_sensor_id]:
                payload[KEY_DEVICE_CLASS] = lights_bin_sensors_classes[bin_sensor_id]
            if lights_bin_sensors_tpls and lights_bin_sensors_tpls[bin_sensor_id]:
                payload[KEY_VALUE_TEMPLATE] = lights_bin_sensors_tpls[bin_sensor_id]
            else:
                payload[KEY_PAYLOAD_ON] = lights_bin_sensors_pl[bin_sensor_id][VALUE_ON]
                payload[KEY_PAYLOAD_OFF] = lights_bin_sensors_pl[bin_sensor_id][
                    VALUE_OFF
                ]
        else:
            payload = ""
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # color light's sensors
    for sensor_id in range(len(lights_sensors)):
        device_config = get_device_config(dev_id)
        force_update = False
        if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
            force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
        unique_id = f"{dev_id}-color-{lights_sensors[sensor_id]}-{light_id}".lower()
        config_topic = f"{disc_prefix}/sensor/{dev_id}-color-{lights_sensors[sensor_id]}-{light_id}/config"
        sensor_name = f"{device_name} {lights_sensors[sensor_id].title()} {light_id}"
        state_topic = f"~color/{light_id}/status"
        if config_mode == LIGHT_RGBW:
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
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# white lights
for light_id in range(white_lights):
    device_config = get_device_config(dev_id)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    if device_config.get(f"light-{light_id}-name"):
        light_name = device_config[f"light-{light_id}-name"]
    else:
        light_name = f"{device_name} Light {light_id}"
    default_topic = f"shellies/{dev_id}/"
    if model in [
        MODEL_SHELLYDIMMER,
        MODEL_SHELLYDIMMER2,
        MODEL_SHELLYDUO,
        MODEL_SHELLYVINTAGE,
    ]:
        state_topic = f"~light/{light_id}/status"
        command_topic = f"~light/{light_id}/set"
        unique_id = f"{dev_id}-light-{light_id}".lower()
        config_topic = f"{disc_prefix}/light/{dev_id}-{light_id}/config"
    else:
        state_topic = f"~white/{light_id}/status"
        command_topic = f"~white/{light_id}/set"
        unique_id = f"{dev_id}-light-white-{light_id}".lower()
        config_topic = f"{disc_prefix}/light/{dev_id}-white-{light_id}/config"
    availability_topic = "~online"
    config_mode = LIGHT_RGBW
    if device_config.get(CONF_MODE):
        config_mode = device_config[CONF_MODE]

    payload = {
        KEY_SCHEMA: ATTR_TEMPLATE,
        KEY_NAME: light_name,
        KEY_COMMAND_TOPIC: command_topic,
        KEY_STATE_TOPIC: state_topic,
        KEY_AVAILABILITY_TOPIC: availability_topic,
        KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_COMMAND_OFF_TEMPLATE: "{^turn^:^off^}",
        KEY_STATE_TEMPLATE: "{% if value_json.ison %}on{% else %}off{% endif %}",
        KEY_BRIGHTNESS_TEMPLATE: "{{value_json.brightness|float|multiply(2.55)|round}}",
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
    if config_mode == LIGHT_WHITE and model == MODEL_SHELLYRGBW2:
        payload[
            KEY_COMMAND_ON_TEMPLATE
        ] = "{^turn^:^on^{% if brightness is defined %},^brightness^:{{brightness|float|multiply(0.3922)|round}}{% endif %}{% if white_value is defined %},^white^:{{white_value}}{% endif %}{% if effect is defined %},^effect^:{{effect}}{% endif %}}"
    elif model in [MODEL_SHELLYDIMMER, MODEL_SHELLYDIMMER2]:
        payload[
            KEY_COMMAND_ON_TEMPLATE
        ] = "{^turn^:^on^{% if brightness is defined %},^brightness^:{{brightness|float|multiply(0.3922)|round}}{% endif %}}"
    elif model == MODEL_SHELLYDUO:
        payload[
            KEY_COMMAND_ON_TEMPLATE
        ] = "{^turn^:^on^{% if brightness is defined %},^brightness^:{{brightness|float|multiply(0.3922)|round}}{% endif %}{% if color_temp is defined %},^temp^:{{(1000000/(color_temp|int))|round(0,^floor^)}}{% endif %}}"
        payload[
            KEY_COLOR_TEMP_TEMPLATE
        ] = "{{((1000000/(value_json.temp|int))|round(0,^floor^))}}"
        payload[KEY_MAX_MIREDS] = 370
        payload[KEY_MIN_MIREDS] = 153
    elif model == MODEL_SHELLYVINTAGE:
        payload[
            KEY_COMMAND_ON_TEMPLATE
        ] = "{^turn^:^on^{% if brightness is defined %},^brightness^:{{brightness|float|multiply(0.3922)|round}}{% endif %}}"
    else:
        payload = ""
    if dev_id.lower() in ignored:
        payload = ""
    mqtt_publish(
        config_topic, str(payload).replace("'", '"').replace("^", "'"), retain, qos
    )

    # white light's binary sensors
    for bin_sensor_id in range(len(lights_bin_sensors)):
        if (
            lights_bin_sensors[bin_sensor_id] == SENSOR_INPUT and light_id == 0
        ) or lights_bin_sensors[bin_sensor_id] != SENSOR_INPUT:
            unique_id = (
                f"{dev_id}-white-{lights_bin_sensors[bin_sensor_id]}-{light_id}".lower()
            )
            config_topic = f"{disc_prefix}/binary_sensor/{dev_id}-white-{lights_bin_sensors[bin_sensor_id]}-{light_id}/config"
            if lights_bin_sensors[bin_sensor_id] == SENSOR_INPUT:
                state_topic = f"~{lights_bin_sensors[bin_sensor_id]}/{light_id}"
            else:
                state_topic = f"~white/{light_id}/status"
            sensor_name = (
                f"{device_name} {lights_bin_sensors[bin_sensor_id].title()} {light_id}"
            )
            if config_mode != LIGHT_RGBW:
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
                if (
                    lights_bin_sensors_classes
                    and lights_bin_sensors_classes[bin_sensor_id]
                ):
                    payload[KEY_DEVICE_CLASS] = lights_bin_sensors_classes[
                        bin_sensor_id
                    ]
                if lights_bin_sensors_tpls and lights_bin_sensors_tpls[bin_sensor_id]:
                    payload[KEY_VALUE_TEMPLATE] = lights_bin_sensors_tpls[bin_sensor_id]
                else:
                    payload[KEY_PAYLOAD_ON] = lights_bin_sensors_pl[bin_sensor_id][
                        VALUE_ON
                    ]
                    payload[KEY_PAYLOAD_OFF] = lights_bin_sensors_pl[bin_sensor_id][
                        VALUE_OFF
                    ]

            else:
                payload = ""
            if dev_id.lower() in ignored:
                payload = ""
            mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

    # white light's sensors
    for sensor_id in range(len(lights_sensors)):
        device_config = get_device_config(dev_id)
        force_update = False
        if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
            force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
        unique_id = f"{dev_id}-white-{lights_sensors[sensor_id]}-{light_id}".lower()
        config_topic = f"{disc_prefix}/sensor/{dev_id}-white-{lights_sensors[sensor_id]}-{light_id}/config"
        sensor_name = f"{device_name} {lights_sensors[sensor_id].title()} {light_id}"
        if model in [
            MODEL_SHELLYDIMMER,
            MODEL_SHELLYDIMMER2,
            MODEL_SHELLYDUO,
            MODEL_SHELLYVINTAGE,
        ]:
            state_topic = f"~light/{light_id}/{lights_sensors[sensor_id]}"
        else:
            state_topic = f"~white/{light_id}/status"
        if model in [
            MODEL_SHELLYDIMMER,
            MODEL_SHELLYDIMMER2,
            MODEL_SHELLYDUO,
            MODEL_SHELLYVINTAGE,
        ]:
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
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)

# meters
for meter_id in range(meters):
    device_config = get_device_config(dev_id)
    force_update = False
    if isinstance(device_config.get(CONF_FORCE_UPDATE_SENSORS), bool):
        force_update = device_config.get(CONF_FORCE_UPDATE_SENSORS)
    device_name = f"{model} {dev_id.split('-')[-1]}"
    default_topic = f"shellies/{dev_id}/"
    availability_topic = "~online"
    for sensor_id in range(len(meters_sensors)):
        unique_id = f"{dev_id}-emeter-{meters_sensors[sensor_id]}-{meter_id}".lower()
        config_topic = f"{disc_prefix}/sensor/{dev_id}-emeter-{meters_sensors[sensor_id]}-{meter_id}/config"
        sensor_name = (
            f"{device_name} Meter {meters_sensors[sensor_id].title()} {meter_id}"
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
        if meters_sensors_classes and meters_sensors_classes[sensor_id]:
            payload[KEY_DEVICE_CLASS] = meters_sensors_classes[sensor_id]
        if dev_id.lower() in ignored:
            payload = ""
        mqtt_publish(config_topic, str(payload).replace("'", '"'), retain, qos)
