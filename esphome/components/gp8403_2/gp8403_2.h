#pragma once

#include "esphome/components/i2c/i2c.h"
#include "esphome/core/component.h"

namespace esphome {
namespace GP8403_C {

enum GP8403_CVoltage {
  GP8403_C_VOLTAGE_5V = 0x00,
  GP8403_C_VOLTAGE_10V = 0x11,
};

class GP8403_C : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::DATA; }

  void set_voltage(GP8403_C::GP8403_CVoltage voltage) { this->voltage_ = voltage; }

 protected:
  GP8403_CVoltage voltage_;
};

}  // namespace GP8403_C
}  // namespace esphome
