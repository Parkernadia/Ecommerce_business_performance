from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

def main():
    sessions = pd.read_csv(
        RAW_DATA_DIR / "website_sessions.csv",
        low_memory=False
    )

    print("\n" + "=" * 65)
    print("MISSING MARKETING ATTRIBUTION ANALYSIS")
    print("=" * 65)

    missing_utm = sessions["utm_source"].isna()
    missing_referer = sessions["http_referer"].isna()

    print(f"Total sessions: {len(sessions):,}")
    print(f"Missing UTM source: {missing_utm.sum():,}")
    print(f"Missing UTM campaign: {sessions['utm_campaign'].isna().sum():,}")
    print(f"Missing UTM content: {sessions['utm_content'].isna().sum():,}")
    print(f"Missing HTTP referer: {missing_referer.sum():,}")

    print("\nMissing value combinations:")
    print(
        pd.crosstab(
            missing_utm,
            missing_referer,
            rownames=["UTM source missing"],
            colnames=["HTTP referer missing"]
        )
    )

    print("\n" + "=" * 65)
    print("HTTP REFERER VALUES")
    print("=" * 65)

    print(sessions["http_referer"].value_counts(dropna=False).head(15))

    print("\n" + "=" * 65)
    print("UTM SOURCE BY DEVICE TYPE")
    print("=" * 65)

    print(
        pd.crosstab(
            sessions["utm_source"].fillna("Missing"),
            sessions["device_type"],
            margins=True
        )
    )

if __name__ == "__main__":
    main()