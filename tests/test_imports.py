import inspect
from dex_client_geckoterminal import GeckoTerminalClient


def test_client_imports_and_instantiates():
    client = GeckoTerminalClient()
    assert client is not None


def test_public_methods_present():
    methods = [name for name, value in inspect.getmembers(GeckoTerminalClient, inspect.isfunction) if not name.startswith('_')]
    assert set(['networks', 'trending_themes', 'trends', 'global_stats', 'pools', 'pool_detail', 'token_info_snapshots', 'related_pools', 'sender_swaps', 'swaps', 'candlesticks', 'token_ads', 'token_ads_track']) <= set(methods)
