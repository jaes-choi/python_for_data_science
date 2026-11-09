"""쇼핑 계산기: 누락 가격을 추측하지 않고 확정 여부를 구분한다."""
from __future__ import annotations

ITEM_PRICES = {"우유": 1000, "계란": 3000, "소고기": 9000, "라면": 800}
SHOPPING_LIST = [["우유", 2], ["빵", 3], ["라면", 5]]


def calculate(prices: dict[str, int], items: list[list]) -> dict:
    """검증된 금액 소계/누락 품목/확정 총액을 반환한다."""
    for name, price in prices.items():
        if isinstance(price, bool) or not isinstance(price, int) or price < 0:
            raise ValueError(f"가격 오류: {name}")
    lines, missing, subtotal = [], [], 0
    for row in items:
        if not isinstance(row, (list, tuple)) or len(row) != 2:
            raise ValueError(f"구매 목록 형식 오류: {row!r}")
        name, quantity = row
        if not isinstance(name, str) or not name.strip():
            raise ValueError("품목명은 비어 있을 수 없습니다")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(f"수량 오류: {name}")
        if name not in prices:
            missing.append(name)
            lines.append({"item": name, "quantity": quantity, "unit_price": None, "amount": None})
            continue
        price = prices[name]
        amount = price * quantity
        subtotal += amount
        lines.append({"item": name, "quantity": quantity, "unit_price": price, "amount": amount})
    return {"lines": lines, "known_subtotal": subtotal,
            "missing": missing, "total": None if missing else subtotal}


def main() -> None:
    result = calculate(ITEM_PRICES, SHOPPING_LIST)
    for row in result["lines"]:
        amount = "가격 미확인" if row["amount"] is None else f'{row["amount"]:,}원'
        print(f'{row["item"]}: {row["quantity"]}개 → {amount}')
    print(f'확인된 소계: {result["known_subtotal"]:,}원')
    print("전체 총액: 미확정" if result["total"] is None else f'전체 총액: {result["total"]:,}원')
    if result["missing"]:
        print("가격 누락:", ", ".join(result["missing"]))


if __name__ == "__main__":
    main()
