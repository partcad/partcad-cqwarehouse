if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    DomedCapNut,
)

# cq_warehouse 0.8.0 tabulates the height of DIN 1587's M10 as 88 mm, where the
# standard says 8 (its dk of 15 and its s of 16 are the standard's, and so are
# its neighbours' heights: 6.5 for the M8 and 10 for the M12). The table is read
# whenever a nut is made, so it is corrected here, before this one is - and
# only while it still says 88, so a cq_warehouse that has fixed it is left as
# it is.
_M10 = DomedCapNut.fastener_data.get("M10-1.5", {})
if _M10.get("din1587:m") == "88":
    _M10["din1587:m"] = "8"

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
