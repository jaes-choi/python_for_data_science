"""pandas 설치 시에만 실행되는 확장 검증."""
import unittest

try:
    import pandas as pd
    from traffic_report import aggregate
except ImportError:
    pd = None


@unittest.skipIf(pd is None, "pandas가 없는 기본 실습은 건너뜁니다")
class TrafficTests(unittest.TestCase):
    def test_aggregate(self):
        df = pd.DataFrame({
            "요일": ["월", "월", "화"],
            "발생지시도": ["서울", "부산", "서울"],
            "사망자수": [1, 2, 3],
        })
        weekdays, regions = aggregate(df)
        self.assertEqual(weekdays["월"], 2)
        self.assertEqual(weekdays["화"], 1)
        self.assertEqual(weekdays.sum(), 3)
        self.assertEqual(regions["서울"], 4)
        self.assertEqual(regions.sum(), 6)

    def test_missing_column(self):
        df = pd.DataFrame({"요일": ["월"]})
        with self.assertRaises(ValueError):
            aggregate(df)

    def test_missing_values_not_silently_dropped(self):
        df = pd.DataFrame({"요일": [None], "발생지시도": ["서울"], "사망자수": [1]})
        with self.assertRaises(ValueError):
            aggregate(df)


if __name__ == "__main__":
    unittest.main()
