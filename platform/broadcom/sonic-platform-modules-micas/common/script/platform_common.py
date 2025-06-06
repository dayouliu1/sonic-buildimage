#!/usr/bin/python3
#
# Copyright (C) 2024 Micas Networks Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__all__ = [
    "BLACKLIST_DRIVERS",
    "DRIVERLISTS",
    "DEVICE",
    "STARTMODULE",
    "MAC_LED_RESET",
    "MAC_DEFAULT_PARAM",
    "DEV_MONITOR_PARAM",
    "SLOT_MONITOR_PARAM",
    "MANUINFO_CONF",
    "REBOOT_CTRL_PARAM",
    "PMON_SYSLOG_STATUS",
    "OPTOE",
    "REBOOT_CAUSE_PARA",
    "UPGRADE_SUMMARY",
    "FW_UPGRADE_STARTED_FLAG",
    "WARM_UPGRADE_PARAM",
    "WARM_UPG_FLAG",
    "WARM_UPGRADE_STARTED_FLAG",
    "PLATFORM_E2_CONF",
    "AIR_FLOW_CONF",
    "AIRFLOW_RESULT_FILE",
    "INIT_PARAM_PRE",
    "INIT_COMMAND_PRE",
    "INIT_PARAM",
    "INIT_COMMAND",
    "SET_MAC_CONF",
    "DRVIER_UPDATE_CONF",
    "MONITOR_TEMP_MIN",
    "MONITOR_K",
    "MONITOR_MAC_IN",
    "MONITOR_DEFAULT_SPEED",
    "MONITOR_MAX_SPEED",
    "MONITOR_MIN_SPEED",
    "MONITOR_MAC_ERROR_SPEED",
    "MONITOR_FAN_TOTAL_NUM",
    "MONITOR_MAC_UP_TEMP",
    "MONITOR_MAC_LOWER_TEMP",
    "MONITOR_MAC_MAX_TEMP",
    "MONITOR_FALL_TEMP",
    "MONITOR_MAC_WARNING_THRESHOLD",
    "MONITOR_OUTTEMP_WARNING_THRESHOLD",
    "MONITOR_BOARDTEMP_WARNING_THRESHOLD",
    "MONITOR_CPUTEMP_WARNING_THRESHOLD",
    "MONITOR_INTEMP_WARNING_THRESHOLD",
    "MONITOR_MAC_CRITICAL_THRESHOLD",
    "MONITOR_OUTTEMP_CRITICAL_THRESHOLD",
    "MONITOR_BOARDTEMP_CRITICAL_THRESHOLD",
    "MONITOR_CPUTEMP_CRITICAL_THRESHOLD",
    "MONITOR_INTEMP_CRITICAL_THRESHOLD",
    "MONITOR_CRITICAL_NUM",
    "MONITOR_SHAKE_TIME",
    "MONITOR_INTERVAL",
    "MONITOR_LED_INTERVAL",
    "MONITOR_PID_FLAG",
    "MONITOR_MAC_SOURCE_SYSFS",
    "MONITOR_MAC_SOURCE_PATH",
    "MONITOR_PID_MODULE",
    "PSU_FAN_FOLLOW",
    "MONITOR_SYS_LED",
    "MONITOR_SYS_FAN_LED",
    "MONITOR_FANS_LED",
    "MONITOR_SYS_PSU_LED",
    "MONITOR_FAN_STATUS",
    "MONITOR_PSU_STATUS",
    "MONITOR_DEV_STATUS",
    "MONITOR_DEV_STATUS_DECODE",
    "DEV_LEDS",
    "fanloc",
    "PLATFORM_POWER_CONF",
    "POWER_CTRL_CONF"
]

# driver blacklist parameter
BLACKLIST_DRIVERS = []

# driver list parameter
DRIVERLISTS = []

# device list parameter
DEVICE = []

# start module parameters
STARTMODULE = {}

