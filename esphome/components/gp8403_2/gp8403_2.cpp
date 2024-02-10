#include "GP8403_C.h"

#include "esphome/core/log.h"

namespace esphome {
namespace GP8403_C {

static const char *const TAG = "GP8403_C";

static const uint8_t RANGE_REGISTER = 0x01;

void GP8403_C::setup() { this->write_register(RANGE_REGISTER, (uint8_t *) (&this->voltage_), 1); }

void GP8403_C::dump_config() {
  ESP_LOGCONFIG(TAG, "GP8403_C:");
  ESP_LOGCONFIG(TAG, "  Voltage: %dV", this->voltage_ == GP8403_C_VOLTAGE_5V ? 5 : 10);
  LOG_I2C_DEVICE(this);
}

}  // namespace GP8403_C
}  // namespace esphome
