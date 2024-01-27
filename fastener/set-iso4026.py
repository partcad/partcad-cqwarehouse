if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    SetScrew,
)

size = "M1.4-0.3"
simple = False
length = 10
hand = "right"

screw = SetScrew(
    size=size,
    fastener_type="iso4026",
    length=length,
    simple=simple,
    hand=hand,
)

show_object(screw)
