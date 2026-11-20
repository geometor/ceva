"""Extract contrast-normalized archival bitmaps from Ceva (1678) 300-DPI scans.

Crops all 10 folding copperplate plates (Tabulae I-X), all 85 individual
geometric figures (figs. 1-85), and the 6 frontispiece/woodcut ornaments
directly into their corresponding Book Codex leaf directories.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps

REPO_ROOT = Path(__file__).resolve().parents[1]
FOLIOS_DIR = REPO_ROOT / "resources" / "de_lineis_rectis" / "folios"
CODEX_DIR = REPO_ROOT / "docsrc" / "de_lineis_rectis"

# (folio_id, target_rel_path, crop_box (left, top, right, bottom))
CROPS: tuple[tuple[str, str, tuple[int, int, int, int]], ...] = (
    # Frontmatter & Colophon woodcuts / title page
    ("0010", "statica_prolegomena/frontispiece/0010.g1.png", (420, 440, 1615, 2245)),
    ("0010", "statica_prolegomena/frontispiece/0010.g2.png", (875, 1740, 1135, 1985)),
    ("0012", "statica_prolegomena/dedicatio/0012.g1.png", (430, 540, 1650, 910)),
    ("0015", "statica_prolegomena/prooemium/0015.g1.png", (865, 520, 2005, 815)),
    ("0077", "liber_secundus/prop_21/0077.g1.png", (1320, 1595, 1785, 1780)),
    ("0101", "appendix_geometrica/colophon/0101.g1.png", (1020, 1080, 1995, 1780)),
    # Full folding copperplate plates (Tabulae I-X) -> appendix_geometrica/tabulae/
    ("0103", "appendix_geometrica/tabulae/0103.g0.png", (1280, 240, 2240, 1545)),
    ("0105", "appendix_geometrica/tabulae/0105.g0.png", (1295, 250, 2265, 1560)),
    ("0107", "appendix_geometrica/tabulae/0107.g0.png", (1305, 260, 2285, 1580)),
    ("0109", "appendix_geometrica/tabulae/0109.g0.png", (1295, 240, 2270, 1565)),
    ("0111", "appendix_geometrica/tabulae/0111.g0.png", (1285, 235, 2260, 1535)),
    ("0113", "appendix_geometrica/tabulae/0113.g0.png", (1285, 265, 2275, 1625)),
    ("0115", "appendix_geometrica/tabulae/0115.g0.png", (1295, 230, 2295, 1585)),
    ("0117", "appendix_geometrica/tabulae/0117.g0.png", (1305, 240, 2295, 1585)),
    ("0119", "appendix_geometrica/tabulae/0119.g0.png", (1320, 180, 2305, 1545)),
    ("0121", "appendix_geometrica/tabulae/0121.g0.png", (1300, 230, 2295, 1595)),
    # Tabula I (0103) — Figs. 1-12 -> Liber Primus
    ("0103", "liber_primus/axiomata_lemmata/0103.g1.png", (1340, 325, 1610, 595)),
    ("0103", "liber_primus/axiomata_lemmata/0103.g2.png", (1625, 325, 1900, 595)),
    ("0103", "liber_primus/axiomata_lemmata/0103.g3.png", (1910, 300, 2210, 535)),
    ("0103", "liber_primus/prop_01/0103.g4.png", (1315, 585, 1605, 885)),
    ("0103", "liber_primus/prop_02/0103.g5.png", (1600, 590, 1900, 885)),
    ("0103", "liber_primus/prop_03/0103.g6.png", (1900, 585, 2195, 885)),
    ("0103", "liber_primus/prop_04/0103.g7.png", (1315, 870, 1615, 1180)),
    ("0103", "liber_primus/prop_05/0103.g8.png", (1615, 875, 1905, 1180)),
    ("0103", "liber_primus/prop_06/0103.g9.png", (1910, 875, 2210, 1080)),
    ("0103", "liber_primus/prop_06/0103.g10.png", (1315, 1175, 1615, 1480)),
    ("0103", "liber_primus/prop_07/0103.g11.png", (1610, 1175, 1890, 1475)),
    ("0103", "liber_primus/prop_07/0103.g12.png", (1895, 1175, 2190, 1475)),
    # Tabula II (0105) — Figs. 13-24 -> Liber Primus
    ("0105", "liber_primus/prop_10/0105.g13.png", (1330, 290, 1650, 610)),
    ("0105", "liber_primus/prop_10/0105.g14.png", (1655, 300, 1915, 625)),
    ("0105", "liber_primus/prop_12/0105.g15.png", (1925, 295, 2215, 615)),
    ("0105", "liber_primus/prop_13/0105.g16.png", (1330, 600, 1645, 905)),
    ("0105", "liber_primus/prop_15/0105.g17.png", (1625, 610, 1935, 900)),
    ("0105", "liber_primus/prop_17/0105.g18.png", (1910, 625, 2245, 910)),
    ("0105", "liber_primus/prop_17/0105.g19.png", (1325, 890, 1630, 1200)),
    ("0105", "liber_primus/prop_18/0105.g20.png", (1620, 905, 1925, 1200)),
    ("0105", "liber_primus/prop_19/0105.g21.png", (1920, 900, 2230, 1200)),
    ("0105", "liber_primus/prop_20/0105.g22.png", (1325, 1195, 1645, 1495)),
    ("0105", "liber_primus/prop_20/0105.g23.png", (1635, 1185, 1955, 1480)),
    ("0105", "liber_primus/prop_21/0105.g24.png", (1940, 1200, 2235, 1525)),
    # Tabula III (0107) — Figs. 25-31 -> Liber Primus
    ("0107", "liber_primus/prop_22/0107.g25.png", (1330, 295, 1615, 630)),
    ("0107", "liber_primus/prop_22/0107.g26.png", (1620, 285, 1920, 630)),
    ("0107", "liber_primus/prop_22/0107.g27.png", (1915, 295, 2205, 635)),
    ("0107", "liber_primus/prop_23/0107.g28.png", (1330, 625, 1795, 1095)),
    ("0107", "liber_primus/prop_24/0107.g29.png", (1790, 620, 2255, 1085)),
    ("0107", "liber_primus/prop_25/0107.g30.png", (1345, 1085, 1815, 1545)),
    ("0107", "liber_primus/prop_26/0107.g31.png", (1790, 1085, 2235, 1550)),
    # Tabula IIII (0109) — Figs. 32-38 -> Liber Secundus
    ("0109", "liber_secundus/lemmata_conica/0109.g32.png", (1315, 265, 1615, 610)),
    ("0109", "liber_secundus/lemmata_conica/0109.g33.png", (1590, 265, 1925, 615)),
    ("0109", "liber_secundus/lemmata_conica/0109.g34.png", (1915, 265, 2225, 600)),
    ("0109", "liber_secundus/lemmata_conica/0109.g35.png", (1315, 595, 1775, 1045)),
    ("0109", "liber_secundus/lemmata_conica/0109.g36.png", (1775, 600, 2250, 1075)),
    ("0109", "liber_secundus/lemmata_conica/0109.g37.png", (1335, 1065, 1790, 1465)),
    ("0109", "liber_secundus/prop_01/0109.g38.png", (1765, 1065, 2265, 1520)),
    # Tabula V (0111) — Figs. 39-46 -> Liber Secundus
    ("0111", "liber_secundus/prop_03/0111.g39.png", (1325, 255, 1635, 585)),
    ("0111", "liber_secundus/prop_04/0111.g40.png", (1620, 255, 1915, 590)),
    ("0111", "liber_secundus/prop_05/0111.g41.png", (1905, 260, 2245, 595)),
    ("0111", "liber_secundus/prop_06/0111.g42.png", (1315, 575, 1920, 880)),
    ("0111", "liber_secundus/prop_07/0111.g43.png", (1900, 585, 2235, 895)),
    ("0111", "liber_secundus/prop_09/0111.g44.png", (1320, 935, 1910, 1445)),
    ("0111", "liber_secundus/prop_07/0111.g45.png", (1880, 900, 2175, 1215)),
    ("0111", "liber_secundus/prop_08/0111.g46.png", (1880, 1200, 2215, 1510)),
    # Tabula VI (0113) — Figs. 47-54 -> Liber Secundus
    ("0113", "liber_secundus/prop_09/0113.g47.png", (1325, 285, 1625, 825)),
    ("0113", "liber_secundus/prop_09/0113.g48.png", (1615, 290, 1915, 825)),
    ("0113", "liber_secundus/prop_09/0113.g49.png", (1905, 285, 2260, 835)),
    ("0113", "liber_secundus/prop_10/0113.g50.png", (1335, 810, 1640, 1165)),
    ("0113", "liber_secundus/prop_13/0113.g51.png", (1645, 805, 1935, 1085)),
    ("0113", "liber_secundus/prop_13/0113.g52.png", (1895, 835, 2240, 1580)),
    ("0113", "liber_secundus/prop_14/0113.g53.png", (1325, 1140, 1615, 1565)),
    ("0113", "liber_secundus/prop_14/0113.g54.png", (1600, 1020, 1915, 1595)),
    # Tabula VII (0115) — Figs. 55-61 -> Liber Secundus
    ("0115", "liber_secundus/prop_14/0115.g55.png", (1325, 255, 1650, 615)),
    ("0115", "liber_secundus/prop_14/0115.g56.png", (1645, 250, 1930, 610)),
    ("0115", "liber_secundus/prop_16/0115.g57.png", (1930, 255, 2255, 620)),
    ("0115", "liber_secundus/prop_16/0115.g58.png", (1330, 595, 1930, 900)),
    ("0115", "liber_secundus/prop_18/0115.g59.png", (1915, 665, 2245, 1230)),
    ("0115", "liber_secundus/prop_16/0115.g60.png", (1335, 910, 1875, 1205)),
    ("0115", "liber_secundus/prop_16/0115.g61.png", (1335, 1200, 2135, 1545)),
    # Tabula VIII (0117) — Figs. 62-67 -> Liber Secundus; Figs. 68-73 -> Appendix
    ("0117", "liber_secundus/prop_17/0117.g62.png", (1330, 270, 1660, 615)),
    ("0117", "liber_secundus/prop_19/0117.g63.png", (1615, 260, 1945, 615)),
    ("0117", "liber_secundus/prop_19/0117.g64.png", (1935, 260, 2280, 610)),
    ("0117", "liber_secundus/prop_19/0117.g65.png", (1345, 600, 1660, 915)),
    ("0117", "liber_secundus/prop_19/0117.g66.png", (1640, 600, 1955, 930)),
    ("0117", "liber_secundus/prop_20/0117.g67.png", (1935, 600, 2275, 935)),
    ("0117", "appendix_geometrica/prop_01/0117.g68.png", (1345, 920, 1665, 1185)),
    ("0117", "appendix_geometrica/prop_02/0117.g69.png", (1655, 915, 1940, 1205)),
    ("0117", "appendix_geometrica/prop_02/0117.g70.png", (1955, 905, 2235, 1205)),
    ("0117", "appendix_geometrica/prop_04/0117.g71.png", (1345, 1200, 1660, 1535)),
    ("0117", "appendix_geometrica/prop_05/0117.g72.png", (1625, 1190, 1970, 1445)),
    ("0117", "appendix_geometrica/prop_06/0117.g73.png", (1955, 1205, 2255, 1535)),
    # Tabula IX (0119) — Figs. 74-77 -> Appendix
    ("0119", "appendix_geometrica/prop_07/0119.g74.png", (1355, 195, 1835, 835)),
    ("0119", "appendix_geometrica/prop_08/0119.g75.png", (1850, 195, 2215, 815)),
    ("0119", "appendix_geometrica/prop_09/0119.g76.png", (1350, 825, 1825, 1515)),
    ("0119", "appendix_geometrica/prop_10/0119.g77.png", (1815, 845, 2255, 1445)),
    # Tabula X (0121) — Figs. 78-84 -> Appendix; Fig. 85 -> Liber Secundus Prop. XXI
    ("0121", "appendix_geometrica/prop_11/0121.g78.png", (1345, 250, 1665, 600)),
    ("0121", "appendix_geometrica/prop_12/0121.g79.png", (1655, 255, 1945, 600)),
    ("0121", "appendix_geometrica/prop_13/0121.g80.png", (1920, 255, 2250, 600)),
    ("0121", "appendix_geometrica/prop_14/0121.g81.png", (1340, 585, 1835, 885)),
    ("0121", "appendix_geometrica/prop_15/0121.g82.png", (1790, 585, 2260, 945)),
    ("0121", "appendix_geometrica/prop_16/0121.g83.png", (1365, 920, 2235, 1200)),
    ("0121", "appendix_geometrica/scholium_indivisibilia/0121.g84.png", (1560, 1195, 2005, 1545)),
    ("0121", "liber_secundus/prop_21/0121.g85.png", (1980, 1185, 2275, 1555)),
)


def normalize_plate(crop: Image.Image) -> Image.Image:
    """Apply gentle parchment-preserving autocontrast for crisp engraving legibility."""
    gray = crop.convert("L")
    enhanced = ImageOps.autocontrast(gray, cutoff=(0.5, 2.0))
    return enhanced.convert("RGB")


def main() -> None:
    """Run deterministic extraction of all 101 archival bitmaps from 1678 scans."""
    cache: dict[str, Image.Image] = {}
    for folio_id, rel_out, box in CROPS:
        if folio_id not in cache:
            cache[folio_id] = Image.open(FOLIOS_DIR / f"{folio_id}.png").convert("RGB")
        src = cache[folio_id]
        cropped = normalize_plate(src.crop(box))
        out_path = CODEX_DIR / rel_out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        cropped.save(out_path, format="PNG", optimize=True)
    print(f"Extracted {len(CROPS)} archival bitmaps across {len(cache)} 1678 folios.")


if __name__ == "__main__":
    main()
