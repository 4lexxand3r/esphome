#pragma once

#include "esphome/components/i2c/i2c.h"
#include "esphome/core/component.h"

namespace esphome {
namespace gp8403_2_2 {

enum gp8403_2_2Voltage {
  gp8403_2_2_VOLTAGE_5V = 0x00,
  gp8403_2_2_VOLTAGE_10V = 0x11,
};

class gp8403_2_2 : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::DATA; }

  void set_voltage(gp8403_2_2::gp8403_2_2Voltage voltage) { this->voltage_ = voltage; }

 protected:
  gp8403_2_2Voltage voltage_;
};

}  // namespace gp8403_2_2
}  // namespace esphome
