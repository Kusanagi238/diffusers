__all__ = [
    "AsymmetricAutoencoderKL",
    "AutoencoderKL",
    "AutoencoderKLTemporalDecoder",
    "AutoencoderTiny",
    "ConsistencyDecoderVAE",
]

from importlib import import_module as _import_module
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .autoencoder_asym_kl import AsymmetricAutoencoderKL
    from .autoencoder_kl import AutoencoderKL
    from .autoencoder_kl_temporal_decoder import AutoencoderKLTemporalDecoder
    from .autoencoder_tiny import AutoencoderTiny
    from .consistency_decoder_vae import ConsistencyDecoderVAE

_module_map = {
    "AsymmetricAutoencoderKL": "autoencoder_asym_kl",
    "AutoencoderKL": "autoencoder_kl",
    "AutoencoderKLTemporalDecoder": "autoencoder_kl_temporal_decoder",
    "AutoencoderTiny": "autoencoder_tiny",
    "ConsistencyDecoderVAE": "consistency_decoder_vae",
}


def __getattr__(name):
    if name in __all__:
        module = _import_module(f"{__package__}.{_module_map[name]}")
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")
