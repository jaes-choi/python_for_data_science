"""기본 모듈 unittest: 외부 패키지 없음."""
import unittest

from shopping import calculate, ITEM_PRICES, SHOPPING_LIST


class ShoppingTests(unittest.TestCase):
    def test_missing_price_keeps_total_unknown(self):
        result = calculate(ITEM_PRICES, SHOPPING_LIST)
        self.assertEqual(result["known_subtotal"], 6000)
        self.assertEqual(result["missing"], ["빵"])
        self.assertIsNone(result["total"])

    def test_bread_price_completes_total(self):
        result = calculate({**ITEM_PRICES, "빵": 1500}, SHOPPING_LIST)
        self.assertEqual(result["total"], 10500)
        self.assertEqual(result["missing"], [])

    def test_unknown_is_not_zero(self):
        result = calculate({}, [["없는상품", 2]])
        self.assertEqual(result["known_subtotal"], 0)
        self.assertIsNone(result["total"])

    def test_invalid_quantities(self):
        for quantity in [0, -1, True, 1.5, "2"]:
            with self.subTest(quantity=quantity):
                with self.assertRaises(ValueError):
                    calculate(ITEM_PRICES, [["우유", quantity]])

    def test_invalid_prices(self):
        with self.assertRaises(ValueError):
            calculate({"우유": -100}, [["우유", 1]])

    def test_empty_list(self):
        self.assertEqual(calculate(ITEM_PRICES, [])["total"], 0)


if __name__ == "__main__":
    unittest.main()
