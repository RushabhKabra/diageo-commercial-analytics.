#!/usr/bin/env python3
"""Matplotlib chart PNGs — official Diageo figures only."""
from pathlib import Path
import matplotlib.pyplot as plt
from diageo_data import GROUP_KPIS, REGIONAL, CATEGORIES, BRANDS, NAM_CANADA

REPO_ROOT = Path(__file__).resolve().parent.parent
CHARTS = REPO_ROOT / "charts"

# Diageo brand palette (https://imgcolorpicker.org/brand-colors/diageo/ and https://brandcolor.dev/brands/diageo)
CHARCOAL = "#2B2B2B"
PINK = "#C80651"
WHITE = "#FFFFFF"
LIGHT_GREY = "#F2F2F2"
MID_GREY = "#6B6B6B"
SOFT_GREY = "#9A9A9A"
PINK_DARK = "#8A0438"
PINK_LIGHT = "#E36A96"
SLATE = "#6B6B6B"
GRID = "#D6D6D6"

REGION_COLORS = {
    "North America": CHARCOAL,
    "Europe": PINK,
    "Asia Pacific": MID_GREY,
    "Latin America and Caribbean": PINK_LIGHT,
    "Africa": PINK_DARK,
    "Corporate": SOFT_GREY,
}


def setup():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.facecolor": WHITE,
        "figure.facecolor": WHITE,
        "axes.edgecolor": GRID,
        "axes.labelcolor": CHARCOAL,
        "xtick.color": CHARCOAL,
        "ytick.color": CHARCOAL,
        "text.color": CHARCOAL,
        "axes.titleweight": "bold",
        "axes.titlesize": 14,
        "axes.labelsize": 10,
        "axes.grid": True,
        "grid.color": LIGHT_GREY,
        "grid.linewidth": 0.6,
        "axes.axisbelow": True,
    })


def footnote(fig, text):
    fig.text(0.02, 0.015, text, fontsize=7, color=SLATE, style="italic", ha="left", va="bottom")


def title(ax, heading, subtitle=None):
    ax.set_title(heading, loc="left", color=CHARCOAL, pad=14)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=8.5, color=SLATE, va="bottom")


def chart_regional_ns():
    years = ["FY23", "FY24", "FY25", "FY26"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America and Caribbean", "Africa"]
    data = {r: [] for r in regions}
    for y in years:
        for r in regions:
            row = next(x for x in REGIONAL if x["fiscal_year"] == y and x["region"] == r)
            data[r].append(row["reported_ns_usd_m"] / 1000)
    fig, ax = plt.subplots(figsize=(11.5, 6.2), dpi=180)
    x = range(len(years))
    n = len(regions)
    width = 0.15
    for i, r in enumerate(regions):
        offs = [xi + (i - (n - 1) / 2) * width for xi in x]
        label = "LAC" if r == "Latin America and Caribbean" else r
        bars = ax.bar(offs, data[r], width=width * 0.92, color=REGION_COLORS[r], label=label, zorder=3)
        for b, val in zip(bars, data[r]):
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.08, f"{val:.2f}", ha="center", va="bottom", fontsize=6.5, color=CHARCOAL)
    ax.set_xticks(list(x))
    ax.set_xticklabels(years)
    ax.set_ylabel("Reported net sales (USD billion)")
    ax.set_ylim(0, 9.4)
    title(ax, "Reported net sales by region", "USD, as published  •  FY23 figures are restated comparatives from the FY24 prelim")
    ax.legend(frameon=False, ncol=5, loc="upper right", bbox_to_anchor=(1, 1.02), fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    footnote(fig, "Sources: Diageo Preliminary Results FY24, FY25 and FY26 (diageo.com). Values converted to USD bn for axis readability only (divided by 1,000 from official USD m). No other adjustments.")
    fig.tight_layout(rect=[0, 0.05, 1, 0.98])
    fig.savefig(CHARTS / "01_regional_net_sales.png", dpi=180)
    plt.close()


def chart_category_mix():
    rows = [c for c in CATEGORIES if c["fiscal_year"] == "FY26" and c["category"] != "Spirits" and c["reported_ns_by_category_pct"] is not None]
    rows = sorted(rows, key=lambda r: r["reported_ns_by_category_pct"], reverse=True)
    labels = [r["category"] for r in rows]
    share = [r["reported_ns_by_category_pct"] for r in rows]
    org = [r["organic_ns_mov_pct"] for r in rows]
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 6.4), dpi=180, gridspec_kw={"width_ratios": [1.05, 1]})
    y = range(len(labels))
    colors = [PINK if s >= 10 else CHARCOAL for s in share]
    axes[0].barh(list(y), share, color=colors, zorder=3)
    axes[0].set_yticks(list(y))
    axes[0].set_yticklabels(labels)
    axes[0].invert_yaxis()
    axes[0].set_xlabel("Share of reported net sales (%)")
    axes[0].set_xlim(0, 28)
    for i, s in enumerate(share):
        axes[0].text(s + 0.4, i, f"{s:.0f}%", va="center", fontsize=8, color=CHARCOAL)
    title(axes[0], "FY26 category mix", "Official share of reported net sales  •  shares do not sum to 100%")
    axes[0].spines["top"].set_visible(False)
    axes[0].spines["right"].set_visible(False)

    org_colors = [PINK if v >= 0 else CHARCOAL for v in org]
    axes[1].barh(list(y), org, color=org_colors, zorder=3)
    axes[1].set_yticks(list(y))
    axes[1].set_yticklabels([""] * len(labels))
    axes[1].invert_yaxis()
    axes[1].axvline(0, color=CHARCOAL, linewidth=0.8)
    axes[1].set_xlabel("Organic net sales movement (%)")
    axes[1].set_xlim(-55, 25)
    for i, v in enumerate(org):
        ha = "left" if v >= 0 else "right"
        axes[1].text(v + (0.8 if v >= 0 else -0.8), i, f"{v:+.0f}%", va="center", ha=ha, fontsize=8, color=CHARCOAL)
    title(axes[1], "FY26 organic net sales growth", "Official organic movement by category")
    axes[1].spines["top"].set_visible(False)
    axes[1].spines["right"].set_visible(False)
    footnote(fig, "Source: Diageo Preliminary Results FY26, Key categories table. Category dollar sales are not disclosed. Shares as published; they do not always sum to 100% because of rounding and undisclosed categories.")
    fig.tight_layout(rect=[0, 0.05, 1, 0.98])
    fig.savefig(CHARTS / "02_category_mix_and_growth_fy26.png", dpi=180)
    plt.close()


