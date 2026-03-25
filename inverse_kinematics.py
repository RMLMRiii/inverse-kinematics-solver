import math
from typing import Tuple


def inverse_kinematics(link1: float, link2: float, x: float, y: float) -> Tuple[float, float]:
    distance_squared = x**2 + y**2

    cos_theta2 = (distance_squared - link1**2 - link2**2) / (2 * link1 * link2)

    if cos_theta2 < -1 or cos_theta2 > 1:
        raise ValueError("Target position is unreachable.")

    theta2 = math.acos(cos_theta2)

    k1 = link1 + link2 * math.cos(theta2)
    k2 = link2 * math.sin(theta2)

    theta1 = math.atan2(y, x) - math.atan2(k2, k1)

    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)

    return theta1_deg, theta2_deg


def display_result(link1: float, link2: float, x: float, y: float, theta1: float, theta2: float) -> None:
    print("\nINVERSE KINEMATICS")
    print("-" * 40)
    print(f"Link 1 length: {link1:.2f}")
    print(f"Link 2 length: {link2:.2f}")
    print(f"Target position: ({x:.2f}, {y:.2f})")
    print(f"Theta 1: {theta1:.2f} degrees")
    print(f"Theta 2: {theta2:.2f} degrees")


def main() -> None:
    link1 = 5.0
    link2 = 3.0
    x = 6.0
    y = 2.0

    theta1, theta2 = inverse_kinematics(link1, link2, x, y)
    display_result(link1, link2, x, y, theta1, theta2)


if __name__ == "__main__":
    main()
