// #include "../../../../../../Python312/include/Python.h"


float jump(float initial_v, const unsigned int frame, const float gravity, const unsigned int frame_rate, const unsigned int pixels_per_meter) {
    const float gravity_new_units = (gravity * pixels_per_meter) / (frame_rate * frame_rate);
    return initial_v + gravity_new_units * frame;
}

int main() {
    return 0;
}