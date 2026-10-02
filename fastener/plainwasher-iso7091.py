if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PlainWasher,
)

size = "M1.6"

washer = PlainWasher(
    size=size,
    fastener_type="iso7091",
)

show_object(washer)
