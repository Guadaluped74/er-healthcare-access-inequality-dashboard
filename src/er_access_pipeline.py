from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PROJECT_TITLE = "ER Wait Time & Healthcare Access Inequality Dashboard"
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "output"

LEGACY_FACILITY_FILE = DATA_DIR / "california_healthcare_facilities_raw.csv"
RAW_FACILITY_FILE = RAW_DIR / "california_healthcare_facilities_raw.csv"

CENTRAL_VALLEY_COUNTY_DATA = [
    {
        "county": "Butte",
        "fips": "06007",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Small Metro",
        "population": 208309,
        "median_household_income": 67000,
        "poverty_rate": 17.9,
        "uninsured_rate": 7.2,
        "synthetic_er_visits_per_1k": 415,
        "latitude": 39.667,
        "longitude": -121.601,
    },
    {
        "county": "Colusa",
        "fips": "06011",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Rural",
        "population": 22000,
        "median_household_income": 70500,
        "poverty_rate": 13.8,
        "uninsured_rate": 8.8,
        "synthetic_er_visits_per_1k": 438,
        "latitude": 39.178,
        "longitude": -122.238,
    },
    {
        "county": "Fresno",
        "fips": "06019",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Large Metro",
        "population": 1016000,
        "median_household_income": 69000,
        "poverty_rate": 19.3,
        "uninsured_rate": 8.9,
        "synthetic_er_visits_per_1k": 462,
        "latitude": 36.758,
        "longitude": -119.649,
    },
    {
        "county": "Glenn",
        "fips": "06021",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Rural",
        "population": 29000,
        "median_household_income": 64000,
        "poverty_rate": 15.7,
        "uninsured_rate": 9.4,
        "synthetic_er_visits_per_1k": 452,
        "latitude": 39.598,
        "longitude": -122.393,
    },
    {
        "county": "Kern",
        "fips": "06029",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Large Metro",
        "population": 917000,
        "median_household_income": 68000,
        "poverty_rate": 18.7,
        "uninsured_rate": 10.1,
        "synthetic_er_visits_per_1k": 489,
        "latitude": 35.342,
        "longitude": -118.729,
    },
    {
        "county": "Kings",
        "fips": "06031",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Small Metro",
        "population": 153000,
        "median_household_income": 62000,
        "poverty_rate": 17.4,
        "uninsured_rate": 9.7,
        "synthetic_er_visits_per_1k": 477,
        "latitude": 36.075,
        "longitude": -119.815,
    },
    {
        "county": "Madera",
        "fips": "06039",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Small Metro",
        "population": 160000,
        "median_household_income": 67500,
        "poverty_rate": 16.5,
        "uninsured_rate": 8.5,
        "synthetic_er_visits_per_1k": 455,
        "latitude": 37.218,
        "longitude": -119.763,
    },
    {
        "county": "Merced",
        "fips": "06047",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Small Metro",
        "population": 287000,
        "median_household_income": 64000,
        "poverty_rate": 18.5,
        "uninsured_rate": 8.6,
        "synthetic_er_visits_per_1k": 468,
        "latitude": 37.191,
        "longitude": -120.718,
    },
    {
        "county": "Sacramento",
        "fips": "06067",
        "region": "Sacramento Metro",
        "rural_urban_category": "Large Metro",
        "population": 1589000,
        "median_household_income": 82500,
        "poverty_rate": 13.2,
        "uninsured_rate": 6.5,
        "synthetic_er_visits_per_1k": 386,
        "latitude": 38.450,
        "longitude": -121.340,
    },
    {
        "county": "San Joaquin",
        "fips": "06077",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Large Metro",
        "population": 793000,
        "median_household_income": 80000,
        "poverty_rate": 13.4,
        "uninsured_rate": 7.1,
        "synthetic_er_visits_per_1k": 421,
        "latitude": 37.935,
        "longitude": -121.272,
    },
    {
        "county": "Shasta",
        "fips": "06089",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Small Metro",
        "population": 181000,
        "median_household_income": 62500,
        "poverty_rate": 16.1,
        "uninsured_rate": 7.3,
        "synthetic_er_visits_per_1k": 474,
        "latitude": 40.763,
        "longitude": -122.040,
    },
    {
        "county": "Stanislaus",
        "fips": "06099",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Large Metro",
        "population": 552000,
        "median_household_income": 73500,
        "poverty_rate": 14.9,
        "uninsured_rate": 7.9,
        "synthetic_er_visits_per_1k": 443,
        "latitude": 37.562,
        "longitude": -121.002,
    },
    {
        "county": "Sutter",
        "fips": "06101",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Small Metro",
        "population": 99000,
        "median_household_income": 73000,
        "poverty_rate": 14.2,
        "uninsured_rate": 7.4,
        "synthetic_er_visits_per_1k": 430,
        "latitude": 39.034,
        "longitude": -121.694,
    },
    {
        "county": "Tehama",
        "fips": "06103",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Rural",
        "population": 66000,
        "median_household_income": 56000,
        "poverty_rate": 18.9,
        "uninsured_rate": 8.7,
        "synthetic_er_visits_per_1k": 493,
        "latitude": 40.126,
        "longitude": -122.233,
    },
    {
        "county": "Tulare",
        "fips": "06107",
        "region": "San Joaquin Valley",
        "rural_urban_category": "Small Metro",
        "population": 477000,
        "median_household_income": 61500,
        "poverty_rate": 20.2,
        "uninsured_rate": 10.4,
        "synthetic_er_visits_per_1k": 505,
        "latitude": 36.228,
        "longitude": -118.781,
    },
    {
        "county": "Yolo",
        "fips": "06113",
        "region": "Sacramento Metro",
        "rural_urban_category": "Small Metro",
        "population": 221000,
        "median_household_income": 82000,
        "poverty_rate": 15.1,
        "uninsured_rate": 5.8,
        "synthetic_er_visits_per_1k": 355,
        "latitude": 38.686,
        "longitude": -121.902,
    },
    {
        "county": "Yuba",
        "fips": "06115",
        "region": "Northern Sacramento Valley",
        "rural_urban_category": "Small Metro",
        "population": 84000,
        "median_household_income": 62500,
        "poverty_rate": 17.6,
        "uninsured_rate": 7.6,
        "synthetic_er_visits_per_1k": 465,
        "latitude": 39.270,
        "longitude": -121.344,
    },
]

