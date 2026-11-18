# Power BI build guide — Diageo Commercial Analytics

A true `.pbix` file is not included: Power BI Desktop is a Windows application, and there is no supported headless way to write a binary `.pbix` from this repository. The tidy CSVs in `data/` plus this guide are enough to recreate the model and visuals in Power BI Desktop in about 20 minutes.

All figures in the CSVs are official Diageo public disclosures. Blank cells mean the figure was not found. Do not fill them with estimates. Organic growth rates are official non-GAAP measures — do not recompute “organic growth” from reported dollars.

## 1. Get the files (1 minute)

In this repository the CSVs live in `data/` (alongside `Diageo_Tableau_Data.xlsx`). Copy that folder, or copy these CSVs:

| File | Role |
|---|---|
| `dim_fiscal_year.csv` | Date/year dimension |
| `dim_region.csv` | Region dimension (sort order included) |
| `dim_category.csv` | Category dimension |
| `dim_brand.csv` | Brand dimension |
| `dim_source.csv` | Source catalogue (PDF and web URLs) |
| `fact_group_kpis.csv` | One row per fiscal year, group measures |
| `fact_regional.csv` | One row per year and region |
| `fact_category.csv` | One row per year and category |
| `fact_brands.csv` | One row per year and brand |
| `fact_nam_canada.csv` | One row per year and NAM market (including Canada) |

## 2. Load into Power BI Desktop (2 minutes)

1. Open Power BI Desktop → **Get data** → **Text/CSV** (or **Folder** if you point at `data/`).
2. Load all 10 CSVs.
3. Open **Power Query**. For every `*_pct`, `*_pps` column, set the type to **Decimal number**. For `*_usd_m`, `*_eu_m`, `*_cents`, `*_bps`, use **Decimal number** or **Fixed decimal**. Leave text columns as text.
4. Close and Apply.

Optional: in Power Query, replace empty strings with null so blanks stay blank.

## 3. Star schema relationships (3 minutes)

Create a standard star, with dimensions on the one-side:

```
dim_fiscal_year[fiscal_year]  1—*  fact_group_kpis[fiscal_year]
dim_fiscal_year[fiscal_year]  1—*  fact_regional[fiscal_year]
dim_fiscal_year[fiscal_year]  1—*  fact_category[fiscal_year]
dim_fiscal_year[fiscal_year]  1—*  fact_brands[fiscal_year]
dim_fiscal_year[fiscal_year]  1—*  fact_nam_canada[fiscal_year]

dim_region[region]            1—*  fact_regional[region]
dim_category[category]        1—*  fact_category[category]
dim_brand[brand]              1—*  fact_brands[brand]
```

Cross-filter direction: **single** (dimension filters facts). Do not relate the fact tables to each other.

Hide the raw foreign keys on the fact tables if you like, and use the dimension fields on visuals (for example `dim_region[region]`, `dim_fiscal_year[fiscal_year]`). Set `dim_fiscal_year[sort]` as the sort column for `fiscal_year`, and `dim_region[sort]` as the sort column for `region`.

## 4. Measures (5 minutes)

Create a measure table named `_Measures`. Paste these DAX measures. They either aggregate official dollar figures or expose official percentage fields. They do **not** invent organic growth.

```dax
-- Group (use only with fact_group_kpis, typically one year selected)
Reported Net Sales $m =
SUM ( fact_group_kpis[reported_net_sales_usd_m] )

Reported OP $m =
SUM ( fact_group_kpis[reported_operating_profit_usd_m] )

OP Before Exceptionals $m =
SUM ( fact_group_kpis[op_before_exceptionals_usd_m] )

Free Cash Flow $m =
SUM ( fact_group_kpis[free_cash_flow_usd_m] )

Marketing $m =
SUM ( fact_group_kpis[marketing_usd_m] )

-- Margins from official dollars (safe to compute; this is Diageo's own definition)
Reported OP Margin % =
DIVIDE ( [Reported OP $m], [Reported Net Sales $m] )

Adj OP Margin % =
DIVIDE ( [OP Before Exceptionals $m], [Reported Net Sales $m] )

-- Official movement fields (already percentage points, e.g. 1.7 means 1.7%).
-- Use AVERAGE or MAX in a single-year context; do not SUM them across years.
Organic NS % (official) =
AVERAGE ( fact_group_kpis[organic_ns_movement_pct] )

Organic Volume % (official) =
AVERAGE ( fact_group_kpis[organic_volume_movement_pct] )

Organic Price Mix pps (official) =
AVERAGE ( fact_group_kpis[organic_price_mix_pps] )

Organic OP % (official) =
AVERAGE ( fact_group_kpis[organic_op_movement_pct] )

-- Regional
Regional NS $m =
SUM ( fact_regional[reported_ns_usd_m] )

Regional Mix % =
DIVIDE (
    [Regional NS $m],
    CALCULATE ( [Regional NS $m], ALL ( dim_region ) )
)

Regional Organic NS % (official) =
AVERAGE ( fact_regional[organic_ns_mov_pct] )

Regional Official Share % =
AVERAGE ( fact_regional[official_share_of_group_ns_pct] )

-- Use Regional Official Share % when you want Diageo's printed share
-- (NAM 37% in FY26, and so on). Use Regional Mix % when you want the exact
-- ratio of official dollars (Corporate included). Do not expect them
-- to match to 0.1pp: official shares are rounded and often exclude Corporate.

-- Category (share is official; do not convert share × group NS into dollars)
Category Organic NS % (official) =
AVERAGE ( fact_category[organic_ns_mov_pct] )

Category Share % (official) =
AVERAGE ( fact_category[reported_ns_by_category_pct] )

-- Brands and Canada
Brand Organic NS % (official) =
AVERAGE ( fact_brands[organic_ns_mov_pct] )

Market Organic NS % (official) =
AVERAGE ( fact_nam_canada[organic_ns_mov_pct] )
```

