#include "gp8403_C_output.h"

#include "esphome/core/log.h"

namespace esphome {
namespace gp8403_C {

static const char *const TAG = "gp8403_C.output";

static const uint8_t OUTPUT_REGISTER = 0x02;

void gp8403_COutput::dump_config() {
  ESP_LOGCONFIG(TAG, "gp8403_C Output:");
  ESP_LOGCONFIG(TAG, "  Channel: %u", this->channel_);
}

void gp8403_COutput::write_state(float state) {
  uint16_t value = ((uint16_t) (state * 4095)) << 4;
  i2c::ErrorCode err = this->parent_->write_register(OUTPUT_REGISTER + (2 * this->channel_), (uint8_t *) &value, 2);
  if (err != i2c::ERROR_OK) {
    ESP_LOGE(TAG, "Error writing to gp8403_C, code %d", err);
  }
}

}  // namespace gp8403_C
}  // namespace esphome
