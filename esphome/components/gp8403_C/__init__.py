import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.components import i2c
from esphome.const import CONF_ID, CONF_VOLTAGE

CODEOWNERS = ["@jesserockz"]
DEPENDENCIES = ["i2c"]
MULTI_CONF = True

GP8403_C_ns = cg.esphome_ns.namespace("GP8403_C")
GP8403_C = GP8403_C_ns.class_("GP8403_C", cg.Component, i2c.I2CDevice)

GP8403_CVoltage = GP8403_C_ns.enum("GP8403_CVoltage")

CONF_GP8403_C_ID = "GP8403_C_id"

VOLTAGES = {
    "5V": GP8403_CVoltage.GP8403_C_VOLTAGE_5V,
    "10V": GP8403_CVoltage.GP8403_C_VOLTAGE_10V,
}

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(GP8403_C),
            cv.Required(CONF_VOLTAGE): cv.enum(VOLTAGES, upper=True),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x58))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    cg.add(var.set_voltage(config[CONF_VOLTAGE]))
