from src.er_access_pipeline import run_pipeline


if __name__ == "__main__":
    result = run_pipeline()
    print("ER Wait Time & Healthcare Access Inequality Dashboard outputs created.")
    print(f"Cleaned facilities: {result.cleaned_facilities_path}")
    print(f"Community metrics: {result.community_metrics_path}")
    print(f"Ranked risk table: {result.ranked_risk_path}")
    print(f"Insight summary: {result.insight_summary_path}")
    print(f"Excel workbook: {result.excel_path}")
