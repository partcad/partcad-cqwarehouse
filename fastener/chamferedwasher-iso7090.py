if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    ChamferedWasher,
)

size = "M5"

washer = ChamferedWasher(
    size=size,
    fastener_type="iso7090",
)

show_object(washer)