# mac led reset parameter
MAC_LED_RESET = {}

# avscontrol parameter
MAC_DEFAULT_PARAM = []

# dev_monitor parameter
DEV_MONITOR_PARAM = {}

# slot_monitor parameter
SLOT_MONITOR_PARAM = {}

# platform_manufacturer parameter
MANUINFO_CONF = {}

# reboot_ctrl parameter
REBOOT_CTRL_PARAM = {}

# pmon_syslog parameter
PMON_SYSLOG_STATUS = {}

# sfp optoe device parameter
OPTOE = []

# reboot_cause parameter
REBOOT_CAUSE_PARA = []

# upgrade parameter
UPGRADE_SUMMARY = {}
FW_UPGRADE_STARTED_FLAG = "/etc/sonic/.doing_fw_upg"

# warm_uprade parameter
WARM_UPGRADE_PARAM = {}
WARM_UPG_FLAG = "/etc/sonic/.warm_upg_flag"
WARM_UPGRADE_STARTED_FLAG = "/etc/sonic/.doing_warm_upg"

# platform_e2 parameter
PLATFORM_E2_CONF = {}

# generate_airflow parameter
AIR_FLOW_CONF = {}
AIRFLOW_RESULT_FILE = "/etc/sonic/.airflow"

# Initialization parameters
INIT_PARAM_PRE = []
INIT_COMMAND_PRE = []
INIT_PARAM = []
INIT_COMMAND = []

# Set eth mac address parameters
SET_MAC_CONF = []

# driver update config
DRVIER_UPDATE_CONF = {}

# platform power config
PLATFORM_POWER_CONF = []

# power control config
POWER_CTRL_CONF = {}

################################ fancontrol parameter###################################
MONITOR_TEMP_MIN = 38
MONITOR_K = 11
MONITOR_MAC_IN = 35
MONITOR_DEFAULT_SPEED = 0x60
MONITOR_MAX_SPEED = 0xFF
MONITOR_MIN_SPEED = 0x60
MONITOR_MAC_ERROR_SPEED = 0XBB
MONITOR_FAN_TOTAL_NUM = 4
MONITOR_MAC_UP_TEMP = 50
MONITOR_MAC_LOWER_TEMP = -50
MONITOR_MAC_MAX_TEMP = 100   #

MONITOR_FALL_TEMP = 4
MONITOR_MAC_WARNING_THRESHOLD = 100
MONITOR_OUTTEMP_WARNING_THRESHOLD = 85
MONITOR_BOARDTEMP_WARNING_THRESHOLD = 85
MONITOR_CPUTEMP_WARNING_THRESHOLD = 85
MONITOR_INTEMP_WARNING_THRESHOLD = 70

MONITOR_MAC_CRITICAL_THRESHOLD = 105
MONITOR_OUTTEMP_CRITICAL_THRESHOLD = 90
MONITOR_BOARDTEMP_CRITICAL_THRESHOLD = 90
MONITOR_CPUTEMP_CRITICAL_THRESHOLD = 100
MONITOR_INTEMP_CRITICAL_THRESHOLD = 80
MONITOR_CRITICAL_NUM = 3
MONITOR_SHAKE_TIME = 20
MONITOR_INTERVAL = 60
MONITOR_LED_INTERVAL = 2
MONITOR_PID_FLAG = 0

MONITOR_MAC_SOURCE_SYSFS = 0
MONITOR_MAC_SOURCE_PATH = None

MONITOR_PID_MODULE = {}

PSU_FAN_FOLLOW = {}

MONITOR_SYS_LED = []
MONITOR_SYS_FAN_LED = []
MONITOR_FANS_LED = []
MONITOR_SYS_PSU_LED = []
MONITOR_FAN_STATUS = []
MONITOR_PSU_STATUS = []
MONITOR_DEV_STATUS = {}
MONITOR_DEV_STATUS_DECODE = {}
DEV_LEDS = {}
fanloc = []
