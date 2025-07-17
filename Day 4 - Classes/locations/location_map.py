from .old_oak import OldOak
from .rainbow_falls import RainbowFalls
from .pixie_housing import PixieHousing
from .evil_bunnies import EvilBunnies

location_map = {
    "old_oak": OldOak(),
    "rainbow_falls": RainbowFalls(),
    "pixie_housing": PixieHousing(),
    "evil_bunnies": EvilBunnies()
}
