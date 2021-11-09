"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice
import factory.fuzzy as fuzzy
from service.models import Inventory
from service import keys


class InventoryFactory(factory.Factory):
    """Creates fake inventory for testing"""

    class Meta:
        model = Inventory

    id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(choices=["chocolate", "noodle", "fan", "computer", "speaker", "pencil"])
    quantity = fuzzy.FuzzyInteger(keys.QTY_LOW,keys.QTY_HIGH,keys.QTY_STEP)
    restock_level = fuzzy.FuzzyInteger(keys.QTY_LOW,keys.RESTOCK_LVL,keys.QTY_STEP)
    condition = fuzzy.FuzzyChoice(choices=keys.CONDITIONS)


