#!/usr/bin/env python3
"""Build Diageo_Commercial_Dashboard.xlsx from official public figures only."""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.marker import Marker
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.page import PageMargins

from diageo_data import (
    BRANDS, CATEGORIES, EXTRA_FACTS, GROUP_KPIS, INSIGHTS,
    NAM_CANADA, NOT_FOUND, REGIONAL, SOURCES,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
XLSX = REPO_ROOT / "excel" / "Diageo_Commercial_Dashboard.xlsx"

# Diageo brand palette (https://imgcolorpicker.org/brand-colors/diageo/ and https://brandcolor.dev/brands/diageo)
CHARCOAL, PINK = "2B2B2B", "C80651"
WHITE, LIGHT_GREY = "FFFFFF", "F2F2F2"
SLATE, GRID = "6B6B6B", "D6D6D6"
PINK_PALE, PINK_LIGHT, PINK_DARK = "F5C6D6", "E36A96", "8A0438"
MID_GREY, SOFT_GREY, KPI_EDGE = "6B6B6B", "9A9A9A", "3A3A3A"

thin = Border(
    left=Side(style="thin", color=GRID), right=Side(style="thin", color=GRID),
    top=Side(style="thin", color=GRID), bottom=Side(style="thin", color=GRID),
)
hair = Border(
    left=Side(style="hair", color=GRID), right=Side(style="hair", color=GRID),
    top=Side(style="hair", color=GRID), bottom=Side(style="hair", color=GRID),
)
fill_charcoal = PatternFill("solid", fgColor=CHARCOAL)
fill_band = PatternFill("solid", fgColor=LIGHT_GREY)
fill_ivory = PatternFill("solid", fgColor=LIGHT_GREY)
fill_white = PatternFill("solid", fgColor=WHITE)
fill_header = PatternFill("solid", fgColor=CHARCOAL)
fill_alt = PatternFill("solid", fgColor=LIGHT_GREY)
fill_kpi = PatternFill("solid", fgColor=CHARCOAL)

font_title = Font(name="Calibri", size=22, bold=True, color=WHITE)
font_subtitle = Font(name="Calibri", size=11, italic=True, color=PINK_PALE)
font_section = Font(name="Calibri", size=13, bold=True, color=CHARCOAL)
font_header = Font(name="Calibri", size=9, bold=True, color=WHITE)
font_body = Font(name="Calibri", size=10, color=CHARCOAL)
font_small = Font(name="Calibri", size=8, color=SLATE, italic=True)
font_kpi_label = Font(name="Calibri", size=8, bold=True, color=PINK_PALE)
font_kpi_value = Font(name="Calibri", size=18, bold=True, color=WHITE)
font_kpi_sub = Font(name="Calibri", size=8, color=PINK_PALE)
font_insight_title = Font(name="Calibri", size=12, bold=True, color=CHARCOAL)
font_link = Font(name="Calibri", size=9, color=PINK, underline="single")

center = Alignment(horizontal="center", vertical="center", wrap_text=True)
left = Alignment(horizontal="left", vertical="center", wrap_text=True)
left_top = Alignment(horizontal="left", vertical="top", wrap_text=True)


def source_url(codes):
    return SOURCES[codes.split(";")[0].strip()]["url"]


def source_docs(codes):
    return " | ".join(SOURCES[c.strip()]["document"] for c in codes.split(";"))


def enrich(row):
    out = dict(row)
    out["source_document"] = source_docs(row["source_codes"])
    out["source_url"] = source_url(row["source_codes"])
    return out


def write_header_row(ws, row, headers, start_col=1):
    for i, h in enumerate(headers, start_col):
        cell = ws.cell(row, i, h)
        cell.font, cell.fill, cell.alignment, cell.border = font_header, fill_header, center, thin


def apply_data_row(cell, even=False, fmt=None, align=None):
    cell.font = font_body
    cell.fill = fill_alt if even else fill_white
    cell.border = hair
    cell.alignment = align or left
    if fmt:
        cell.number_format = fmt


def style_sheet(ws, tab_color=PINK):
    ws.sheet_properties.tabColor = tab_color
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.page_setup.paperSize = ws.PAPERSIZE_TABLOID
    ws.page_margins = PageMargins(0.4, 0.4, 0.5, 0.4, 0.3, 0.3)
    ws.sheet_view.showGridLines = False
    ws.oddFooter.left.text = "Diageo Commercial Analytics  |  Public disclosures only  |  Rushabh Kabra portfolio"
    ws.oddFooter.right.text = "Sources on the Sources sheet  |  Page &P"


def paint_range(ws, r1, c1, r2, c2, fill):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            ws.cell(r, c).fill = fill


GROUP_FIELDS = [
    "fiscal_year", "year_ended", "reported_net_sales_usd_m", "reported_ns_movement_pct",
    "organic_ns_movement_usd_m", "organic_ns_movement_pct", "organic_volume_movement_pct",
    "organic_price_mix_pps", "volume_eu_m", "reported_volume_movement_pct",
    "reported_operating_profit_usd_m", "reported_op_movement_pct", "reported_op_margin_pct",
    "reported_op_margin_basis", "op_before_exceptionals_usd_m", "organic_op_movement_pct",
    "organic_op_margin_movement_bps", "op_margin_before_exceptionals_pct",
    "op_margin_before_exceptionals_basis", "gross_profit_usd_m", "marketing_usd_m",
    "free_cash_flow_usd_m", "eps_before_exceptionals_cents", "recommended_dividend_cents",
    "source_codes", "source_document", "source_url", "notes",
]
GROUP_HEADERS = [
    "Fiscal year", "Year ended", "Reported net sales ($m)", "Reported NS movement (%)",
    "Organic NS movement ($m)", "Organic NS movement (%)", "Organic volume movement (%)",
    "Organic price/mix (pps)", "Volume (EUm)", "Reported volume movement (%)",
    "Reported operating profit ($m)", "Reported OP movement (%)", "Reported OP margin (%)",
    "Reported OP margin basis", "OP before exceptionals ($m)", "Organic OP movement (%)",
    "Organic OP margin movement (bps)", "OP margin before exceptionals (%)",
    "Before-exceptionals margin basis", "Gross profit ($m)", "Marketing ($m)",
    "Free cash flow ($m)", "EPS before exceptionals (cents)", "Recommended dividend (cents)",
    "Source codes", "Source document", "Source URL", "Notes",
]
REGIONAL_FIELDS = [
    "fiscal_year", "region", "volume_eu_m", "reported_ns_usd_m", "marketing_usd_m",
    "opbe_usd_m", "reported_op_usd_m", "reported_volume_mov_pct", "reported_ns_mov_pct",
    "organic_volume_mov_pct", "organic_ns_mov_pct", "organic_marketing_mov_pct",
    "organic_opbe_mov_pct", "official_share_of_group_ns_pct", "organic_price_mix_pps",
    "organic_op_margin_movement_bps", "stated_operating_margin_pct",
    "source_codes", "source_document", "source_url", "notes",
]
REGIONAL_HEADERS = [
    "Fiscal year", "Region", "Volume (EUm)", "Reported net sales ($m)", "Marketing ($m)",
    "OP before exceptionals ($m)", "Reported operating profit ($m)", "Reported volume movement (%)",
    "Reported NS movement (%)", "Organic volume movement (%)", "Organic NS movement (%)",
    "Organic marketing movement (%)", "Organic OPBE movement (%)", "Official share of group NS (%)",
    "Organic price/mix (pps)", "Organic OP margin movement (bps)", "Stated operating margin (%)",
    "Source codes", "Source document", "Source URL", "Notes",
]
CAT_FIELDS = [
    "fiscal_year", "category", "organic_volume_mov_pct", "organic_ns_mov_pct",
    "reported_ns_mov_pct", "reported_ns_by_category_pct",
    "source_codes", "source_document", "source_url", "notes",
]
CAT_HEADERS = [
    "Fiscal year", "Category", "Organic volume movement (%)", "Organic NS movement (%)",
    "Reported NS movement (%)", "Reported NS by category (%)",
    "Source codes", "Source document", "Source URL", "Notes",
]
BRAND_FIELDS = [
    "fiscal_year", "brand", "organic_volume_mov_pct", "organic_ns_mov_pct",
    "reported_ns_mov_pct", "source_codes", "source_document", "source_url", "notes",
]
BRAND_HEADERS = [
    "Fiscal year", "Brand", "Organic volume movement (%)", "Organic NS movement (%)",
    "Reported NS movement (%)", "Source codes", "Source document", "Source URL", "Notes",
]
NAM_FIELDS = [
    "fiscal_year", "market", "organic_volume_mov_pct", "reported_volume_mov_pct",
    "organic_ns_mov_pct", "reported_ns_mov_pct",
    "source_codes", "source_document", "source_url", "notes",
]
NAM_HEADERS = [
    "Fiscal year", "Market", "Organic volume movement (%)", "Reported volume movement (%)",
    "Organic NS movement (%)", "Reported NS movement (%)",
    "Source codes", "Source document", "Source URL", "Notes",
]


def add_data_sheet(wb, name, title, fields, headers, rows, tab_color=PINK):
    ws = wb.create_sheet(name)
    style_sheet(ws, tab_color)
    paint_range(ws, 1, 1, 3, len(headers), fill_charcoal)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(headers))
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(headers))
    ws.cell(1, 1, title).font = Font(name="Calibri", size=16, bold=True, color=WHITE)
    ws.cell(1, 1).alignment = Alignment(vertical="center", horizontal="left")
    ws.cell(2, 1, "Official Diageo public disclosures only. Blank cells mean the figure was not found in the cited sources — nothing has been estimated. Every row has a source URL.").font = font_subtitle
    ws.row_dimensions[1].height = 22
    ws.row_dimensions[2].height = 18
    write_header_row(ws, 4, headers)
    ws.freeze_panes = "A5"
    pct_keys = {f for f in fields if f.endswith("_pct") or f.endswith("_pps")}
    for i, raw in enumerate(rows):
        r = enrich(raw)
        even = i % 2 == 1
        for j, f in enumerate(fields, 1):
            val = r.get(f)
            cell = ws.cell(5 + i, j, None if val == "" else val)
            fmt = None
            if f in pct_keys and val is not None:
                fmt = "0.0"
            elif f.endswith("_usd_m") and val is not None:
                fmt = "#,##0.0" if isinstance(val, float) and not float(val).is_integer() else "#,##0"
            elif f.endswith("_eu_m") and val is not None:
                fmt = "0.0"
            elif f.endswith("_cents") and val is not None:
                fmt = "0.0"
            elif f.endswith("_bps") and val is not None:
                fmt = "+0;-0;0"
            long = f in ("notes", "source_document", "source_url", "reported_op_margin_basis", "op_margin_before_exceptionals_basis")
            apply_data_row(cell, even, fmt=fmt, align=left_top if long else left)
            if f == "source_url" and val:
                cell.hyperlink = val
                cell.font = font_link
        ws.row_dimensions[5 + i].height = 48 if "notes" in fields else 18
    widths = {}
    for j, f in enumerate(fields, 1):
        letter = get_column_letter(j)
        if f in ("notes", "source_document", "reported_op_margin_basis", "op_margin_before_exceptionals_basis"):
            widths[letter] = 44
        elif f == "source_url":
            widths[letter] = 28
        elif f in ("fiscal_year", "source_codes", "year_ended"):
            widths[letter] = 12
        elif f in ("region", "category", "brand", "market"):
            widths[letter] = 22
        else:
            widths[letter] = 14
        ws.column_dimensions[letter].width = widths[letter]
    ws.auto_filter.ref = f"A4:{get_column_letter(len(headers))}{4 + len(rows)}"
    return ws


