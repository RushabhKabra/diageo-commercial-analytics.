"""Official Diageo public figures only. Missing values are None, never estimated.

Source short codes:
  F26PR  FY26 Preliminary Results PDF, 6 August 2026
  F25PR  FY25 Preliminary Results PDF, 5 August 2025
  F24PR  FY24 Preliminary Results PDF, 30 July 2024
  AR24   Diageo Annual Report 2024 (year ended 30 June 2024)
  AR23   Diageo Annual Report 2023 (year ended 30 June 2023)
"""

SOURCES = {
    "F26PR": {
        "document": "Diageo Preliminary Results, year ended 30 June 2026 (6 August 2026)",
        "url": "https://www.diageo.com/~/media/Files/D/Diageo-V2/Diageo-Corp/press-release/2026/f26-preliminary-results-press-release.pdf",
        "web": "https://www.diageo.com/en/news-and-media/press-releases/2026/2026-preliminary-results-year-ended-30-june-2026",
    },
    "F25PR": {
        "document": "Diageo Preliminary Results, year ended 30 June 2025 (5 August 2025)",
        "url": "https://www.diageo.com/~/media/Files/D/Diageo-V2/Diageo-Corp/press-release/2025/f25-preliminary-results-press-release.pdf",
        "web": "https://www.diageo.com/en/news-and-media/press-releases/2025/2025-preliminary-results-year-ended-30-june-2025",
    },
    "F24PR": {
        "document": "Diageo Preliminary Results, year ended 30 June 2024 (30 July 2024)",
        "url": "https://www.diageo.com/~/media/Files/D/Diageo-V2/Diageo-Corp/press-release/2024/f24-prelims-results-press-release.pdf",
        "web": "https://www.diageo.com/en/news-and-media/press-releases/2024/2024-preliminary-results-year-ended-30-june-2024",
    },
    "AR25": {
        "document": "Diageo Annual Report 2025 (year ended 30 June 2025)",
        "url": "https://www.diageo.com/~/media/Files/D/Diageo-V2/Diageo-Corp/investors/results-reports-and-events/annual-reports/2025/annual-report-2025.ashx",
        "web": "https://www.diageo.com/en/investors/results-reports-and-events/annual-report-2025",
    },
    "AR24": {
        "document": "Diageo Annual Report 2024 (year ended 30 June 2024), Chief Executive's statement",
        "url": "https://www.diageo.com/~/media/Files/D/Diageo-V2/Diageo-Corp/investors/results-reports-and-events/annual-reports/diageo-annual-report-2024.pdf",
        "web": "https://www.diageo.com/en/investors/results-reports-and-events/annual-report-2024",
    },
    "AR23": {
        "document": "Diageo Annual Report 2023 (year ended 30 June 2023)",
        "url": "https://www.diageo.com/~/media/Files/D/Diageo-V2/Diageo-Corp/investors/results-reports-and-events/annual-reports/diageo-annual-report-2023.pdf",
        "web": "https://www.diageo.com/en/investors/results-reports-and-events/annual-report-2023",
    },
}

# Percentages stored as percentage points (1.7 means 1.7%), not decimals,
# so the Excel/CSV stay human-readable and match Diageo's presentation.

