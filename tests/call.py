from device.qalgebra import *
CONTRACT(
    "call",
    PAY(
        MAX(
            SPOT("undl1", "2022-05-03") / SPOT("undl1", "2021-05-03") - 1,
            0
        ),
        "2022-05-07",
        "cc1"
    )
)