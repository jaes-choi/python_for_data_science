"""교통사고 CSV를 읽어 집계 CSV와 그래프를 생성한다. 원본 파일은 읽기만 한다."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "2016년_교통사망사고정보.csv"
OUTPUT = Path(__file__).resolve().parent / "output"


def aggregate(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    needed = {"요일", "발생지시도", "사망자수"}
    absent = needed - set(df.columns)
    if absent:
        raise ValueError(f"필수 열 누락: {sorted(absent)}")
    if df[list(needed)].isna().any().any():
        raise ValueError("필수 열에 결측값이 있습니다. 임의 삭제·대체하지 않습니다.")
    death_counts = pd.to_numeric(df["사망자수"], errors="raise")
    if (death_counts < 0).any():
        raise ValueError("사망자수는 음수일 수 없습니다")
    weekday_order = list("월화수목금토일")
    by_weekday = df.groupby("요일").size().reindex(weekday_order, fill_value=0)
    by_region = death_counts.groupby(df["발생지시도"]).sum().sort_values(ascending=False)
    if by_weekday.sum() != len(df):
        raise AssertionError("요일 집계 총합이 원본 행 수와 다릅니다")
    if by_region.sum() != death_counts.sum():
        raise AssertionError("지역 사망자 합계가 원본 합계와 다릅니다")
    return by_weekday, by_region


def main() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    df = pd.read_csv(SOURCE, encoding="cp949")
    weekday, region = aggregate(df)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    weekday.rename("사망사고_건수").to_csv(OUTPUT / "weekday_accidents.csv", encoding="utf-8-sig")
    region.rename("사망자_수").to_csv(OUTPUT / "region_deaths.csv", encoding="utf-8-sig")
    # 원본 항목명은 CSV에서 확인 가능. 폰트 문제를 피하기 위해 가로축은 요일 순번.
    ax = weekday.plot(kind="bar", title="Fatal accident records by day of week")
    ax.set_xlabel("Mon Tue Wed Thu Fri Sat Sun")
    ax.set_ylabel("Records")
    ax.figure.tight_layout()
    ax.figure.savefig(OUTPUT / "weekday_accidents.png")
    plt.close(ax.figure)
    (OUTPUT / "traffic_summary.md").write_text(
        f"# 교통사고 데이터 집계 결과\n\n- 원본 파일: {SOURCE.name}\n"
        f"- 관측 행 수: {len(df):,}\n- 사망자 수 합계: {pd.to_numeric(df['사망자수']).sum():,}\n"
        "- 주의: 사망사고 자료이며 전체 교통사고 위험도나 인과관계를 직접 설명하지 않습니다.\n",
        encoding="utf-8"
    )
    print("분석 완료:", OUTPUT)


if __name__ == "__main__":
    main()