PRIMARY_CARE_CODES = {"COMTYC", "FQHC", "FREEC", "RHC", "RHC/COMTYC", "RHC/MD", "RHC/OP"}
HOSPITAL_CODES = {"GACH", "APH", "CDRH", "PSYCHC", "PPSPSCH", "PPSREHB"}
ED_PROXY_CODES = {"GACH"}


@dataclass(frozen=True)
class BuildResult:
    cleaned_facilities_path: Path
    community_metrics_path: Path
    ranked_risk_path: Path
    insight_summary_path: Path
    excel_path: Path


def ensure_directories() -> None:
    for directory in [RAW_DIR, PROCESSED_DIR, OUTPUT_DIR]:
        directory.mkdir(parents=True, exist_ok=True)


def load_facility_data() -> pd.DataFrame:
    source = RAW_FACILITY_FILE if RAW_FACILITY_FILE.exists() else LEGACY_FACILITY_FILE
    if not source.exists():
        raise FileNotFoundError(
            "Expected the public CDPH facility file at "
            f"{RAW_FACILITY_FILE} or {LEGACY_FACILITY_FILE}."
        )
    return pd.read_csv(source, dtype=str)


def clean_facility_data(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = [
        "FACNAME",
        "FAC_TYPE_CODE",
        "FAC_FDR",
        "ADDRESS",
        "CITY",
        "ZIP",
        "COUNTY_NAME",
        "LATITUDE",
        "LONGITUDE",
        "TRAUMA_CTR",
        "FIPS_COUNTY_CODE",
    ]
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Facility file is missing required columns: {missing}")

    cleaned = df[required_columns].copy()
    cleaned.columns = [
        "facility_name",
        "facility_type_code",
        "facility_type",
        "address",
        "city",
        "zip_code",
        "county",
        "latitude",
        "longitude",
        "trauma_center_flag",
        "fips_county_code",
    ]

    text_columns = [
        "facility_name",
        "facility_type_code",
        "facility_type",
        "address",
        "city",
        "zip_code",
        "county",
        "trauma_center_flag",
        "fips_county_code",
    ]
    for column in text_columns:
        cleaned[column] = cleaned[column].fillna("").astype(str).str.strip()

    cleaned["county"] = cleaned["county"].str.title()
    cleaned["facility_type_code"] = cleaned["facility_type_code"].str.upper()
    cleaned["zip_code"] = cleaned["zip_code"].str.extract(r"(\d{5})", expand=False)
    cleaned["latitude"] = pd.to_numeric(cleaned["latitude"], errors="coerce")
    cleaned["longitude"] = pd.to_numeric(cleaned["longitude"], errors="coerce")

    cleaned = cleaned.drop_duplicates(
        subset=["facility_name", "address", "city", "zip_code", "county"]
    )
    cleaned["is_primary_care"] = cleaned["facility_type_code"].isin(PRIMARY_CARE_CODES)
    cleaned["is_hospital"] = cleaned["facility_type_code"].isin(HOSPITAL_CODES)
    cleaned["is_emergency_department_proxy"] = cleaned["facility_type_code"].isin(ED_PROXY_CODES)
    cleaned["has_valid_coordinates"] = (
        cleaned["latitude"].between(32, 43) & cleaned["longitude"].between(-125, -113)
    )
    return cleaned.sort_values(["county", "facility_name"]).reset_index(drop=True)


def build_facility_summary(cleaned_facilities: pd.DataFrame) -> pd.DataFrame:
    summary = (
        cleaned_facilities.groupby("county", as_index=False)
        .agg(
            total_facilities=("facility_name", "count"),
            primary_care_clinics=("is_primary_care", "sum"),
            hospitals=("is_hospital", "sum"),
            emergency_departments=("is_emergency_department_proxy", "sum"),
            mapped_facilities=("has_valid_coordinates", "sum"),
        )
    )
    count_columns = [
        "total_facilities",
        "primary_care_clinics",
        "hospitals",
        "emergency_departments",
        "mapped_facilities",
    ]
    summary[count_columns] = summary[count_columns].astype(int)
    return summary


def percentile(series: pd.Series) -> pd.Series:
    if series.nunique(dropna=False) <= 1:
        return pd.Series(0.5, index=series.index)
    return series.rank(pct=True)


def min_max_score(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    minimum = series.min()
    maximum = series.max()
    if minimum == maximum:
        return pd.Series(50.0, index=series.index)
    score = (series - minimum) / (maximum - minimum) * 100
    if not higher_is_better:
        score = 100 - score
    return score.round(1)


def add_scores(df: pd.DataFrame) -> pd.DataFrame:
    scored = df.copy()
    scored["facilities_per_100k"] = (
        scored["total_facilities"] / scored["population"] * 100000
    ).round(2)
    scored["clinics_per_100k"] = (
        scored["primary_care_clinics"] / scored["population"] * 100000
    ).round(2)
    scored["hospitals_per_100k"] = (scored["hospitals"] / scored["population"] * 100000).round(2)
    scored["ed_locations_per_100k"] = (
        scored["emergency_departments"] / scored["population"] * 100000
    ).round(2)
    scored["population_per_clinic"] = (
        scored["population"] / scored["primary_care_clinics"].replace(0, pd.NA)
    ).round(0)
    scored["population_per_clinic"] = scored["population_per_clinic"].fillna(scored["population"])

    scored["clinic_access_index"] = min_max_score(scored["clinics_per_100k"])
    scored["hospital_access_index"] = min_max_score(scored["hospitals_per_100k"])
    scored["income_access_index"] = min_max_score(scored["median_household_income"])
    scored["insurance_access_index"] = min_max_score(scored["uninsured_rate"], higher_is_better=False)
    scored["poverty_access_index"] = min_max_score(scored["poverty_rate"], higher_is_better=False)

    scored["healthcare_access_score"] = (
        scored["clinic_access_index"] * 0.35
        + scored["hospital_access_index"] * 0.20
        + scored["insurance_access_index"] * 0.20
        + scored["poverty_access_index"] * 0.15
        + scored["income_access_index"] * 0.10
    ).round(1)

    low_clinic_risk = 1 - percentile(scored["clinics_per_100k"])
    low_hospital_risk = 1 - percentile(scored["hospitals_per_100k"])
    scored["er_dependence_risk_score"] = (
        percentile(scored["uninsured_rate"]) * 25
        + percentile(scored["poverty_rate"]) * 20
        + low_clinic_risk * 25
        + low_hospital_risk * 10
        + percentile(scored["population"]) * 5
        + percentile(scored["synthetic_er_visits_per_1k"]) * 15
    ).round(1)

    scored["risk_rank"] = scored["er_dependence_risk_score"].rank(
        method="dense", ascending=False
    ).astype(int)
    scored["risk_level"] = pd.cut(
        scored["er_dependence_risk_score"],
        bins=[-0.1, 45, 65, 100],
        labels=["Low", "Moderate", "High"],
    ).astype(str)
    scored["low_primary_care_access"] = scored["clinic_access_index"] < 35
    scored["low_hospital_access"] = scored["hospital_access_index"] < 25
    scored["access_gap_score"] = (
        (100 - scored["healthcare_access_score"]) * 0.55
        + scored["er_dependence_risk_score"] * 0.45
    ).round(1)
    scored["access_gap_rank"] = scored["access_gap_score"].rank(
        method="dense", ascending=False
    ).astype(int)
    scored["market_facility_share"] = (
        scored["total_facilities"] / scored["total_facilities"].sum() * 100
    ).round(1)
    scored["clinic_share_of_facilities"] = (
        scored["primary_care_clinics"]
        .div(scored["total_facilities"].replace(0, pd.NA))
        .mul(100)
        .fillna(0)
        .round(1)
    )
    scored["hospital_share_of_facilities"] = (
        scored["hospitals"]
        .div(scored["total_facilities"].replace(0, pd.NA))
        .mul(100)
        .fillna(0)
        .round(1)
    )

    scored["risk_driver_summary"] = scored.apply(build_risk_driver_summary, axis=1)
    scored["access_story"] = scored.apply(build_access_story, axis=1)
    scored["priority_recommendation"] = scored.apply(build_priority_recommendation, axis=1)
    return scored.sort_values(["risk_rank", "county"]).reset_index(drop=True)


def build_risk_driver_summary(row: pd.Series) -> str:
    drivers = []
    if row["uninsured_rate"] >= 8.5:
        drivers.append("higher uninsured rate")
    if row["poverty_rate"] >= 17.5:
        drivers.append("higher poverty rate")
    if row["clinic_access_index"] < 35:
        drivers.append("low clinic access")
    if row["hospital_access_index"] < 25:
        drivers.append("low hospital access")
    if row["synthetic_er_visits_per_1k"] >= 465:
        drivers.append("higher modeled ER use")
    if not drivers:
        drivers.append("comparatively stronger access profile")
    return ", ".join(drivers)


def build_access_story(row: pd.Series) -> str:
    if row["risk_level"] == "High" and row["low_primary_care_access"]:
        return "High risk with limited primary care availability relative to population."
    if row["risk_level"] == "High":
        return "High modeled ER dependence risk despite some visible facility access points."
    if row["healthcare_access_score"] >= 55:
        return "Stronger modeled access profile compared with other project counties."
    if row["low_primary_care_access"]:
        return "Primary care availability is a key access watchpoint."
    return "Moderate access profile; monitor affordability and service mix indicators."


def build_priority_recommendation(row: pd.Series) -> str:
    if row["risk_level"] == "High" and row["low_primary_care_access"]:
        return "Prioritize primary care access, insurance outreach, and avoidable ER-use reduction."
    if row["risk_level"] == "High":
        return "Prioritize affordability, care navigation, and high-utilization prevention."
    if row["low_hospital_access"]:
        return "Monitor hospital/ED availability and referral pathways."
    if row["low_primary_care_access"]:
        return "Strengthen clinic capacity and preventive-care access."
    return "Maintain access strengths and monitor changes over time."


def build_community_metrics() -> pd.DataFrame:
    demographics = pd.DataFrame(CENTRAL_VALLEY_COUNTY_DATA)
    facilities = build_facility_summary(clean_facility_data(load_facility_data()))
    metrics = demographics.merge(facilities, on="county", how="left")
    facility_count_columns = [
        "total_facilities",
        "primary_care_clinics",
        "hospitals",
        "emergency_departments",
        "mapped_facilities",
    ]
    metrics[facility_count_columns] = metrics[facility_count_columns].fillna(0).astype(int)
    return add_scores(metrics)


def validate_outputs(df: pd.DataFrame) -> None:
    required = {
        "county",
        "population",
        "uninsured_rate",
        "poverty_rate",
        "primary_care_clinics",
        "hospitals",
        "healthcare_access_score",
        "er_dependence_risk_score",
        "risk_level",
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Final table missing expected columns: {sorted(missing)}")
    if df["county"].duplicated().any():
        duplicates = df.loc[df["county"].duplicated(), "county"].tolist()
        raise ValueError(f"Duplicate county rows found: {duplicates}")
    score_columns = ["healthcare_access_score", "er_dependence_risk_score"]
    for column in score_columns:
        if not df[column].between(0, 100).all():
            raise ValueError(f"{column} contains values outside 0-100.")


def write_data_dictionary(path: Path) -> None:
    rows = [
        ("county", "County name used as the community unit of analysis."),
        ("fips", "County FIPS code for future joins to map geometry."),
        ("region", "Central Valley subregion grouping."),
        ("rural_urban_category", "Synthetic rural/urban classification for filtering."),
        ("population", "Synthetic county population estimate for portfolio analysis."),
        ("median_household_income", "Synthetic median household income in US dollars."),
        ("poverty_rate", "Synthetic percent of residents below poverty level."),
        ("uninsured_rate", "Synthetic percent of residents without health insurance."),
        ("primary_care_clinics", "Count of public CDPH facility records classified as clinic access points."),
        ("hospitals", "Count of public CDPH facility records classified as hospitals."),
        ("emergency_departments", "General acute care hospitals used as an ED availability proxy."),
        ("clinics_per_100k", "Primary care clinics per 100,000 residents."),
        ("hospitals_per_100k", "Hospitals per 100,000 residents."),
        ("facilities_per_100k", "All counted healthcare facilities per 100,000 residents."),
        ("healthcare_access_score", "0-100 composite score where higher means stronger modeled access."),
        ("er_dependence_risk_score", "0-100 composite score where higher means greater modeled ER dependence risk."),
        ("access_gap_score", "0-100 composite score combining low access and higher ER dependence risk."),
        ("risk_driver_summary", "Short explanation of the main indicators contributing to modeled risk."),
        ("access_story", "Plain-language interpretation of each county access profile."),
        ("priority_recommendation", "Suggested public-health planning focus based on modeled indicators."),
        ("risk_level", "Low, Moderate, or High risk band based on ER dependence risk score."),
    ]
    dictionary = pd.DataFrame(rows, columns=["field", "definition"])
    dictionary.to_csv(path, index=False)


def run_pipeline() -> BuildResult:
    ensure_directories()

    cleaned_facilities = clean_facility_data(load_facility_data())
    community_metrics = build_community_metrics()
    validate_outputs(community_metrics)

    cleaned_facilities_path = PROCESSED_DIR / "cleaned_healthcare_facilities.csv"
    community_metrics_path = PROCESSED_DIR / "community_healthcare_access_metrics.csv"
    ranked_risk_path = OUTPUT_DIR / "final_ranked_er_access_risk_table.csv"
    insight_summary_path = OUTPUT_DIR / "insight_summary_by_county.csv"
    excel_path = OUTPUT_DIR / "er_healthcare_access_risk_outputs.xlsx"
    dictionary_path = ROOT_DIR / "docs" / "data_dictionary.csv"

    cleaned_facilities.to_csv(cleaned_facilities_path, index=False)
    community_metrics.to_csv(community_metrics_path, index=False)
    community_metrics.to_csv(ranked_risk_path, index=False)
    insight_columns = [
        "access_gap_rank",
        "risk_rank",
        "county",
        "region",
        "rural_urban_category",
        "population",
        "total_facilities",
        "facilities_per_100k",
        "clinics_per_100k",
        "hospitals_per_100k",
        "healthcare_access_score",
        "er_dependence_risk_score",
        "access_gap_score",
        "risk_level",
        "risk_driver_summary",
        "access_story",
        "priority_recommendation",
    ]
    community_metrics[insight_columns].sort_values("access_gap_rank").to_csv(
        insight_summary_path, index=False
    )
    write_data_dictionary(dictionary_path)

    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        community_metrics.to_excel(writer, sheet_name="Ranked Risk Table", index=False)
        community_metrics[insight_columns].sort_values("access_gap_rank").to_excel(
            writer, sheet_name="Insight Summary", index=False
        )
        cleaned_facilities.to_excel(writer, sheet_name="Cleaned Facilities", index=False)
        pd.read_csv(dictionary_path).to_excel(writer, sheet_name="Data Dictionary", index=False)

    return BuildResult(
        cleaned_facilities_path=cleaned_facilities_path,
        community_metrics_path=community_metrics_path,
        ranked_risk_path=ranked_risk_path,
        insight_summary_path=insight_summary_path,
        excel_path=excel_path,
    )


if __name__ == "__main__":
    result = run_pipeline()
    print(f"Built {PROJECT_TITLE}")
    print(f"Cleaned facilities: {result.cleaned_facilities_path}")
    print(f"Community metrics: {result.community_metrics_path}")
    print(f"Ranked risk table: {result.ranked_risk_path}")
    print(f"Excel workbook: {result.excel_path}")