def color_bar_series(chart, colors):
    for s, color in zip(chart.series, colors):
        s.graphicalProperties.solidFill = color
        s.graphicalProperties.line.solidFill = color


def color_line_series(series, color, marker="circle"):
    series.graphicalProperties.line.solidFill = color
    series.graphicalProperties.line.width = 18000
    series.marker = Marker(symbol=marker, size=7)
    series.marker.graphicalProperties.solidFill = color
    series.marker.graphicalProperties.line.solidFill = color


def build_chart_data(wb):
    ws = wb.create_sheet("Chart_Data")
    style_sheet(ws, LIGHT_GREY)
    paint_range(ws, 1, 1, 2, 16, fill_charcoal)
    ws.merge_cells("A1:P1")
    ws.cell(1, 1, "Chart data (binding ranges only)").font = Font(name="Calibri", size=16, bold=True, color=WHITE)
    ws.merge_cells("A2:P2")
    ws.cell(2, 1, "Every value here is copied from the official Data_* tabs. No new figures. Used so Excel charts have clean ranges.").font = font_subtitle
    regions = ["North America", "Europe", "Asia Pacific", "Latin America and Caribbean", "Africa"]

    ws.cell(4, 1, "Regional reported net sales ($m)").font = font_section
    write_header_row(ws, 5, ["Region", "FY23", "FY24", "FY25", "FY26"])
    for i, r in enumerate(regions):
        apply_data_row(ws.cell(6 + i, 1, r), i % 2)
        for j, y in enumerate(["FY23", "FY24", "FY25", "FY26"], 2):
            val = next(x for x in REGIONAL if x["fiscal_year"] == y and x["region"] == r)["reported_ns_usd_m"]
            apply_data_row(ws.cell(6 + i, j, val), i % 2, fmt="#,##0", align=center)

    ws.cell(51, 1, "Regional NS transposed (years as categories)").font = font_section
    write_header_row(ws, 52, ["Fiscal year"] + regions)
    for j, y in enumerate(["FY23", "FY24", "FY25", "FY26"]):
        apply_data_row(ws.cell(53 + j, 1, y), j % 2, align=center)
        for k, r in enumerate(regions, 2):
            val = next(x for x in REGIONAL if x["fiscal_year"] == y and x["region"] == r)["reported_ns_usd_m"]
            apply_data_row(ws.cell(53 + j, k, val), j % 2, fmt="#,##0", align=center)

    ws.cell(58, 1, "Organic regional transposed").font = font_section
    write_header_row(ws, 59, ["Fiscal year"] + regions)
    for j, y in enumerate(["FY24", "FY25", "FY26"]):
        apply_data_row(ws.cell(60 + j, 1, y), j % 2, align=center)
        for k, r in enumerate(regions, 2):
            val = next(x for x in REGIONAL if x["fiscal_year"] == y and x["region"] == r)["organic_ns_mov_pct"]
            apply_data_row(ws.cell(60 + j, k, val), j % 2, fmt="0.0", align=center)

    ws.cell(64, 1, "Volume / price-mix transposed").font = font_section
    write_header_row(ws, 65, ["Fiscal year", "Organic volume %", "Organic price/mix (pps)", "Organic net sales %"])
    for j, y in enumerate(["FY23", "FY24", "FY25", "FY26"]):
        g = next(x for x in GROUP_KPIS if x["fiscal_year"] == y)
        apply_data_row(ws.cell(66 + j, 1, y), j % 2, align=center)
        apply_data_row(ws.cell(66 + j, 2, g["organic_volume_movement_pct"]), j % 2, fmt="0.0", align=center)
        apply_data_row(ws.cell(66 + j, 3, g["organic_price_mix_pps"]), j % 2, fmt="0.0", align=center)
        apply_data_row(ws.cell(66 + j, 4, g["organic_ns_movement_pct"]), j % 2, fmt="0.0", align=center)

    ws.cell(71, 1, "Margins transposed").font = font_section
    write_header_row(ws, 72, ["Fiscal year", "Reported operating margin %", "Margin before exceptional items %"])
    for j, y in enumerate(["FY23", "FY24", "FY25", "FY26"]):
        g = next(x for x in GROUP_KPIS if x["fiscal_year"] == y)
        apply_data_row(ws.cell(73 + j, 1, y), j % 2, align=center)
        apply_data_row(ws.cell(73 + j, 2, g["reported_op_margin_pct"]), j % 2, fmt="0.0", align=center)
        apply_data_row(ws.cell(73 + j, 3, g["op_margin_before_exceptionals_pct"]), j % 2, fmt="0.0", align=center)

    ws.cell(31, 1, "FY26 category share of reported NS (%) and organic NS %").font = font_section
    write_header_row(ws, 32, ["Category", "Share of reported NS %", "Organic NS %"])
    cat_rows = [c for c in CATEGORIES if c["fiscal_year"] == "FY26" and c["category"] != "Spirits" and c["reported_ns_by_category_pct"] is not None]
    cat_rows = sorted(cat_rows, key=lambda r: r["reported_ns_by_category_pct"], reverse=True)
    for i, r in enumerate(cat_rows):
        apply_data_row(ws.cell(33 + i, 1, r["category"]), i % 2)
        apply_data_row(ws.cell(33 + i, 2, r["reported_ns_by_category_pct"]), i % 2, fmt="0.0", align=center)
        apply_data_row(ws.cell(33 + i, 3, r["organic_ns_mov_pct"]), i % 2, fmt="0.0", align=center)

    for i in range(1, 8):
        ws.column_dimensions[get_column_letter(i)].width = 16 if i > 1 else 36
    ws.row_dimensions[1].height = 22
    return ws


