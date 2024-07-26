
from base.models import Advertisement


class AdvertisementService:
    @staticmethod
    def find_all() -> [Advertisement]:
        """
            Взятие всех объявлений
        """
        return Advertisement.objects.all()

    @staticmethod
    def find_by_id(advertisement_id: int) -> Advertisement | None:
        """
            Взятие 1 объявления по его id
        """
        try:
            return Advertisement.objects.get(id=advertisement_id)
        except Advertisement.DoesNotExist:
            return None

