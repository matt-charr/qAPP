from qapy.algebra.language import *

basket = [
    ("undl1", 25.0),
    ("undl2", 35.0),
    ("undl3", 40.0)
]

def PERFORMANCE(start_date, end_date):
    return (
        basket[0][1] * SPOT(basket[0][0], end_date) / SPOT(basket[0][0], start_date) +
        basket[1][1] * SPOT(basket[1][0], end_date) / SPOT(basket[1][0], start_date) +
        basket[2][1] * SPOT(basket[2][0], end_date) / SPOT(basket[2][0], start_date)
    ) / (basket[0][1] + basket[1][1] + basket[2][1])

CONTRACT(
    "factory/tests/output/autocall",
    IF(PERFORMANCE("2020-11-10", "2021-11-10") >= REF("autocall_barrier", 1.30)) (
        PAY(100, "2021-11-10", "cc1") & PAY(1000, "2021-11-10", "cc1"),
        IF(PERFORMANCE("2020-11-10", "2022-11-10") >= REF("autocall_barrier", 1.30)) (
            PAY(200, "2022-11-10", "cc1") & PAY(1000, "2022-11-10", "cc1"),
            IF(PERFORMANCE("2020-11-10", "2023-11-10") >= REF("autocall_barrier", 1.30)) (
                PAY(300, "2023-11-10", "cc1") & PAY(1000, "2023-11-10", "cc1"),
                IF(PERFORMANCE("2020-11-10", "2024-11-10") >= REF("autocall_barrier", 1.30)) (
                    PAY(400, "2024-11-11", "cc1") & PAY(1000, "2024-11-11", "cc1"),
                    IF(PERFORMANCE("2020-11-10", "2024-11-10") >= REF("strike", 0.60)) (
                        PAY(1000, "2024-11-11", "cc1") & PAY(1000 * PERFORMANCE("2020-11-10", "2024-11-10"), "2024-11-11", "cc1"),
                        PAY(1000, "2024-11-11", "cc1")
                    )
                )
            )
        )
    )
)