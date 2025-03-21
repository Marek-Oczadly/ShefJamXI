#include <cmath>
constexpr const double root_2 = 0.70710678118654752440084436210485;

void make_unit_v(double& x, double& y) {
    if (x == 0 || y == 0) return;
    else {
        x *= root_2;
        y *= root_2;
    }
}