GROUP_KPIS = [
    {
        "fiscal_year": "FY23",
        "year_ended": "2023-06-30",
        "reported_net_sales_usd_m": 20555,
        "reported_ns_movement_pct": None,  # FY23 statutory accounts were in GBP; USD is a FY24 restatement
        "organic_ns_movement_usd_m": None,
        "organic_ns_movement_pct": 6.5,
        "organic_volume_movement_pct": -0.8,
        "organic_price_mix_pps": 7.3,
        "volume_eu_m": 243.4,
        "reported_volume_movement_pct": None,
        "reported_operating_profit_usd_m": 5547,
        "reported_op_movement_pct": None,
        "reported_op_margin_pct": 27.0,  # 5547/20555
        "reported_op_margin_basis": "Calculated as reported operating profit ÷ reported net sales, using FY24 prelim restated FY23 USD comparatives (5547/20555). Not a separately printed headline figure.",
        "op_before_exceptionals_usd_m": 6313,
        "organic_op_movement_pct": None,
        "organic_op_margin_movement_bps": None,
        "op_margin_before_exceptionals_pct": 30.7,  # 6313/20555
        "op_margin_before_exceptionals_basis": "Calculated as operating profit before exceptional items ÷ reported net sales (6313/20555) from FY24 prelim restated FY23 comparatives. Diageo defines organic/adjusted operating margin this way.",
        "gross_profit_usd_m": 12266,
        "marketing_usd_m": 3663,
        "free_cash_flow_usd_m": None,  # FY23 FCF in FY24 prelim is $2,235m — include? F24PR says F23 free cash flow $2,235m
        "eps_before_exceptionals_cents": None,  # 196.5c is in FY24 table as F23 — yes "Basic earnings per share before exceptional items 196.5" for 2023
        "recommended_dividend_cents": 98.55,
        "source_codes": "F24PR; AR23",
        "notes": (
            "Reported $ figures and volume are FY24 Preliminary Results restated/re-presented USD comparatives for the year ended 30 June 2023 "
            "(Diageo changed its presentation currency). Organic net sales +6.5%, price/mix +7.3pps and organic volume -0.8% are from the Annual Report 2023: "
            "\"Organic net sales growth of 6.5% reflects 7.3 percentage points of positive price/mix and a decline in organic volume of 0.8%.\" "
            "FY23 reported growth rates in USD are omitted because the original FY23 statutory presentation was in pounds sterling."
        ),
    },
    {
        "fiscal_year": "FY24",
        "year_ended": "2024-06-30",
        "reported_net_sales_usd_m": 20269,
        "reported_ns_movement_pct": -1.4,
        "organic_ns_movement_usd_m": -129,
        "organic_ns_movement_pct": -0.6,
        "organic_volume_movement_pct": -3.5,
        "organic_price_mix_pps": 2.9,
        "volume_eu_m": 230.5,
        "reported_volume_movement_pct": -5,
        "reported_operating_profit_usd_m": 6001,
        "reported_op_movement_pct": 8.2,
        "reported_op_margin_pct": 29.6,  # 6001/20269; official text: reported operating profit margin grew 262bps
        "reported_op_margin_basis": "Calculated as 6001/20269 = 29.6%. FY24 prelim states reported operating profit margin grew 262bps (consistent with FY23 calculated 27.0% + 262bps).",
        "op_before_exceptionals_usd_m": 5945,
        "organic_op_movement_pct": -4.8,
        "organic_op_margin_movement_bps": -130,
        "op_margin_before_exceptionals_pct": 29.3,  # 5945/20269
        "op_margin_before_exceptionals_basis": "Calculated as operating profit before exceptional items ÷ reported net sales (5945/20269). Organic operating margin contracted 130bps (official).",
        "gross_profit_usd_m": 12198,  # from additional financial information walk, reported 2024
        "marketing_usd_m": 3691,
        "free_cash_flow_usd_m": 2609,
        "eps_before_exceptionals_cents": 179.6,
        "recommended_dividend_cents": 103.48,
        "source_codes": "F24PR",
        "notes": (
            "Headline figures. Organic volume decline of 3.5% and price/mix of 2.9pps are the unrounded headline figures; "
            "the organic-by-region table rounds group organic volume to (4)% and organic net sales to (1)%. "
            "Excluding LAC, organic net sales grew $330m or 1.8% (price/mix 3.9pps, volume -2.1%). "
            "Organic operating profit declined $304m, of which $302m was attributable to LAC. "
            "Reported net sales declined 1.4% due to unfavourable FX, organic decline and acquisitions/disposals, partly offset by hyperinflation. "
            "Diageo grew or held total market share in over 75% of total net sales in measured markets."
        ),
    },
    {
        "fiscal_year": "FY25",
        "year_ended": "2025-06-30",
        "reported_net_sales_usd_m": 20245,
        "reported_ns_movement_pct": -0.1,
        "organic_ns_movement_usd_m": 338,
        "organic_ns_movement_pct": 1.7,
        "organic_volume_movement_pct": 0.9,
        "organic_price_mix_pps": 0.8,
        "volume_eu_m": 230.1,
        "reported_volume_movement_pct": -0.2,
        "reported_operating_profit_usd_m": 4335,
        "reported_op_movement_pct": -27.8,
        "reported_op_margin_pct": 21.4,
        "reported_op_margin_basis": "Official headline: reported operating profit margin 21.4%, down 819bps.",
        "op_before_exceptionals_usd_m": 5704,
        "organic_op_movement_pct": -0.7,
        "organic_op_margin_movement_bps": -68,
        "op_margin_before_exceptionals_pct": 28.2,
        "op_margin_before_exceptionals_basis": "Official headline: operating profit margin before exceptional items 28.2%, down 68bps (organic).",
        "gross_profit_usd_m": 12248,  # summary financial information (P12)
        "marketing_usd_m": 3662,
        "free_cash_flow_usd_m": 2748,
        "eps_before_exceptionals_cents": 164.2,
        "recommended_dividend_cents": 103.48,
        "source_codes": "F25PR",
        "notes": (
            "Reported net sales $20.2bn declined 0.1% due to unfavourable FX of (0.6)% and acquisition and disposal adjustments of (1.1)%, "
            "partially offset by hyperinflation adjustments and organic net sales growth. "
            "Excluding the Cîroc transaction, organic net sales growth was 1.5%, with 0.8% volume growth and 0.7% price/mix; "
            "organic operating profit declined 1.0% and organic operating margin declined 70bps. "
            "Diageo grew or held total market share in 65% of total net sales in measured markets, including in the US. "
            "Net debt $21.9bn; leverage 3.4x. Standout brands cited: Don Julio, Guinness and Crown Royal Blackberry."
        ),
    },
    {
        "fiscal_year": "FY26",
        "year_ended": "2026-06-30",
        "reported_net_sales_usd_m": 19643,
        "reported_ns_movement_pct": -3.0,
        "organic_ns_movement_usd_m": -386,
        "organic_ns_movement_pct": -2.0,
        "organic_volume_movement_pct": -0.4,
        "organic_price_mix_pps": -1.6,
        "volume_eu_m": 227.1,
        "reported_volume_movement_pct": -1.2,
        "reported_operating_profit_usd_m": 3156,
        "reported_op_movement_pct": -27.2,
        "reported_op_margin_pct": 16.1,
        "reported_op_margin_basis": "Official headline: reported operating profit margin 16.1%, down 535bps (fiscal 25: 21.4%).",
        "op_before_exceptionals_usd_m": 5683,
        "organic_op_movement_pct": 2.0,
        "organic_op_margin_movement_bps": 116,
        "op_margin_before_exceptionals_pct": 28.9,
        "op_margin_before_exceptionals_basis": "Official headline: operating profit margin before exceptional items 28.9%, up 116bps (organic).",
        "gross_profit_usd_m": 11712,
        "marketing_usd_m": 3183,
        "free_cash_flow_usd_m": 3211,
        "eps_before_exceptionals_cents": 165.3,
        "recommended_dividend_cents": 50.0,
        "source_codes": "F26PR",
        "notes": (
            "Negative price/mix primarily from adverse mix due to US Spirits performance and weaker Chinese white spirits (CWS). "
            "Excluding CWS, organic net sales for the group would have been c.1.5% higher, with volume broadly flat and price/mix down c.0.5% "
            "(official approximate language). Organic operating profit +2.0% mainly due to cost savings, partly offset by adverse mix and tariffs. "
            "Organic gross margin was down 141bps. Marketing -13.1% organic and reported. "
            "Accelerate savings of $540m secured through fiscal 26. Recommended dividend 50 cents under the new payout policy announced 25 February 2026. "
            "Standout performers cited on the results page: Guinness, Smirnoff RTD and Johnnie Walker."
        ),
    },
]

# Add FY23 FCF and EPS from F24PR now that I confirmed them
GROUP_KPIS[0]["free_cash_flow_usd_m"] = 2235  # F24PR: F23 free cash flow $2,235m
GROUP_KPIS[0]["eps_before_exceptionals_cents"] = 196.5  # F24PR summary table, 2023 re-presented

