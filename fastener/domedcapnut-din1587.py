if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    DomedCapNut,
)

size = "M4-0.7"
simple = False
hand = "right"

nut = DomedCapNut(
    size=size,
    fastener_type="din1587",
    hand=hand,
    simple=simple,
)

show_object(nut)
