import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.components import i2c, output
from esphome.const import CONF_ID, CONF_CHANNEL

from .. import gp8403_2_2_ns, gp8403_2_2, CONF_gp8403_2_2_ID

DEPENDENCIES = ["gp8403_2_2"]

gp8403_2_2Output = gp8403_2_2_ns.class_(
    "gp8403_2_2Output", cg.Component, i2c.I2CDevice, output.FloatOutput
)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(gp8403_2_2Output),
        cv.GenerateID(CONF_gp8403_2_2_ID): cv.use_id(gp8403_2_2),
        cv.Required(CONF_CHANNEL): cv.one_of(0, 1),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)

    await cg.register_parented(var, config[CONF_gp8403_2_2_ID])

    cg.add(var.set_channel(config[CONF_CHANNEL]))
