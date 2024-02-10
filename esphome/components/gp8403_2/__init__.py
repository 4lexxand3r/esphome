import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.components import i2c
from esphome.const import CONF_ID, CONF_VOLTAGE

CODEOWNERS = ["@jesserockz"]
DEPENDENCIES = ["i2c"]
MULTI_CONF = True

gp8403_2_2_ns = cg.esphome_ns.namespace("gp8403_2_2")
gp8403_2_2 = gp8403_2_2_ns.class_("gp8403_2_2", cg.Component, i2c.I2CDevice)

gp8403_2_2Voltage = gp8403_2_2_ns.enum("gp8403_2_2Voltage")

CONF_gp8403_2_2_ID = "gp8403_2_2_id"

VOLTAGES = {
    "5V": gp8403_2_2Voltage.gp8403_2_2_VOLTAGE_5V,
    "10V": gp8403_2_2Voltage.gp8403_2_2_VOLTAGE_10V,
}

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(gp8403_2_2),
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