def kpi_card(ws, r, c, label, value, sub, cols=3, rows=5):
    for rr in range(r, r + rows):
        for cc in range(c, c + cols):
            ws.cell(rr, cc).fill = fill_kpi
            ws.cell(rr, cc).border = Border(
                left=Side(style="thin", color=KPI_EDGE),
                right=Side(style="thin", color=KPI_EDGE),
                top=Side(style="thin", color=PINK) if rr == r else Side(style="thin", color=KPI_EDGE),
                bottom=Side(style="thin", color=KPI_EDGE),
            )
    ws.merge_cells(start_row=r, start_column=c, end_row=r + 1, end_column=c + cols - 1)
    lab = ws.cell(r, c, label.upper())
    lab.font = font_kpi_label
    lab.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.merge_cells(start_row=r + 2, start_column=c, end_row=r + 3, end_column=c + cols - 1)
    val = ws.cell(r + 2, c, value)
    val.font = font_kpi_value
    val.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.merge_cells(start_row=r + 4, start_column=c, end_row=r + 4, end_column=c + cols - 1)
    subc = ws.cell(r + 4, c, sub)
    subc.font = font_kpi_sub
    subc.alignment = Alignment(horizontal="left", vertical="center", indent=1, wrap_text=True)


def build_dashboard(wb):
    ws = wb.create_sheet("Dashboard", 0)
    style_sheet(ws, CHARCOAL)
    for col in range(1, 19):
        ws.column_dimensions[get_column_letter(col)].width = 11.2
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["R"].width = 3

    paint_range(ws, 1, 1, 4, 18, fill_charcoal)
    ws.merge_cells("B2:L2")
    ws.cell(2, 2, "DIAGEO  ·  COMMERCIAL ANALYTICS DASHBOARD").font = font_title
    ws.merge_cells("B3:L3")
    ws.cell(3, 2, "Portfolio analysis for the Commercial Analyst (Canada) role  ·  Rushabh Kabra  ·  Public company disclosures only").font = font_subtitle
    ws.merge_cells("M2:Q3")
    ws.cell(2, 13, "FY26 year ended 30 June 2026\nResults published 6 August 2026\nCurrency: USD").font = Font(name="Calibri", size=9, color=PINK_PALE)
    ws.cell(2, 13).alignment = Alignment(horizontal="right", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 10
    ws.row_dimensions[2].height = 24
    ws.row_dimensions[3].height = 18
    ws.row_dimensions[4].height = 8

    kpi_card(ws, 6, 2, "Reported net sales", "$19,643m", "FY26  ·  reported -3.0%  ·  FY25 $20,245m")
    kpi_card(ws, 6, 5, "Organic net sales", "-2.0%", "Volume -0.4%  ·  price/mix -1.6pps  ·  -$386m")
    kpi_card(ws, 6, 8, "Adj. operating margin", "28.9%", "Before exceptionals  ·  +116bps organic  ·  OP +2.0%")
    kpi_card(ws, 6, 11, "Reported OP margin", "16.1%", "Down 535bps  ·  reported OP $3,156m (-27.2%)")
    kpi_card(ws, 6, 14, "North America share", "37%", "FY26 organic NS -8.4%  ·  reported NS $7,249m")
    for r in range(6, 11):
        ws.row_dimensions[r].height = 16
    ws.row_dimensions[8].height = 20
    ws.row_dimensions[9].height = 20
    ws.row_dimensions[11].height = 10

    ws.merge_cells("B12:I12")
    ws.cell(12, 2, "REGIONAL REPORTED NET SALES ($m)").font = font_section
    ws.merge_cells("J12:Q12")
    ws.cell(12, 10, "ORGANIC NS: VOLUME VS PRICE/MIX").font = font_section
    ws.row_dimensions[12].height = 18

    cd = "Chart_Data"
    c1 = BarChart()
    c1.type, c1.grouping = "col", "clustered"
    c1.title = "Reported net sales by region"
    c1.y_axis.title = "$ million"
    c1.y_axis.numFmt = "#,##0"
    c1.style = 10
    data = Reference(wb[cd], min_col=2, min_row=52, max_col=6, max_row=56)
    cats = Reference(wb[cd], min_col=1, min_row=53, max_row=56)
    c1.add_data(data, from_rows=False, titles_from_data=True)
    c1.set_categories(cats)
    color_bar_series(c1, [CHARCOAL, PINK, MID_GREY, PINK_LIGHT, PINK_DARK])
    c1.legend.position = "b"
    c1.y_axis.majorGridlines.spPr = GraphicalProperties(ln=LineProperties(solidFill="D6D6D6"))
    c1.width, c1.height = 15, 8
    ws.add_chart(c1, "B13")

    bar = BarChart()
    bar.type, bar.grouping = "col", "clustered"
    bar.title = "Organic volume, price/mix and net sales"
    bar.y_axis.title = "%"
    bar.y_axis.numFmt = "0.0"
    bar.style = 10
    data = Reference(wb[cd], min_col=2, min_row=65, max_col=3, max_row=69)
    cats = Reference(wb[cd], min_col=1, min_row=66, max_row=69)
    bar.add_data(data, titles_from_data=True)
    bar.set_categories(cats)
    color_bar_series(bar, [CHARCOAL, PINK])
    line = LineChart()
    ldata = Reference(wb[cd], min_col=4, min_row=65, max_row=69)
    line.add_data(ldata, titles_from_data=True)
    line.set_categories(cats)
    color_line_series(line.series[0], PINK, "circle")
    line.y_axis.numFmt = "0.0"
    bar.legend.position = "b"
    bar.width, bar.height = 15, 8
    bar += line
    ws.add_chart(bar, "J13")

    ws.row_dimensions[13].height = 8
    for r in range(14, 28):
        ws.row_dimensions[r].height = 15
    ws.row_dimensions[28].height = 8

    ws.merge_cells("B29:I29")
    ws.cell(29, 2, "OPERATING MARGIN TREND (%)").font = font_section
    ws.merge_cells("J29:Q29")
    ws.cell(29, 10, "FY26 CATEGORY MIX (% OF REPORTED NET SALES)").font = font_section

    m = LineChart()
    m.title = "Reported vs before-exceptional operating margin"
    m.style = 10
    m.y_axis.title = "%"
    m.y_axis.numFmt = "0.0"
    mdata = Reference(wb[cd], min_col=2, min_row=72, max_col=3, max_row=76)
    mcats = Reference(wb[cd], min_col=1, min_row=73, max_row=76)
    m.add_data(mdata, titles_from_data=True)
    m.set_categories(mcats)
    color_line_series(m.series[0], CHARCOAL, "circle")
    color_line_series(m.series[1], PINK, "square")
    m.legend.position = "b"
    m.width, m.height = 15, 8
    m.y_axis.scaling.min = 12
    m.y_axis.scaling.max = 34
    ws.add_chart(m, "B30")

    cat = BarChart()
    cat.type, cat.grouping = "bar", "clustered"
    cat.title = "FY26 share of reported net sales"
    cat.style = 10
    cat.x_axis.title = "% of reported net sales"
    cdata = Reference(wb[cd], min_col=2, min_row=32, max_row=44)
    ccats = Reference(wb[cd], min_col=1, min_row=33, max_row=44)
    cat.add_data(cdata, titles_from_data=True)
    cat.set_categories(ccats)
    color_bar_series(cat, [PINK])
    cat.legend = None
    cat.width, cat.height = 15, 8
    ws.add_chart(cat, "J30")

    for r in range(30, 45):
        ws.row_dimensions[r].height = 15

    ws.merge_cells("B46:Q46")
    ws.cell(46, 2, "SELECTED FY26 COMMERCIAL SIGNALS  ·  each figure is official and cited on the Insights and Sources sheets").font = font_section
    callouts = [
        ("Europe / LAC / Africa", "Organic NS +3.4% / +7.7% / +13.3%\nOffsetting NAM -8.4% and APAC -6.3%"),
        ("Guinness / beer", "Guinness organic NS +12%\nBeer 18% of reported net sales"),
        ("Tequila reversal", "Tequila organic NS -16%\nAfter +18% in FY25"),
        ("Crown Royal / Canada", "Crown Royal whisky NS -15.9%\nCanada organic NS +7.7% (includes a one-off)"),
        ("Cost vs mix", "Organic OP +2.0% and margin +116bps\ndespite organic NS -2.0%; marketing -13.1%"),
    ]
    start = 2
    for i, (t, body) in enumerate(callouts):
        c = start + i * 3
        paint_range(ws, 47, c, 50, c + 2, fill_band)
        for rr in range(47, 51):
            for cc in range(c, c + 3):
                ws.cell(rr, cc).border = Border(
                    left=Side(style="thin", color=GRID),
                    right=Side(style="thin", color=GRID),
                    top=Side(style="medium", color=PINK) if rr == 47 else Side(style="thin", color=GRID),
                    bottom=Side(style="thin", color=GRID),
                )
        ws.merge_cells(start_row=47, start_column=c, end_row=47, end_column=c + 2)
        ws.cell(47, c, t.upper()).font = Font(name="Calibri", size=8, bold=True, color=PINK)
        ws.cell(47, c).alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.merge_cells(start_row=48, start_column=c, end_row=50, end_column=c + 2)
        ws.cell(48, c, body).font = Font(name="Calibri", size=9, color=CHARCOAL)
        ws.cell(48, c).alignment = Alignment(horizontal="left", vertical="top", indent=1, wrap_text=True)
    for rr in (47, 48, 49, 50):
        ws.row_dimensions[rr].height = 16

    ws.merge_cells("B52:Q53")
    ws.cell(52, 2, (
        "Notes: Organic measures are non-GAAP as defined by Diageo (see each prelim, calculation and use of non-GAAP measures). "
        "FY23 reported dollar figures are restated USD comparatives from the FY24 prelim (Diageo changed presentation currency). "
        "FY23-FY24 before-exceptional and FY23-FY24 reported margin levels are calculated as official profit divided by official net sales; FY25-FY26 margin headlines are as printed. "
        "Category shares do not always sum to 100%. No category or Canada dollar figures have been back-calculated. "
        "Sources: Diageo plc Preliminary Results FY24, FY25, FY26 and Annual Reports 2023 and 2024, all at diageo.com. Prepared 12 November 2026 for interview/recruiter use — not submitted as a HireVue assessment and not an official Diageo report."
    )).font = font_small
    ws.cell(52, 2).alignment = left_top
    ws.row_dimensions[52].height = 20
    ws.row_dimensions[53].height = 20
    ws.print_area = "A1:R54"
    ws.page_setup.fitToHeight = 1
    ws.sheet_view.zoomScale = 90
    return ws


def build_insights(wb):
    ws = wb.create_sheet("Insights")
    style_sheet(ws, PINK)
    for col, w in {"A": 3, "B": 8, "C": 36, "D": 90, "E": 42, "F": 28, "G": 3}.items():
        ws.column_dimensions[col].width = w
    paint_range(ws, 1, 1, 4, 7, fill_charcoal)
    ws.merge_cells("B2:F2")
    ws.cell(2, 2, "ANALYST TAKEAWAYS").font = font_title
    ws.merge_cells("B3:F3")
    ws.cell(3, 2, "Six commercial observations, each tied to a cited official figure. Nothing here is estimated or invented.").font = font_subtitle
    ws.row_dimensions[2].height = 24
    write_header_row(ws, 5, ["#", "Takeaway", "Analysis", "Key official figures", "Source and URL"], start_col=2)
    r = 6
    for ins in INSIGHTS:
        for col in range(2, 7):
            apply_data_row(ws.cell(r, col), False, align=left_top)
            ws.cell(r, col).fill = fill_ivory
        ws.cell(r, 2, ins["n"]).font = Font(name="Calibri", size=16, bold=True, color=PINK)
        ws.cell(r, 2).alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(r, 3, ins["title"]).font = font_insight_title
        ws.cell(r, 4, ins["takeaway"]).font = font_body
        ws.cell(r, 5, ins["key_figures"]).font = Font(name="Calibri", size=10, bold=True, color=CHARCOAL)
        codes = ins["source_codes"]
        ws.cell(r, 6, source_docs(codes) + "\n" + source_url(codes)).font = font_link
        ws.cell(r, 6).hyperlink = source_url(codes)
        ws.row_dimensions[r].height = 120
        r += 1
    r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    ws.cell(r, 2, "Additional official facts used in the dashboard (not otherwise a standalone takeaway)").font = font_section
    r += 1
    write_header_row(ws, r, ["#", "Fact (continues in next columns)", " ", "Source document", "Source URL"], start_col=2)
    r += 1
    for i, fact in enumerate(EXTRA_FACTS, 1):
        apply_data_row(ws.cell(r, 2, i), i % 2 == 0, align=center)
        apply_data_row(ws.cell(r, 3, fact["fact"]), i % 2 == 0, align=left_top)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        apply_data_row(ws.cell(r, 4), i % 2 == 0)
        apply_data_row(ws.cell(r, 5, source_docs(fact["source_codes"])), i % 2 == 0, align=left_top)
        apply_data_row(ws.cell(r, 6, source_url(fact["source_codes"])), i % 2 == 0, align=left_top)
        ws.cell(r, 6).hyperlink = source_url(fact["source_codes"])
        ws.cell(r, 6).font = font_link
        ws.row_dimensions[r].height = 48
        r += 1
    r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
    ws.cell(r, 2, "What could not be found in official sources (left out on purpose)").font = font_section
    r += 1
    for i, item in enumerate(NOT_FOUND, 1):
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
        apply_data_row(ws.cell(r, 2, f"{i}.  {item}"), False, align=left_top)
        ws.row_dimensions[r].height = 28
        r += 1
    ws.freeze_panes = "B6"
    return ws


def build_sources(wb):
    ws = wb.create_sheet("Sources")
    style_sheet(ws, CHARCOAL)
    for col, w in {"A": 3, "B": 16, "C": 70, "D": 70, "E": 70, "F": 3}.items():
        ws.column_dimensions[col].width = w
    paint_range(ws, 1, 1, 4, 6, fill_charcoal)
    ws.merge_cells("B2:E2")
    ws.cell(2, 2, "SOURCES AND METHODOLOGY").font = font_title
    ws.merge_cells("B3:E3")
    ws.cell(3, 2, "Every number in this workbook traces to one of the documents below. PDFs were downloaded from diageo.com on 12 November 2026.").font = font_subtitle
    write_header_row(ws, 5, ["Code", "Document", "PDF (primary source)", "Web page"], start_col=2)
    r = 6
    for code, meta in SOURCES.items():
        apply_data_row(ws.cell(r, 2, code), False, align=center)
        ws.cell(r, 2).font = Font(name="Calibri", size=11, bold=True, color=CHARCOAL)
        apply_data_row(ws.cell(r, 3, meta["document"]), False, align=left)
        apply_data_row(ws.cell(r, 4, meta["url"]), False, align=left)
        ws.cell(r, 4).hyperlink = meta["url"]
        ws.cell(r, 4).font = font_link
        apply_data_row(ws.cell(r, 5, meta["web"]), False, align=left)
        ws.cell(r, 5).hyperlink = meta["web"]
        ws.cell(r, 5).font = font_link
        ws.row_dimensions[r].height = 28
        r += 1
    r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    ws.cell(r, 2, "Methodology").font = font_section
    r += 1
    method = (
        "Scope. Group, regional, category, brand and North America/Canada figures for fiscal years ended 30 June 2023, 2024, 2025 and 2026, taken from Diageo plc preliminary results and annual reports published on diageo.com.\n\n"
        "No estimates. If a figure was not printed, the cell is left blank. Category and brand net sales in dollars are not disclosed and have not been back-calculated from rounded percentages. Organic price/mix in pps is included only where Diageo printed it, not as organic NS minus organic volume.\n\n"
        "Organic measures. Treated as non-GAAP measures as defined by Diageo. Price/mix is the number of percentage points difference between the organic movement in net sales and the organic movement in volume (FY25 prelim definition). Percentage movements in commentary are organic unless stated as reported.\n\n"
        "Currency and restatement. Diageo presents results in US dollars in the FY24-FY26 prelims. FY23 reported dollar figures and volumes used here are the re-presented comparatives printed in the FY24 prelim, not a currency translation performed for this workbook. FY23 organic growth rates (6.5%, volume -0.8%, price/mix +7.3pps) are from Annual Report 2023 and are currency-independent percentages.\n\n"
        "Calculated margins. Operating margin is defined by Diageo as operating profit (or operating profit before exceptional items) divided by net sales. FY25 and FY26 reported and before-exceptional margins are official headlines (21.4% / 28.2% and 16.1% / 28.9%). FY23 and FY24 margin levels are calculated from official profit and official net sales and are labelled as calculated; the FY24 official +262bps reported-margin movement is consistent with those calculated levels.\n\n"
        "Rounding. Where a document prints both a rounded table and a more precise headline (for example FY24 group organic NS -0.6% vs a table of (1)%, or LAC -21.1% vs (21)%), the more precise official figure is used, and the notes column records the rounding.\n\n"
        "Purpose. Prepared on 12 November 2026 as a portfolio piece for Rushabh Kabra, candidate for Diageo's Commercial Analyst role in Canada, to show structured commercial analysis of public data. It is not an official Diageo document, not investment advice, and not a submission of any HireVue or online assessment."
    )
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    apply_data_row(ws.cell(r, 2, method), False, align=left_top)
    ws.row_dimensions[r].height = 220
    r += 2
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    ws.cell(r, 2, "What could not be found").font = font_section
    r += 1
    for item in NOT_FOUND:
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
        apply_data_row(ws.cell(r, 2, "•  " + item), False, align=left_top)
        ws.row_dimensions[r].height = 28
        r += 1
    return ws


def build_workbook():
    wb = Workbook()
    default = wb.active
    default.title = "_tmp"
    build_chart_data(wb)
    add_data_sheet(wb, "Data_Group_KPIs", "Group KPIs  ·  official reported and organic measures", GROUP_FIELDS, GROUP_HEADERS, GROUP_KPIS)
    add_data_sheet(wb, "Data_Regional", "Regional results  ·  official reported $ and organic movements", REGIONAL_FIELDS, REGIONAL_HEADERS, REGIONAL)
    add_data_sheet(wb, "Data_Category", "Category results  ·  official growth rates and share of reported net sales", CAT_FIELDS, CAT_HEADERS, CATEGORIES)
    add_data_sheet(wb, "Data_Brands", "Key brands  ·  official organic and reported movements (brand dollar sales not disclosed)", BRAND_FIELDS, BRAND_HEADERS, BRANDS)
    add_data_sheet(wb, "Data_NAM_Canada", "North America markets, including Canada  ·  official movements (Canada dollar sales not disclosed)", NAM_FIELDS, NAM_HEADERS, NAM_CANADA, tab_color=PINK_DARK)
    build_insights(wb)
    build_sources(wb)
    build_dashboard(wb)
    order = [
        "Dashboard", "Insights", "Data_Group_KPIs", "Data_Regional",
        "Data_Category", "Data_Brands", "Data_NAM_Canada", "Chart_Data", "Sources",
    ]
    for i, name in enumerate(order):
        wb.move_sheet(name, offset=i - wb.sheetnames.index(name))
    if "_tmp" in wb.sheetnames:
        del wb["_tmp"]
    wb.properties.title = "Diageo Commercial Analytics Dashboard"
    wb.properties.creator = "Rushabh Kabra — portfolio dashboard from public Diageo disclosures"
    wb.properties.description = (
        "Commercial analytics dashboard built from Diageo plc official preliminary results and annual reports. "
        "No estimated figures. Prepared 12 November 2026."
    )
    wb.save(XLSX)
    return XLSX


if __name__ == "__main__":
    path = build_workbook()
    print("Workbook written to", path, "size", path.stat().st_size)
