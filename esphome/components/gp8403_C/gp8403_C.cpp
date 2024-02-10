#include "gp8403_C.h"

#include "esphome/core/log.h"

namespace esphome {
namespace gp8403_C {

static const char *const TAG = "gp8403_C";

static const uint8_t RANGE_REGISTER = 0x01;

void gp8403_C::setup() { this->write_register(RANGE_REGISTER, (uint8_t *) (&this->voltage_), 1); }

void gp8403_C::dump_config() {
  ESP_LOGCONFIG(TAG, "gp8403_C:");
  ESP_LOGCONFIG(TAG, "  Voltage: %dV", this->voltage_ == gp8403_CVOLTAGE_5V ? 5 : 10);  //gp8403_C_VOLTAGE_5V
  LOG_I2C_DEVICE(this);
}

}  // namespace gp8403_C
}  // namespace esphome
