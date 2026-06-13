        # GeckoTerminal Web Client

        Python client for endpoints used by [https://www.geckoterminal.com](https://www.geckoterminal.com). The implementation is browser/reverse-engineered and mirrors the internal clients used in local DEX modules.

        ## Install

        ```bash
        pip install git+https://github.com/bigidulka/dex-client-geckoterminal.git
        ```

        For local development:

        ```bash
        pip install -e '.[dev]'
        pytest
        ```

        ## Quick start

        ```python
        from dex_client_geckoterminal import GeckoTerminalClient

        client = GeckoTerminalClient()
        # call any method below; all methods return decoded JSON dict/list payloads
        ```

        ## Methods

        - `networks`
- `trending_themes`
- `trends`
- `global_stats`
- `pools`
- `pool_detail`
- `token_info_snapshots`
- `related_pools`
- `sender_swaps`
- `swaps`
- `candlesticks`
- `token_ads`
- `token_ads_track`

        ## Endpoint inventory

        Extracted from existing Local clients and rechecked with browser-harness network capture where the site allowed capture.

        - `['GET', '/networks', 'networks']`
- `['GET', '/trending_themes', 'trending themes']`
- `['GET', '/trends', 'trends']`
- `['GET', '/global_stats', 'global stats']`
- `['GET', '/{network}/pools', 'pools']`
- `['GET', '/{network}/pools/{address}', 'pool detail']`
- `['GET', '/{network}/pools/{address}/token_info_snapshots', 'token snapshots']`
- `['GET', '/{network}/pools/{address}/related_pools', 'related pools']`
- `['GET', '/{network}/pools/{address}/sender_swaps', 'sender swaps']`
- `['GET', '/{network}/pools/{address}/swaps', 'swaps']`
- `['GET', '/candlesticks/{base_token_id}/{pool_id}', 'candlesticks']`
- `['GET', '/token_ads', 'token ads']`
- `['POST', '/token_ads/track', 'token ads track']`

        Full details: [`endpoint_inventory.json`](endpoint_inventory.json).

        ## Notes

        - No official SDK is used.
        - Some endpoints require Cloudflare/browser behavior; pass `use_curl_cffi=True` where available.
        - Auth/session-only methods need your own cookies/tokens. Do not commit secrets.
        - These clients are thin transport wrappers; normalize data in your application layer.
