from .base import BaseNetwork
from .registry import registry


@registry.register('dogecoin', 'DOGE')
class Dogecoin(BaseNetwork):
    pubkey_address_prefix = 0x1E