Format the percentage and pps measures as **1 decimal**. The source values are already in percentage points (1.7, not 0.017). A custom format such as `0.0"%"` will display 1.7 as 1.7%. If you prefer Power BI’s percentage data type, divide the official field by 100 in the measure instead, and say so on the visual.

**Do not write** a measure such as `Organic Growth = this year NS / last year NS - 1`. That would be *reported* growth, not organic, and would contradict Diageo’s published organic figures (which adjust for exchange, acquisitions and disposals, and hyperinflation).

## 5. Report page and visuals (8 minutes)

Use a charcoal + amber theme so the page matches the Excel dashboard:

- Background: `#F7F3EB`
- Foreground / titles: `#2C2A26`
- Accent: `#C4A35A`
- Decline / emphasis: `#8B4A32`
- Grid: `#D9D0C3`

**Page 1 — Executive dashboard (title: Diageo Commercial Analytics)**

Slicer: `dim_fiscal_year[fiscal_year]` (default FY26).

KPI cards (new card visual, FY26 selected):

1. Reported Net Sales $m — subtitle: official reported NS movement
2. Organic NS % (official) — subtitle: volume and price/mix official fields
3. Adj OP Margin %
4. Reported OP Margin %
5. Regional Official Share % for North America (filter the card to NAM)

Visuals:

1. **Clustered column** — `Regional NS $m` by `fiscal_year`, legend `region` (exclude Corporate, or keep it). Title: “Reported net sales by region.”
2. **Clustered column + line** (combo) — columns: `Organic Volume % (official)` and `Organic Price Mix pps (official)`; line: `Organic NS % (official)`, axis `fiscal_year`. Title: “Organic net sales: volume versus price/mix.”
3. **Line chart** — `Reported OP Margin %` and `Adj OP Margin %` by `fiscal_year`. Title: “Operating margin trend.” In the footnote, state that FY23–FY24 levels are calculated from official profit divided by official net sales; FY25–FY26 are official headlines.
4. **Horizontal bar** — `Category Share % (official)` by `category`, filtered to FY26 and excluding the “Spirits” aggregate (it is a roll-up of the spirit categories). Sort descending. Title: “FY26 category mix (official share of reported NS).”
5. Optional second bar: `Category Organic NS % (official)` for FY26, same category list.
6. Optional: clustered bar of `Market Organic NS % (official)` for Canada, US Spirits, DBC USA, North America, by year.

Add a text box footnote:

> All figures are from Diageo plc preliminary results and annual reports on diageo.com. Organic measures are non-GAAP. Blank means not disclosed. Category and Canada dollar sales are not published and have not been estimated. Prepared as a portfolio piece for Rushabh Kabra — not an official Diageo report.

**Page 2 — Insights (optional)**

Copy the six takeaways from the Excel `Insights` sheet into text boxes, each next to the supporting visual (NAM trend, tequila/Crown Royal brand bars, Guinness/beer, regional organic, Canada). Every takeaway already carries its source URL.

## 6. QA before you publish (1 minute)

- FY26 reported net sales card shows **19,643**.
- FY26 organic NS shows **−2.0**, volume **−0.4**, price/mix **−1.6**.
- FY26 before-exceptional margin shows **28.9%** (5683 / 19643).
- NAM FY26 reported NS is **7,249** and official share is **37**.
- Canada FY26 organic NS is **7.7**, with the notes field visible (it includes a one-off).
- No visual invents category dollars or Canada dollars.
- A source URL is available when a value is clicked through (tooltips can show `source_url` and `notes`).

## 7. Theme

In View → Themes → Customize, set the colours above and save as a `.json` theme. There is no `.pbix` to attach; once saved, any colleague with the CSVs and this guide can rebuild the report in roughly 20 minutes.
