if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexNutWithFlange,
)

size = "M5-0.8"
simple = False
hand = "right"

nut = HexNutWithFlange(
    size=size,
    fastener_type="din1665",
    hand=hand,
    simple=simple,
)

show_object(nut)
