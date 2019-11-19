"""
This script adds MQTT discovery support for Shellies devices.
"""
ATTR_DEVELOP = "develop"

ATTR_ID = "id"
ATTR_MAC = "mac"
ATTR_FW_VER = "fw_ver"
ATTR_DISCOVERY_PREFIX = "discovery_prefix"
ATTR_TEMP_UNIT = "temp_unit"
ATTR_QOS = "qos"

ATTR_TPL_TEMPERATURE = "{{ value | float | round(1) }}"
ATTR_TPL_HUMIDITY = "{{ value | float | round(1) }}"
ATTR_TPL_LUX = "{{ value | float | round }}"
ATTR_TPL_POWER = "{{ value | float | round(1) }}"
ATTR_TPL_REACTIVE_POWER = "{{ value | float | round(1) }}"
ATTR_TPL_VOLTAGE = "{{ value | float | round(1) }}"
ATTR_TPL_ENERGY = "{{ (value | float / 60 / 1000) | round(2) }}"
ATTR_TPL_BATTERY = "{{ value | float | round }}"
ATTR_TPL_OVERPOWER = "{% if value_json.overpower == true %}ON{% else %}OFF{% endif %}"

ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_MODEL_SHELLY1 = "Shelly1"
ATTR_MODEL_SHELLY1PM = "Shelly1PM"
ATTR_MODEL_SHELLY2 = "Shelly2"
ATTR_MODEL_SHELLY25 = "Shelly2.5"
ATTR_MODEL_SHELLYPLUG = "Shelly Plug"
ATTR_MODEL_SHELLYPLUG_S = "Shelly Plug S"
ATTR_MODEL_SHELLY4PRO = "Shelly4Pro"
ATTR_MODEL_SHELLYHT = "Shelly H&T"
ATTR_MODEL_SHELLYSMOKE = "Shelly Smoke"
ATTR_MODEL_SHELLYSENSE = "Shelly Sense"
ATTR_MODEL_SHELLYRGBW2 = "Shelly RGBW2"
ATTR_MODEL_SHELLYBULB = "Shelly Bulb"
ATTR_MODEL_SHELLYEM = "ShellyEM"
ATTR_MODEL_SHELLYFLOOD = "Shelly Flood"
ATTR_MODEL_SHELLYDIMMER = "Shelly Dimmer"

ATTR_SHELLY = "Shelly"
ATTR_TEMPERATURE = "temperature"
ATTR_HUMIDITY = "humidity"
ATTR_BATTERY = "battery"
ATTR_LUX = "lux"
ATTR_ILLUMINANCE = "illuminance"
ATTR_POWER = "power"
ATTR_REACTIVE_POWER = "reactive_power"
ATTR_VOLTAGE = "voltage"
ATTR_ENERGY = "energy"
ATTR_RETURNED_ENERGY = "returned_energy"
ATTR_SWITCH = "switch"
ATTR_LIGHT = "light"
ATTR_RGBW = "rgbw"
ATTR_WHITE = "white"
ATTR_FAN = "fan"
ATTR_SMOKE = "smoke"
ATTR_FLOOD = "flood"
ATTR_MOISTURE = "moisture"
ATTR_MOTION = "motion"
ATTR_CHARGER = "charger"
ATTR_INPUT = "input"
ATTR_LONGPUSH = "longpush"
ATTR_OVERTEMPERATURE = "overtemperature"
ATTR_OVERPOWER = "overpower"
ATTR_HEAT = "heat"
ATTR_COVER = "cover"
ATTR_UNIT_W = "W"
ATTR_UNIT_KWH = "kWh"
ATTR_UNIT_V = "V"
ATTR_UNIT_VAR = "VAR"
ATTR_UNIT_PERCENT = "%"
ATTR_UNIT_LUX = "lx"
ATTR_UNIT_CELSIUS = "°C"
ATTR_UNIT_FARENHEIT = "°F"
ATTR_ON = "on"
ATTR_OFF = "off"
ATTR_TRUE_FALSE_PL = {ATTR_ON: "true", ATTR_OFF: "false"}
ATTR_1_0_PL = {ATTR_ON: "1", ATTR_OFF: "0"}
ATTR_AC_POWER = "ac_power"

DEFAULT_DISC_PREFIX = "homeassistant"

expire_after = "43200"

