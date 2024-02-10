#pragma once

#include "esphome/components/output/float_output.h"
#include "esphome/core/component.h"

#include "esphome/components/GP8403_C/GP8403_C.h"

namespace esphome {
namespace GP8403_C {

class GP8403_COutput : public Component, public output::FloatOutput, public Parented<GP8403_C> {
 public:
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::DATA - 1; }

  void set_channel(uint8_t channel) { this->channel_ = channel; }

  void write_state(float state) override;

 protected:
  uint8_t channel_;
};

}  // namespace GP8403_C
}  // namespace esphome
