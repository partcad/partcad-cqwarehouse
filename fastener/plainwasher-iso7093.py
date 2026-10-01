if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PlainWasher,
)

size = "M2.5"

washer = PlainWasher(
    size=size,
    fastener_type="iso7093",
)

show_object(washer)
