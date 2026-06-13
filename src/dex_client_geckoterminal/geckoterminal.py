from __future__ import annotations
from typing import Any
from .core import BaseClient, Json

class GeckoTerminalClient(BaseClient):
    def __init__(self, *, base_url: str = "https://app.geckoterminal.com/api/p1", timeout: float = 10.0):
        super().__init__(base_url, timeout=timeout, headers={"Accept": "application/json, text/plain, */*", "Origin": "https://www.geckoterminal.com", "Referer": "https://www.geckoterminal.com/"})

    def networks(self) -> Json: return self.get("/networks", params={"fields[network]": "name,identifier,image_url,is_new", "show_for_sidebar": 1, "sort": "-24h_volume"})
    def trending_themes(self, network: str | None = None) -> Json: return self.get("/trending_themes", params={"network": network} if network else None)
    def trends(self) -> Json: return self.get("/trends")
    def global_stats(self) -> Json: return self.get("/global_stats")
    def pools(self, network: str, *, page: int = 1, items: int = 50, include: str = "dex,dex.network,tokens", sort: str | None = None, include_network_metrics: bool = False, include_meta: bool = False) -> Json:
        params: dict[str, Any] = {"page": page, "items": items, "include": include}
        if sort: params["sort"] = sort
        if include_network_metrics: params["include_network_metrics"] = "true"
        if include_meta: params["include_meta"] = "1"
        return self.get(f"/{network}/pools", params=params)
    def pool_detail(self, network: str, address: str, base_token: int = 0) -> Json: return self.get(f"/{network}/pools/{address}", params={"include": "dex,dex.network,tokens", "base_token": base_token})
    def token_info_snapshots(self, network: str, address: str) -> Json: return self.get(f"/{network}/pools/{address}/token_info_snapshots")
    def related_pools(self, network: str, address: str) -> Json: return self.get(f"/{network}/pools/{address}/related_pools", params={"include": "tokens,dex,dex.network", "fields[related_pool]": "address,pool_fee,token_id,liquidity,volume_in_usd_24h,tokens,dex", "fields[token]": "symbol", "fields[dex]": "network,name,image_url,network", "fields[network]": "identifier"})
    def sender_swaps(self, network: str, address: str, *, pair_id: int | None = None, from_timestamp: int | None = None, to_timestamp: int | None = None) -> Json:
        p: dict[str, Any] = {}
        if pair_id: p["pair_id"] = pair_id
        if from_timestamp: p["from_timestamp"] = from_timestamp
        if to_timestamp: p["to_timestamp"] = to_timestamp
        return self.get(f"/{network}/pools/{address}/sender_swaps", params=p)
    def swaps(self, network: str, address: str, **params: Any) -> Json: return self.get(f"/{network}/pools/{address}/swaps", params=params)
    def candlesticks(self, base_token_id: str | int, pool_id: str | int, *, resolution: str = "15", count_back: int = 329, currency: str = "usd", is_inverted: bool = False, for_update: bool = False, from_timestamp: int | None = None, to_timestamp: int | None = None) -> Json:
        p: dict[str, Any] = {"resolution": resolution, "count_back": count_back, "currency": currency, "is_inverted": str(is_inverted).lower(), "for_update": str(for_update).lower()}
        if from_timestamp: p["from_timestamp"] = from_timestamp
        if to_timestamp: p["to_timestamp"] = to_timestamp
        return self.get(f"/candlesticks/{base_token_id}/{pool_id}", params=p)
    def token_ads(self, country: str = "US") -> Json: return self.get("/token_ads", params={"country": country})
    def token_ads_track(self, body: dict[str, Any]) -> Json: return self.post("/token_ads/track", json_body=body)
