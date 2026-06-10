from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
RISK_TABLE_PATH = ROOT_DIR / "output" / "final_ranked_er_access_risk_table.csv"
INSIGHT_TABLE_PATH = ROOT_DIR / "output" / "insight_summary_by_county.csv"

RISK_COLORS = {"High": "#c2410c", "Moderate": "#ca8a04", "Low": "#0f766e"}
REGION_COLORS = {
    "San Joaquin Valley": "#2563eb",
    "Northern Sacramento Valley": "#0f766e",
    "Sacramento Metro": "#7c3aed",
}
ACCENT_COLORS = ["#2563eb", "#0f766e", "#7c3aed", "#c2410c", "#ca8a04"]


st.set_page_config(
    page_title="Healthcare Access & ER Dependence Dashboard",
    page_icon="CA",
    layout="wide",
)


def apply_page_style() -> None:
    st.markdown(
        """
        <style>
        :root {
            --ink: #132033;
            --muted: #526174;
            --line: #d8e2ee;
            --panel: #ffffff;
            --soft: #f7fafc;
            --blue: #2563eb;
            --teal: #0f766e;
            --violet: #7c3aed;
            --amber: #ca8a04;
            --red: #c2410c;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background:
                linear-gradient(180deg, #eef6ff 0%, #f8fbff 34%, #ffffff 100%);
            color: var(--ink);
        }

        .block-container {
            padding-top: 1.05rem;
            padding-bottom: 2.2rem;
            max-width: 1500px;
        }

        [data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, #f8fbff 0%, #ffffff 100%);
            border-right: 1px solid var(--line);
        }

        [data-testid="stSidebar"] h1 {
            font-size: 1.25rem;
            margin-bottom: 0.65rem;
        }

        [data-baseweb="tag"] {
            border-radius: 999px;
            background: #eaf2ff;
            color: #1d4ed8;
            border: 1px solid #cfe0ff;
        }

        section.main div[data-testid="stVerticalBlock"] > div:has(.stPlotlyChart),
        section.main div[data-testid="stVerticalBlock"] > div:has([data-testid="stDataFrame"]) {
            border-radius: 14px;
        }

        h1, h2, h3 {
            letter-spacing: 0;
        }

        .hero {
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(37, 99, 235, 0.18);
            border-radius: 18px;
            padding: 28px 30px 24px;
            background:
                linear-gradient(135deg, rgba(37,99,235,0.14), rgba(15,118,110,0.10) 50%, rgba(124,58,237,0.09)),
                #ffffff;
            box-shadow: 0 18px 55px rgba(30, 64, 175, 0.12);
            margin-bottom: 18px;
        }

        .hero::after {
            content: "";
            position: absolute;
            inset: auto -18px -52px 56%;
            height: 170px;
            background:
                repeating-linear-gradient(
                    135deg,
                    rgba(37, 99, 235, 0.08) 0,
                    rgba(37, 99, 235, 0.08) 2px,
                    transparent 2px,
                    transparent 12px
                );
            transform: rotate(-2deg);
            pointer-events: none;
        }

        .hero h1 {
            position: relative;
            margin: 0 0 10px;
            font-size: clamp(2.1rem, 4.2vw, 4.6rem);
            line-height: 1.1;
            max-width: 970px;
            color: #101828;
        }

        .hero p {
            position: relative;
            margin: 0;
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.5;
            max-width: 930px;
        }

        .hero-kicker {
            position: relative;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 13px;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            border: 1px solid rgba(37, 99, 235, 0.18);
            border-radius: 999px;
            padding: 6px 10px;
            background: rgba(255, 255, 255, 0.76);
            color: #25415f;
            font-size: 0.77rem;
            font-weight: 750;
            text-transform: uppercase;
        }

        .pill-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--teal);
        }

        .insight-card {
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(216, 226, 238, 0.95);
            border-radius: 12px;
            padding: 11px 12px 10px;
            background:
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,251,255,0.98));
            min-height: 94px;
            box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
        }

        .insight-card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--blue), var(--teal), var(--violet));
        }

        .insight-label {
            color: var(--muted);
            font-size: 0.62rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 5px;
        }

        .insight-value {
            color: var(--ink);
            font-size: 1.2rem;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 4px;
        }

        .insight-note {
            color: var(--muted);
            font-size: 0.72rem;
            line-height: 1.25;
        }

        .callout {
            border: 1px solid #cfe0ff;
            border-left: 6px solid var(--blue);
            border-radius: 14px;
            padding: 15px 17px;
            background:
                linear-gradient(90deg, rgba(37,99,235,0.08), rgba(15,118,110,0.05)),
                #ffffff;
            color: var(--ink);
            margin: 12px 0 16px;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
        }

        .callout strong {
            display: block;
            margin-bottom: 5px;
        }

        .mini-metric-grid {
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: 10px;
            margin: 12px 0 14px;
        }

        .mini-metric {
            border: 1px solid rgba(216, 226, 238, 0.9);
            border-radius: 12px;
            padding: 10px 11px;
            background:
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,251,255,0.98));
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        }

        .mini-metric-label {
            color: var(--muted);
            font-size: 0.66rem;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 3px;
        }

        .mini-metric-value {
            color: var(--ink);
            font-size: 1.28rem;
            line-height: 1.1;
            font-weight: 850;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: rgba(255,255,255,0.9);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 8px;
            width: 100%;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 12px;
            padding: 10px 10px;
            flex: 1 1 0;
            justify-content: center;
            font-size: 0.9rem;
            font-weight: 800;
        }

        .stTabs [aria-selected="true"] {
            background: #132033;
            color: #ffffff;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
        }

        .stDownloadButton button {
            border-radius: 999px;
            border: 1px solid #1d4ed8;
            background: #2563eb;
            color: #ffffff;
            font-weight: 750;
        }

        @media (max-width: 900px) {
            .mini-metric-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .hero {
                padding: 22px 20px;
            }

            .hero h1 {
                font-size: 2.15rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_chart_theme(fig: go.Figure, height: int | None = None) -> go.Figure:
    fig.update_layout(
        font=dict(family="Inter, Arial, sans-serif", color="#132033"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#ffffff",
        title=dict(font=dict(size=18, color="#132033"), x=0.01, xanchor="left"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(255,255,255,0)",
        ),
        margin=dict(l=18, r=18, t=58, b=34),
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="#e8eef6",
        zeroline=False,
        linecolor="#d8e2ee",
        tickfont=dict(color="#526174"),
        title_font=dict(color="#526174"),
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#eef3f8",
        zeroline=False,
        linecolor="#d8e2ee",
        tickfont=dict(color="#526174"),
        title_font=dict(color="#526174"),
    )
    if height is not None:
        fig.update_layout(height=height)
    return fig


@st.cache_data
def load_data(path: Path, modified_time: float) -> pd.DataFrame:
    if not path.exists():
        st.error("Run `python main.py` first to generate the ranked risk table.")
        st.stop()
    df = pd.read_csv(path)
    required_columns = {
        "access_gap_score",
        "access_gap_rank",
        "healthcare_access_score",
        "er_dependence_risk_score",
        "risk_driver_summary",
        "access_story",
        "priority_recommendation",
    }
    missing_columns = sorted(required_columns.difference(df.columns))
    if missing_columns:
        st.error(
            "The ranked output is missing required dashboard columns: "
            f"{', '.join(missing_columns)}. Run `python main.py` to rebuild the outputs."
        )
        st.stop()
    return df


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    with st.sidebar:
        st.title("Filters")
        selected_counties = st.multiselect(
            "County",
            options=sorted(df["county"].unique()),
            default=sorted(df["county"].unique()),
        )
        selected_regions = st.multiselect(
            "Region",
            options=sorted(df["region"].unique()),
            default=sorted(df["region"].unique()),
        )
        selected_categories = st.multiselect(
            "Rural/urban category",
            options=sorted(df["rural_urban_category"].unique()),
            default=sorted(df["rural_urban_category"].unique()),
        )
        selected_risk = st.multiselect(
            "Risk level",
            options=["High", "Moderate", "Low"],
            default=["High", "Moderate", "Low"],
        )
        st.divider()
        st.caption(
            "This project uses public CDPH facility data and synthetic county-level indicators. "
            "It does not use patient records, employer data, or PHI."
        )

    return df[
        df["county"].isin(selected_counties)
        & df["region"].isin(selected_regions)
        & df["rural_urban_category"].isin(selected_categories)
        & df["risk_level"].isin(selected_risk)
    ].copy()


def risk_color_scale() -> list[tuple[float, str]]:
    return [
        (0.0, "#15803d"),
        (0.45, "#f2c94c"),
        (0.72, "#f97316"),
        (1.0, "#b42318"),
    ]


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
          <div class="hero-kicker">
            <span class="pill"><span class="pill-dot"></span>Public-health analytics</span>
            <span class="pill">Central Valley focus</span>
            <span class="pill">No PHI</span>
          </div>
          <h1>Healthcare Access & ER Dependence Risk</h1>
          <p>
            A portfolio dashboard for exploring where Central Valley communities may face higher
            healthcare access pressure, using public facility counts and privacy-safe county-level
            indicators.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_insight_cards(df: pd.DataFrame) -> None:
    highest_risk = df.sort_values("er_dependence_risk_score", ascending=False).iloc[0]
    largest_gap = df.sort_values("access_gap_score", ascending=False).iloc[0]
    lowest_access = df.sort_values("healthcare_access_score", ascending=True).iloc[0]
    highest_er = df.sort_values("synthetic_er_visits_per_1k", ascending=False).iloc[0]

    card_data = [
        (
            "ER Risk",
            highest_risk["county"],
            f"{highest_risk['er_dependence_risk_score']:.1f} score; {highest_risk['risk_level']} risk.",
        ),
        (
            "Access Gap",
            largest_gap["county"],
            f"{largest_gap['access_gap_score']:.1f} score; limited care availability.",
        ),
        (
            "Lowest Access",
            lowest_access["county"],
            f"{lowest_access['healthcare_access_score']:.1f} score; priority county.",
        ),
        (
            "Modeled ER Use",
            highest_er["county"],
            f"{highest_er['synthetic_er_visits_per_1k']:.0f} visits per 1,000.",
        ),
    ]

    cols = st.columns(4)
    for col, (label, value, note) in zip(cols, card_data):
        col.markdown(
            f"""
            <div class="insight-card">
              <div class="insight-label">{label}</div>
              <div class="insight-value">{value}</div>
              <div class="insight-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_metric_row(df: pd.DataFrame) -> None:
    metrics = [
        ("Counties", f"{len(df):,}"),
        ("Population", f"{df['population'].sum():,.0f}"),
        ("Avg Access", f"{df['healthcare_access_score'].mean():.1f}"),
        ("Avg Risk", f"{df['er_dependence_risk_score'].mean():.1f}"),
        ("High Risk", f"{(df['risk_level'] == 'High').sum():,}"),
        ("Low Clinic Access", f"{df['low_primary_care_access'].sum():,}"),
    ]
    metric_html = "".join(
        f'<div class="mini-metric"><div class="mini-metric-label">{label}</div>'
        f'<div class="mini-metric-value">{value}</div></div>'
        for label, value in metrics
    )
    st.markdown(f'<div class="mini-metric-grid">{metric_html}</div>', unsafe_allow_html=True)


def render_map(df: pd.DataFrame) -> None:
    fig = px.scatter_map(
        df,
        lat="latitude",
        lon="longitude",
        color="er_dependence_risk_score",
        size="access_gap_score",
        hover_name="county",
        hover_data={
            "region": True,
            "risk_level": True,
            "access_gap_score": ":.1f",
            "healthcare_access_score": ":.1f",
            "er_dependence_risk_score": ":.1f",
            "uninsured_rate": ":.1f",
            "poverty_rate": ":.1f",
            "clinics_per_100k": ":.2f",
            "hospitals_per_100k": ":.2f",
            "risk_driver_summary": True,
            "latitude": False,
            "longitude": False,
        },
        color_continuous_scale=risk_color_scale(),
        zoom=5,
        height=640,
    )
    fig.update_traces(marker=dict(opacity=0.88, sizemin=11))
    fig.update_layout(
        map_style="carto-positron",
        margin=dict(l=0, r=0, t=8, b=0),
        coloraxis_colorbar=dict(title="Risk score", thickness=14, bgcolor="rgba(255,255,255,0.78)"),
    )
    st.plotly_chart(fig, width="stretch")


def render_priority_table(df: pd.DataFrame) -> None:
    st.subheader("Priority Planning View")
    columns = [
        "access_gap_rank",
        "risk_rank",
        "county",
        "region",
        "risk_level",
        "access_gap_score",
        "healthcare_access_score",
        "er_dependence_risk_score",
        "risk_driver_summary",
        "priority_recommendation",
    ]
    st.dataframe(
        df.sort_values("access_gap_rank")[columns],
        width="stretch",
        hide_index=True,
    )


def render_overview_charts(df: pd.DataFrame) -> None:
    left, right = st.columns([1.1, 1])

    with left:
        ranked = df.sort_values("access_gap_score", ascending=True)
        fig = px.bar(
            ranked,
            x="access_gap_score",
            y="county",
            color="risk_level",
            orientation="h",
            title="Access Gap Score by County",
            color_discrete_map=RISK_COLORS,
            hover_data=["risk_driver_summary", "priority_recommendation"],
        )
        fig.update_traces(marker_line_width=0, opacity=0.94)
        fig.update_layout(xaxis_title="Access gap score", yaxis_title="", legend_title="")
        apply_chart_theme(fig, height=560)
        st.plotly_chart(fig, width="stretch")

    with right:
        fig = px.scatter(
            df,
            x="healthcare_access_score",
            y="er_dependence_risk_score",
            size="population",
            color="risk_level",
            hover_name="county",
            text="county",
            title="Access Score vs ER Dependence Risk",
            color_discrete_map=RISK_COLORS,
        )
        fig.update_traces(
            textposition="top center",
            textfont_size=10,
            marker=dict(line=dict(width=1.2, color="#ffffff"), opacity=0.88),
        )
        fig.update_layout(
            xaxis_title="Healthcare access score",
            yaxis_title="ER dependence risk score",
            legend_title="",
        )
        apply_chart_theme(fig, height=560)
        st.plotly_chart(fig, width="stretch")


def render_equity_charts(df: pd.DataFrame) -> None:
    left, right = st.columns(2)

    with left:
        fig = px.scatter(
            df,
            x="uninsured_rate",
            y="poverty_rate",
            size="er_dependence_risk_score",
            color="risk_level",
            hover_name="county",
            title="Affordability Pressure: Uninsured Rate vs Poverty Rate",
            color_discrete_map=RISK_COLORS,
        )
        fig.update_traces(marker=dict(line=dict(width=1.2, color="#ffffff"), opacity=0.88))
        fig.update_layout(xaxis_title="Uninsured rate (%)", yaxis_title="Poverty rate (%)")
        apply_chart_theme(fig, height=470)
        st.plotly_chart(fig, width="stretch")

    with right:
        fig = px.bar(
            df.sort_values("population_per_clinic", ascending=False),
            x="county",
            y="population_per_clinic",
            color="rural_urban_category",
            title="Population per Primary Care Clinic",
            color_discrete_sequence=ACCENT_COLORS,
        )
        fig.update_traces(marker_line_width=0, opacity=0.94)
        fig.update_layout(xaxis_title="", yaxis_title="Residents per clinic")
        apply_chart_theme(fig, height=470)
        st.plotly_chart(fig, width="stretch")

    left, right = st.columns(2)

    with left:
        fig = px.box(
            df,
            x="rural_urban_category",
            y="er_dependence_risk_score",
            color="rural_urban_category",
            points="all",
            title="Risk Score Distribution by Rural/Urban Category",
            color_discrete_sequence=ACCENT_COLORS,
        )
        fig.update_layout(xaxis_title="", yaxis_title="ER dependence risk score", showlegend=False)
        apply_chart_theme(fig, height=430)
        st.plotly_chart(fig, width="stretch")

    with right:
        region_summary = (
            df.groupby("region", as_index=False)
            .agg(
                avg_access_gap=("access_gap_score", "mean"),
                avg_risk=("er_dependence_risk_score", "mean"),
                counties=("county", "count"),
            )
            .round(1)
        )
        fig = px.bar(
            region_summary.sort_values("avg_access_gap"),
            x="avg_access_gap",
            y="region",
            color="region",
            orientation="h",
            text="avg_access_gap",
            title="Average Access Gap by Region",
            color_discrete_map=REGION_COLORS,
        )
        fig.update_traces(marker_line_width=0, opacity=0.94, textposition="outside")
        fig.update_layout(xaxis_title="Average access gap score", yaxis_title="", showlegend=False)
        apply_chart_theme(fig, height=430)
        st.plotly_chart(fig, width="stretch")


def render_service_mix(df: pd.DataFrame) -> None:
    left, right = st.columns(2)

    with left:
        mix_df = df.melt(
            id_vars=["county", "risk_level"],
            value_vars=["primary_care_clinics", "hospitals", "emergency_departments"],
            var_name="facility_category",
            value_name="facility_count",
        )
        fig = px.bar(
            mix_df,
            x="county",
            y="facility_count",
            color="facility_category",
            title="Service Mix by County",
            color_discrete_map={
                "primary_care_clinics": "#2563eb",
                "hospitals": "#0f766e",
                "emergency_departments": "#ca8a04",
            },
        )
        fig.update_traces(marker_line_width=0, opacity=0.95)
        fig.update_layout(xaxis_title="", yaxis_title="Facility count", legend_title="")
        apply_chart_theme(fig, height=500)
        st.plotly_chart(fig, width="stretch")

    with right:
        fig = px.scatter(
            df,
            x="clinics_per_100k",
            y="hospitals_per_100k",
            size="total_facilities",
            color="region",
            hover_name="county",
            title="Clinic Availability vs Hospital Availability",
            color_discrete_map=REGION_COLORS,
        )
        fig.update_traces(marker=dict(line=dict(width=1.2, color="#ffffff"), opacity=0.88))
        fig.update_layout(
            xaxis_title="Clinics per 100k residents",
            yaxis_title="Hospitals per 100k residents",
            legend_title="",
        )
        apply_chart_theme(fig, height=500)
        st.plotly_chart(fig, width="stretch")


def render_county_deep_dive(df: pd.DataFrame) -> None:
    selected = st.selectbox(
        "Select a county",
        options=df.sort_values("access_gap_rank")["county"].tolist(),
    )
    row = df[df["county"] == selected].iloc[0]

    st.markdown(
        f"""
        <div class="callout">
          <strong>{row['county']} County insight</strong>
          {row['access_story']} Main drivers: {row['risk_driver_summary']}.
          Recommended focus: {row['priority_recommendation']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(5)
    cols[0].metric("Access Gap Rank", f"#{int(row['access_gap_rank'])}")
    cols[1].metric("Risk Rank", f"#{int(row['risk_rank'])}")
    cols[2].metric("Access Score", f"{row['healthcare_access_score']:.1f}")
    cols[3].metric("Risk Score", f"{row['er_dependence_risk_score']:.1f}")
    cols[4].metric("Facilities per 100k", f"{row['facilities_per_100k']:.1f}")

    radar_categories = [
        "Clinic access",
        "Hospital access",
        "Insurance access",
        "Poverty resilience",
        "Income index",
    ]
    radar_values = [
        row["clinic_access_index"],
        row["hospital_access_index"],
        row["insurance_access_index"],
        row["poverty_access_index"],
        row["income_access_index"],
    ]
    fig = go.Figure(
        data=go.Scatterpolar(
            r=radar_values + [radar_values[0]],
            theta=radar_categories + [radar_categories[0]],
            fill="toself",
            line_color="#2563eb",
            fillcolor="rgba(37,99,235,0.22)",
        )
    )
    fig.update_layout(
        title=f"{row['county']} County Access Index Profile",
        polar=dict(
            bgcolor="#ffffff",
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#e8eef6"),
            angularaxis=dict(gridcolor="#e8eef6"),
        ),
        showlegend=False,
    )
    apply_chart_theme(fig, height=500)
    st.plotly_chart(fig, width="stretch")


def render_data_table(df: pd.DataFrame) -> None:
    display_columns = [
        "access_gap_rank",
        "risk_rank",
        "county",
        "region",
        "rural_urban_category",
        "population",
        "total_facilities",
        "primary_care_clinics",
        "hospitals",
        "facilities_per_100k",
        "clinics_per_100k",
        "hospitals_per_100k",
        "uninsured_rate",
        "poverty_rate",
        "healthcare_access_score",
        "er_dependence_risk_score",
        "access_gap_score",
        "risk_level",
        "risk_driver_summary",
        "priority_recommendation",
    ]
    st.dataframe(df[display_columns].sort_values("access_gap_rank"), width="stretch", hide_index=True)

    csv = df[display_columns].to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download filtered insight table",
        data=csv,
        file_name="filtered_healthcare_access_insight_table.csv",
        mime="text/csv",
    )


apply_page_style()
data = load_data(RISK_TABLE_PATH, RISK_TABLE_PATH.stat().st_mtime if RISK_TABLE_PATH.exists() else 0)
filtered = apply_filters(data)

render_hero()

if filtered.empty:
    st.warning("No communities match the current filters.")
    st.stop()

overview_tab, equity_tab, services_tab, county_tab, table_tab = st.tabs(
    ["Overview", "Equity Signals", "Service Mix", "County Deep Dive", "Data Table"]
)

with overview_tab:
    render_metric_row(filtered)
    render_insight_cards(filtered)
    st.markdown(
        """
        <div class="callout">
          <strong>How to read this dashboard</strong>
          Larger map markers indicate a higher access gap score, while darker color indicates higher modeled ER dependence risk.
          Use the tabs above as the main workflow: scan the overview, inspect equity signals, compare service mix, then open the county deep dive.
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_map(filtered)
    render_overview_charts(filtered)
    render_priority_table(filtered)

with equity_tab:
    render_equity_charts(filtered)

with services_tab:
    render_service_mix(filtered)

with county_tab:
    render_county_deep_dive(filtered)

with table_tab:
    render_data_table(filtered)
