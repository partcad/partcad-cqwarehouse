if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexNut,
)

size = "M5-0.8"
simple = False
hand = "right"

nut = HexNut(
    size=size,
    fastener_type="iso4033",
    hand=hand,
    simple=simple,
)

show_object(nut)
