from fractions import Fraction as Q
from math import isqrt

left, pivot, right = Q(7, 100), Q(4, 25), Q(37, 200)
half = Q(1, 2)
grid = 10**8
step = Q(1, grid)


def root(x):
    """Lower endpoint of an enclosure of sqrt(x) of length 1/grid."""
    return Q(isqrt((x * grid**2) // 1), grid)


def arc(x):
    return root(x * (2 - x))


b0 = root(Q(3, 4))
b1 = b0 + step
c0, c1 = 1 - b1, 1 - b0


def moment_upper(v):
    z = min(v, 1 - v)
    simpson = (z - c1) * (half + 4 * arc((c0 + z) / 2) + arc(z)) / 6
    integral = simpson + 2 * b0 * max(0, v - half)
    return 3 * (v - c0) / 4 + b1 / 2 - b0 * integral / (v - c0)


def check_profile():
    u, ell = Q(1, 25), Q(47, 200)
    assert c1 < ell < (26 - 14 * b1) / 50
    assert (26 - 14 * b0) / 50 < ell + left and ell + right < half
    eps = Q("0.00117")
    # Use upper endpoints for both Gaussian nodes and both heights.
    low_node = u + (c1 - u) * (1 - 1 / (2 * b1)) / 2
    high_node = u + (c1 - u) * (1 + 1 / (2 * b0)) / 2
    excess = arc(low_node) + arc(high_node) + 2 * step - Q(7, 25) - half
    assert (c1 - u) * excess / 2 < eps
    assert Q(5, 2) * Q(27, 32768) < 2 * eps

    mass = 4 * b0 - 3                   # lower bound for the mass M
    assert (242 * (2 * b0) - 207) / 625 > Q(1, 3)
    assert moment_upper(ell) < Q("0.0100")
    for e, cap in [(left, Q("0.1688")), (right, Q("0.1211"))]:
        v = 1 - ell - e
        assert moment_upper(v) < cap
        assert v - c1 > Q(2, 5)
        assert Q(3, 2) - b1 * v / arc(1 - v) > half + 2 * e
        lower = mass + (2 * c0 - u - ell) / 2 - cap - eps / e
        assert lower > Q(6, 25) + e / 2
    assert mass - Q("0.0100") - Q("0.1211") > Q(6, 25) + right / 2


# Value and derivative of d^(3/2) (a + t*d) at pivot = (2/5)^2.
sqrt2_lo, sqrt2_hi = Q("1.414"), Q("1.415")
sqrt_hi = Q("1.540")                  # upper bound for sqrt(2 + 2*right)
a = 4 * sqrt2_lo / 3
t = Q(28, 15) / (sqrt2_hi + sqrt_hi)
disk_value = Q(2, 5) * pivot * (a + t * pivot)
disk_slope = Q(2, 5) * (3 * a + 5 * t * pivot) / 2


def disk_tangent(d):
    return disk_value + disk_slope * (d - pivot)


# Apply the quotient rule to (d - disk_tangent(d))/(6/25 - d/2).
denom = Q(6, 25) - pivot / 2
height = (pivot - disk_value) / denom
height_slope = (1 - disk_slope + height / 2) / denom


def switch(d):
    return height + height_slope * (d - pivot)


def secant(d):
    def value(x):
        return x**2 * (2 + switch(x) + x) / (1 + x)**2
    weight = (d - left) / (right - left)
    return (1 - weight) * value(left) + weight * value(right)


# Rounded arc coefficient and resulting tilt-loss coefficient.
sqrt3_lo, sqrt3_hi = Q("1.732"), Q("1.733")
arc_constant = (half - 2 * right / 9) / sqrt3_hi
arc_tilt = Q(9, 16) * sqrt3_hi / (half - 2 * right / 3)


def bounds(v):
    d = pivot + v
    h = switch(d)
    common = (Q(6, 25) - d / 2) * h - d
    disk = common + disk_tangent(d)
    arcs = common + 3 * d * (sqrt3_lo - 1 - h) / 2
    arcs += arc_constant * d**2 - arc_tilt * (h - d) * secant(d)
    return disk, arcs


def check_widths():
    small_root = Q(173, 100)
    small_mass = 3 * small_root - 5
    assert small_mass - 5 * left / 2 - 3 * left**2 / 2 > 0
    assert small_mass + 3 * small_root / 2 - Q(5, 2) - 4 * left > 0
    assert sqrt3_lo**2 < 3 < sqrt3_hi**2
    assert Q(181, 1200) * Q(31, 10) + 3 > 2 * sqrt3_hi
    assert sqrt2_lo**2 < 2 < sqrt2_hi**2
    assert 2 + 2 * right < sqrt_hi**2
    assert height_slope < 0 and switch(right) >= right
    base = Q(6, 25) - 1 + 3 * (sqrt3_lo - 1) / 2
    assert arc_constant < 2 and base + (arc_constant - 2) * right > 0
    assert disk_tangent(right) + right * (Q(6, 25) - right / 2 - 1) > 0

    # Positivity of the second derivative justifies the endpoint secant.
    a0, a1 = 2 + switch(0), 1 + height_slope
    for d in (left, right):
        assert 2 * a0 + (6 * a1 - 4 * a0) * d > 0

    # The three samples determine each quadratic in v = d - pivot.
    delta = Q(1, 100)
    values = []
    for v in (-delta, 0, delta):
        disk, arcs = bounds(v)
        assert disk == -height_slope * v**2 / 2
        values.append(arcs)
    low, const, high = values
    linear = (high - low) / (2 * delta)
    quadratic = ((high + low) / 2 - const) / delta**2
    assert const > Q(1, 10000) and abs(linear) < Q(1, 50)
    assert quadratic > 1


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O so that assertions are checked.")
    check_profile()
    check_widths()
    print("All rational comparisons passed.")
