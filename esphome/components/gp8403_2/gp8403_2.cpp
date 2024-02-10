#include "gp8403_2.h"

#include "esphome/core/log.h"

namespace esphome {
namespace gp8403_2 {

static const char *const TAG = "gp8403_2";

static const uint8_t RANGE_REGISTER = 0x01;

void gp8403_2::setup() { this->write_register(RANGE_REGISTER, (uint8_t *) (&this->voltage_), 1); }

void gp8403_2::dump_config() {
  ESP_LOGCONFIG(TAG, "gp8403_2:");
  ESP_LOGCONFIG(TAG, "  Voltage: %dV", this->voltage_ == gp8403_2_VOLTAGE_5V ? 5 : 10);
  LOG_I2C_DEVICE(this);
}

}  // namespace gp8403_2
}  // namespace esphome
