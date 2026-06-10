# ER Wait Time & Healthcare Access Inequality Dashboard

## Project Overview

This portfolio project analyzes which California Central Valley communities may face the highest healthcare access risk and how that could contribute to emergency room dependence. It combines public healthcare facility data with synthetic county-level population, income, poverty, uninsured, rural/urban, and ER utilization indicators.

The dashboard is designed to tell a clearer portfolio story: where access gaps appear largest, which indicators are driving those gaps, and what planning priority each county may need.

The project is designed for healthcare analyst, public health analyst, data analyst, and business intelligence analyst portfolios.

## Key Question

Which communities may face the highest healthcare access risk, and how might that contribute to emergency room dependence?

## Privacy Statement

This project uses public datasets and synthetic county-level indicators only. It does not use patient-level data, medical records, claims, appointment records, addresses of patients, or protected health information.

## Data Sources

- Public facility data: California Department of Public Health Licensed and Certified Healthcare Facility Listing.
- Synthetic county-level indicators: population, median household income, poverty rate, uninsured rate, rural/urban category, and ER visit rate.

The project starts with Central Valley counties and is structured so additional California or U.S. counties can be added later.

## Features

- Cleans and standardizes public healthcare facility data with Python and pandas.
- Counts hospitals, primary care clinics, and emergency department proxy locations by county.
- Creates a healthcare access score by county.
- Creates an ER dependence risk score using uninsured rate, poverty rate, clinic availability, hospital availability, population size, and synthetic ER visit rate.
- Creates an access gap score that combines lower modeled access with higher modeled ER dependence risk.
- Adds plain-language insight fields: risk drivers, access story, and priority recommendation.
- Ranks communities from highest to lowest healthcare access risk.
- Builds an interactive Streamlit and Plotly dashboard.
- Includes county, region, rural/urban, and risk-level filters.
- Exports cleaned CSV files, a ranked risk table, an insight summary, a data dictionary, and an Excel workbook.

## Dashboard Views

- Polished overview with insight cards for highest risk, largest access gap, lowest access score, and highest modeled ER use.
- Map of access gap and ER dependence risk by county.
- Access gap score ranking by county.
- Access score vs ER dependence risk quadrant chart.
- Equity signal charts for uninsured rate, poverty rate, rural/urban category, and population per clinic.
- Service mix charts comparing clinics, hospitals, and ED proxy locations.
- County deep dive with access story, priority recommendation, and radar profile.
- Downloadable filtered risk table.

## Folder Structure

```text
.
├── dashboard/
│   └── app.py
├── data/
│   ├── california_healthcare_facilities_raw.csv
│   ├── processed/
│   └── raw/
├── docs/
│   ├── data_dictionary.csv
│   ├── data_sources.md
│   └── linkedin_project_summary.md
├── output/
│   ├── final_ranked_er_access_risk_table.csv
│   └── er_healthcare_access_risk_outputs.xlsx
├── src/
│   └── er_access_pipeline.py
├── main.py
├── README.md
└── requirements.txt
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the cleaned datasets and ranked outputs:

```bash
python main.py
```

Run the interactive dashboard:

```bash
streamlit run dashboard/app.py
```

## Final Outputs

- `data/processed/cleaned_healthcare_facilities.csv`
- `data/processed/community_healthcare_access_metrics.csv`
- `output/final_ranked_er_access_risk_table.csv`
- `output/insight_summary_by_county.csv`
- `output/er_healthcare_access_risk_outputs.xlsx`
- `docs/data_dictionary.csv`
- `docs/linkedin_project_summary.md`

## Scoring Approach

The healthcare access score is a 0-100 composite score where higher means stronger modeled access. It combines clinic availability, hospital availability, insurance access, poverty burden, and income.

The ER dependence risk score is a 0-100 composite score where higher means greater modeled risk. It uses uninsured rate, poverty rate, low clinic availability, low hospital availability, population size, and synthetic ER visits per 1,000 residents.

The access gap score is a 0-100 composite score where higher means a county has both lower modeled access and higher modeled ER dependence risk. This is useful for prioritization because it highlights communities where access limitations and utilization pressure may overlap.

## Project Screenshots

Add screenshots after running the Streamlit dashboard:

- Dashboard overview
- High-risk county map
- Risk ranking chart
- Final ranked table

## 3-Sentence Project Summary

This portfolio project analyzes healthcare access risk across California Central Valley counties using public healthcare facility data and synthetic county-level demographic indicators. The dashboard ranks communities by modeled ER dependence risk and compares uninsured rate, poverty rate, clinic availability, hospital availability, and synthetic ER visit rates. The goal is to show how healthcare analytics can help public health teams identify communities that may need stronger primary care access, outreach, or resource planning.

## Technical Skills

- Python
- pandas
- Streamlit
- Plotly
- Healthcare analytics
- Public health analytics
- Composite risk scoring
- Insight storytelling
- Interactive visualization
- Data validation
- CSV and Excel reporting
- Interactive dashboard design

## Business/Public-Health Value

- Identifies counties that may have higher emergency room dependence risk.
- Highlights communities with lower primary care availability relative to population.
- Supports better targeting for public health outreach, planning, and resource allocation.
- Demonstrates privacy-safe healthcare analytics without PHI.

## Future Improvements

- Replace synthetic indicators with ACS, Census, CDC PLACES, HRSA, or HPSA public datasets.
- Add ZIP-code level analysis.
- Add true travel-time analysis to nearby clinics and emergency departments.
- Expand to all California counties and then all U.S. counties.
- Add year-over-year trends.
- Incorporate aggregated public ER utilization data if available.
