class TikTokLinkValidator:
    def __init__(self):
        self.allowed_domains = [
            "tiktok.com",
            "www.tiktok.com",
            "vm.tiktok.com",
            "vt.tiktok.com"
        ]

    def is_tiktok_link(self, link):
        if not link:
            return False

        link = link.strip().lower()

        if not link.startswith("http"):
            return False

        for domain in self.allowed_domains:
            if domain in link:
                return True

        return False