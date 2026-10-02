if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CheeseHeadWasher,
)

size = "M1"

washer = CheeseHeadWasher(
    size=size,
    fastener_type="iso7092",
)

show_object(washer)
