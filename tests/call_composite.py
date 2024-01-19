from device.qalgebra import *
CONTRACT(
    "call_composite",
    PAY(
        MAX(
            SPOT_COMPOSITE("undl1", "2022-05-03", "cc2") / SPOT_COMPOSITE("undl1", "2021-05-03", "cc2") - 1,
            0
        ),
        "2022-05-03",
        "cc1"
    )
)