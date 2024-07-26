from base.models import Advertisement


class AdvertisementUtil:
    @staticmethod
    def list(advertisements: [Advertisement]) -> [dict]:
        """
            Собираем список с словарями данных объявлений
        """
        return [{
            'id': ad.id,
            'title': ad.title,
            'user': ad.user.username,
            'view_count': ad.view_count,
            'position': ad.position
        } for ad in advertisements]

    @staticmethod
    def detail(advertisement: Advertisement) -> dict:
        """
            Собираем словарь данного объявления
        """
        return {
            'id': advertisement.id,
            'title': advertisement.title,
            'user': advertisement.user.username,
            'view_count': advertisement.view_count,
            'position': advertisement.position
        }