def chart_volume_pricemix():
    years = ["FY23", "FY24", "FY25", "FY26"]
    vol = [next(g for g in GROUP_KPIS if g["fiscal_year"] == y)["organic_volume_movement_pct"] for y in years]
    px = [next(g for g in GROUP_KPIS if g["fiscal_year"] == y)["organic_price_mix_pps"] for y in years]
    ons = [next(g for g in GROUP_KPIS if g["fiscal_year"] == y)["organic_ns_movement_pct"] for y in years]
    fig, ax = plt.subplots(figsize=(11.2, 6.2), dpi=180)
    x = list(range(len(years)))
    w = 0.36
    vol_pos = [v if v > 0 else 0 for v in vol]
    vol_neg = [v if v < 0 else 0 for v in vol]
    ax.bar(x, vol_pos, width=w, color=CHARCOAL, label="Organic volume %", zorder=3)
    ax.bar(x, vol_neg, width=w, color=CHARCOAL, zorder=3)
    px_pos = [v if v > 0 else 0 for v in px]
    px_neg = [v if v < 0 else 0 for v in px]
    ax.bar(x, px_pos, width=w, bottom=vol_pos, color=PINK, label="Organic price/mix (pps)", zorder=3)
    ax.bar(x, px_neg, width=w, bottom=vol_neg, color=PINK, zorder=3)
    ax.plot(x, ons, color=PINK_DARK, marker="o", linewidth=2, markersize=7, label="Organic net sales %", zorder=4)
    for i, v in enumerate(ons):
        ax.annotate(f"{v:+.1f}%", (i, v), textcoords="offset points", xytext=(14, 0), fontsize=8.5, color=PINK_DARK, fontweight="bold", va="center")
    ax.axhline(0, color=CHARCOAL, linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("Organic movement (%)")
    ax.set_ylim(-5, 10)
    title(ax, "Organic net sales: volume versus price/mix", "By Diageo’s definition, price/mix (pps) plus organic volume % equals organic net sales growth")
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    footnote(fig, "Sources: Annual Report 2023 (FY23 volume and price/mix); Preliminary Results FY24, FY25 and FY26. FY24 uses unrounded headline figures (volume -3.5%, price/mix +2.9pps), not the integer-rounded region table.")
    fig.tight_layout(rect=[0, 0.05, 1, 0.98])
    fig.savefig(CHARTS / "03_organic_volume_vs_price_mix.png", dpi=180)
    plt.close()


def chart_operating_margin():
    years = ["FY23", "FY24", "FY25", "FY26"]
    reported = [next(g for g in GROUP_KPIS if g["fiscal_year"] == y)["reported_op_margin_pct"] for y in years]
    adj = [next(g for g in GROUP_KPIS if g["fiscal_year"] == y)["op_margin_before_exceptionals_pct"] for y in years]
    fig, ax = plt.subplots(figsize=(11.2, 6.2), dpi=180)
    x = list(range(len(years)))
    ax.plot(x, reported, color=CHARCOAL, marker="o", linewidth=2.2, markersize=8, label="Reported operating margin", zorder=3)
    ax.plot(x, adj, color=PINK, marker="s", linewidth=2.2, markersize=8, label="Operating margin before exceptional items", zorder=3)
    for i, (r, a) in enumerate(zip(reported, adj)):
        ax.annotate(f"{r:.1f}%", (i, r), textcoords="offset points", xytext=(0, -14), ha="center", fontsize=8, color=CHARCOAL)
        ax.annotate(f"{a:.1f}%", (i, a), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8, color=PINK, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("Operating margin (%)")
    ax.set_ylim(12, 34)
    title(ax, "Operating margin trend", "FY25–FY26 headline figures are as printed; FY23–FY24 levels are calculated from official profit  divided by  official net sales")
    ax.legend(frameon=False, loc="center right", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    footnote(fig, "Sources: Preliminary Results FY24 (incl. restated FY23 USD comparatives), FY25 and FY26. Before-exceptionals margin is Diageo’s defined ratio (OP before exceptional items  divided by  net sales). Reported FY25 21.4% and FY26 16.1% are official headlines; FY23 27.0% and FY24 29.6% are calculated (consistent with the official +262bps FY24 movement).")
    fig.tight_layout(rect=[0, 0.06, 1, 0.98])
    fig.savefig(CHARTS / "04_operating_margin_trend.png", dpi=180)
    plt.close()


def chart_regional_organic():
    years = ["FY24", "FY25", "FY26"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America and Caribbean", "Africa"]
    data = {r: [] for r in regions}
    for y in years:
        for r in regions:
            row = next(x for x in REGIONAL if x["fiscal_year"] == y and x["region"] == r)
            data[r].append(row["organic_ns_mov_pct"])
    fig, ax = plt.subplots(figsize=(11.5, 6.2), dpi=180)
    x = range(len(years))
    n = len(regions)
    width = 0.15
    for i, r in enumerate(regions):
        offs = [xi + (i - (n - 1) / 2) * width for xi in x]
        label = "LAC" if r == "Latin America and Caribbean" else r
        bars = ax.bar(offs, data[r], width=width * 0.92, color=REGION_COLORS[r], label=label, zorder=3)
        for b, val in zip(bars, data[r]):
            va = "bottom" if val >= 0 else "top"
            ax.text(b.get_x() + b.get_width() / 2, val + (0.4 if val >= 0 else -0.4), f"{val:+.1f}", ha="center", va=va, fontsize=6.5, color=CHARCOAL)
    ax.axhline(0, color=CHARCOAL, linewidth=0.8)
    ax.set_xticks(list(x))
    ax.set_xticklabels(years)
    ax.set_ylabel("Organic net sales movement (%)")
    ax.set_ylim(-26, 18)
    title(ax, "Organic net sales growth by region", "Official organic movements  •  FY23 regional organic rates omitted (USD sources did not publish a complete set)")
    ax.legend(frameon=False, ncol=5, loc="upper left", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    footnote(fig, "Sources: Diageo Preliminary Results FY24, FY25 and FY26. FY24 NAM uses the more precise -2.5% from the excluding-LAC paragraph (table rounds to -3%). FY24 LAC uses the headline -21.1% (table rounds to -21%).")
    fig.tight_layout(rect=[0, 0.05, 1, 0.98])
    fig.savefig(CHARTS / "05_regional_organic_growth.png", dpi=180)
    plt.close()


def chart_brands():
    wanted = ["Don Julio", "Guinness", "Crown Royal", "Johnnie Walker", "Casamigos", "Smirnoff", "Captain Morgan", "Baileys"]
    fy25 = {b["brand"]: b["organic_ns_mov_pct"] for b in BRANDS if b["fiscal_year"] == "FY25"}
    fy26 = {b["brand"]: b["organic_ns_mov_pct"] for b in BRANDS if b["fiscal_year"] == "FY26"}
    labels = [b for b in wanted if b in fy25 and b in fy26]
    fig, ax = plt.subplots(figsize=(11.5, 6.3), dpi=180)
    y = list(range(len(labels)))
    h = 0.36
    v25 = [fy25[b] for b in labels]
    v26 = [fy26[b] for b in labels]
    ax.barh([yi + h / 2 for yi in y], v25, height=h, color=PINK, label="FY25 organic NS %", zorder=3)
    ax.barh([yi - h / 2 for yi in y], v26, height=h, color=CHARCOAL, label="FY26 organic NS %", zorder=3)
    ax.axvline(0, color=CHARCOAL, linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Organic net sales movement (%)")
    ax.set_xlim(-32, 50)
    for yi, a, b in zip(y, v25, v26):
        ax.text(a + (0.7 if a >= 0 else -0.7), yi + h / 2, f"{a:+.0f}%", va="center", ha="left" if a >= 0 else "right", fontsize=7, color=PINK)
        ax.text(b + (0.7 if b >= 0 else -0.7), yi - h / 2, f"{b:+.0f}%", va="center", ha="left" if b >= 0 else "right", fontsize=7, color=CHARCOAL)
    title(ax, "Key brand organic net sales: FY25 versus FY26", "Official group brand table  •  brand dollar sales are not disclosed")
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    footnote(fig, "Sources: Diageo Preliminary Results FY25 and FY26, Key brands tables. Crown Royal FY26 group organic NS is -15%; the NAM narrative states Crown Royal whisky net sales declined 15.9%. Don Julio FY25 group organic NS is +38%; the US Spirits narrative states Don Julio net sales grew 41.9%.")
    fig.tight_layout(rect=[0, 0.05, 1, 0.98])
    fig.savefig(CHARTS / "06_brand_organic_growth_fy25_fy26.png", dpi=180)
    plt.close()


def chart_canada_nam():
    years = ["FY24", "FY25", "FY26"]
    markets = ["Canada", "US Spirits", "DBC USA", "North America"]
    colors = {"Canada": PINK, "US Spirits": CHARCOAL, "DBC USA": MID_GREY, "North America": SOFT_GREY}
    fig, ax = plt.subplots(figsize=(11.2, 6.2), dpi=180)
    x = list(range(len(years)))
    n = len(markets)
    width = 0.18
    for i, m in enumerate(markets):
        vals = []
        for y in years:
            row = next(r for r in NAM_CANADA if r["fiscal_year"] == y and r["market"] == m)
            vals.append(row["organic_ns_mov_pct"])
        offs = [xi + (i - (n - 1) / 2) * width for xi in x]
        bars = ax.bar(offs, vals, width=width * 0.9, color=colors[m], label=m, zorder=3)
        for b, val in zip(bars, vals):
            va = "bottom" if val >= 0 else "top"
            ax.text(b.get_x() + b.get_width() / 2, val + (0.25 if val >= 0 else -0.25), f"{val:+.1f}", ha="center", va=va, fontsize=7, color=CHARCOAL)
    ax.axhline(0, color=CHARCOAL, linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("Organic net sales movement (%)")
    ax.set_ylim(-16, 14)
    title(ax, "North America markets, including Canada", "Official organic net sales  •  Canada dollar sales are not disclosed  •  FY26 Canada +7.7% includes a one-off")
    ax.legend(frameon=False, ncol=4, loc="upper right", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    footnote(fig, "Sources: Diageo Preliminary Results FY24, FY25 and FY26, North America markets tables. FY26 Canada +7.7% is supported by Guinness and Ketel One and a one-off item relating to a favourable resolution of commercial terms with a customer.")
    fig.tight_layout(rect=[0, 0.05, 1, 0.98])
    fig.savefig(CHARTS / "07_canada_and_nam_markets.png", dpi=180)
    plt.close()


def export_charts():
    CHARTS.mkdir(parents=True, exist_ok=True)
    setup()
    chart_regional_ns()
    chart_category_mix()
    chart_volume_pricemix()
    chart_operating_margin()
    chart_regional_organic()
    chart_brands()
    chart_canada_nam()


if __name__ == "__main__":
    export_charts()
    print("charts:", sorted(p.name for p in CHARTS.glob("*.png")))
