from device.qalgebra import *
CONTRACT(
    "digital_call",
    IF(SPOT("undl1", "2022-05-03") > SPOT("undl1", "2021-05-03")) (
        PAY(100., "2022-05-05", "cc1"),
        END()
    )
)