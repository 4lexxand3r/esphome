import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.components import i2c, output
from esphome.const import CONF_ID, CONF_CHANNEL

from .. import GP8403_C_ns, GP8403_C, CONF_GP8403_C_ID

DEPENDENCIES = ["GP8403_C"]

GP8403_COutput = GP8403_C_ns.class_(
    "GP8403_COutput", cg.Component, i2c.I2CDevice, output.FloatOutput
)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(GP8403_COutput),
        cv.GenerateID(CONF_GP8403_C_ID): cv.use_id(GP8403_C),
        cv.Required(CONF_CHANNEL): cv.one_of(0, 1),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)

    await cg.register_parented(var, config[CONF_GP8403_C_ID])

    cg.add(var.set_channel(config[CONF_CHANNEL]))
