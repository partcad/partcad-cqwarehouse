if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PlainWasher,
)

size = "M5"

washer = PlainWasher(
    size=size,
    fastener_type="iso7094",
)

show_object(washer)
