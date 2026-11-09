import csv
import tempfile
import unittest
from pathlib import Path

from shopping_report import read_items, write_report


class ReportTests(unittest.TestCase):
    def test_sample_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(__file__).resolve().parent
            out = Path(tmp) / "report.csv"
            result = write_report(base / "sample_shopping.csv", out)
            self.assertEqual(result["known_subtotal"], 6000)
            self.assertIsNone(result["total"])
            with out.open(encoding="utf-8-sig", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[1]["status"], "PRICE_MISSING")
            self.assertEqual(rows[1]["amount"], "")

    def test_bread_price_total(self):
        from shopping import ITEM_PRICES
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(__file__).resolve().parent
            result = write_report(base / "sample_shopping.csv", Path(tmp) / "out.csv",
                                  {**ITEM_PRICES, "빵": 1500})
            self.assertEqual(result["total"], 10500)

    def test_bad_csv_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            path.write_text("name,count\n우유,2\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_items(path)

    def test_bad_quantity(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            path.write_text("item,quantity\n우유,abc\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_items(path)


if __name__ == "__main__":
    unittest.main()