REGIONAL = [
    # FY23 reported $ from F24PR key financials / comparatives (re-presented). Volumes and organic % not taken from GBP-era tables.
    {"fiscal_year": "FY23", "region": "North America", "volume_eu_m": None, "reported_ns_usd_m": 8109, "marketing_usd_m": 1631, "opbe_usd_m": 3222, "reported_op_usd_m": 3104,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": None, "organic_volume_mov_pct": None, "organic_ns_mov_pct": None, "organic_marketing_mov_pct": None, "organic_opbe_mov_pct": None,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "FY23 USD comparatives from FY24 prelim North America key financials (2023 re-presented). Official share of group net sales for FY23 not taken from a USD headline."},
    {"fiscal_year": "FY23", "region": "Europe", "volume_eu_m": None, "reported_ns_usd_m": 4303, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": None, "organic_volume_mov_pct": None, "organic_ns_mov_pct": None, "organic_marketing_mov_pct": None, "organic_opbe_mov_pct": None,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "FY23 USD net sales from FY24 prelim Europe key financials (2023 re-presented). Other FY23 Europe line items omitted where not captured as official USD."},
    {"fiscal_year": "FY23", "region": "Asia Pacific", "volume_eu_m": None, "reported_ns_usd_m": 3841, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": None, "organic_volume_mov_pct": None, "organic_ns_mov_pct": None, "organic_marketing_mov_pct": None, "organic_opbe_mov_pct": None,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "FY23 USD net sales from FY24 prelim Asia Pacific key financials (2023 re-presented)."},
    {"fiscal_year": "FY23", "region": "Latin America and Caribbean", "volume_eu_m": None, "reported_ns_usd_m": 2159, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": None, "organic_volume_mov_pct": None, "organic_ns_mov_pct": None, "organic_marketing_mov_pct": None, "organic_opbe_mov_pct": None,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "FY23 USD net sales from FY24 prelim LAC key financials (2023 re-presented). AR24 CEO statement: LAC makes up 8% of Diageo’s organic net sales value in the fiscal 24 discussion of the prior-year mix context."},
    {"fiscal_year": "FY23", "region": "Africa", "volume_eu_m": None, "reported_ns_usd_m": 2039, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": None, "organic_volume_mov_pct": None, "organic_ns_mov_pct": None, "organic_marketing_mov_pct": None, "organic_opbe_mov_pct": None,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "FY23 USD net sales from FY24 prelim Africa key financials (2023 re-presented)."},
    {"fiscal_year": "FY23", "region": "Corporate", "volume_eu_m": None, "reported_ns_usd_m": 104, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": None, "organic_volume_mov_pct": None, "organic_ns_mov_pct": None, "organic_marketing_mov_pct": None, "organic_opbe_mov_pct": None,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Residual of group reported net sales $20,555m less the five published regional totals ($20,451m), as shown in the FY24 prelim reported net sales by region comparative ($104m)."},

    # FY24
    {"fiscal_year": "FY24", "region": "North America", "volume_eu_m": None, "reported_ns_usd_m": 7908, "marketing_usd_m": 1627, "opbe_usd_m": 3236, "reported_op_usd_m": 3039,
     "reported_volume_mov_pct": -4, "reported_ns_mov_pct": -2, "organic_volume_mov_pct": -4, "organic_ns_mov_pct": -2.5, "organic_marketing_mov_pct": -1, "organic_opbe_mov_pct": -5,
     "official_share_of_group_ns_pct": 39, "organic_price_mix_pps": 2.0, "organic_op_margin_movement_bps": -79, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Official share: “North America contributed 39% of Diageo reported net sales in fiscal 24.” Organic NS: the regional table rounds to (3)%; the same document’s excluding-LAC paragraph states a 2.5% decrease (organic movement -$206m on FY23 NS $8,109m). Price/mix +2pps and volume -4% from the NAM narrative. Organic operating margin declined 79bps. Organic OPBE movement -$142m / table (5)%."},
    {"fiscal_year": "FY24", "region": "Europe", "volume_eu_m": None, "reported_ns_usd_m": 4804, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": 0, "reported_ns_mov_pct": 12, "organic_volume_mov_pct": -1, "organic_ns_mov_pct": 3, "organic_marketing_mov_pct": 4, "organic_opbe_mov_pct": -1,
     "official_share_of_group_ns_pct": 24, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": -121, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Official share 24%. Organic and reported movements from the organic/reported growth-by-region tables (integer rounded). Organic operating margin declined 121bps. Reported NS $4,804m from Europe key financials."},
    {"fiscal_year": "FY24", "region": "Asia Pacific", "volume_eu_m": None, "reported_ns_usd_m": 3817, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": -7, "reported_ns_mov_pct": -1, "organic_volume_mov_pct": 1, "organic_ns_mov_pct": 4, "organic_marketing_mov_pct": 2, "organic_opbe_mov_pct": 6,
     "official_share_of_group_ns_pct": 19, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": 35, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Official share 19%. Organic operating margin increased 35bps. Reported NS $3,817m from APAC key financials."},
    {"fiscal_year": "FY24", "region": "Latin America and Caribbean", "volume_eu_m": None, "reported_ns_usd_m": 1839, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": -16, "reported_ns_mov_pct": -15, "organic_volume_mov_pct": -16, "organic_ns_mov_pct": -21.1, "organic_marketing_mov_pct": -20, "organic_opbe_mov_pct": -37,
     "official_share_of_group_ns_pct": 9, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": -746, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Official share 9%. Headline states a 21.1% organic net sales decline in LAC (the region table rounds to (21)%). Organic operating profit decline of $302m; organic operating margin declined 746bps. Reported NS $1,839m."},
    {"fiscal_year": "FY24", "region": "Africa", "volume_eu_m": None, "reported_ns_usd_m": 1778, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": -2, "reported_ns_mov_pct": -13, "organic_volume_mov_pct": -6, "organic_ns_mov_pct": 12, "organic_marketing_mov_pct": 16, "organic_opbe_mov_pct": 24,
     "official_share_of_group_ns_pct": 9, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": 194, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Official share 9%. Organic operating margin increased 194bps. Reported NS $1,778m. Reported NS -13% vs organic +12% reflects FX (Africa key financials show a large exchange movement)."},
    {"fiscal_year": "FY24", "region": "Corporate", "volume_eu_m": None, "reported_ns_usd_m": 123, "marketing_usd_m": None, "opbe_usd_m": None, "reported_op_usd_m": None,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": 18, "organic_volume_mov_pct": None, "organic_ns_mov_pct": 12, "organic_marketing_mov_pct": 8, "organic_opbe_mov_pct": 3,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F24PR", "notes": "Corporate reported net sales $123m from the FY24 prelim reported net sales by region table (group $20,269m). No official “share of net sales” headline for Corporate."},

    # FY25
    {"fiscal_year": "FY25", "region": "North America", "volume_eu_m": 49.5, "reported_ns_usd_m": 7973, "marketing_usd_m": 1616, "opbe_usd_m": 3053, "reported_op_usd_m": 2222,
     "reported_volume_mov_pct": -1.2, "reported_ns_mov_pct": 0.8, "organic_volume_mov_pct": -0.8, "organic_ns_mov_pct": 1.5, "organic_marketing_mov_pct": -0.6, "organic_opbe_mov_pct": 0.3,
     "official_share_of_group_ns_pct": 39, "organic_price_mix_pps": 2.3, "organic_op_margin_movement_bps": -42, "stated_operating_margin_pct": 38.3,
     "source_codes": "F25PR", "notes": "Official share 39%. “Operating margin of 38.3%, decreased 42bps organically.” Volume decline 0.8% offset by positive price/mix of 2.3%. Excluding the Cîroc transaction, organic net sales grew 0.8% and organic operating profit declined 0.4%."},
    {"fiscal_year": "FY25", "region": "Europe", "volume_eu_m": 48.9, "reported_ns_usd_m": 4821, "marketing_usd_m": 898, "opbe_usd_m": 1302, "reported_op_usd_m": 823,
     "reported_volume_mov_pct": -4.7, "reported_ns_mov_pct": 0.4, "organic_volume_mov_pct": -4.3, "organic_ns_mov_pct": 0.3, "organic_marketing_mov_pct": 1.9, "organic_opbe_mov_pct": -2.5,
     "official_share_of_group_ns_pct": 24, "organic_price_mix_pps": 4.5, "organic_op_margin_movement_bps": -80, "stated_operating_margin_pct": None,
     "source_codes": "F25PR", "notes": "Official share 24%. Volume decline of 4.3% offset by price/mix up 4.5%. Organic operating margin movement -80bps from the organic operating margin table."},
    {"fiscal_year": "FY25", "region": "Asia Pacific", "volume_eu_m": 77.7, "reported_ns_usd_m": 3635, "marketing_usd_m": 630, "opbe_usd_m": 930, "reported_op_usd_m": 890,
     "reported_volume_mov_pct": 3.7, "reported_ns_mov_pct": -4.8, "organic_volume_mov_pct": 3.9, "organic_ns_mov_pct": -3.2, "organic_marketing_mov_pct": -2.5, "organic_opbe_mov_pct": -11.0,
     "official_share_of_group_ns_pct": 18, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": -223, "stated_operating_margin_pct": None,
     "source_codes": "F25PR", "notes": "Official share 18%. Negative price/mix in Asia Pacific is described (consumer downtrading in South East Asia and China; unfavourable market mix with strong volume in India) but no official price/mix pps figure is printed, so it is left blank rather than implied. Organic operating margin movement -223bps."},
    {"fiscal_year": "FY25", "region": "Latin America and Caribbean", "volume_eu_m": 22.9, "reported_ns_usd_m": 1847, "marketing_usd_m": 304, "opbe_usd_m": 528, "reported_op_usd_m": 509,
     "reported_volume_mov_pct": 3.6, "reported_ns_mov_pct": 0.4, "organic_volume_mov_pct": 3.2, "organic_ns_mov_pct": 9.2, "organic_marketing_mov_pct": 8.7, "organic_opbe_mov_pct": 11.7,
     "official_share_of_group_ns_pct": 9, "organic_price_mix_pps": 6.0, "organic_op_margin_movement_bps": 68, "stated_operating_margin_pct": None,
     "source_codes": "F25PR", "notes": "Official share 9%. Volume up 3.2% and price/mix growth of 6.0%. Organic operating margin movement +68bps."},
    {"fiscal_year": "FY25", "region": "Africa", "volume_eu_m": 31.1, "reported_ns_usd_m": 1834, "marketing_usd_m": 192, "opbe_usd_m": 283, "reported_op_usd_m": 283,
     "reported_volume_mov_pct": -3.1, "reported_ns_mov_pct": 3.1, "organic_volume_mov_pct": 3.7, "organic_ns_mov_pct": 10.5, "organic_marketing_mov_pct": -4.4, "organic_opbe_mov_pct": 27.7,
     "official_share_of_group_ns_pct": 9, "organic_price_mix_pps": 6.9, "organic_op_margin_movement_bps": 232, "stated_operating_margin_pct": None,
     "source_codes": "F25PR", "notes": "Official share 9%. Volume grew 3.7% and price/mix grew 6.9%, the latter mainly due to pricing and premiumisation through East Africa. Organic operating margin movement +232bps."},
    {"fiscal_year": "FY25", "region": "Corporate", "volume_eu_m": None, "reported_ns_usd_m": 135, "marketing_usd_m": 22, "opbe_usd_m": -392, "reported_op_usd_m": -392,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": 9.8, "organic_volume_mov_pct": None, "organic_ns_mov_pct": 8.1, "organic_marketing_mov_pct": -21.4, "organic_opbe_mov_pct": -6.2,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F25PR", "notes": "From the FY25 reported results by region table. No official share-of-net-sales headline for Corporate."},

    # FY26
    {"fiscal_year": "FY26", "region": "North America", "volume_eu_m": 46.1, "reported_ns_usd_m": 7249, "marketing_usd_m": 1367, "opbe_usd_m": 2601, "reported_op_usd_m": 2031,
     "reported_volume_mov_pct": -6.9, "reported_ns_mov_pct": -9.1, "organic_volume_mov_pct": -6.7, "organic_ns_mov_pct": -8.4, "organic_marketing_mov_pct": -13.6, "organic_opbe_mov_pct": -10.0,
     "official_share_of_group_ns_pct": 37, "organic_price_mix_pps": -1.7, "organic_op_margin_movement_bps": -66, "stated_operating_margin_pct": 35.9,
     "source_codes": "F26PR", "notes": "Official share 37%. Organic volume -6.7%, price/mix -1.7%. “Operating margin of 35.9%, reduced by 66bps organically.” Driven primarily by US Spirits (organic NS -11.5%), partly offset by DBC USA (+4.4%)."},
    {"fiscal_year": "FY26", "region": "Europe", "volume_eu_m": 48.9, "reported_ns_usd_m": 5097, "marketing_usd_m": 773, "opbe_usd_m": 1612, "reported_op_usd_m": 7,
     "reported_volume_mov_pct": 0, "reported_ns_mov_pct": 5.7, "organic_volume_mov_pct": 0, "organic_ns_mov_pct": 3.4, "organic_marketing_mov_pct": -17.2, "organic_opbe_mov_pct": 15.7,
     "official_share_of_group_ns_pct": 26, "organic_price_mix_pps": 3.4, "organic_op_margin_movement_bps": 328, "stated_operating_margin_pct": None,
     "source_codes": "F26PR", "notes": "Official share 26%. Volume was flat with price/mix increasing 3.4%. Beer increased double-digit, led by Guinness in Great Britain and Ireland. Organic operating margin movement +328bps. Reported operating profit of $7m vs OPBE of $1,612m reflects exceptional items."},
    {"fiscal_year": "FY26", "region": "Asia Pacific", "volume_eu_m": 75.8, "reported_ns_usd_m": 3333, "marketing_usd_m": 524, "opbe_usd_m": 846, "reported_op_usd_m": 690,
     "reported_volume_mov_pct": -2.4, "reported_ns_mov_pct": -8.3, "organic_volume_mov_pct": -2.4, "organic_ns_mov_pct": -6.3, "organic_marketing_mov_pct": -16.3, "organic_opbe_mov_pct": -5.4,
     "official_share_of_group_ns_pct": 17, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": 26, "stated_operating_margin_pct": None,
     "source_codes": "F26PR", "notes": "Official share 17%. Weaker results in Chinese white spirits are cited as a group mix headwind. No official APAC price/mix pps is printed, so it is left blank. Organic operating margin movement +26bps."},
    {"fiscal_year": "FY26", "region": "Latin America and Caribbean", "volume_eu_m": 23.4, "reported_ns_usd_m": 2160, "marketing_usd_m": 325, "opbe_usd_m": 587, "reported_op_usd_m": 395,
     "reported_volume_mov_pct": 2.2, "reported_ns_mov_pct": 16.9, "organic_volume_mov_pct": 3.1, "organic_ns_mov_pct": 7.7, "organic_marketing_mov_pct": 0.3, "organic_opbe_mov_pct": 15.8,
     "official_share_of_group_ns_pct": 11, "organic_price_mix_pps": 4.6, "organic_op_margin_movement_bps": 210, "stated_operating_margin_pct": None,
     "source_codes": "F26PR", "notes": "Official share 11%. Volume growth of 3.1% and 4.6% price/mix growth. Organic operating margin movement +210bps."},
    {"fiscal_year": "FY26", "region": "Africa", "volume_eu_m": 32.9, "reported_ns_usd_m": 1642, "marketing_usd_m": 173, "opbe_usd_m": 356, "reported_op_usd_m": 352,
     "reported_volume_mov_pct": 6.8, "reported_ns_mov_pct": -10.5, "organic_volume_mov_pct": 14.0, "organic_ns_mov_pct": 13.3, "organic_marketing_mov_pct": -1.2, "organic_opbe_mov_pct": 43.5,
     "official_share_of_group_ns_pct": 8, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": 458, "stated_operating_margin_pct": None,
     "source_codes": "F26PR", "notes": "Official share 8%. Reported net sales -10.5% vs organic +13.3% (disposals/FX). No official Africa price/mix pps is printed, so it is left blank. Organic operating margin movement +458bps. EABL sale noted as on track for calendar H2 2026."},
    {"fiscal_year": "FY26", "region": "Corporate", "volume_eu_m": None, "reported_ns_usd_m": 162, "marketing_usd_m": 21, "opbe_usd_m": -319, "reported_op_usd_m": -319,
     "reported_volume_mov_pct": None, "reported_ns_mov_pct": 20.0, "organic_volume_mov_pct": None, "organic_ns_mov_pct": 14.3, "organic_marketing_mov_pct": 4.5, "organic_opbe_mov_pct": 19.1,
     "official_share_of_group_ns_pct": None, "organic_price_mix_pps": None, "organic_op_margin_movement_bps": None, "stated_operating_margin_pct": None,
     "source_codes": "F26PR", "notes": "From the FY26 reported results by region table. No official share-of-net-sales headline for Corporate."},
]

# Category tables: official organic vol, organic NS, reported NS movement, reported NS by category %
# FY23 only the three categories explicitly stated in AR23 (organic NS).
CATEGORIES = [
    # FY23 (AR23) — organic NS only for categories explicitly cited
    {"fiscal_year": "FY23", "category": "Scotch", "organic_volume_mov_pct": None, "organic_ns_mov_pct": 12, "reported_ns_mov_pct": None, "reported_ns_by_category_pct": None, "source_codes": "AR23", "notes": "AR2023: “Scotch grew 12%, tequila grew 19% and beer was up 9% respectively.” Interpreted as organic net sales, consistent with Diageo’s standard category commentary convention in later years. Volume and share not stated here."},
    {"fiscal_year": "FY23", "category": "Tequila", "organic_volume_mov_pct": None, "organic_ns_mov_pct": 19, "reported_ns_mov_pct": None, "reported_ns_by_category_pct": None, "source_codes": "AR23", "notes": "AR2023: tequila grew 19%."},
    {"fiscal_year": "FY23", "category": "Beer", "organic_volume_mov_pct": None, "organic_ns_mov_pct": 9, "reported_ns_mov_pct": None, "reported_ns_by_category_pct": None, "source_codes": "AR23", "notes": "AR2023: beer was up 9%."},
]

# FY24/25/26 full official category tables
_CAT_FY24 = [
    # category, org vol, org ns, rep ns, share
    ("Spirits", -5, -4, -2, 78),
    ("Scotch", -7, -10, -6, 24),
    ("Tequila", -4, -7, -7, 11),
    ("Vodka", -9, -7, -6, 9),
    ("Canadian whisky", -2, -1, -1, 6),
    ("Rum", -11, -6, -2, 5),
    ("Liqueurs", -2, 2, 3, 5),
    ("Gin", -10, -8, 2, 5),
    ("IMFL whisky", 5, 10, 2, 4),
    ("Chinese white spirits", 32, 27, 23, 3),
    ("US whiskey", -3, 3, 3, 2),
    ("Beer", 5, 14, 3, 16),
    ("Ready to drink", -7, -1, -10, 4),
]
_CAT_FY25 = [
    ("Spirits", 0, 0, -2, 76),
    ("Scotch", -2, -4, -7, 22),
    ("Tequila", 15, 18, 17, 13),
    ("Vodka", -4, -5, -9, 8),
    ("Canadian whisky", 5, 3, 3, 7),
    ("Rum", -3, -5, -7, 5),
    ("Liqueurs", -7, -4, -4, 5),
    ("Gin", -1, -4, -11, 4),
    ("IMFL whisky", 7, 10, 8, 4),
    ("Chinese white spirits", 5, -8, -8, 3),
    ("US whiskey", -8, -9, -9, 2),
    ("Beer", 6, 10, 10, 18),
    ("Ready to drink", 4, 2, 0, 4),
]
_CAT_FY26 = [
    ("Spirits", -1, -5, -5, 75),
    ("Scotch", 3, 2, 5, 24),
    ("Tequila", -15, -16, -16, 12),
    ("Vodka", -1, 0, -3, 8),
    ("Canadian whisky", -14, -15, -15, 6),
    ("Rum", 7, 2, 2, 5),
    ("Liqueurs", -5, -4, -2, 5),
    ("Gin", 2, -2, 1, 4),
    ("IMFL whisky", -5, 0, -6, 4),
    ("US whiskey", -6, -8, -8, 2),
    ("Chinese white spirits", -42, -47, -45, 2),
    ("Beer", 5, 9, 2, 18),
    ("Ready-to-drink", 25, 15, 12, 4),
]

_CAT_NOTES = {
    ("FY24", "Spirits"): "Spirits brands excluding ready to drink and non-alcoholic variants. Category shares are as published and do not always sum to 100% because of rounding and categories not separately disclosed.",
    ("FY24", "Vodka"): "Vodka includes Ketel One Botanical. Vodka, rum and gin include IMFL variants.",
    ("FY24", "Canadian whisky"): "See FY24 prelim NAM review for Crown Royal detail.",
    ("FY25", "Spirits"): "Organic volume and organic net sales printed as “—” (treated as 0). Spirits excluding RTD and non-alcoholic variants. Published category shares do not always sum to 100%.",
    ("FY25", "Tequila"): "Group tequila organic net sales +18%. US Spirits narrative: tequila net sales grew 16.9%, driven by Don Julio, partially offset by Casamigos (US Spirits scope).",
    ("FY25", "Vodka"): "Vodka includes Ketel One Botanical. Vodka, rum and gin include IMFL variants.",
    ("FY25", "Canadian whisky"): "Crown Royal is the principal brand. Group Canadian whisky organic NS +3%.",
    ("FY25", "Beer"): "Beer was 18% of reported net sales in FY25.",
    ("FY26", "Spirits"): "Spirits excluding RTD and non-alcoholic variants. Published category shares do not always sum to 100%.",
    ("FY26", "Tequila"): "Sharp reversal after FY25’s +18% organic NS, reflecting US category pressure and Casamigos weakness.",
    ("FY26", "Canadian whisky"): "Crown Royal is the principal brand. Group Canadian whisky organic NS -15%.",
    ("FY26", "Chinese white spirits"): "A major FY26 mix headwind. Group commentary: excluding CWS, organic net sales would have been c.1.5% higher.",
    ("FY26", "Beer"): "Beer category includes flavoured malt beverage (FMB) products. Beer 18% of reported net sales.",
    ("FY26", "Ready-to-drink"): "Includes spirit-based ready-to-drink, ready-to-serve and non-alcoholic variants. Organic volume +25%, organic NS +15%.",
    ("FY26", "Vodka"): "Organic net sales movement printed as “—” (treated as 0). Vodka includes Ketel One Botanical. Vodka, rum and gin include IMFL variants.",
}

for fy, rows, src in (("FY24", _CAT_FY24, "F24PR"), ("FY25", _CAT_FY25, "F25PR"), ("FY26", _CAT_FY26, "F26PR")):
    for cat, ov, ons, rns, share in rows:
        CATEGORIES.append({
            "fiscal_year": fy,
            "category": cat,
            "organic_volume_mov_pct": ov,
            "organic_ns_mov_pct": ons,
            "reported_ns_mov_pct": rns,
            "reported_ns_by_category_pct": share,
            "source_codes": src,
            "notes": _CAT_NOTES.get((fy, cat), "From the official Key categories table. Absolute category net sales in $ are not disclosed; only the published share of reported net sales is shown. No $ figures have been back-calculated from rounded percentages."),
        })

BRANDS = []
_BR_FY24 = [
    ("Johnnie Walker", -5, -6, -2, ""),
    ("Guinness", 5, 15, 6, "Organic equals reported volume except Guinness reported volume 4% (footnote)."),
    ("Don Julio", 7, 3, 4, "Group brand table. In US Spirits highlights, Don Julio net sales increased 12% (US Spirits scope) with depletions +21%."),
    ("Crown Royal", 0, -1, -1, "Net sales declined 1%, primarily due to Crown Royal Deluxe and Crown Royal Peach, mostly offset by the successful launch of Crown Royal Blackberry. Held share for the full year and gained share of the spirits industry in H2."),
    ("Smirnoff", -7, -3, -3, ""),
    ("Baileys", -1, 1, 2, ""),
    ("Casamigos", -15, -20, -20, "Trademark includes tequila and mezcal. US Spirits: Casamigos net sales declined 22% in one US Spirits highlight table; group brand table shows organic NS -20%."),
    ("Captain Morgan", -7, -5, -4, ""),
    ("Shui Jing Fang", 32, 27, 23, "Growth figures represent total Chinese white spirits of which Shui Jing Fang is the principal brand."),
    ("McDowell's", -2, 3, 1, ""),
    ("Buchanan's", -9, -15, -7, ""),
    ("Ketel One", -5, -5, -5, "Includes Ketel One vodka and Ketel One Botanical."),
    ("Bulleit whiskey", 6, 11, 11, "Excludes Bulleit Crafted Cocktails."),
]
_BR_FY25 = [
    ("Johnnie Walker", -3, -5, -7, "US Spirits: Johnnie Walker net sales declined 10.6% (US Spirits scope); trademark gained share of scotch and held share of total spirits."),
    ("Don Julio", 41, 38, 37, "Group brand table: organic volume +41%, organic NS +38%, reported NS +37%. US Spirits narrative: “Don Julio net sales grew 41.9%”; depletions growth of 36%; shipments grew ahead of depletions."),
    ("Guinness", 14, 13, 12, "Organic volume equals reported except Guinness reported volume 11% (footnote). A standout group performer in FY25."),
    ("Crown Royal", 4, 3, 3, "Group brand table organic NS +3%. US Spirits/NAM narrative: “Crown Royal whisky net sales grew 3.8%”, primarily driven by Crown Royal Blackberry (launched H2 FY24)."),
    ("Smirnoff", -3, -5, -6, ""),
    ("Baileys", -1, -4, -3, "Organic equals reported volume except Baileys reported volume (2)%."),
    ("Captain Morgan", -3, -6, -6, "Organic equals reported volume except Captain Morgan reported volume (4)%. US Spirits: Captain Morgan net sales declined 9.3% (US Spirits scope)."),
    ("Casamigos", -16, -16, -16, "Trademark includes tequila and mezcal. US Spirits: Casamigos net sales declined 18%."),
    ("Shui Jing Fang", 5, -8, -8, "Figures represent total Chinese white spirits of which Shui Jing Fang is the principal brand."),
    ("McDowell's", 2, 7, 4, ""),
]
_BR_FY26 = [
    ("Johnnie Walker", 3, 2, 4, "Cited as a standout performer. US Spirits: Johnnie Walker net sales up 1.0% (US Spirits scope)."),
    ("Guinness", 7, 12, 11, "Organic equals reported volume except Guinness reported volume 6%. Cited as a standout performer. Europe beer increased double-digit, led by Guinness in GB and Ireland."),
    ("Don Julio", -14, -14, -13, "Reversal after FY25’s very strong growth."),
    ("Crown Royal", -14, -15, -15, "NAM narrative: “Crown Royal whisky net sales declined 15.9%”, primarily due to softness in Crown Royal Deluxe and lapping strong comparatives for Crown Royal Blackberry through fiscal 25."),
    ("Smirnoff", 0, -1, 1, "Organic equals reported volume except Smirnoff reported volume (1)%. US Spirits: Smirnoff down 5.0%; Ketel One grew 4.5%."),
    ("Baileys", -4, -4, -1, ""),
    ("Captain Morgan", -3, -4, -3, ""),
    ("Buchanan's", 14, 12, 21, "US Spirits: Buchanan's down 7.3% (US Spirits scope) — group growth reflects performance outside US Spirits."),
    ("Casamigos", -19, -25, -25, "Trademark includes tequila and mezcal. US Spirits: Casamigos net sales declined 27.7%, depletions down 23.1%."),
    ("McDowell's", -7, -7, -12, ""),
]
for fy, rows, src in (("FY24", _BR_FY24, "F24PR"), ("FY25", _BR_FY25, "F25PR"), ("FY26", _BR_FY26, "F26PR")):
    for brand, ov, ons, rns, note in rows:
        BRANDS.append({
            "fiscal_year": fy,
            "brand": brand,
            "organic_volume_mov_pct": ov,
            "organic_ns_mov_pct": ons,
            "reported_ns_mov_pct": rns,
            "source_codes": src,
            "notes": note or "From the official Key brands table. Brands excluding ready-to-drink, non-alcoholic variants and beer except Guinness. Absolute brand net sales in $ are not disclosed.",
        })

NAM_CANADA = [
    # FY24
    {"fiscal_year": "FY24", "market": "North America", "organic_volume_mov_pct": -4, "reported_volume_mov_pct": -4, "organic_ns_mov_pct": -3, "reported_ns_mov_pct": -2,
     "source_codes": "F24PR", "notes": "Markets table (integer rounded). Narrative also states organic NS declined 3% and, in the excluding-LAC paragraph, a 2.5% decrease."},
    {"fiscal_year": "FY24", "market": "US Spirits", "organic_volume_mov_pct": -5, "reported_volume_mov_pct": -4, "organic_ns_mov_pct": -3, "reported_ns_mov_pct": -3,
     "source_codes": "F24PR", "notes": "Organic NS declined 3%, driven by a volume decline of 5%. Depletion growth approximately one percentage point ahead of shipment growth. Inventory at distributors in line with historical levels."},
    {"fiscal_year": "FY24", "market": "DBC USA", "organic_volume_mov_pct": 1, "reported_volume_mov_pct": 1, "organic_ns_mov_pct": 3, "reported_ns_mov_pct": 3,
     "source_codes": "F24PR", "notes": "Net sales grew 3%, reflecting strong growth in Guinness, Smirnoff flavoured malt beverages, and the launch of Captain Morgan Sliced Apple."},
    {"fiscal_year": "FY24", "market": "Canada", "organic_volume_mov_pct": -5, "reported_volume_mov_pct": -4, "organic_ns_mov_pct": -2, "reported_ns_mov_pct": -3,
     "source_codes": "F24PR", "notes": "From the North America markets table. Absolute Canada net sales in $ are not disclosed. NAM organic decline was due to lower sales in US Spirits and Canada, partially offset by DBC USA."},
    # FY25
    {"fiscal_year": "FY25", "market": "North America", "organic_volume_mov_pct": -0.8, "reported_volume_mov_pct": -1.2, "organic_ns_mov_pct": 1.5, "reported_ns_mov_pct": 0.8,
     "source_codes": "F25PR", "notes": "Growth in US Spirits and DBC USA offset by a slight decline in Canada. Price/mix +2.3%."},
    {"fiscal_year": "FY25", "market": "US Spirits", "organic_volume_mov_pct": -1.3, "reported_volume_mov_pct": -1.8, "organic_ns_mov_pct": 1.6, "reported_ns_mov_pct": 1.0,
     "source_codes": "F25PR", "notes": "Positive price/mix of 2.9% offset by slight volume decline. Shipments grew 1.6pp ahead of depletions as distributors replenished Don Julio and Crown Royal. Tequila NS +16.9%; Crown Royal whisky NS +3.8%; vodka NS -4.5%; Johnnie Walker NS -10.6%; Captain Morgan NS -9.3% (all US Spirits scope)."},
    {"fiscal_year": "FY25", "market": "DBC USA", "organic_volume_mov_pct": 2.6, "reported_volume_mov_pct": 2.7, "organic_ns_mov_pct": 4.8, "reported_ns_mov_pct": 4.9,
     "source_codes": "F25PR", "notes": "Driven by strong growth in Guinness variants including Guinness Draught, Extra Stout and Guinness 0.0."},
    {"fiscal_year": "FY25", "market": "Canada", "organic_volume_mov_pct": -3.2, "reported_volume_mov_pct": -3.3, "organic_ns_mov_pct": -0.9, "reported_ns_mov_pct": -3.7,
     "source_codes": "F25PR", "notes": "“Canada net sales declined 0.9%, reflecting a weaker spirits category amid a challenging regulatory and operational backdrop which was partially offset by strong growth in Guinness.” Absolute Canada net sales in $ are not disclosed."},
    # FY26
    {"fiscal_year": "FY26", "market": "North America", "organic_volume_mov_pct": -6.7, "reported_volume_mov_pct": -6.9, "organic_ns_mov_pct": -8.4, "reported_ns_mov_pct": -9.1,
     "source_codes": "F26PR", "notes": "US weakness only partly offset by DBC USA. Price/mix -1.7%. Canada organic NS grew high-single-digit, mainly driven by a one-off item in the second half."},
    {"fiscal_year": "FY26", "market": "US Spirits", "organic_volume_mov_pct": -9.0, "reported_volume_mov_pct": -10.5, "organic_ns_mov_pct": -11.5, "reported_ns_mov_pct": -13.2,
     "source_codes": "F26PR", "notes": "Volume -9.0% and negative price/mix of 2.5%. Crown Royal whisky NS -15.9%; Casamigos NS -27.7%; RTDs/Cocktails NS +35.1%; vodka NS -1.0%; scotch NS -1.1% (US Spirits scope)."},
    {"fiscal_year": "FY26", "market": "DBC USA", "organic_volume_mov_pct": 3.4, "reported_volume_mov_pct": 3.4, "organic_ns_mov_pct": 4.4, "reported_ns_mov_pct": 4.4,
     "source_codes": "F26PR", "notes": "Driven by growth in Guinness, led by Guinness Draught, and Smirnoff RTD which grew mid-single-digit."},
    {"fiscal_year": "FY26", "market": "Canada", "organic_volume_mov_pct": -0.3, "reported_volume_mov_pct": 0.1, "organic_ns_mov_pct": 7.7, "reported_ns_mov_pct": 11.3,
     "source_codes": "F26PR", "notes": "“Canada net sales grew 7.7%, supported by growth in Guinness and Ketel One vodka and a one-off item relating to a favourable resolution of commercial terms with a customer.” The 7.7% therefore includes a one-off and should not be read as the underlying run-rate. Absolute Canada net sales in $ are not disclosed."},
]

INSIGHTS = [
    {
        "n": 1,
        "title": "Price/mix, the FY21–FY23 growth engine, has reversed — RGM is the commercial priority again",
        "takeaway": (
            "Diageo’s post-pandemic upcycle was a price/mix story. Fiscal 23 organic net sales grew 6.5%, made up of 7.3 percentage points of price/mix and a 0.8% volume decline "
            "(Annual Report 2023). After “three years of extraordinary topline growth, with 14.5% CAGR from fiscal 21 to fiscal 23” (Annual Report 2024), that lever faded: "
            "price/mix was +2.9pps in FY24, only +0.8pps in FY25, and turned negative at -1.6pps in FY26, leaving organic net sales at -2.0% (FY24, FY25 and FY26 prelims). "
            "FY26 commentary attributes the negative mix to US Spirits and Chinese white spirits. For a Commercial Analyst, this is a revenue-growth-management brief: pack/price architecture, "
            "mix management across tequila and Canadian whisky, and protecting premium price points without losing competitiveness."
        ),
        "key_figures": "FY23 price/mix +7.3pps and organic NS +6.5%; FY26 price/mix -1.6pps and organic NS -2.0%.",
        "source_codes": "AR23; AR24; F24PR; F25PR; F26PR",
    },
    {
        "n": 2,
        "title": "North America, still more than a third of the group, is the drag",
        "takeaway": (
            "North America was 39% of reported net sales in FY24 and FY25, and 37% in FY26. Organic net sales were -2.5% in FY24 (excluding-LAC paragraph; regional table rounds to -3%), "
            "recovered to +1.5% in FY25, then fell 8.4% in FY26. Reported NAM net sales were $7,908m (FY24), $7,973m (FY25) and $7,249m (FY26). "
            "The FY26 decline was concentrated in US Spirits (organic NS -11.5%, volume -9.0%, price/mix -2.5%), only partly offset by DBC USA at +4.4%. "
            "NAM operating margin was 38.3% in FY25 (down 42bps organically) and 35.9% in FY26 (down 66bps organically). The commercial issue is not just volume; mix and tariffs are also hitting the margin."
        ),
        "key_figures": "NAM FY26: 37% of group NS; organic NS -8.4%; US Spirits organic NS -11.5%; operating margin 35.9%.",
        "source_codes": "F24PR; F25PR; F26PR",
    },
    {
        "n": 3,
        "title": "Premiumisation in tequila and Crown Royal turned in FY26 — the cycle has two sides",
        "takeaway": (
            "FY25 was a premium-brand year: group tequila organic net sales grew 18%, Don Julio organic NS grew 38% (US Spirits narrative: Don Julio net sales +41.9%), "
            "and Canadian whisky organic NS grew 3%, with Crown Royal whisky net sales +3.8% “primarily driven by continued strong consumer demand for Crown Royal Blackberry” (FY25 prelim). "
            "FY26 reversed those same engines: tequila organic NS -16%, Don Julio organic NS -14%, Casamigos organic NS -25% (US Spirits Casamigos NS -27.7%), "
            "Canadian whisky organic NS -15%, and Crown Royal whisky net sales -15.9%, “primarily due to softness in Crown Royal Deluxe and lapping strong comparatives for Crown Royal Blackberry.” "
            "Absolute brand or category net sales in dollars are not disclosed. The lesson for a Canada-based Commercial Analyst is that Crown Royal — the flagship Canadian-origin brand, "
            "in a category that was 7% of group net sales in FY25 and 6% in FY26 — is both a growth lever and a concentration risk when innovation comparatives roll off."
        ),
        "key_figures": "FY25 tequila organic NS +18% and Crown Royal whisky NS +3.8%; FY26 tequila organic NS -16% and Crown Royal whisky NS -15.9%.",
        "source_codes": "F25PR; F26PR",
    },
    {
        "n": 4,
        "title": "Guinness and beer have been the consistent growth engine across all three years",
        "takeaway": (
            "Beer organic net sales grew 14% in FY24, 10% in FY25 and 9% in FY26. Guinness organic NS grew 15%, 13% and 12% in those years. "
            "Beer’s share of reported net sales rose from 16% in FY24 to 18% in FY25 and stayed 18% in FY26. In Europe (26% of FY26 net sales), organic NS grew 3.4% in FY26 "
            "with volume flat and price/mix +3.4%, and “beer increased double-digit, led by Guinness growth in Great Britain and Ireland.” "
            "DBC USA grew organic NS 3% (FY24), 4.8% (FY25) and 4.4% (FY26), with Guinness repeatedly cited as the driver, including Guinness 0.0 in FY25. "
            "This is the clearest official example of brand strength plus mix (draught, 0.0, geographic expansion) contributing to commercial growth while spirits were under pressure."
        ),
        "key_figures": "Guinness organic NS +15% / +13% / +12% (FY24–FY26); beer 18% of FY26 reported net sales.",
        "source_codes": "F24PR; F25PR; F26PR",
    },
    {
        "n": 5,
        "title": "Geographic diversification is doing real work: Europe, LAC and Africa offset NAM and APAC",
        "takeaway": (
            "In FY26, organic net sales grew in three of five regions: Europe +3.4%, Latin America and Caribbean +7.7% (volume +3.1%, price/mix +4.6%), and Africa +13.3%, "
            "while North America was -8.4% and Asia Pacific -6.3%. Chinese white spirits organic NS fell 47% and was called out as a group mix headwind "
            "(excluding CWS, group organic NS would have been c.1.5% higher). The same diversification pattern appeared in FY25: Africa +10.5% and LAC +9.2% versus APAC -3.2% and only modest NAM +1.5%. "
            "FY24 was the inverse in LAC (organic NS -21.1%), which is why the subsequent two-year LAC recovery is commercially important. "
            "Reported regional net sales in FY26 were NAM $7,249m, Europe $5,097m, APAC $3,333m, LAC $2,160m and Africa $1,642m."
        ),
        "key_figures": "FY26 organic NS: Africa +13.3%, LAC +7.7%, Europe +3.4%, APAC -6.3%, NAM -8.4%.",
        "source_codes": "F24PR; F25PR; F26PR",
    },
    {
        "n": 6,
        "title": "Canada is not just a NAM footnote — and FY26’s +7.7% includes a one-off",
        "takeaway": (
            "Canada is reported inside North America, and Diageo does not disclose Canada net sales in dollars. The official growth series is still useful. "
            "Canada organic net sales were -2% in FY24, -0.9% in FY25, and +7.7% in FY26. FY25’s decline “reflect[ed] a weaker spirits category amid a challenging regulatory and operational backdrop which was partially offset by strong growth in Guinness.” "
            "FY26 growth was “supported by growth in Guinness and Ketel One vodka and a one-off item relating to a favourable resolution of commercial terms with a customer.” "
            "The 7.7% should therefore be read with that one-off in mind; organic volume was still -0.3%. Combined with Crown Royal’s FY26 trademark decline, the Canada commercial agenda is about underlying spirits category weakness, "
            "Guinness as an offset, and not over-reading a headline that includes a customer-terms settlement."
        ),
        "key_figures": "Canada organic NS: FY24 -2%, FY25 -0.9%, FY26 +7.7% (includes a one-off); FY26 organic volume -0.3%.",
        "source_codes": "F24PR; F25PR; F26PR",
    },
]

# Additional official facts used in commentary (not always tabular)
EXTRA_FACTS = [
    {"fact": "After three years of extraordinary topline growth, with 14.5% CAGR from fiscal 21 to fiscal 23, this fiscal, group organic net sales declined 0.6%. The main driver was materially weaker performance in LAC, which makes up 8% of Diageo’s organic net sales value. Excluding LAC, organic net sales grew 1.8%, driven by good growth in Africa, Asia Pacific, and Europe, partially offset by a decline in North America.", "source_codes": "AR24"},
    {"fact": "FY26 organic operating profit +2.0% and organic operating margin +116bps, mainly due to the benefit of cost savings, partly offset by adverse mix and tariffs. Organic gross margin down 141bps.", "source_codes": "F26PR"},
    {"fact": "Cost savings from the Accelerate programme over-delivered on guidance with $540 million Accelerate savings secured through fiscal 26.", "source_codes": "F26PR"},
    {"fact": "FY26 recommended full year dividend of 50 cents per share, in line with the new dividend policy announced on 25 February 2026.", "source_codes": "F26PR"},
    {"fact": "FY25: Diageo grew or held total market share in 65% of total net sales in measured markets, including in the US. Measured market net sales value sums to 89% of total Diageo net sales value for the twelve months ended 30 June 2025.", "source_codes": "F25PR"},
    {"fact": "FY24: Diageo grew or held total market share in over 75% of total net sales in measured markets, including in the US.", "source_codes": "F24PR"},
    {"fact": "FY25 US Spirits tequila net sales grew 16.9%; Casamigos net sales declined 18%; Don Julio shipments grew ahead of depletions growth of 36%.", "source_codes": "F25PR"},
    {"fact": "FY26 US Spirits RTDs/Cocktails net sales grew 35.1%, mainly driven by the successful launch of Casamigos RTS for the FIFA World Cup and growth in Casamigos RTD, as well as Bulleit and Ketel One Cocktails.", "source_codes": "F26PR"},
    {"fact": "FY26 net debt as at 30 June 2026 was $20.5 billion, with net debt to adjusted EBITDA of 3.1x. FY25 net debt was $21.9 billion, leverage 3.4x.", "source_codes": "F26PR; F25PR"},
]

NOT_FOUND = [
    "Absolute net sales in US dollars for individual categories (Scotch, tequila, vodka, Canadian whisky, beer, etc.). Only the published share of reported net sales and official growth rates are disclosed. Dollar amounts were not back-calculated from rounded percentages.",
    "Absolute net sales in US dollars for Canada, or for individual brands (Crown Royal, Don Julio, Guinness, etc.).",
    "Official Canada market share, Canada category size, or a standalone Canada P&L.",
    "FY23 category mix (% of net sales) and most FY23 regional organic growth rates in USD. FY23 statutory reporting was in pounds sterling; USD figures used here are only the restated comparatives printed in the FY24 prelim.",
    "FY23 reported growth rates in USD (same currency-change reason).",
    "A complete USD time series before FY23 (for example FY21–FY22 reported net sales in dollars).",
    "Official organic price/mix in percentage points for Asia Pacific (FY25 and FY26) and for Africa in FY26. The documents describe the direction of mix but do not print a pps figure; none was implied from volume and net sales.",
    "The FY26 results presentation PDF (the press release PDF was found and used; the presentation URL patterns tried returned no file).",
    "Organic operating profit growth and organic operating margin level (as opposed to the bps movement) for FY23.",
]