retain = True
qos = 0
roller_mode = False

id = data.get(ATTR_ID)
mac = data.get(ATTR_MAC)
fw_ver = data.get(ATTR_FW_VER)

if not id or not mac or not fw_ver:
    logger.error("Wrong arguments! Please read the script documentation.")
else:
    try:
        if data.get(ATTR_QOS):
            if int(data.get(ATTR_QOS)) in [0, 1, 2]:
                qos = int(data.get(ATTR_QOS))
            else:
                raise ValueError
    except ValueError:
        logger.error(
            "Wrong qos argument! Should be 0, 1 or 2. The default value 0 was used."
        )

    temp_unit = ATTR_UNIT_CELSIUS
    if data.get(ATTR_TEMP_UNIT, "C") == "F":
        temp_unit = ATTR_UNIT_FARENHEIT

    disc_prefix = data.get(ATTR_DISCOVERY_PREFIX, DEFAULT_DISC_PREFIX)

    develop = data.get(ATTR_DEVELOP, False)
    if develop:
        disc_prefix = "develop"
        retain = False
        logger.error("DEVELOP MODE !!!")

    if id == "" or mac == "":
        logger.error("Expected id and mac as arguments.")
    else:
        relays = 0
        rollers = 0
        meters = 0
        relay_components = [ATTR_SWITCH, ATTR_LIGHT, ATTR_FAN]
        config_component = ATTR_SWITCH
        config_light = ATTR_RGBW
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
        battery_powered = False

        if id[:-7] == "shelly1":
            model = ATTR_MODEL_SHELLY1
            relays = 1
            relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
            relays_bin_sensors_pl = [ATTR_1_0_PL, ATTR_1_0_PL]

        if id[:-7] == "shelly1pm":
            model = ATTR_MODEL_SHELLY1PM
            relays = 1
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]
            relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
            relays_bin_sensors_pl = [ATTR_1_0_PL, ATTR_1_0_PL]
            sensors = [ATTR_TEMPERATURE]
            sensors_classes = sensors
            sensors_units = [temp_unit]
            sensors_tpls = [ATTR_TPL_TEMPERATURE]
            bin_sensors = [ATTR_OVERTEMPERATURE]
            bin_sensors_classes = [ATTR_HEAT]
            bin_sensors_pl = [ATTR_1_0_PL]

        if id[:-7] == "shellyswitch":
            model = ATTR_MODEL_SHELLY2
            relays = 2
            rollers = 1
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]
            relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
            relays_bin_sensors_pl = [ATTR_1_0_PL, ATTR_1_0_PL]

        if id[:-7] == "shellyswitch25":
            model = ATTR_MODEL_SHELLY25
            relays = 2
            rollers = 1
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]
            relays_bin_sensors = [ATTR_INPUT, ATTR_LONGPUSH]
            relays_bin_sensors_pl = [ATTR_1_0_PL, ATTR_1_0_PL]
            sensors = [ATTR_TEMPERATURE]
            sensors_classes = sensors
            sensors_units = [temp_unit]
            sensors_tpls = [ATTR_TPL_TEMPERATURE]
            bin_sensors = [ATTR_OVERTEMPERATURE]
            bin_sensors_classes = [ATTR_HEAT]
            bin_sensors_pl = [ATTR_1_0_PL]

        if id[:-7] == "shellyplug":
            model = ATTR_MODEL_SHELLYPLUG
            relays = 1
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]

        if id[:-7] == "shellyplug-s":
            model = ATTR_MODEL_SHELLYPLUG_S
            relays = 1
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]
            sensors = [ATTR_TEMPERATURE]
            sensors_classes = sensors
            sensors_units = [temp_unit]
            sensors_tpls = [ATTR_TPL_TEMPERATURE]
            bin_sensors = [ATTR_OVERTEMPERATURE]
            bin_sensors_classes = [ATTR_HEAT]
            bin_sensors_pl = [ATTR_1_0_PL]

        if id[:-7] == "shelly4pro":
            model = ATTR_MODEL_SHELLY4PRO
            relays = 4
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]

        if id[:-7] == "shellyht":
            model = ATTR_MODEL_SHELLYHT
            sensors = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_BATTERY]
            sensors_classes = sensors
            sensors_units = [temp_unit, ATTR_UNIT_PERCENT, ATTR_UNIT_PERCENT]
            sensors_tpls = [
                ATTR_TPL_TEMPERATURE,
                ATTR_TPL_HUMIDITY,
                ATTR_TPL_BATTERY,
            ]
            battery_powered = True

        if id[:-7] == "shellysmoke":
            model = ATTR_MODEL_SHELLYSMOKE
            sensors = [ATTR_TEMPERATURE, ATTR_BATTERY]
            sensors_classes = sensors
            sensors_units = [temp_unit, ATTR_UNIT_PERCENT]
            sensors_tpls = [ATTR_TPL_TEMPERATURE, ATTR_TPL_BATTERY]
            bin_sensors = [ATTR_SMOKE]
            bin_sensors_classes = bin_sensors
            bin_sensors_pl = [ATTR_TRUE_FALSE_PL]
            battery_powered = True

        if id[:-7] == "shellysense":
            model = ATTR_MODEL_SHELLYSENSE
            sensors = [ATTR_TEMPERATURE, ATTR_HUMIDITY, ATTR_LUX, ATTR_BATTERY]
            sensors_classes = [
                ATTR_TEMPERATURE,
                ATTR_HUMIDITY,
                ATTR_ILLUMINANCE,
                ATTR_BATTERY,
            ]
            sensors_units = [temp_unit, ATTR_UNIT_PERCENT, ATTR_UNIT_LUX, ATTR_UNIT_PERCENT]
            sensors_tpls = [
                ATTR_TPL_TEMPERATURE,
                ATTR_TPL_HUMIDITY,
                ATTR_TPL_LUX,
                ATTR_TPL_BATTERY,
            ]
            bin_sensors = [ATTR_MOTION, ATTR_CHARGER]
            bin_sensors_classes = [ATTR_MOTION, ATTR_POWER]
            bin_sensors_pl = [ATTR_TRUE_FALSE_PL, ATTR_TRUE_FALSE_PL]
            battery_powered = True

        if id[:-7] == "shellyrgbw2":
            model = ATTR_MODEL_SHELLYRGBW2
            rgbw_lights = 1
            white_lights = 4
            lights_sensors = [ATTR_POWER]
            lights_sensors_classes = [ATTR_POWER]
            lights_sensors_units = [ATTR_UNIT_W]
            lights_sensors_tpls = ["{{ value_json.power | float | round(1) }}"]
            lights_bin_sensors = [ATTR_OVERPOWER]
            lights_bin_sensors_classes = [ATTR_POWER]
            lights_bin_sensors_tpls = [ATTR_TPL_OVERPOWER]
            lights_bin_sensors_pl = [ATTR_TRUE_FALSE_PL]

        if id[:-7] == "shellydimmer":
            model = ATTR_MODEL_SHELLYDIMMER
            white_lights = 1
            sensors = [ATTR_TEMPERATURE]
            sensors_classes = sensors
            sensors_units = [temp_unit]
            sensors_tpls = [ATTR_TPL_TEMPERATURE]
            bin_sensors = [ATTR_OVERTEMPERATURE]
            bin_sensors_classes = [ATTR_HEAT]
            bin_sensors_pl = [ATTR_1_0_PL]

        if id[:-7] == "shellybulb":
            model = ATTR_MODEL_SHELLYBULB
            rgbw_lights = 1

        if id[:-7] == "shellyem":
            model = ATTR_MODEL_SHELLYEM
            relays = 1
            relays_sensors = [ATTR_POWER, ATTR_ENERGY]
            relays_sensors_units = [ATTR_UNIT_W, ATTR_UNIT_KWH]
            relays_sensors_classes = [ATTR_POWER, ATTR_POWER]
            relays_sensors_tpls = [ATTR_TPL_POWER, ATTR_TPL_ENERGY]
            meters = 2
            meters_sensors = [
                ATTR_POWER,
                ATTR_REACTIVE_POWER,
                ATTR_VOLTAGE,
                ATTR_ENERGY,
                ATTR_RETURNED_ENERGY,
            ]
            meters_sensors_units = [
                ATTR_UNIT_W,
                ATTR_UNIT_VAR,
                ATTR_UNIT_V,
                ATTR_UNIT_KWH,
                ATTR_UNIT_KWH,
            ]
            meters_sensors_classes = [ATTR_POWER, None, None, ATTR_POWER, ATTR_POWER]
            meters_sensors_tpls = [
                ATTR_TPL_POWER,
                ATTR_TPL_REACTIVE_POWER,
                ATTR_TPL_VOLTAGE,
                ATTR_TPL_ENERGY,
                ATTR_TPL_ENERGY,
            ]

        if id[:-7] == "shellyflood":
            model = ATTR_MODEL_SHELLYFLOOD
            sensors = [ATTR_TEMPERATURE, ATTR_BATTERY]
            sensors_classes = sensors
            sensors_units = [temp_unit, ATTR_UNIT_PERCENT]
            sensors_tpls = [ATTR_TPL_TEMPERATURE, ATTR_TPL_BATTERY]
            bin_sensors = [ATTR_FLOOD]
            bin_sensors_classes = [ATTR_MOISTURE]
            bin_sensors_pl = [ATTR_TRUE_FALSE_PL]
            battery_powered = True

        # rollers
        for roller_id in range(0, rollers):
            device_name = "{} {}".format(model, id.split("-")[-1])
            roller_name = "{} Roller {}".format(device_name, roller_id)
            default_topic = "shellies/{}/".format(id)
            state_topic = "~roller/{}".format(roller_id)
            command_topic = "{}/command".format(state_topic)
            position_topic = "{}/pos".format(state_topic)
            set_position_topic = "{}/command/pos".format(state_topic)
            availability_topic = "~online"
            unique_id = "{}-roller-{}".format(id, roller_id)
            if data.get(id):
                config_component = data.get(id)
            elif data.get(id.lower()):
                config_component = data.get(id.lower())
            component = ATTR_COVER
            config_topic = "{}/{}/{}-roller-{}/config".format(
                disc_prefix, component, id, roller_id
            )
            if config_component == component:
                roller_mode = True
                payload = (
                    '{"name":"' + roller_name + '",'
                    '"cmd_t":"' + command_topic + '",'
                    '"pos_t":"' + position_topic + '",'
                    '"set_pos_t":"' + set_position_topic + '",'
                    '"pl_open":"open",'
                    '"pl_cls":"close",'
                    '"pl_stop":"stop",'
                    '"opt":"false",'
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
            service_data = {
                "topic": config_topic,
                "payload": payload,
                "retain": retain,
                "qos": qos,
            }
            hass.services.call("mqtt", "publish", service_data, False)

        # relays
        for relay_id in range(0, relays):
            device_name = "{} {}".format(model, id.split("-")[-1])
            relay_name = "{} Relay {}".format(device_name, relay_id)
            default_topic = "shellies/{}/".format(id)
            state_topic = "~relay/{}".format(relay_id)
            command_topic = "{}/command".format(state_topic)
            availability_topic = "~online"
            unique_id = "{}-relay-{}".format(id, relay_id)
            if data.get(unique_id):
                config_component = data.get(unique_id)
            elif data.get(unique_id.lower()):
                config_component = data.get(unique_id.lower())
            for component in relay_components:
                config_topic = "{}/{}/{}-relay-{}/config".format(
                    disc_prefix, component, id, relay_id
                )
                if component == config_component and not roller_mode:
                    payload = (
                        '{"name":"' + relay_name + '",'
                        '"cmd_t":"' + command_topic + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"pl_off":"off",'
                        '"pl_on":"on",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

            # relay's sensors
            if relay_id == relays - 1:
                for sensor_id in range(0, len(relays_sensors)):
                    unique_id = "{}-relay-{}".format(id, relays_sensors[sensor_id])
                    config_topic = "{}/sensor/{}-{}/config".format(
                        disc_prefix, id, relays_sensors[sensor_id]
                    )
                    sensor_name = "{} {}".format(
                        device_name, relays_sensors[sensor_id].capitalize()
                    )
                    state_topic = "~relay/{}".format(relays_sensors[sensor_id])
                    if model == ATTR_MODEL_SHELLY2 or roller_mode:
                        payload = (
                            '{"name":"' + sensor_name + '",'
                            '"stat_t":"' + state_topic + '",'
                            '"unit_of_meas":"' + relays_sensors_units[sensor_id] + '",'
                            '"dev_cla":"' + relays_sensors_classes[sensor_id] + '",'
                            '"val_tpl":"' + relays_sensors_tpls[sensor_id] + '",'
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
                    service_data = {
                        "topic": config_topic,
                        "payload": payload,
                        "retain": retain,
                        "qos": qos,
                    }
                    hass.services.call("mqtt", "publish", service_data, False)

            # relay's sensors
            for sensor_id in range(0, len(relays_sensors)):
                unique_id = "{}-relay-{}-{}".format(id, relays_sensors[sensor_id], relay_id)
                config_topic = "{}/sensor/{}-{}-{}/config".format(
                    disc_prefix, id, relays_sensors[sensor_id], relay_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, relays_sensors[sensor_id].capitalize(), relay_id
                )
                state_topic = "~relay/{}/{}".format(relay_id, relays_sensors[sensor_id])
                if model != ATTR_MODEL_SHELLY2 and not roller_mode:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"unit_of_meas":"' + relays_sensors_units[sensor_id] + '",'
                        '"dev_cla":"' + relays_sensors_classes[sensor_id] + '",'
                        '"val_tpl":"' + relays_sensors_tpls[sensor_id] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

            # relay's binary sensors
            for bin_sensor_id in range(0, len(relays_bin_sensors)):
                unique_id = "{}-{}-{}".format(
                    id, relays_bin_sensors[bin_sensor_id], relay_id
                )
                config_topic = "{}/binary_sensor/{}-{}-{}/config".format(
                    disc_prefix, id, relays_bin_sensors[bin_sensor_id], relay_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, relays_bin_sensors[bin_sensor_id].capitalize(), relay_id
                )
                state_topic = "~{}/{}".format(relays_bin_sensors[bin_sensor_id], relay_id)
                if not roller_mode:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"pl_on":"' + relays_bin_sensors_pl[bin_sensor_id][ATTR_ON] + '",'
                        '"pl_off":"' + relays_bin_sensors_pl[bin_sensor_id][ATTR_OFF] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

        # sensors
        for sensor_id in range(0, len(sensors)):
            device_name = "{} {}".format(model, id.split("-")[-1])
            unique_id = "{}-{}".format(id, sensors[sensor_id])
            config_topic = "{}/sensor/{}-{}/config".format(
                disc_prefix, id, sensors[sensor_id]
            )
            default_topic = "shellies/{}/".format(id)
            availability_topic = "~online"
            sensor_name = "{} {}".format(device_name, sensors[sensor_id].capitalize())
            if relays > 0 or white_lights > 0:
                state_topic = "~{}".format(sensors[sensor_id])
            else:
                state_topic = "~sensor/{}".format(sensors[sensor_id])
            if data.get(id) or data.get(id.lower()):
                if (data.get(id) or data.get(id.lower())) == ATTR_AC_POWER:
                    expire_after = "7200"
            if battery_powered:
                payload = (
                    '{"name":"' + sensor_name + '",'
                    '"stat_t":"' + state_topic + '",'
                    '"unit_of_meas":"' + sensors_units[sensor_id] + '",'
                    '"dev_cla":"' + sensors_classes[sensor_id] + '",'
                    '"val_tpl":"' + sensors_tpls[sensor_id] + '",'
                    '"exp_aft":"' + expire_after + '",'
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
                payload = (
                    '{"name":"' + sensor_name + '",'
                    '"stat_t":"' + state_topic + '",'
                    '"unit_of_meas":"' + sensors_units[sensor_id] + '",'
                    '"dev_cla":"' + sensors_classes[sensor_id] + '",'
                    '"val_tpl":"' + sensors_tpls[sensor_id] + '",'
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
            service_data = {
                "topic": config_topic,
                "payload": payload,
                "retain": retain,
                "qos": qos,
            }
            hass.services.call("mqtt", "publish", service_data, False)

        # binary sensors
        for bin_sensor_id in range(0, len(bin_sensors)):
            device_name = "{} {}".format(model, id.split("-")[-1])
            unique_id = "{}-{}".format(id, bin_sensors[bin_sensor_id])
            config_topic = "{}/binary_sensor/{}-{}/config".format(
                disc_prefix, id, bin_sensors[bin_sensor_id]
            )
            default_topic = "shellies/{}/".format(id)
            availability_topic = "~online"
            sensor_name = "{} {}".format(
                device_name, bin_sensors[bin_sensor_id].capitalize()
            )
            if relays > 0 or white_lights > 0:
                state_topic = "~{}".format(bin_sensors[bin_sensor_id])
            else:
                state_topic = "~sensor/{}".format(bin_sensors[bin_sensor_id])
            if battery_powered:
                payload = (
                    '{"name":"' + sensor_name + '",'
                    '"stat_t":"' + state_topic + '",'
                    '"pl_on":"' + bin_sensors_pl[bin_sensor_id][ATTR_ON] + '",'
                    '"pl_off":"' + bin_sensors_pl[bin_sensor_id][ATTR_OFF] + '",'
                    '"dev_cla":"' + bin_sensors_classes[bin_sensor_id] + '",'
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
                payload = (
                    '{"name":"' + sensor_name + '",'
                    '"stat_t":"' + state_topic + '",'
                    '"pl_on":"' + bin_sensors_pl[bin_sensor_id][ATTR_ON] + '",'
                    '"pl_off":"' + bin_sensors_pl[bin_sensor_id][ATTR_OFF] + '",'
                    '"avty_t":"' + availability_topic + '",'
                    '"pl_avail":"true",'
                    '"pl_not_avail":"false",'
                    '"dev_cla":"' + bin_sensors_classes[bin_sensor_id] + '",'
                    '"uniq_id":"' + unique_id + '",'
                    '"qos":"' + str(qos) + '",'
                    '"dev": {"ids": ["' + mac + '"],'
                    '"name":"' + device_name + '",'
                    '"mdl":"' + model + '",'
                    '"sw":"' + fw_ver + '",'
                    '"mf":"' + ATTR_MANUFACTURER + '"},'
                    '"~":"' + default_topic + '"}'
                )
            service_data = {
                "topic": config_topic,
                "payload": payload,
                "retain": retain,
                "qos": qos,
            }
            hass.services.call("mqtt", "publish", service_data, False)

        # color lights
        for light_id in range(0, rgbw_lights):
            device_name = "{} {}".format(model, id.split("-")[-1])
            light_name = "{} Light {}".format(device_name, light_id)
            default_topic = "shellies/{}/".format(id)
            state_topic = "~color/{}/status".format(light_id)
            command_topic = "~color/{}/set".format(light_id)
            availability_topic = "~online"
            unique_id = "{}-light-{}".format(id, light_id)
            config_topic = "{}/light/{}-{}/config".format(disc_prefix, id, light_id)
            if data.get(id):
                config_light = data.get(id)
            elif data.get(id.lower()):
                config_light = data.get(id.lower())
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
                    '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"gain\\":{{ brightness | float | multiply(0.3922) | round(0) }}{% endif %}{% if red is defined and green is defined and blue is defined %},\\"red\\":{{ red }},\\"green\\":{{ green }},\\"blue\\":{{ blue }}{% endif %}{% if white_value is defined %},\\"white\\":{{ white_value }}{% endif %}{% if effect is defined %}{% if effect == \\"Meteor Shower\\" %}\\"effect\\":1{% elif effect == \\"Gradual Change\\" %}\\"effect\\":2{% elif effect == \\"Breath\\" %}\\"effect\\":3{% elif effect == \\"Flash\\" %}\\"effect\\":4{% elif effect == \\"On/Off Gradual\\" %}\\"effect\\":5{% elif effect == \\"Red/Green Change\\" %}\\"effect\\":6{% else %}\\"effect\\":0{% endif %}{% else %}\\"effect\\":0{% endif %}}",'
                    '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
                    '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
                    '"bri_tpl":"{{ value_json.gain | float | multiply(2.55) | round(0) }}",'
                    '"r_tpl":"{{ value_json.red }}",'
                    '"g_tpl":"{{ value_json.green }}",'
                    '"b_tpl":"{{ value_json.blue }}",'
                    '"whit_val_tpl":"{{ value_json.white }}",'
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
                    '"cmd_on_tpl":"{\\"turn\\":\\"on\\",\\"mode\\":\\"color\\",{% if red is defined and green is defined and blue is defined %}\\"red\\":{{ red }},\\"green\\":{{ green }},\\"blue\\":{{ blue }},{% endif %}{% if white_value is defined %}\\"white\\":{{ white_value }},{% endif %}{% if brightness is defined %}\\"gain\\":{{ brightness | float | multiply(0.3922) | round(0) }},{% endif %}{% if effect is defined %}{% if effect == \\"Meteor Shower\\" %}\\"effect\\":1{% elif effect == \\"Gradual Change\\" %}\\"effect\\":2{% elif effect == \\"Breath\\" %}\\"effect\\":3{% elif effect == \\"Flash\\" %}\\"effect\\":4{% elif effect == \\"On/Off Gradual\\" %}\\"effect\\":5{% elif effect == \\"Red/Green Change\\" %}\\"effect\\":6{% else %}\\"effect\\":0{% endif %}{% else %}\\"effect\\":0{% endif %}}",'
                    '"cmd_off_tpl":"{\\"turn\\":\\"off\\",\\"mode\\":\\"color\\",\\"effect\\": 0}",'
                    '"stat_tpl":"{% if value_json.ison == true and value_json.mode == \\"color\\" %}on{% else %}off{% endif %}",'
                    '"bri_tpl":"{{ value_json.gain | float | multiply(2.55) | round(0) }}",'
                    '"r_tpl":"{{ value_json.red }}",'
                    '"g_tpl":"{{ value_json.green }}",'
                    '"b_tpl":"{{ value_json.blue }}",'
                    '"whit_val_tpl":"{{ value_json.white }}",'
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
            service_data = {
                "topic": config_topic,
                "payload": payload,
                "retain": retain,
                "qos": qos,
            }
            hass.services.call("mqtt", "publish", service_data, False)

            # color light's binary sensors
            for bin_sensor_id in range(0, len(lights_bin_sensors)):
                unique_id = "{}-color-{}-{}".format(
                    id, lights_bin_sensors[bin_sensor_id], light_id
                )
                config_topic = "{}/binary_sensor/{}-color-{}-{}/config".format(
                    disc_prefix, id, lights_bin_sensors[bin_sensor_id], light_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, lights_bin_sensors[bin_sensor_id].capitalize(), light_id
                )
                state_topic = "~color/{}/status".format(light_id)
                if config_light == ATTR_RGBW:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"val_tpl":"' + lights_bin_sensors_tpls[bin_sensor_id] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

            # color light's sensors
            for sensor_id in range(0, len(lights_sensors)):
                unique_id = "{}-color-{}-{}".format(
                    id, lights_sensors[sensor_id], light_id
                )
                config_topic = "{}/sensor/{}-color-{}-{}/config".format(
                    disc_prefix, id, lights_sensors[sensor_id], light_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, lights_sensors[sensor_id].capitalize(), light_id
                )
                state_topic = "~color/{}/status".format(light_id)
                if config_light == ATTR_RGBW:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"unit_of_meas":"' + lights_sensors_units[sensor_id] + '",'
                        '"dev_cla":"' + lights_sensors_classes[sensor_id] + '",'
                        '"val_tpl":"' + lights_sensors_tpls[sensor_id] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

        # white lights
        for light_id in range(0, white_lights):
            device_name = "{} {}".format(model, id.split("-")[-1])
            light_name = "{} Light {}".format(device_name, light_id)
            default_topic = "shellies/{}/".format(id)
            if model == ATTR_MODEL_SHELLYDIMMER:
                state_topic = "~light/{}/status".format(light_id)
                command_topic = "~light/{}/set".format(light_id)
                unique_id = "{}-light-{}".format(id, light_id)
                config_topic = "{}/light/{}-{}/config".format(disc_prefix, id, light_id)
            else:
                state_topic = "~white/{}/status".format(light_id)
                command_topic = "~white/{}/set".format(light_id)
                unique_id = "{}-light-white-{}".format(id, light_id)
                config_topic = "{}/light/{}-white-{}/config".format(disc_prefix, id, light_id)
            availability_topic = "~online"
            if data.get(id):
                config_light = data.get(id)
            elif data.get(id.lower()):
                config_light = data.get(id.lower())
            if config_light == ATTR_WHITE and model == ATTR_MODEL_SHELLYRGBW2:
                payload = (
                    '{"schema":"template",'
                    '"name":"' + light_name + '",'
                    '"cmd_t":"' + command_topic + '",'
                    '"stat_t":"' + state_topic + '",'
                    '"avty_t":"' + availability_topic + '",'
                    '"pl_avail":"true",'
                    '"pl_not_avail":"false",'
                    '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"brightness\\":{{brightness | float | multiply(0.3922) | round(0)}}{% endif %}{% if white_value is defined %},\\"white\\":{{ white_value }}{% endif %}{% if effect is defined %},\\"effect\\":{{ effect }}{% endif %}}",'
                    '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
                    '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
                    '"bri_tpl":"{{ value_json.brightness | float | multiply(2.55) | round(0) }}",'
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
                    '"cmd_on_tpl":"{\\"turn\\":\\"on\\"{% if brightness is defined %},\\"brightness\\":{{brightness | float | multiply(0.3922) | round(0)}}{% endif %}}",'
                    '"cmd_off_tpl":"{\\"turn\\":\\"off\\"}",'
                    '"stat_tpl":"{% if value_json.ison %}on{% else %}off{% endif %}",'
                    '"bri_tpl":"{{ value_json.brightness | float | multiply(2.55) | round(0) }}",'
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
            service_data = {
                "topic": config_topic,
                "payload": payload,
                "retain": retain,
                "qos": qos,
            }
            hass.services.call("mqtt", "publish", service_data, False)

            # white light's binary sensors
            for bin_sensor_id in range(0, len(lights_bin_sensors)):
                unique_id = "{}-white-{}-{}".format(
                    id, lights_bin_sensors[bin_sensor_id], light_id
                )
                config_topic = "{}/binary_sensor/{}-white-{}-{}/config".format(
                    disc_prefix, id, lights_bin_sensors[bin_sensor_id], light_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, lights_bin_sensors[bin_sensor_id].capitalize(), light_id
                )
                state_topic = "~white/{}/status".format(light_id)
                if config_light != ATTR_RGBW:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"val_tpl":"' + lights_bin_sensors_tpls[bin_sensor_id] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

            # white light's sensors
            for sensor_id in range(0, len(lights_sensors)):
                unique_id = "{}-white-{}-{}".format(
                    id, lights_sensors[sensor_id], light_id
                )
                config_topic = "{}/sensor/{}-white-{}-{}/config".format(
                    disc_prefix, id, lights_sensors[sensor_id], light_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, lights_sensors[sensor_id].capitalize(), light_id
                )
                state_topic = "~white/{}/status".format(light_id)
                if config_light != ATTR_RGBW:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"unit_of_meas":"' + lights_sensors_units[sensor_id] + '",'
                        '"dev_cla":"' + lights_sensors_classes[sensor_id] + '",'
                        '"val_tpl":"' + lights_sensors_tpls[sensor_id] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)

        # meters
        for meter_id in range(0, meters):
            device_name = "{} {}".format(model, id.split("-")[-1])
            meter_name = "{} Meter {}".format(device_name, meter_id)
            default_topic = "shellies/{}/".format(id)
            state_topic = "~emeter/{}".format(meter_id)
            availability_topic = "~online"
            for sensor_id in range(0, len(meters_sensors)):
                unique_id = "{}-emeter-{}-{}".format(
                    id, meters_sensors[sensor_id], meter_id
                )
                config_topic = "{}/sensor/{}-{}-{}/config".format(
                    disc_prefix, id, meters_sensors[sensor_id], meter_id
                )
                sensor_name = "{} {} {}".format(
                    device_name, meters_sensors[sensor_id].capitalize(), meter_id
                )
                state_topic = "~emeter/{}/{}".format(meter_id, meters_sensors[sensor_id])
                if meters_sensors_classes[sensor_id]:
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"unit_of_meas":"' + meters_sensors_units[sensor_id] + '",'
                        '"val_tpl":"' + meters_sensors_tpls[sensor_id] + '",'
                        '"dev_cla":"' + meters_sensors_classes[sensor_id] + '",'
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
                    payload = (
                        '{"name":"' + sensor_name + '",'
                        '"stat_t":"' + state_topic + '",'
                        '"unit_of_meas":"' + meters_sensors_units[sensor_id] + '",'
                        '"val_tpl":"' + meters_sensors_tpls[sensor_id] + '",'
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
                service_data = {
                    "topic": config_topic,
                    "payload": payload,
                    "retain": retain,
                    "qos": qos,
                }
                hass.services.call("mqtt", "publish", service_data, False)
