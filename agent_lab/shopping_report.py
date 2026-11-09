"""CSV 구매 목록을 읽어 품목별 결과 CSV를 만든다. 표준 라이브러리만 사용."""
from __future__ import annotations

import csv
from pathlib import Path
from shopping import ITEM_PRICES, calculate

BASE = Path(__file__).resolve().parent


def read_items(path: Path) -> list[list]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not {"item", "quantity"}.issubset(reader.fieldnames):
            raise ValueError("CSV에는 item,quantity 열이 필요합니다")
        result = []
        for number, row in enumerate(reader, start=2):
            try:
                quantity = int(row["quantity"])
            except (ValueError, TypeError):
                raise ValueError(f"{number}행 수량이 정수가 아닙니다") from None
            result.append([row["item"], quantity])
    return result


def write_report(input_file: Path, output_file: Path, prices: dict[str, int] | None = None) -> dict:
    result = calculate(ITEM_PRICES if prices is None else prices, read_items(input_file))
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["item", "quantity", "unit_price", "amount", "status"])
        for row in result["lines"]:
            writer.writerow([row["item"], row["quantity"],
                             "" if row["unit_price"] is None else row["unit_price"],
                             "" if row["amount"] is None else row["amount"],
                             "PRICE_MISSING" if row["amount"] is None else "OK"])
    return result


def main() -> None:
    destination = BASE / "output" / "shopping_report.csv"
    result = write_report(BASE / "sample_shopping.csv", destination)
    print(f"보고서 저장: {destination}")
    print(f'확인된 소계: {result["known_subtotal"]:,}원')
    print("전체 총액: 미확정" if result["total"] is None else f'전체 총액: {result["total"]:,}원')


if __name__ == "__main__":
    main()
