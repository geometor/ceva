#!/usr/bin/env python3
"""Generate Phase B calibrated 5-layer .euclid-graphic SVGs for Ceva (1678) plates.

Covers all 63 remaining geometric plates across Liber Primus (22),
Liber Secundus (30), and Appendix Geometrica (11), bringing total
paired codex SVGs from 22 to 85 (100% of geometric plates).
"""

from __future__ import annotations

import math

from build_codex_svgs import CalibratedSVG, Point2F, intersect_lines, lerp, write_svg


def _pts(s: CalibratedSVG, items: list[tuple[Point2F, str, str, float, float]]) -> None:
    """Batch-add standard points with labels."""
    for pos, ref, lbl, dx, dy in items:
        s.pt(pos, ref, lbl, dx=dx, dy=dy, r=3.5)


def build_liber_primus(count: int = 0) -> int:
    """Generate the 22 remaining Liber Primus SVGs."""
    # g2: Tab. I Fig. 2 (Lemma I: Perpendicular/Oblique Balance)
    s = CalibratedSVG(360, 300, "Ceva 1678 Tabula I Fig. 2: Lemma I")
    B, C = (75.0, 250.0), (290.0, 185.0)
    H = lerp(B, C, 0.62)
    E_top = (145.0, 65.0)
    E_mid = lerp(E_top, H, 0.65)
    s.seg(B, C, "BC", width=2.2)
    s.seg(E_top, H, "EH", stroke="var(--geom-highlight, #d97706)", width=2.1)
    _pts(
        s,
        [
            (B, "B", "B", -16, 10),
            (C, "C", "C", 16, 4),
            (H, "H", "H", 12, 16),
            (E_top, "E", "E", -16, 4),
            (E_mid, "E", "E", 14, -4),
        ],
    )
    s.text((92, 72), "A", "A")
    s.text((240, 82), "D", "D")
    write_svg("liber_primus/axiomata_lemmata/0103.g2.svg", s)
    count += 1

    # g3: Tab. I Fig. 3 (Axioma / Lemma II: Lever Segments)
    s = CalibratedSVG(380, 160, "Ceva 1678 Tabula I Fig. 3: Lever Segments A-F-K-B")
    A, B = (65.0, 95.0), (315.0, 95.0)
    F = lerp(A, B, 0.44)
    K = lerp(A, B, 0.72)
    s.seg(A, B, "AB", width=2.4)
    _pts(s, [(A, "A", "A", -14, 5), (B, "B", "B", 14, 5), (K, "K", "K", 0, -14)])
    s.pt(F, "F", "F", dx=0, dy=-14, highlight=True)
    write_svg("liber_primus/axiomata_lemmata/0103.g3.svg", s)
    count += 1

    # g9: Tab. I Fig. 9 (Prop. VI: Collinear Lever A-B-C)
    s = CalibratedSVG(380, 160, "Ceva 1678 Tabula I Fig. 9: Prop. VI Collinear Balance")
    A, C = (60.0, 95.0), (320.0, 95.0)
    B = lerp(A, C, 0.40)
    s.seg(A, C, "AC", width=2.4)
    _pts(s, [(A, "A", "A", 0, -14), (C, "C", "C", 0, -14)])
    s.pt(B, "B", "B", dx=0, dy=-14, highlight=True)
    write_svg("liber_primus/prop_06/0103.g9.svg", s)
    count += 1

    # g11: Tab. I Fig. 11 (Prop. VII: Menelaus Sector AEC)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula I Fig. 11: Prop. VII")
    A, E, C = (185.0, 42.0), (65.0, 295.0), (295.0, 295.0)
    D = lerp(A, E, 0.56)
    B = lerp(A, C, 0.62)
    F = intersect_lines(E, B, C, D)
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, D, "CD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(
        s,
        [
            (A, "A", "A", 0, -14),
            (E, "E", "E", -16, 4),
            (C, "C", "C", 16, 4),
            (D, "D", "D", -16, -4),
            (B, "B", "B", 16, -4),
        ],
    )
    s.pt(F, "F", "F", dx=0, dy=20, highlight=True)
    write_svg("liber_primus/prop_07/0103.g11.svg", s)
    count += 1

    # g12: Tab. I Fig. 12 (Prop. VII with Chord DB)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula I Fig. 12: Prop. VII Chord DB")
    A, E, C = (165.0, 40.0), (65.0, 295.0), (285.0, 295.0)
    D = lerp(A, E, 0.42)
    B = lerp(A, C, 0.34)
    F = intersect_lines(E, B, C, D)
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, D, "CD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(D, B, "DB", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    _pts(
        s,
        [
            (A, "A", "A", 0, -14),
            (E, "E", "E", -16, 8),
            (C, "C", "C", 16, 4),
            (D, "D", "D", -16, -2),
            (B, "B", "B", 14, -8),
        ],
    )
    s.pt(F, "F", "F", dx=2, dy=20, highlight=True)
    write_svg("liber_primus/prop_07/0103.g12.svg", s)
    count += 1

    # g13: Tab. II Fig. 13 (Prop. X: Harmonic Pencil / Butterfly)
    s = CalibratedSVG(420, 380, "Ceva 1678 Tabula II Fig. 13: Prop. X")
    A = (210.0, 48.0)
    C = (210.0, 330.0)
    B = (105.0, 330.0)
    D = (315.0, 330.0)
    L = (75.0, 48.0)
    K = (345.0, 48.0)
    F = lerp(L, A, 0.55)
    E = lerp(A, K, 0.55)
    G = intersect_lines(A, C, L, D)
    I_pt = intersect_lines(A, B, L, D)
    H = intersect_lines(A, D, K, B)
    s.seg(L, K, "LK", width=2.1)
    s.seg(B, D, "BD", width=2.2)
    s.seg(A, C, "AC", width=2.0)
    s.seg(A, B, "AB", width=2.0)
    s.seg(A, D, "AD", width=2.0)
    s.seg(F, C, "FC", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(E, C, "EC", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(L, D, "LD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(K, B, "KB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(
        s,
        [
            (L, "L", "L", -12, -12),
            (F, "F", "F", 0, -14),
            (A, "A", "A", 0, -14),
            (E, "E", "E", 0, -14),
            (K, "K", "K", 12, -12),
            (B, "B", "B", -16, 4),
            (C, "C", "C", -14, 14),
            (D, "D", "D", 16, 4),
            (I_pt, "I", "I", -16, 4),
            (H, "H", "H", 16, 4),
        ],
    )
    s.pt(G, "G", "G", dx=-14, dy=4, highlight=True)
    write_svg("liber_primus/prop_10/0105.g13.svg", s)
    count += 1

    # g14: Tab. II Fig. 14 (Prop. X Variant)
    s = CalibratedSVG(360, 400, "Ceva 1678 Tabula II Fig. 14: Prop. X Variant")
    A = (180.0, 52.0)
    B = (120.0, 52.0)
    C = (240.0, 52.0)
    H = (85.0, 355.0)
    E = (275.0, 355.0)
    F = (180.0, 355.0)
    K = intersect_lines(A, H, B, F)
    D = intersect_lines(A, E, C, F)
    I_pt = intersect_lines(A, F, K, E)
    G = lerp(H, F, 0.35)
    s.seg(B, C, "BC", width=2.0)
    s.seg(H, E, "HE", width=2.2)
    s.seg(A, H, "AH", width=2.1)
    s.seg(A, E, "AE", width=2.1)
    s.seg(A, F, "AF", width=2.0)
    s.seg(B, F, "BF", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(C, F, "CF", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(K, E, "KE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(H, D, "HD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, G, "AG", dash="4 3", width=1.7)
    _pts(
        s,
        [
            (B, "B", "B", -14, -10),
            (A, "A", "A", 0, -14),
            (C, "C", "C", 14, -10),
            (H, "H", "H", -16, 4),
            (F, "F", "F", 0, 20),
            (E, "E", "E", 16, 4),
            (K, "K", "K", -16, -2),
            (D, "D", "D", 16, -2),
            (G, "G", "G", 14, -10),
        ],
    )
    s.pt(I_pt, "I", "I", dx=-14, dy=-4, highlight=True)
    write_svg("liber_primus/prop_10/0105.g14.svg", s)
    count += 1

    # g15: Tab. II Fig. 15 (Prop. XII)
    s = CalibratedSVG(360, 360, "Ceva 1678 Tabula II Fig. 15: Prop. XII")
    E, A, C = (185.0, 42.0), (70.0, 315.0), (295.0, 315.0)
    B = lerp(A, C, 0.42)
    F = lerp(E, A, 0.62)
    D = lerp(E, C, 0.52)
    I_pt = lerp(E, C, 0.78)
    G = intersect_lines(E, B, F, D)
    H = intersect_lines(E, B, A, I_pt)
    s.poly([E, A, C], "EAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(E, A, "EA", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(F, D, "FD", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(A, I_pt, "AI", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    _pts(
        s,
        [
            (E, "E", "E", 0, -14),
            (A, "A", "A", -16, 4),
            (B, "B", "B", 0, 20),
            (C, "C", "C", 16, 4),
            (F, "F", "F", -16, -4),
            (D, "D", "D", 16, -6),
            (I_pt, "I", "I", 16, -4),
            (G, "G", "G", -14, -10),
            (H, "H", "H", 14, -8),
        ],
    )
    write_svg("liber_primus/prop_12/0105.g15.svg", s)
    count += 1

    # g16: Tab. II Fig. 16 (Prop. XIII)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 16: Prop. XIII")
    E, A, C = (180.0, 44.0), (62.0, 295.0), (300.0, 295.0)
    B = lerp(A, C, 0.52)
    F = lerp(E, A, 0.48)
    D = lerp(E, C, 0.48)
    G = intersect_lines(E, B, F, D)
    P_ceva = intersect_lines(E, B, F, C)
    s.poly([E, A, C], "EAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(E, A, "EA", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(F, C, "FC", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, D, "AD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(F, D, "FD", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    _pts(
        s,
        [
            (E, "E", "E", 0, -14),
            (A, "A", "A", -16, 4),
            (B, "B", "B", 0, 20),
            (C, "C", "C", 16, 4),
            (F, "F", "F", -16, -4),
            (D, "D", "D", 16, -4),
            (G, "G", "G", 12, -10),
        ],
    )
    s.pt(P_ceva, "P", None, highlight=True)
    write_svg("liber_primus/prop_13/0105.g16.svg", s)
    count += 1

    # g17: Tab. II Fig. 17 (Prop. XV)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 17: Prop. XV")
    E, A, C = (165.0, 40.0), (60.0, 295.0), (305.0, 295.0)
    B = lerp(A, C, 0.54)
    F = lerp(E, A, 0.66)
    D = lerp(E, C, 0.48)
    G = intersect_lines(E, B, F, D)
    s.poly([E, A, C], "EAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(E, A, "EA", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(F, D, "FD", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(F, B, "FB", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(A, G, "AG", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(
        s,
        [
            (E, "E", "E", -14, -4),
            (A, "A", "A", -16, 4),
            (B, "B", "B", 14, -12),
            (C, "C", "C", 16, 4),
            (F, "F", "F", -16, -6),
            (D, "D", "D", 16, -6),
        ],
    )
    s.pt(G, "G", "G", dx=-12, dy=-12, highlight=True)
    write_svg("liber_primus/prop_15/0105.g17.svg", s)
    count += 1

    # g18: Tab. II Fig. 18 (Prop. XVII: Exterior Pencil)
    s = CalibratedSVG(380, 320, "Ceva 1678 Tabula II Fig. 18: Prop. XVII")
    A, H = (58.0, 48.0), (330.0, 128.0)
    F = (78.0, 275.0)
    B = lerp(A, H, 0.30)
    C = lerp(A, H, 0.46)
    P = intersect_lines(A, (165.0, 222.0), F, C)
    F_prime = intersect_lines(A, P, F, H)
    G = intersect_lines(B, P, F, H)
    s.seg(A, H, "AH", width=2.2)
    s.seg(F, H, "FH", width=2.2)
    s.seg(A, F_prime, "AF'", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, F, "CF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(
        s,
        [
            (A, "A", "A", -14, 4),
            (B, "B", "B", 12, 14),
            (C, "C", "C", 14, 14),
            (H, "H", "H", 0, 18),
            (F, "F", "F", -14, 6),
            (G, "G", "G", 0, 20),
            (F_prime, "F'", "F", 8, 18),
        ],
    )
    s.pt(P, "P", None, highlight=True)
    write_svg("liber_primus/prop_17/0105.g18.svg", s)
    count += 1

    # g19: Tab. II Fig. 19 (Prop. XVII Bowtie Equilibrium)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 19: Prop. XVII Bowtie")
    A, C = (105.0, 48.0), (285.0, 48.0)
    E, F = (80.0, 290.0), (310.0, 290.0)
    B = lerp(A, C, 0.48)
    D = intersect_lines(A, F, C, E)
    G = intersect_lines(B, D, E, F)
    H = lerp(A, D, 0.42)
    I_pt = lerp(A, D, 0.72)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, F, "EF", width=2.2)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(C, E, "CE", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(B, G, "BG", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    _pts(
        s,
        [
            (A, "A", "A (1)", -14, -12),
            (B, "B", "B", 0, -14),
            (C, "C", "C (5)", 14, -12),
            (E, "E", "E (4)", -18, 6),
            (G, "G", "G", 0, 20),
            (F, "F", "F (3)", 18, 6),
            (H, "H", "H", 12, -4),
            (I_pt, "I", "I", 12, -4),
        ],
    )
    s.pt(D, "D", "D", dx=14, dy=4, highlight=True)
    write_svg("liber_primus/prop_17/0105.g19.svg", s)
    count += 1

    # g20: Tab. II Fig. 20 (Prop. XVIII: Quadrilateral Diagonals)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 20: Prop. XVIII")
    A, C = (85.0, 48.0), (295.0, 48.0)
    E, F = (95.0, 295.0), (288.0, 295.0)
    B = lerp(A, C, 0.48)
    D = intersect_lines(A, F, C, E)
    G = intersect_lines(B, D, E, F)
    s.poly([A, C, F, E], "ACFE", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, C, "AC", width=2.2)
    s.seg(C, F, "CF", width=2.2)
    s.seg(F, E, "FE", width=2.2)
    s.seg(E, A, "EA", width=2.2)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, E, "CE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    _pts(
        s,
        [
            (A, "A", "A", -16, 0),
            (B, "B", "B", 14, 14),
            (C, "C", "C", 16, 0),
            (E, "E", "E", 0, 20),
            (G, "G", "G", 0, 20),
            (F, "F", "F", 0, 20),
        ],
    )
    s.pt(D, "D", "D", dx=16, dy=0, highlight=True)
    write_svg("liber_primus/prop_18/0105.g20.svg", s)
    count += 1

    # g21: Tab. II Fig. 21 (Prop. XIX: Crossed Bowtie with BE, CG)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 21: Prop. XIX")
    A, C = (75.0, 48.0), (305.0, 48.0)
    E, F = (75.0, 295.0), (305.0, 295.0)
    B = lerp(A, C, 0.50)
    G = lerp(E, F, 0.50)
    D = intersect_lines(A, F, C, E)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, F, "EF", width=2.2)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, E, "CE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(B, E, "BE", width=2.0)
    s.seg(C, G, "CG", width=2.0)
    _pts(
        s,
        [
            (A, "A", "A", 0, -14),
            (B, "B", "B", 0, -14),
            (C, "C", "C", 0, -14),
            (E, "E", "E", 0, 20),
            (G, "G", "G", 0, 20),
            (F, "F", "F", 0, 20),
        ],
    )
    s.pt(D, "D", "D", dx=16, dy=0, highlight=True)
    write_svg("liber_primus/prop_19/0105.g21.svg", s)
    count += 1

    # g22: Tab. II Fig. 22 (Prop. XX: Quadrilateral Bimedians)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 22: Prop. XX")
    G, E = (75.0, 56.0), (305.0, 56.0)
    A, C = (75.0, 285.0), (305.0, 245.0)
    F = lerp(G, E, 0.48)
    B = lerp(A, C, 0.68)
    H = lerp(G, A, 0.38)
    D = lerp(E, C, 0.48)
    I_pt = intersect_lines(F, B, H, D)
    s.poly([G, E, C, A], "GECA", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(G, E, "GE", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(C, A, "CA", width=2.2)
    s.seg(A, G, "AG", width=2.2)
    s.seg(F, B, "FB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(H, D, "HD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(
        s,
        [
            (G, "G", "G", 0, -14),
            (F, "F", "F", 0, -14),
            (E, "E", "E", 16, 0),
            (H, "H", "H", -18, 4),
            (D, "D", "D", 18, 4),
            (A, "A", "A", 0, 20),
            (B, "B", "B", 6, 20),
            (C, "C", "C", 16, 6),
        ],
    )
    s.pt(I_pt, "I", "I", dx=-12, dy=18, highlight=True)
    write_svg("liber_primus/prop_20/0105.g22.svg", s)
    count += 1

    # g23: Tab. II Fig. 23 (Prop. XX: Weighted Quadrants)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula II Fig. 23: Prop. XX Weighted Quadrants")
    G, E = (70.0, 56.0), (300.0, 56.0)
    A, C = (80.0, 275.0), (295.0, 285.0)
    F = lerp(G, E, 0.50)
    B = lerp(A, C, 0.34)
    H = lerp(G, A, 0.42)
    D = lerp(E, C, 0.42)
    I_pt = intersect_lines(F, B, H, D)
    s.poly([G, E, C, A], "GECA", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(G, E, "GE", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(C, A, "CA", width=2.2)
    s.seg(A, G, "AG", width=2.2)
    s.seg(F, B, "FB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(H, D, "HD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(
        s,
        [
            (G, "G", "G", 0, -14),
            (F, "F", "F", 0, -14),
            (E, "E", "E", 0, -14),
            (H, "H", "H", -18, 4),
            (D, "D", "D", 18, 4),
            (A, "A", "A", -14, 14),
            (B, "B", "B", 0, 20),
            (C, "C", "C", 0, 20),
        ],
    )
    s.pt(I_pt, "I", "I", dx=12, dy=16, highlight=True)
    s.text((120, 88), "R 1 2/5", "w_GE", size=12, italic=False)
    s.text((255, 88), "R 1", "w_EF", size=12, italic=False)
    s.text((98, 175), "19", "w_HA", size=12, italic=False)
    s.text((275, 175), "12", "w_DC", size=12, italic=False)
    s.text((120, 255), "A 1 3/7", "w_AB", size=12, italic=False)
    s.text((255, 255), "A 1", "w_BC", size=12, italic=False)
    write_svg("liber_primus/prop_20/0105.g23.svg", s)
    count += 1

    # g25: Tab. III Fig. 25 (Prop. XXII: Skew Quadrilateral Equilibrium I)
    s = CalibratedSVG(360, 380, "Ceva 1678 Tabula III Fig. 25: Prop. XXII")
    D, A = (75.0, 56.0), (70.0, 335.0)
    B, C = (220.0, 88.0), (305.0, 325.0)
    H = lerp(D, A, 0.50)
    F = lerp(B, C, 0.45)
    E = lerp(D, C, 0.20)
    G = lerp(B, A, 0.65)
    I_pt = intersect_lines(H, F, E, G)
    s.seg(D, A, "DA", width=2.2)
    s.seg(D, C, "DC", width=2.2)
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(H, F, "HF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(E, G, "EG", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.weight_badge((105, 52), "K", "K")
    s.weight_badge((100, 335), "L", "L")
    s.weight_badge((252, 82), "M", "M")
    s.weight_badge((272, 325), "N", "N")
    _pts(
        s,
        [
            (D, "D", "D", -16, 4),
            (A, "A", "A", -16, 4),
            (B, "B", "B", -16, -4),
            (C, "C", "C", 16, 4),
            (H, "H", "H", -16, 4),
            (F, "F", "F", 16, 4),
            (E, "E", "E", -16, 4),
            (G, "G", "G", -16, 4),
        ],
    )
    s.pt(I_pt, "I", "I", dx=-12, dy=-10, highlight=True)
    write_svg("liber_primus/prop_22/0107.g25.svg", s)
    count += 1

    # g26: Tab. III Fig. 26 (Prop. XXII: Skew Quadrilateral II)
    s = CalibratedSVG(360, 360, "Ceva 1678 Tabula III Fig. 26: Prop. XXII Case II")
    D, A, C = (165.0, 52.0), (55.0, 315.0), (315.0, 310.0)
    B = (165.0, 175.0)
    H = lerp(D, A, 0.56)
    E = lerp(D, C, 0.62)
    G = lerp(B, A, 0.48)
    F = lerp(B, C, 0.54)
    I_pt = intersect_lines(H, F, G, E)
    s.seg(D, A, "DA", width=2.2)
    s.seg(D, C, "DC", width=2.2)
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(H, F, "HF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(G, E, "GE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.weight_badge((195, 52), "K", "K")
    s.weight_badge((85, 315), "L", "L")
    s.weight_badge((198, 175), "M", "M")
    s.weight_badge((282, 310), "N", "N")
    _pts(
        s,
        [
            (D, "D", "D", -16, 4),
            (A, "A", "A", -14, 12),
            (C, "C", "C", 16, 4),
            (B, "B", "B", 0, -14),
            (H, "H", "H", -16, 0),
            (E, "E", "E", 16, 0),
            (G, "G", "G", 6, 16),
            (F, "F", "F", -6, 16),
        ],
    )
    s.pt(I_pt, "I", "I", dx=0, dy=18, highlight=True)
    write_svg("liber_primus/prop_22/0107.g26.svg", s)
    count += 1

    # g27: Tab. III Fig. 27 (Prop. XXII: Skew Quadrilateral III)
    s = CalibratedSVG(360, 380, "Ceva 1678 Tabula III Fig. 27: Prop. XXII Case III")
    A, B, C = (95.0, 42.0), (55.0, 335.0), (275.0, 275.0)
    H = lerp(A, B, 0.12)
    D = lerp(A, B, 0.42)
    G = lerp(A, B, 0.80)
    F = lerp(B, C, 0.58)
    E = lerp(D, C, 0.72)
    I_pt = intersect_lines(H, F, G, E)
    s.seg(A, B, "AB", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(D, C, "DC", width=2.2)
    s.seg(H, F, "HF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(G, E, "GE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.weight_badge((122, 42), "L", "L")
    s.weight_badge((115, 160), "K", "K")
    s.weight_badge((82, 345), "M", "M")
    s.weight_badge((290, 245), "N", "N")
    _pts(
        s,
        [
            (A, "A", "A", -14, 0),
            (H, "H", "H", -14, 4),
            (D, "D", "D", -16, 0),
            (G, "G", "G", 14, 14),
            (B, "B", "B", -16, 4),
            (F, "F", "F", 4, 18),
            (C, "C", "C", 0, 18),
            (E, "E", "E", -10, 16),
        ],
    )
    s.pt(I_pt, "I", "I", dx=12, dy=14, highlight=True)
    write_svg("liber_primus/prop_22/0107.g27.svg", s)
    count += 1

    # g29: Tab. III Fig. 29 (Prop. XXIV: Quadrilateral Sub-Centers & Equilibrium)
    s = CalibratedSVG(420, 420, "Ceva 1678 Tabula III Fig. 29: Prop. XXIV")
    B, C, D, A = (95.0, 82.0), (345.0, 78.0), (355.0, 338.0), (70.0, 365.0)
    E = (195.0, 195.0)
    P = intersect_lines(B, C, E, (215.0, 80.0))
    I_pt = intersect_lines(A, D, P, E)
    R = intersect_lines(A, B, E, (82.0, 245.0))
    M = intersect_lines(C, D, R, E)
    F = lerp(A, E, 0.38)
    G = lerp(D, E, 0.45)
    K = lerp(C, E, 0.42)
    O_pt = lerp(B, E, 0.44)
    H = intersect_lines(A, G, D, F)
    L = intersect_lines(C, G, D, K)
    N = intersect_lines(B, K, C, O_pt)
    Q = intersect_lines(A, O_pt, B, F)
    S = lerp(E, I_pt, 0.35)
    T = lerp(E, S, 0.65)
    s.poly([A, B, C, D], "ABCD", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(A, B, "AB", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(C, D, "CD", width=2.2)
    s.seg(D, A, "DA", width=2.2)
    for v, nm in [(A, "AE"), (B, "BE"), (C, "CE"), (D, "DE")]:
        s.seg(v, E, nm, width=1.8)
    s.seg(P, I_pt, "PI", stroke="var(--geom-secondary, #0284c7)", width=1.7)
    s.seg(R, M, "RM", stroke="var(--geom-secondary, #0284c7)", width=1.7)
    for p1, p2, nm in [
        (A, G, "AG"), (D, F, "DF"), (C, G, "CG"), (D, K, "DK"),
        (B, K, "BK"), (C, O_pt, "CO"), (A, O_pt, "AO"), (B, F, "BF"),
    ]:
        s.seg(p1, p2, nm, stroke="var(--geom-highlight, #d97706)", width=1.5)
    s.seg(E, (S[0] + 15, S[1]), "ES", dash="3 2", width=1.4)
    _pts(
        s,
        [
            (A, "A", "A", -16, 0),
            (B, "B", "B", -16, 0),
            (C, "C", "C", 16, 0),
            (D, "D", "D", 16, 0),
            (P, "P", "P", 0, -14),
            (I_pt, "I", "I", 0, 18),
            (R, "R", "R", -16, 6),
            (M, "M", "M", 16, 6),
            (F, "F", "F", 0, 18),
            (G, "G", "G", 14, 0),
            (K, "K", "K", 14, 8),
            (O_pt, "O", "O", -14, 0),
            (H, "H", "H", 0, -12),
            (L, "L", "L", 14, 0),
            (N, "N", "N", 0, 16),
            (Q, "Q", "Q", 14, 4),
            (T, "T", "T", -10, 4),
            (S, "S", "S", 0, 16),
        ],
    )
    s.pt(E, "E", "E", dx=-16, dy=-2, highlight=True)
    write_svg("liber_primus/prop_24/0107.g29.svg", s)
    count += 1

    # g30: Tab. III Fig. 30 (Prop. XXV: Pyramid/Triangle Weight Concurrency)
    s = CalibratedSVG(380, 380, "Ceva 1678 Tabula III Fig. 30: Prop. XXV")
    E, A, C = (205.0, 42.0), (60.0, 335.0), (345.0, 295.0)
    B = lerp(A, C, 0.65)
    F = lerp(E, A, 0.28)
    D = lerp(E, C, 0.24)
    M = intersect_lines(E, B, F, C)
    H = lerp(A, M, 0.45)
    K = lerp(C, M, 0.48)
    P_top = lerp(E, M, 0.40)
    G = intersect_lines(H, P_top, F, M)
    L = intersect_lines(K, P_top, D, M)
    I_pt = intersect_lines(H, K, M, B)
    s.poly([E, A, C], "EAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(E, A, "EA", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(F, C, "FC", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, D, "AD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(P_top, H, "PH", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(P_top, K, "PK", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(H, K, "HK", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    _pts(
        s,
        [
            (E, "E", "E", -14, 0),
            (A, "A", "A", -14, 0),
            (B, "B", "B", 0, 18),
            (C, "C", "C", 0, 18),
            (F, "F", "F", -14, 0),
            (D, "D", "D", 14, 0),
            (H, "H", "H", 0, 18),
            (K, "K", "K", 14, -4),
            (G, "G", "G", -14, -4),
            (L, "L", "L", 14, 0),
            (I_pt, "I", "I", 0, 18),
            (P_top, "+", "+", 12, 0),
        ],
    )
    s.pt(M, "M", "M", dx=14, dy=4, highlight=True)
    write_svg("liber_primus/prop_25/0107.g30.svg", s)
    count += 1

    # g31: Tab. III Fig. 31 (Prop. XXVI: Central Projection of Quadrilaterals)
    s = CalibratedSVG(400, 420, "Ceva 1678 Tabula III Fig. 31: Prop. XXVI")
    H = (185.0, 165.0)
    A, B, C, E = (55.0, 200.0), (55.0, 285.0), (50.0, 370.0), (225.0, 365.0)
    D = lerp(C, E, 0.52)
    G = intersect_lines(A, D, B, E)
    F = intersect_lines(A, E, C, G)
    L = (150.0, 56.0)
    I_pt = (340.0, 118.0)
    X_pt = (268.0, 32.0)
    M = lerp(L, X_pt, 0.45)
    O_pt = lerp(X_pt, I_pt, 0.35)
    P = intersect_lines(L, O_pt, M, I_pt)
    K = intersect_lines(L, I_pt, H, F)
    s.seg(A, C, "AC", width=2.2)
    s.seg(C, E, "CE", width=2.2)
    s.seg(L, X_pt, "LX", width=2.2)
    s.seg(X_pt, I_pt, "XI", width=2.2)
    for p1, p2, nm in [
        (A, I_pt, "AI"), (E, L, "EL"), (C, X_pt, "CX"),
        (B, O_pt, "BO"), (D, M, "DM"), (F, K, "FK"), (G, P, "GP"),
    ]:
        s.seg(p1, p2, nm, stroke="var(--geom-secondary, #0284c7)", width=1.6)
    for p1, p2, nm in [
        (A, E, "AE"), (A, D, "AD"), (B, E, "BE"), (C, F, "CF"),
        (L, O_pt, "LO"), (L, I_pt, "LI"), (M, I_pt, "MI"), (X_pt, K, "XK"),
    ]:
        s.seg(p1, p2, nm, stroke="var(--geom-highlight, #d97706)", width=1.7)
    _pts(
        s,
        [
            (A, "A", "A", -14, -4),
            (B, "B", "B", -14, 0),
            (C, "C", "C", -14, 4),
            (D, "D", "D", 0, 18),
            (E, "E", "E", 14, 0),
            (F, "F", "F", -12, 0),
            (G, "G", "G", -12, 14),
            (L, "L", "L", -14, 4),
            (M, "M", "M", 0, -12),
            (O_pt, "O", "O", 14, 0),
            (I_pt, "I", "I", 12, 12),
            (P, "P", "P", 0, 14),
            (K, "K", "K", 12, 10),
        ],
    )
    s.pt(H, "H", "H", dx=16, dy=8, highlight=True)
    write_svg("liber_primus/prop_26/0107.g31.svg", s)
    count += 1

    return count


def build_liber_secundus(count: int = 0) -> int:
    """Generate the 30 remaining Liber Secundus SVGs."""
    # g32: Tab. IV Fig. 32 (Conic Lemma I: Inscribed Ellipse in Triangle)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IV Fig. 32: Inscribed Conic in Triangle")
    A, E, C = (195.0, 44.0), (52.0, 305.0), (325.0, 305.0)
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.ellipse((182.0, 212.0), 76.0, 98.0, "conic_FBD", rot=22.0, stroke="var(--geom-secondary, #0284c7)", width=2.1)
    F, B, D = (122.0, 178.0), (255.0, 152.0), (165.0, 305.0)
    _pts(s, [(A, "A", "A", 0, 18), (E, "E", "E", -14, 10), (C, "C", "C", 14, 10),
             (F, "F", "F", -16, -2), (B, "B", "B", 16, -4), (D, "D", "D", 0, 18)])
    write_svg("liber_secundus/lemmata_conica/0109.g32.svg", s)
    count += 1

    # g33: Tab. IV Fig. 33 (Conic Lemma II: Inscribed Ellipse in Quadrilateral)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IV Fig. 33: Inscribed Ellipse in Quadrilateral")
    C, E, G, A = (56.0, 82.0), (320.0, 44.0), (300.0, 305.0), (58.0, 295.0)
    s.poly([C, E, G, A], "CEGA", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    for p1, p2, nm in [(C, E, "CE"), (E, G, "EG"), (G, A, "GA"), (A, C, "AC")]:
        s.seg(p1, p2, nm, width=2.2)
    s.ellipse((184.0, 178.0), 152.0, 96.0, "conic_BDF", rot=-42.0, stroke="var(--geom-secondary, #0284c7)", width=2.1)
    B, D, F, plus = (57.0, 222.0), (218.0, 59.0), (311.0, 146.0), (116.0, 298.0)
    _pts(s, [(C, "C", "C", -16, -4), (E, "E", "E", -14, 14), (G, "G", "G", -14, -8),
             (A, "A", "A", 0, 18), (B, "B", "B", 16, 4), (D, "D", "D", -12, -12),
             (F, "F", "F", -14, 4), (plus, "+", "+", 0, 18)])
    write_svg("liber_secundus/lemmata_conica/0109.g33.svg", s)
    count += 1

    # g34: Tab. IV Fig. 34 (Conic Lemma III: Inscribed Circle in Quadrilateral)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IV Fig. 34: Inscribed Circle in Quadrilateral")
    C, E, G, A = (82.0, 48.0), (295.0, 108.0), (290.0, 298.0), (52.0, 270.0)
    s.poly([C, E, G, A], "CEGA", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    for p1, p2, nm in [(C, E, "CE"), (E, G, "EG"), (G, A, "GA"), (A, C, "AC")]:
        s.seg(p1, p2, nm, width=2.2)
    s.circle((176.0, 182.0), 104.0, "circle_BDF", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    B, D, F, plus = (72.0, 172.0), (194.0, 80.0), (280.0, 185.0), (165.0, 284.0)
    _pts(s, [(C, "C", "C", -14, -4), (E, "E", "E", 14, -6), (G, "G", "G", 14, 10),
             (A, "A", "A", 0, 18), (B, "B", "B", -16, 4), (D, "D", "D", 4, -14),
             (F, "F", "F", 16, 4), (plus, "+", "+", 0, 18)])
    write_svg("liber_secundus/lemmata_conica/0109.g34.svg", s)
    count += 1

    # g36: Tab. IV Fig. 36 (Cylinder Oblique Section & Conjugate Ellipse)
    s = CalibratedSVG(440, 380, "Ceva 1678 Tabula IV Fig. 36: Oblique Cylinder Section")
    G_top, M = (48.0, 56.0), (218.0, 56.0)
    G_bot, A = (48.0, 325.0), (218.0, 325.0)
    O_pt = (400.0, 325.0)
    E = intersect_lines(M, A, G_top, O_pt)
    P = lerp(G_top, E, 0.50)
    Q = lerp(G_bot, A, 0.50)
    s.seg(G_top, M, "GM", width=1.8)
    s.seg(G_top, G_bot, "GG'", width=2.1)
    s.seg(M, A, "MA", width=2.1)
    s.seg(G_bot, O_pt, "GO", width=2.0)
    s.seg(G_top, O_pt, "G_top_O", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg((372, 355), (416, 308), "NO", width=1.7)
    s.ellipse(P, 112.0, 44.0, "ellipse_top", rot=38.0, stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.ellipse(Q, 86.0, 24.0, "ellipse_base", rot=-4.0, stroke="var(--geom-secondary, #0284c7)", width=2.0)
    H_pt, I_pt = (98.0, 152.0), (166.0, 96.0)
    s.seg(H_pt, I_pt, "HI", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg((88, 345), (175, 302), "Q_chord", width=1.7)
    # Upright comparison ellipse on right
    ctr2 = (322.0, 128.0)
    s.ellipse(ctr2, 76.0, 98.0, "ellipse_orth", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg((ctr2[0], ctr2[1] - 98), (ctr2[0], ctr2[1] + 98), "+D", width=1.8)
    s.seg((ctr2[0] - 76, ctr2[1]), (ctr2[0] + 76, ctr2[1]), "FB", width=1.8)
    _pts(s, [(G_top, "G", "G", -14, 0), (M, "M", "M", -14, 16), (E, "E", "E", 14, 12),
             (P, "P", "P", 0, 18), (H_pt, "H", "H", -12, 14), (I_pt, "I", "I", 12, 12),
             (G_bot, "G'", "G", -14, 4), (Q, "Q", "Q", 0, 18), (A, "A", "A", 0, 18),
             (O_pt, "O", "O", 0, 18)])
    s.text((370, 362), "N", "N")
    s.text((322, 22), "+", "+")
    s.text((322, 244), "D", "D")
    s.text((262, 118), "F", "F")
    s.text((380, 142), "B", "B")
    write_svg("liber_secundus/lemmata_conica/0109.g36.svg", s)
    count += 1

    # g37: Tab. IV Fig. 37 (Conic Lemma: Circle/Ellipse Projection)
    s = CalibratedSVG(380, 320, "Ceva 1678 Tabula IV Fig. 37: Ellipse Ordinate")
    ctr = (195.0, 170.0)
    s.ellipse(ctr, 132.0, 88.0, "ellipse_ECAB", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.ellipse(ctr, 132.0, 96.0, "arc_outer", stroke="var(--geom-primary, currentColor)", width=1.4, dash="4 3")
    E, A = (ctr[0] - 132, ctr[1]), (ctr[0] + 132, ctr[1])
    C, B = (ctr[0], ctr[1] - 88), (ctr[0], ctr[1] + 88)
    H = (E[0], E[1] - 78)
    G = (ctr[0] - 66, ctr[1])
    D = (G[0], ctr[1] + 76)
    F = (G[0], ctr[1] + 83)
    s.seg(E, A, "EA", width=2.0)
    s.seg(C, B, "CB", width=2.0)
    s.seg(E, H, "EH", width=1.9)
    s.seg(G, F, "GF", stroke="var(--geom-highlight, #d97706)", width=1.8)
    _pts(s, [(E, "E", "E", -14, 4), (A, "A", "A", 14, 4), (C, "C", "C", 0, -14),
             (B, "B", "B", 0, 18), (H, "H", "H", -14, 0), (G, "G", "G", 0, -12),
             (D, "D", "D", 12, -4), (F, "F", "F", 0, 18)])
    write_svg("liber_secundus/lemmata_conica/0109.g37.svg", s)
    count += 1

    # g39: Tab. V Fig. 39 (Prop. III: Triangle Cevians CAE)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula V Fig. 39: Prop. III")
    C, A, E = (165.0, 40.0), (58.0, 295.0), (315.0, 308.0)
    B = lerp(A, C, 0.52)
    D = lerp(C, E, 0.45)
    F = intersect_lines(A, D, E, B)
    G = intersect_lines(C, F, A, E)
    s.poly([C, A, E], "CAE", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(C, A, "CA", width=2.2)
    s.seg(C, E, "CE", width=2.2)
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, D, "AD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, G, "CG", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(C, "C", "C", -16, 0), (A, "A", "A", -14, 10), (E, "E", "E", 14, 10),
             (B, "B", "B", -16, -4), (D, "D", "D", 16, 8), (G, "G", "G", 0, 18)])
    s.pt(F, "F", "F", dx=-12, dy=16, highlight=True)
    s.text((168, 322), "H", "H")
    write_svg("liber_secundus/prop_03/0111.g39.svg", s)
    count += 1

    # g40: Tab. V Fig. 40 (Prop. IV: Quadrilateral Harmonic Cross)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula V Fig. 40: Prop. IV")
    A, C_tr, E, C_bl = (68.0, 62.0), (298.0, 102.0), (312.0, 298.0), (58.0, 292.0)
    B = lerp(A, C_bl, 0.46)
    F = lerp(C_tr, E, 0.46)
    H = lerp(A, C_tr, 0.38)
    D = lerp(C_bl, E, 0.42)
    K = lerp(C_bl, E, 0.56)
    I_pt = intersect_lines(B, F, H, D)
    s.poly([A, C_tr, E, C_bl], "ACEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    for p1, p2, nm in [(A, C_tr, "AC"), (C_tr, E, "CE"), (E, C_bl, "EC"), (C_bl, A, "CA")]:
        s.seg(p1, p2, nm, width=2.2)
    s.seg(B, F, "BF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(H, D, "HD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(A, "A", "A", -16, 0), (C_tr, "C", "C", 0, -14), (E, "E", "E", 0, 18),
             (C_bl, "C'", "C", 0, 18), (B, "B", "B", -16, 4), (F, "F", "F", 16, 4),
             (H, "H", "H", 0, -14), (D, "D", "D", 0, 18), (K, "K", "K", 0, 18)])
    s.pt(I_pt, "I", "I", dx=12, dy=-10, highlight=True)
    write_svg("liber_secundus/prop_04/0111.g40.svg", s)
    count += 1

    # g42: Tab. V Fig. 42 (Prop. VI: Triangle DB I Harmonic Grid)
    s = CalibratedSVG(420, 280, "Ceva 1678 Tabula V Fig. 42: Prop. VI")
    D, B, I_pt = (44.0, 44.0), (54.0, 248.0), (392.0, 125.0)
    F = lerp(D, I_pt, 0.24)
    G = lerp(D, I_pt, 0.46)
    A = lerp(B, I_pt, 0.30)
    H = lerp(B, I_pt, 0.46)
    E = intersect_lines(D, A, F, B)
    K = intersect_lines(F, H, G, A)
    s.poly([D, B, I_pt], "DBI", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(D, B, "DB", width=2.2)
    s.seg(D, I_pt, "DI", width=2.2)
    s.seg(B, I_pt, "BI", width=2.2)
    s.seg(D, A, "DA", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, B, "FB", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, H, "FH", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(G, A, "GA", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(G, H, "GH", width=1.8)
    s.seg(E, K, "EK", stroke="var(--geom-highlight, #d97706)", width=1.8)
    _pts(s, [(D, "D", "D", 0, -14), (B, "B", "B", -16, 4), (I_pt, "I", "I", 0, 18),
             (F, "F", "F", 0, -14), (G, "G", "G", 0, -14), (A, "A", "A", 0, 18),
             (H, "H", "H", 0, 18), (E, "E", "E", -16, 4), (K, "K", "K", 14, 4)])
    write_svg("liber_secundus/prop_06/0111.g42.svg", s)
    count += 1

    # g43: Tab. V Fig. 43 (Prop. VII: Inscribed Triangle EDF & Cevians)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula V Fig. 43: Prop. VII")
    B, A, C = (180.0, 40.0), (48.0, 295.0), (318.0, 295.0)
    E = lerp(B, A, 0.44)
    D = lerp(B, C, 0.44)
    F = lerp(A, C, 0.50)
    I_pt = (180.0, 188.0)
    K = intersect_lines(B, I_pt, E, D)
    G = intersect_lines(A, I_pt, E, F)
    H = intersect_lines(C, I_pt, D, F)
    s.poly([A, B, C], "ABC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(A, B, "AB", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(C, A, "CA", width=2.2)
    s.seg(E, D, "ED", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(E, F, "EF", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(D, F, "DF", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(B, I_pt, "BI", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(A, I_pt, "AI", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(C, I_pt, "CI", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(B, "B", "B", 14, -4), (A, "A", "A", 0, 18), (C, "C", "C", 14, 14),
             (E, "E", "E", -16, -2), (D, "D", "D", 16, -2), (F, "F", "F", 0, 18),
             (K, "K", "K", 14, -10), (G, "G", "G", -10, 16), (H, "H", "H", 10, 16)])
    s.pt(I_pt, "I", "I", dx=0, dy=18, highlight=True)
    write_svg("liber_secundus/prop_07/0111.g43.svg", s)
    count += 1

    # g45: Tab. V Fig. 45 (Prop. VII Case II: Extended Base LM)
    s = CalibratedSVG(360, 360, "Ceva 1678 Tabula V Fig. 45: Prop. VII Case II")
    B, A, C = (188.0, 42.0), (54.0, 315.0), (262.0, 315.0)
    L, M = (30.0, 315.0), (305.0, 315.0)
    F_l = lerp(B, A, 0.46)
    D = lerp(B, C, 0.46)
    F_b = lerp(A, C, 0.45)
    I_pt = (165.0, 165.0)
    K = intersect_lines(B, (165.0, 210.0), F_l, D)
    G = intersect_lines(A, I_pt, F_l, F_b)
    H = intersect_lines(C, I_pt, D, F_b)
    s.poly([B, A, C], "BAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(L, M, "LM", width=2.2)
    s.seg(F_l, D, "FD", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(F_l, F_b, "FF'", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(D, F_b, "DF'", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(B, K, "BK", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(A, I_pt, "AI", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(C, I_pt, "CI", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(L, K, "LK", dash="4 3", width=1.6)
    s.seg(M, K, "MK", dash="4 3", width=1.6)
    _pts(s, [(B, "B", "B", 16, 0), (A, "A", "A", 0, 18), (C, "C", "C", 0, 18),
             (L, "L", "L", -12, 16), (M, "M", "M", 12, 16),
             (F_l, "F", "F", -16, 0), (D, "D", "D", 16, 0), (F_b, "F'", "F", 0, 18),
             (G, "G", "G", 14, 8), (H, "H", "H", -14, 8), (K, "K", "K", -12, 16)])
    s.pt(I_pt, "I", "I", dx=12, dy=-8, highlight=True)
    write_svg("liber_secundus/prop_07/0111.g45.svg", s)
    count += 1

    # g46: Tab. V Fig. 46 (Prop. VIII: Secant Transversals)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula V Fig. 46: Prop. VIII")
    C, A, E_r = (145.0, 38.0), (50.0, 295.0), (315.0, 295.0)
    B = lerp(C, A, 0.55)
    D = lerp(C, E_r, 0.45)
    E = lerp(C, E_r, 0.78)
    G = lerp(A, E_r, 0.40)
    H = intersect_lines(A, E, D, G)
    s.seg(C, A, "CA", width=2.2)
    s.seg(C, E_r, "CE", width=2.2)
    s.seg(A, E_r, "AE_base", width=2.2)
    s.seg(D, G, "DG", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, E, "AE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(C, "C", "C", 16, 0), (A, "A", "A", 0, 18), (B, "B", "B", -16, 0),
             (D, "D", "D", 16, -4), (E, "E", "E", 16, -4), (G, "G", "G", 0, 18)])
    s.pt(H, "H", "H", dx=-14, dy=-8, highlight=True)
    write_svg("liber_secundus/prop_08/0111.g46.svg", s)
    count += 1

    # g47: Tab. VI Fig. 47 (Prop. IX: Circumscribed Triangle & Inscribed Ellipse I)
    s = CalibratedSVG(320, 440, "Ceva 1678 Tabula VI Fig. 47: Prop. IX Case I")
    B, A, C = (175.0, 32.0), (42.0, 405.0), (298.0, 405.0)
    D = lerp(A, C, 0.50)
    F = lerp(B, A, 0.62)
    E = lerp(B, C, 0.58)
    G = (172.0, 300.0)
    K_edge = lerp(B, C, 0.66)
    I_pt = intersect_lines(B, G, F, E)
    N = intersect_lines(A, G, F, D)
    K_in = intersect_lines(C, G, E, D)
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.ellipse((166.0, 304.0), 92.0, 102.0, "conic_FDE", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.seg(B, D, "BD", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, E, "BE", width=1.6)
    s.seg(F, E, "FE", width=1.8)
    s.seg(F, K_edge, "FK", width=1.8)
    s.seg(F, D, "FD", width=1.8)
    s.seg(E, D, "ED", width=1.8)
    s.seg(A, G, "AG", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(C, G, "CG", stroke="var(--geom-highlight, #d97706)", width=1.8)
    _pts(s, [(B, "B", "B", 14, 0), (A, "A", "A", 0, 18), (C, "C", "C", 0, 18),
             (D, "D", "D", 0, 18), (F, "F", "F", -14, 0), (E, "E", "E", -12, -10),
             (K_edge, "K", "K", 14, 4), (I_pt, "I", "I", 10, -10),
             (N, "N", "N", -14, 8), (K_in, "K'", "K", -14, 4)])
    s.pt(G, "G", "G", dx=12, dy=-8, highlight=True)
    write_svg("liber_secundus/prop_09/0113.g47.svg", s)
    count += 1

    # g48: Tab. VI Fig. 48 (Prop. IX: Inscribed Ellipse II)
    s = CalibratedSVG(320, 440, "Ceva 1678 Tabula VI Fig. 48: Prop. IX Case II")
    B, A, O_pt = (188.0, 34.0), (38.0, 400.0), (298.0, 400.0)
    R = lerp(A, O_pt, 0.44)
    F = lerp(B, A, 0.60)
    E = lerp(B, O_pt, 0.56)
    C = lerp(B, O_pt, 0.72)
    G = (165.0, 265.0)
    I_pt = intersect_lines(B, G, F, E)
    D = intersect_lines(A, C, E, R)
    M = intersect_lines(A, G, F, R)
    N = intersect_lines(A, G, F, D)
    K = intersect_lines(C, G, E, R)
    P_pt = (262.0, 290.0)
    L = intersect_lines(G, P_pt, E, R)
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, O_pt, "BO", width=2.2)
    s.seg(A, O_pt, "AO", width=2.2)
    s.ellipse((165.0, 290.0), 96.0, 110.0, "conic_FRE", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, E, "FE", width=1.8)
    s.seg(F, R, "FR", width=1.8)
    s.seg(F, D, "FD", width=1.8)
    s.seg(E, R, "ER", width=1.8)
    s.seg(A, C, "AC", width=1.8)
    s.seg(A, G, "AG", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(C, G, "CG", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(G, P_pt, "GP", width=1.7)
    _pts(s, [(B, "B", "B", -14, 0), (A, "A", "A", 0, 18), (R, "R", "R", 0, 18),
             (O_pt, "O", "O", 0, 18), (F, "F", "F", -14, 0), (E, "E", "E", 14, -4),
             (C, "C", "C", 14, 4), (I_pt, "I", "I", 10, -10), (M, "M", "M", -14, -2),
             (N, "N", "N", 0, 16), (D, "D", "D", 10, 14), (K, "K", "K", 4, 16),
             (L, "L", "L", 4, -12), (P_pt, "P", "P", -12, 4)])
    s.pt(G, "G", "G", dx=0, dy=16, highlight=True)
    write_svg("liber_secundus/prop_09/0113.g48.svg", s)
    count += 1

    # g49: Tab. VI Fig. 49 (Prop. IX: Inscribed Ellipse III)
    s = CalibratedSVG(320, 440, "Ceva 1678 Tabula VI Fig. 49: Prop. IX Case III")
    B, A, C = (54.0, 34.0), (34.0, 405.0), (300.0, 368.0)
    D = lerp(A, C, 0.48)
    F = lerp(B, A, 0.46)
    E = lerp(B, C, 0.42)
    O_edge = lerp(B, C, 0.70)
    G = (128.0, 265.0)
    R = (165.0, 338.0)
    I_pt = intersect_lines(B, G, F, E)
    M = intersect_lines(A, G, F, R)
    N = intersect_lines(A, G, F, D)
    P_pt = (192.0, 295.0)
    L = intersect_lines(G, P_pt, E, D)
    K = intersect_lines(C, G, E, D)
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.ellipse((118.0, 228.0), 82.0, 118.0, "conic_FRE", rot=-12.0, stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, E, "FE", width=1.8)
    s.seg(F, R, "FR", width=1.8)
    s.seg(F, D, "FD", width=1.8)
    s.seg(E, D, "ED", width=1.8)
    s.seg(A, O_edge, "AO", width=1.8)
    s.seg(A, G, "AG", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(C, G, "CG", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(G, P_pt, "GP", width=1.7)
    _pts(s, [(B, "B", "B", 14, 0), (A, "A", "A", 0, 18), (D, "D", "D", 0, 18),
             (C, "C", "C", 14, 4), (F, "F", "F", -14, 0), (E, "E", "E", 14, -4),
             (O_edge, "O", "O", 14, -4), (R, "R", "R", 12, 14), (I_pt, "I", "I", 0, -14),
             (M, "M", "M", 12, 4), (N, "N", "N", -14, 0), (L, "L", "L", 12, -8),
             (K, "K", "K", -12, 8), (P_pt, "P", "P", 12, 0)])
    s.pt(G, "G", "G", dx=12, dy=-12, highlight=True)
    write_svg("liber_secundus/prop_09/0113.g49.svg", s)
    count += 1

    # g51: Tab. VII Fig. 51 (Prop. XIII: Conic Arc & Tangents)
    s = CalibratedSVG(360, 320, "Ceva 1678 Tabula VII Fig. 51: Prop. XIII")
    C = (205.0, 42.0)
    A, B = (105.0, 195.0), (268.0, 228.0)
    E = lerp(C, A, 0.30)
    F = lerp(C, B, 0.38)
    D = intersect_lines(A, F, B, E)
    s.path("M 24 272 Q 185 110 315 295", "conic_AB", stroke="var(--geom-secondary, #0284c7)", width=2.2)
    s.seg(C, A, "CA", width=2.1)
    s.seg(C, B, "CB", width=2.1)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, E, "BE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(C, "C", "C", 16, 0), (A, "A", "A", -4, 18), (B, "B", "B", -14, 14),
             (E, "E", "E", -16, -2), (F, "F", "F", 16, -2)])
    s.pt(D, "D", "D", dx=-10, dy=16, highlight=True)
    write_svg("liber_secundus/prop_13/0113.g51.svg", s)
    count += 1

    # g52: Tab. VII Fig. 52 (Prop. XIII: Tall Triangle & Conic Pole-Polar)
    s = CalibratedSVG(320, 480, "Ceva 1678 Tabula VII Fig. 52: Prop. XIII Pole-Polar")
    E, K, L = (172.0, 34.0), (36.0, 442.0), (275.0, 435.0)
    F = lerp(E, K, 0.44)
    D = lerp(E, L, 0.46)
    A = lerp(E, K, 0.68)
    C = lerp(E, L, 0.68)
    I_pt = lerp(K, L, 0.48)
    B = intersect_lines(E, I_pt, F, D)
    N = lerp(F, B, 0.78)
    G = intersect_lines(A, D, F, C)
    M = intersect_lines(A, L, K, C)
    s.seg(E, K, "EK", width=2.2)
    s.seg(E, L, "EL", width=2.2)
    s.seg(K, L, "KL", width=2.2)
    s.seg(F, D, "FD", width=2.0)
    s.seg(E, G, "EG", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(A, D, "AD", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(F, C, "FC", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg(A, L, "AL", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(K, C, "KC", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.ellipse((156.0, 326.0), 88.0, 114.0, "conic_ABCI", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    _pts(s, [(E, "E", "E", -14, 0), (K, "K", "K", -14, 14), (L, "L", "L", 14, 4),
             (F, "F", "F", -14, -4), (D, "D", "D", 14, 0), (B, "B", "B", 10, -10),
             (N, "N", "N", -6, -12), (A, "A", "A", -14, 0), (C, "C", "C", 14, 0),
             (I_pt, "I", "I", 0, 18), (G, "G", "G", 10, 16), (M, "M", "M", 0, 18)])
    write_svg("liber_secundus/prop_13/0113.g52.svg", s)
    count += 1

    # g53: Tab. VII Fig. 53 (Prop. XIV: External Tangents & Secants)
    s = CalibratedSVG(340, 420, "Ceva 1678 Tabula VII Fig. 53: Prop. XIV Case I")
    C = (195.0, 278.0)
    E, F = (48.0, 102.0), (242.0, 58.0)
    A = lerp(C, E, 0.45)
    B = lerp(C, F, 0.48)
    D = intersect_lines(A, F, B, E)
    s.ellipse((195.0, 285.0), 106.0, 112.0, "conic_AB", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.seg(C, E, "CE", width=2.1)
    s.seg(C, F, "CF", width=2.1)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, E, "BE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(C, "C", "C", 0, 18), (E, "E", "E", 0, -14), (F, "F", "F", -14, -10),
             (A, "A", "A", -16, 4), (B, "B", "B", 16, 4)])
    s.pt(D, "D", "D", dx=-12, dy=-12, highlight=True)
    write_svg("liber_secundus/prop_14/0113.g53.svg", s)
    count += 1

    # g54: Tab. VII Fig. 54 (Prop. XIV: Brianchon/Ceva Concurrency on Ellipse)
    s = CalibratedSVG(320, 460, "Ceva 1678 Tabula VII Fig. 54: Prop. XIV Case II")
    E, F, D = (172.0, 32.0), (36.0, 420.0), (275.0, 420.0)
    A = lerp(E, F, 0.56)
    C = lerp(E, D, 0.56)
    B = lerp(F, D, 0.50)
    G = intersect_lines(E, B, F, C)
    s.seg(E, F, "EF", width=2.2)
    s.seg(E, D, "ED", width=2.2)
    s.seg(F, D, "FD", width=2.2)
    s.ellipse((156.0, 305.0), 88.0, 114.0, "conic_ABC", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, C, "FC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(A, D, "AD", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(E, "E", "E", 14, 0), (F, "F", "F", 0, 18), (D, "D", "D", 0, 18),
             (A, "A", "A", -16, -2), (C, "C", "C", 16, -2), (B, "B", "B", 0, 18)])
    s.pt(G, "G", "G", dx=12, dy=-10, highlight=True)
    write_svg("liber_secundus/prop_14/0113.g54.svg", s)
    count += 1

    # g55: Tab. VIII Fig. 55 (Prop. XIV: Third Tangent to Ellipse)
    s = CalibratedSVG(360, 360, "Ceva 1678 Tabula VIII Fig. 55: Prop. XIV Third Tangent")
    E = (320.0, 48.0)
    A, C = (145.0, 138.0), (288.0, 215.0)
    F = lerp(E, A, 0.56)
    D = lerp(E, C, 0.56)
    B = lerp(F, D, 0.50)
    s.ellipse((175.0, 232.0), 118.0, 92.0, "conic_ABC", rot=-38.0, stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(E, A, "EA", width=2.1)
    s.seg(E, C, "EC", width=2.1)
    s.seg(F, D, "FD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(E, "E", "E", 14, 0), (A, "A", "A", -16, -6), (C, "C", "C", 16, 4),
             (F, "F", "F", -8, -14), (D, "D", "D", 16, 4)])
    s.pt(B, "B", "B", dx=10, dy=-12, highlight=True)
    write_svg("liber_secundus/prop_14/0115.g55.svg", s)
    count += 1

    # g56: Tab. VIII Fig. 56 (Prop. XIV: Third Tangent to Circle)
    s = CalibratedSVG(360, 380, "Ceva 1678 Tabula VIII Fig. 56: Prop. XIV Circle Tangent")
    ctr = (188.0, 240.0)
    R = 118.0
    E = (188.0, 36.0)
    A = (ctr[0] - R * math.cos(math.radians(30)), ctr[1] - R * math.sin(math.radians(30)))
    C = (ctr[0] + R * math.cos(math.radians(30)), ctr[1] - R * math.sin(math.radians(30)))
    F = lerp(E, A, 0.58)
    D = lerp(E, C, 0.58)
    B = (ctr[0], ctr[1] - R)
    s.circle(ctr, R, "circle_ABC", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(E, A, "EA", width=2.1)
    s.seg(E, C, "EC", width=2.1)
    s.seg(F, D, "FD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(E, "E", "E", 0, 20), (A, "A", "A", -18, 0), (C, "C", "C", 18, 0),
             (F, "F", "F", -14, -4), (D, "D", "D", 16, -4)])
    s.pt(B, "B", "B", dx=0, dy=-14, highlight=True)
    s.pt(ctr, "O", None, r=2.5)
    write_svg("liber_secundus/prop_14/0115.g56.svg", s)
    count += 1

    # g58: Tab. VIII Fig. 58 (Prop. XVI: Equal Circles Common Tangent)
    s = CalibratedSVG(420, 260, "Ceva 1678 Tabula VIII Fig. 58: Prop. XVI Equal Circles")
    K, I_pt = (115.0, 155.0), (305.0, 155.0)
    R = 72.0
    A, F = (K[0], K[1] - R), (I_pt[0], I_pt[1] - R)
    s.circle(K, R, "circle_K", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.circle(I_pt, R, "circle_I", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(K, I_pt, "KI", width=2.0)
    s.seg(K, A, "KA", width=1.9)
    s.seg(I_pt, F, "IF", width=1.9)
    _pts(s, [(A, "A", "A", 0, -14), (F, "F", "F", 0, -14), (K, "K", "K", 0, 18), (I_pt, "I", "I", 12, 16)])
    write_svg("liber_secundus/prop_16/0115.g58.svg", s)
    count += 1

    # g59: Tab. VIII Fig. 59 (Prop. XVIII: Two Circles Secant & Tangent)
    s = CalibratedSVG(340, 420, "Ceva 1678 Tabula VIII Fig. 59: Prop. XVIII")
    c_bot = (172.0, 295.0)
    r_bot = 112.0
    c_top = (225.0, 120.0)
    r_top = 74.0
    s.circle(c_bot, r_bot, "circle_AF", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.circle(c_top, r_top, "circle_CD", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    A = (c_bot[0] - r_bot * 0.94, c_bot[1] - r_bot * 0.34)
    F = (c_bot[0] + r_bot * 0.94, c_bot[1] - r_bot * 0.34)
    E = lerp(A, F, 0.56)
    C = (152.0, 114.0)
    B = lerp(C, A, 0.16)
    D = intersect_lines(C, E, B, F)
    s.seg(A, F, "AF", width=2.0)
    s.seg(C, A, "CA", width=2.0)
    s.seg(C, E, "CE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, F, "BF", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(A, "A", "A", -16, 4), (F, "F", "F", 16, 4), (E, "E", "E", 0, 18),
             (C, "C", "C", -16, -2), (B, "B", "B", -16, 0)])
    s.pt(D, "D", "D", dx=12, dy=-4, highlight=True)
    write_svg("liber_secundus/prop_18/0115.g59.svg", s)
    count += 1

    # g60: Tab. VIII Fig. 60 (Prop. XVI: Internal Common Tangent)
    s = CalibratedSVG(440, 260, "Ceva 1678 Tabula VIII Fig. 60: Prop. XVI Internal Tangent")
    K, I_pt = (130.0, 138.0), (345.0, 138.0)
    rK, rI = 78.0, 42.0
    ang = math.acos((rK + rI) / (I_pt[0] - K[0]))
    A = (K[0] + rK * math.cos(ang), K[1] - rK * math.sin(ang))
    F = (I_pt[0] - rI * math.cos(ang), I_pt[1] + rI * math.sin(ang))
    L = intersect_lines(K, I_pt, A, F)
    s.circle(K, rK, "circle_K", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.circle(I_pt, rI, "circle_I", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(K, I_pt, "KI", width=2.0)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(K, A, "KA", width=1.9)
    s.seg(I_pt, F, "IF", width=1.9)
    _pts(s, [(K, "K", "K", -10, 16), (I_pt, "I", "I", 12, 10), (A, "A", "A", 4, -14), (F, "F", "F", 0, 18)])
    s.pt(L, "L", "L", dx=-6, dy=16, highlight=True)
    write_svg("liber_secundus/prop_16/0115.g60.svg", s)
    count += 1

    # g61: Tab. VIII Fig. 61 (Prop. XVI: External Common Tangent)
    s = CalibratedSVG(460, 240, "Ceva 1678 Tabula VIII Fig. 61: Prop. XVI External Tangent")
    K, I_pt = (108.0, 118.0), (275.0, 118.0)
    rK, rI = 74.0, 34.0
    ang = math.acos((rK - rI) / (I_pt[0] - K[0]))
    A = (K[0] + rK * math.cos(ang), K[1] + rK * math.sin(ang))
    F = (I_pt[0] + rI * math.cos(ang), I_pt[1] + rI * math.sin(ang))
    L = intersect_lines(K, I_pt, A, F)
    s.circle(K, rK, "circle_K", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.circle(I_pt, rI, "circle_I", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(K, L, "KL", width=2.0)
    s.seg(A, L, "AL", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(K, A, "KA", width=1.9)
    s.seg(I_pt, F, "IF", width=1.9)
    _pts(s, [(K, "K", "K", -12, -8), (I_pt, "I", "I", -12, 16), (A, "A", "A", -14, -4), (F, "F", "F", 0, 18)])
    s.pt(L, "L", "L", dx=14, dy=4, highlight=True)
    write_svg("liber_secundus/prop_16/0115.g61.svg", s)
    count += 1

    # g62: Tab. IX Fig. 62 (Prop. XVII: Malfatti/Inscribed Three-Circle Problem)
    s = CalibratedSVG(380, 360, "Ceva 1678 Tabula IX Fig. 62: Prop. XVII Three Circles")
    E, L, H = (158.0, 36.0), (54.0, 326.0), (336.0, 322.0)
    s.poly([E, L, H], "ELH", fill="var(--geom-accent-fill, rgba(180,120,40,0.04))")
    s.seg(E, L, "EL", width=2.2)
    s.seg(E, H, "EH", width=2.2)
    s.seg(L, H, "LH", width=2.2)
    c_top = (172.0, 134.0)
    c_br = (224.0, 250.0)
    c_bl = (106.0, 282.0)
    s.circle(c_top, 50.0, "circle_top", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.circle(c_br, 72.0, "circle_O", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.circle(c_bl, 42.0, "circle_B", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.seg(E, c_br, "EO", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(L, c_br, "LO", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.seg(H, c_br, "HO", stroke="var(--geom-highlight, #d97706)", width=1.8)
    D, F = (128.0, 118.0), (218.0, 112.0)
    P_pt = intersect_lines(E, c_br, D, F)
    s.seg(D, F, "DF", width=1.7)
    G, I_pt = (284.0, 212.0), (224.0, 322.0)
    s.seg(G, I_pt, "GI", width=1.7)
    M, K = (74.0, 268.0), (110.0, 324.0)
    s.seg(M, K, "MK", width=1.7)
    Q = intersect_lines(L, c_br, M, K)
    _pts(s, [(E, "E", "E", -14, 0), (L, "L", "L", -14, 14), (H, "H", "H", 14, 14),
             (D, "D", "D", -14, 0), (F, "F", "F", 14, -4), (P_pt, "P", "P", 12, -8),
             (G, "G", "G", 14, -4), (I_pt, "I", "I", 0, 18), (M, "M", "M", -14, -4),
             (K, "K", "K", 0, 18), (Q, "Q", "Q", -12, 10), (c_bl, "B", "B", 10, 10)])
    s.pt(c_br, "O", "O", dx=0, dy=18, highlight=True)
    write_svg("liber_secundus/prop_17/0117.g62.svg", s)
    count += 1

    # g63: Tab. IX Fig. 63 (Prop. XIX: Hourglass Triangles & Median Transversal)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IX Fig. 63: Prop. XIX Case I")
    A, C = (48.0, 56.0), (318.0, 56.0)
    B = lerp(A, C, 0.52)
    G, F = (72.0, 305.0), (318.0, 285.0)
    E = lerp(G, F, 0.44)
    H = intersect_lines(A, E, B, G)
    D = intersect_lines(B, F, C, E)
    I_pt = intersect_lines(B, E, H, D)
    s.seg(A, C, "AC", width=2.2)
    s.seg(G, F, "GF", width=2.2)
    s.seg(A, E, "AE", width=2.0)
    s.seg(C, E, "CE", width=2.0)
    s.seg(B, G, "BG", width=2.0)
    s.seg(B, F, "BF", width=2.0)
    s.seg(B, E, "BE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(H, D, "HD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(A, "A", "A", -12, -12), (B, "B", "B", 0, -14), (C, "C", "C", 12, -12),
             (G, "G", "G", -12, 16), (E, "E", "E", 0, 18), (F, "F", "F", 12, 16),
             (H, "H", "H", -16, 4), (D, "D", "D", 16, 4)])
    s.pt(I_pt, "I", "I", dx=12, dy=-8, highlight=True)
    write_svg("liber_secundus/prop_19/0117.g63.svg", s)
    count += 1

    # g64: Tab. IX Fig. 64 (Prop. XIX: Perspective Triangle Pencil)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IX Fig. 64: Prop. XIX Case II")
    A, P_r, G = (42.0, 56.0), (332.0, 118.0), (42.0, 305.0)
    B = lerp(A, P_r, 0.30)
    C = lerp(A, P_r, 0.50)
    E = lerp(G, P_r, 0.24)
    F = lerp(G, P_r, 0.42)
    H = intersect_lines(A, E, B, G)
    D = intersect_lines(B, F, C, E)
    s.seg(A, P_r, "AP", width=2.2)
    s.seg(G, P_r, "GP", width=2.2)
    s.seg(A, E, "AE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(B, F, "BF", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    s.seg(C, E, "CE", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    _pts(s, [(A, "A", "A", 0, -14), (B, "B", "B", 0, -14), (C, "C", "C", 0, -14),
             (G, "G", "G", -12, 16), (E, "E", "E", 4, 18), (F, "F", "F", 4, 18),
             (H, "H", "H", 12, 4), (D, "D", "D", 14, 4)])
    write_svg("liber_secundus/prop_19/0117.g64.svg", s)
    count += 1

    # g65: Tab. IX Fig. 65 (Prop. XIX: Pappus/Hourglass Cross-Chord)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IX Fig. 65: Prop. XIX Case III")
    A, C = (70.0, 52.0), (325.0, 52.0)
    B = lerp(A, C, 0.48)
    G, F = (64.0, 305.0), (325.0, 290.0)
    E = lerp(G, F, 0.44)
    H = intersect_lines(A, E, B, G)
    I_pt = intersect_lines(A, E, G, C)
    K = intersect_lines(B, F, G, C)
    D = intersect_lines(B, F, C, E)
    s.seg(A, C, "AC", width=2.2)
    s.seg(G, F, "GF", width=2.2)
    s.seg(A, E, "AE", width=2.0)
    s.seg(C, E, "CE", width=2.0)
    s.seg(B, G, "BG", width=2.0)
    s.seg(B, F, "BF", width=2.0)
    s.seg(G, C, "GC", stroke="var(--geom-highlight, #d97706)", width=2.1)
    _pts(s, [(A, "A", "A", -14, -10), (B, "B", "B", 0, -14), (C, "C", "C", 14, -10),
             (G, "G", "G", -12, 16), (E, "E", "E", 0, 18), (F, "F", "F", 0, 18),
             (H, "H", "H", -14, 0), (I_pt, "I", "I", 12, 10), (K, "K", "K", 0, -14),
             (D, "D", "D", 14, 4)])
    write_svg("liber_secundus/prop_19/0117.g65.svg", s)
    count += 1

    # g66: Tab. IX Fig. 66 (Prop. XIX: Extended Ray KL)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IX Fig. 66: Prop. XIX Case IV")
    A, C = (48.0, 48.0), (318.0, 48.0)
    B = lerp(A, C, 0.42)
    G, F = (34.0, 290.0), (332.0, 290.0)
    E = lerp(G, F, 0.44)
    K = (46.0, 322.0)
    L = lerp(B, F, 0.80)
    H = intersect_lines(A, E, B, G)
    I_pt = intersect_lines(A, E, B, K)
    D = intersect_lines(B, F, C, E)
    s.seg(A, C, "AC", width=2.2)
    s.seg(G, F, "GF", width=2.2)
    s.seg(A, E, "AE", width=2.0)
    s.seg(C, E, "CE", width=2.0)
    s.seg(B, G, "BG", width=2.0)
    s.seg(B, F, "BF", width=2.0)
    s.seg(B, K, "BK", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(K, L, "KL", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(A, "A", "A", -14, 0), (B, "B", "B", 0, -14), (C, "C", "C", 14, 0),
             (G, "G", "G", 6, -14), (E, "E", "E", 0, 18), (F, "F", "F", -12, -12),
             (K, "K", "K", -14, 8), (L, "L", "L", 12, -10),
             (H, "H", "H", -14, 0), (I_pt, "I", "I", 12, 4), (D, "D", "D", -14, 0)])
    write_svg("liber_secundus/prop_19/0117.g66.svg", s)
    count += 1

    # g67: Tab. IX Fig. 67 (Prop. XX: Bowtie & Scale Segment NOP)
    s = CalibratedSVG(360, 340, "Ceva 1678 Tabula IX Fig. 67: Prop. XX")
    D, C = (112.0, 48.0), (195.0, 48.0)
    A, K = (36.0, 295.0), (328.0, 295.0)
    I_pt = intersect_lines(D, K, A, C)
    E = (D[0], A[1])
    B = intersect_lines(D, E, A, C)
    s.seg(D, C, "DC", width=2.1)
    s.seg(A, K, "AK", width=2.2)
    s.seg(D, K, "DK", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, C, "AC", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(D, E, "DE", stroke="var(--geom-secondary, #0284c7)", width=1.9)
    # Auxiliary scale segment NOP
    N, O_pt, P_pt = (290.0, 48.0), (290.0, 112.0), (290.0, 215.0)
    s.seg(N, P_pt, "NP", width=1.8)
    _pts(s, [(D, "D", "D", -14, 0), (C, "C", "C", 14, 0), (A, "A", "A", -12, 16),
             (K, "K", "K", 12, 16), (B, "B", "B", 14, 4), (E, "E", "E", 14, -10),
             (N, "N", "N", -14, 4), (O_pt, "O", "O", -14, 4), (P_pt, "P", "P", -14, 4)])
    s.pt(I_pt, "I", "I", dx=-12, dy=16, highlight=True)
    write_svg("liber_secundus/prop_20/0117.g67.svg", s)
    count += 1

    return count


def build_appendix_geometrica(count: int = 0) -> int:
    """Generate the 11 remaining Appendix Geometrica SVGs."""
    # g68: Tab. IX Fig. 68 (Appendix Prop. I: Semicircle Chords & Projections)
    s = CalibratedSVG(380, 260, "Ceva 1678 Tabula IX Fig. 68: Appendix Prop. I")
    E = (190.0, 215.0)
    R = 142.0
    A, C = (E[0] - R, E[1]), (E[0] + R, E[1])
    D = (E[0], E[1] - R)
    ang_b = math.radians(38.0)
    B = (E[0] + R * math.cos(ang_b), E[1] - R * math.sin(ang_b))
    G = (B[0], E[1])
    I_pt = intersect_lines(A, B, D, E)
    # Foot of perpendicular from D to AB
    abx, aby = B[0] - A[0], B[1] - A[1]
    t_h = ((D[0] - A[0]) * abx + (D[1] - A[1]) * aby) / (abx * abx + aby * aby)
    H = (A[0] + t_h * abx, A[1] + t_h * aby)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} A {R:.2f} {R:.2f} 0 0 1 {C[0]:.2f} {C[1]:.2f}", "arc_ADC",
           stroke="var(--geom-secondary, #0284c7)", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(A, D, "AD", width=1.9)
    s.seg(D, C, "DC", width=1.9)
    s.seg(D, B, "DB", width=1.9)
    s.seg(B, C, "BC", width=1.9)
    s.seg(A, B, "AB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(D, E, "DE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(D, H, "DH", width=1.7)
    s.seg(E, B, "EB", width=1.7)
    s.seg(B, G, "BG", width=1.8)
    _pts(s, [(A, "A", "A", -10, 18), (E, "E", "E", 0, 18), (G, "G", "G", 0, 18),
             (C, "C", "C", 10, 18), (D, "D", "D", 0, -14), (B, "B", "B", 14, -8),
             (H, "H", "H", 8, 16)])
    s.pt(I_pt, "I", "I", dx=-12, dy=-4, highlight=True)
    write_svg("appendix_geometrica/prop_01/0117.g68.svg", s)
    count += 1

    # g69: Tab. IX Fig. 69 (Appendix Prop. II: Circle & Crescent Arcs)
    s = CalibratedSVG(360, 360, "Ceva 1678 Tabula IX Fig. 69: Appendix Prop. II Case I")
    D = (165.0, 195.0)
    R = 128.0
    A, C = (D[0] - R, D[1]), (D[0] + R, D[1])
    B = (D[0], D[1] - R)
    E = (D[0], D[1] - 72.0)
    F = intersect_lines(B, C, E, (E[0] + 150, E[1] + 22))
    H = (325.0, 148.0)
    s.circle(D, R, "circle_ABC", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(A, C, "AC", width=2.1)
    s.seg(B, D, "BD", width=2.0)
    s.seg(A, B, "AB", width=2.0)
    s.seg(B, C, "BC", width=2.0)
    s.seg(A, E, "AE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(E, C, "EC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(E, H, "EH", width=1.7)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} Q {D[0]:.2f} {D[1] + 62:.2f} {C[0]:.2f} {C[1]:.2f}", "arc_AGC",
           stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} Q {D[0]:.2f} {D[1] + 102:.2f} {C[0]:.2f} {C[1]:.2f}", "arc_AKC",
           stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.path(f"M {C[0]:.2f} {C[1]:.2f} Q {C[0] + 18:.2f} {C[1] - 20:.2f} {H[0]:.2f} {H[1]:.2f}", "arc_CH",
           width=1.6)
    _pts(s, [(A, "A", "A", -14, 4), (C, "C", "C", 14, 4), (B, "B", "B", 0, -14),
             (D, "D", "D", 14, -8), (E, "E", "E", -14, -4), (F, "F", "F", 12, -10),
             (H, "H", "H", 14, -4)])
    s.text((D[0], D[1] + 38), "G", "G")
    s.text((D[0], D[1] + 64), "K", "K")
    write_svg("appendix_geometrica/prop_02/0117.g69.svg", s)
    count += 1

    # g70: Tab. IX Fig. 70 (Appendix Prop. II Case II: Exterior Vertex E)
    s = CalibratedSVG(360, 380, "Ceva 1678 Tabula IX Fig. 70: Appendix Prop. II Case II")
    D = (180.0, 232.0)
    R = 122.0
    A, C = (D[0] - R, D[1]), (D[0] + R, D[1])
    B = (D[0], D[1] - R)
    E = (D[0], 42.0)
    H = (D[0] + 64.0, D[1] + 28.0)
    J = intersect_lines(B, C, E, H)
    s.circle(D, R, "circle_ABC", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.seg(A, C, "AC", width=2.1)
    s.seg(E, D, "ED", width=2.0)
    s.seg(E, A, "EA", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(E, C, "EC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, A, "BA", width=1.9)
    s.seg(B, C, "BC", width=1.9)
    s.seg(E, H, "EH", stroke="var(--geom-highlight, #d97706)", width=1.8)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} Q {D[0]:.2f} {D[1] + 54:.2f} {C[0]:.2f} {C[1]:.2f}", "arc_AKC",
           stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} Q {D[0]:.2f} {D[1] + 92:.2f} {C[0]:.2f} {C[1]:.2f}", "arc_AGC",
           stroke="var(--geom-highlight, #d97706)", width=1.8)
    _pts(s, [(E, "E", "E", 0, -14), (B, "B", "B", -14, -8), (D, "D", "D", 14, -10),
             (A, "A", "A", -16, 4), (C, "C", "C", 16, 4), (J, "J", "J", -12, 8),
             (H, "H", "H", -14, -6)])
    s.text((D[0], D[1] + 22), "K", "K")
    s.text((D[0], D[1] + 68), "G", "G")
    write_svg("appendix_geometrica/prop_02/0117.g70.svg", s)
    count += 1

    # g72: Tab. IX Fig. 72 (Appendix Prop. V: Hippocrates' Lunes)
    s = CalibratedSVG(400, 300, "Ceva 1678 Tabula IX Fig. 72: Appendix Prop. V Hippocrates Lunes")
    O_pt = (200.0, 232.0)
    R = 148.0
    A, C = (O_pt[0] - R, O_pt[1]), (O_pt[0] + R, O_pt[1])
    ang = math.radians(52.0)
    B = (O_pt[0] + R * math.cos(ang), O_pt[1] - R * math.sin(ang))
    r_ab = math.hypot(B[0] - A[0], B[1] - A[1]) / 2.0
    r_bc = math.hypot(C[0] - B[0], C[1] - B[1]) / 2.0
    s.path(f"M {A[0]:.2f} {A[1]:.2f} A {R:.2f} {R:.2f} 0 0 1 {C[0]:.2f} {C[1]:.2f}", "arc_ABC",
           stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} A {r_ab:.2f} {r_ab:.2f} 0 0 1 {B[0]:.2f} {B[1]:.2f}", "lune_E",
           stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.path(f"M {B[0]:.2f} {B[1]:.2f} A {r_bc:.2f} {r_bc:.2f} 0 0 1 {C[0]:.2f} {C[1]:.2f}", "lune_D",
           stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.poly([A, B, C], "ABC", fill="var(--geom-accent-fill, rgba(180,120,40,0.08))")
    s.seg(A, B, "AB", width=2.1)
    s.seg(B, C, "BC", width=2.1)
    s.seg(A, C, "AC", width=2.2)
    _pts(s, [(A, "A", "A", 0, 18), (B, "B", "B", 6, -14), (C, "C", "C", 0, 18)])
    s.text((108, 102), "E", "E", size=18)
    s.text((312, 138), "D", "D", size=18)
    write_svg("appendix_geometrica/prop_05/0117.g72.svg", s)
    count += 1

    # g73: Tab. IX Fig. 73 (Appendix Prop. VI: Inscribed Trapezoid & Lune)
    s = CalibratedSVG(360, 360, "Ceva 1678 Tabula IX Fig. 73: Appendix Prop. VI")
    ctr = (180.0, 188.0)
    R = 136.0
    A, C = (ctr[0] - R, ctr[1] + 18.0), (ctr[0] + R, ctr[1] + 18.0)
    # Adjust A, C to lie on circle
    dy_ac = 18.0
    dx_ac = math.sqrt(R * R - dy_ac * dy_ac)
    A, C = (ctr[0] - dx_ac, ctr[1] + dy_ac), (ctr[0] + dx_ac, ctr[1] + dy_ac)
    dy_be = -92.0
    dx_be = math.sqrt(R * R - dy_be * dy_be)
    B, E_top = (ctr[0] - dx_be, ctr[1] + dy_be), (ctr[0] + dx_be, ctr[1] + dy_be)
    s.circle(ctr, R, "circle_ABEC", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.poly([A, B, E_top, C], "ABEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, B, "AB", width=2.1)
    s.seg(B, E_top, "BE", width=2.1)
    s.seg(E_top, C, "EC", width=2.1)
    s.seg(A, C, "AC", width=2.1)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} Q {ctr[0]:.2f} {ctr[1] + 78:.2f} {C[0]:.2f} {C[1]:.2f}", "arc_AFC",
           stroke="var(--geom-highlight, #d97706)", width=2.0)
    _pts(s, [(A, "A", "A", 14, -8), (B, "B", "B", 6, 16), (E_top, "E_top", "E", -6, 16),
             (C, "C", "C", 14, 0)])
    s.text((180, 145), "D", "D", size=18)
    s.text((310, 132), "G", "G")
    s.text((180, 246), "F", "F")
    s.text((180, 286), "E", "E", size=18)
    write_svg("appendix_geometrica/prop_06/0117.g73.svg", s)
    count += 1

    # g75: Tab. X Fig. 75 (Appendix Prop. VIII: Cylindrical Ungula & Prism)
    s = CalibratedSVG(340, 520, "Ceva 1678 Tabula X Fig. 75: Appendix Prop. VIII Cylindrical Ungula")
    A, L, C = (68.0, 88.0), (168.0, 88.0), (268.0, 88.0)
    I_pt, K, H = (68.0, 475.0), (168.0, 475.0), (268.0, 475.0)
    B = (232.0, 32.0)
    E, F, D = (68.0, 290.0), (168.0, 315.0), (268.0, 340.0)
    M, C_bot = (232.0, 290.0), (232.0, 415.0)
    O_pt = (202.0, 445.0)
    s.seg(A, C, "AC", width=2.0)
    s.seg(I_pt, H, "IH", width=2.0)
    s.seg(A, I_pt, "AI", width=2.1)
    s.seg(L, K, "LK", width=1.9)
    s.seg(C, H, "CH", width=2.1)
    s.seg(B, C_bot, "BC'", width=1.8)
    s.seg(A, B, "AB", width=1.8)
    s.seg(B, L, "BL", width=1.7)
    s.seg(B, F, "BF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(F, C_bot, "FC'", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(E, D, "ED", width=1.9)
    s.seg(I_pt, B, "IB_proj", dash="3 3", width=1.3)
    s.seg(K, C_bot, "KC'", width=1.7)
    # Top, middle, bottom, and oblique curves
    s.path("M 68 88 Q 225 18 282 65 Q 285 80 268 88", "top_arc", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.path("M 68 290 Q 175 262 268 308 Q 288 324 268 340", "mid_arc", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.path("M 68 290 Q 152 405 232 415 Q 290 405 268 340", "ungula_bot", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.path("M 68 290 Q 128 115 232 32 Q 295 145 268 340", "ungula_top", stroke="var(--geom-secondary, #0284c7)", width=2.0)
    s.path("M 68 475 Q 195 395 278 445 Q 278 465 268 475", "bot_arc", stroke="var(--geom-secondary, #0284c7)", width=1.8)
    s.seg((118, 148), (282, 190), "XY", width=1.7)
    s.seg((118, 345), (275, 392), "PQR", width=1.7)
    _pts(s, [(A, "A", "A", -14, 4), (L, "L", "L", -10, 14), (C, "C", "C", -12, -8),
             (B, "B", "B", 14, 0), (E, "E", "E", -14, 0), (F, "F", "F", -12, 14),
             (D, "D", "D", 14, 10), (M, "M", "M", 12, -8), (C_bot, "C'", "C", 14, 8),
             (O_pt, "O", "O", 12, 12), (I_pt, "I", "I", 0, 18), (K, "K", "K", 0, 18),
             (H, "H", "H", 0, 18)])
    s.text((104, 52), "S", "S")
    s.text((208, 56), "N", "N")
    s.text((292, 56), "T", "T")
    s.text((104, 148), "X", "X")
    s.text((294, 195), "Y", "Y")
    s.text((118, 272), "V", "V")
    s.text((294, 336), "Z", "Z")
    s.text((104, 355), "P", "P")
    s.text((168, 376), "Q", "Q")
    s.text((284, 396), "R", "R")
    write_svg("appendix_geometrica/prop_08/0119.g75.svg", s)
    count += 1

    # g76: Tab. X Fig. 76 (Appendix Prop. IX: Circle & Oblique Prism Grid)
    s = CalibratedSVG(360, 520, "Ceva 1678 Tabula X Fig. 76: Appendix Prop. IX")
    V = (242.0, 142.0)
    R = 112.0
    s.circle(V, R, "circle_ABCD", stroke="var(--geom-secondary, #0284c7)", width=2.1)
    dx_a = 94.0
    dy_a = math.sqrt(R * R - dx_a * dx_a)
    A, D = (V[0] - dx_a, V[1] - dy_a), (V[0] + dx_a, V[1] - dy_a)
    L, E = (V[0] - dx_a, V[1] + dy_a), (V[0] + dx_a, V[1] + dy_a)
    G_pt = (V[0], V[1] + R)
    I_pt, H, F = (A[0], G_pt[1]), (V[0] - 52, G_pt[1]), (D[0], G_pt[1])
    s.seg(A, D, "AD", width=1.9)
    s.seg((V[0] - R, V[1]), (V[0] + R, V[1]), "RV", width=1.8)
    s.seg(L, E, "LE", width=1.9)
    s.seg(I_pt, F, "IF", width=2.0)
    s.seg(A, I_pt, "AI", width=1.9)
    s.seg((H[0], V[1] - 99), H, "BH", width=1.8)
    s.seg((V[0], V[1] - R), G_pt, "CG", width=1.9)
    s.seg(D, F, "DF", width=1.9)
    # Oblique prism below
    p3, p4, p8, p6 = (38.0, 478.0), (88.0, 478.0), (140.0, 478.0), (218.0, 478.0)
    s.seg(p3, p6, "3_6", width=2.0)
    s.seg(I_pt, p3, "I3", width=1.9)
    s.seg(H, p4, "H4", width=1.8)
    s.seg(G_pt, p8, "G8", width=1.8)
    s.seg(F, p6, "F6", width=1.9)
    y_mid = 365.0
    ym = intersect_lines(I_pt, p3, (0, y_mid), (300, y_mid))
    zm = intersect_lines(F, p6, (0, y_mid), (300, y_mid))
    s.seg(ym, zm, "y_z", width=1.8)
    s.seg(V, (A[0], V[1] + 85), "V_diag", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} Q {A[0] - 35:.2f} 225 68 385", "curve_A9",
           stroke="var(--geom-highlight, #d97706)", width=1.7)
    s.seg(L, (68, 385), "L9", width=1.5)
    s.seg(L, (86, 405), "LX", width=1.5)
    _pts(s, [(A, "A", "A", -14, -4), (D, "D", "D", 14, -4), (V, "V", "V", 12, 12),
             (L, "L", "L", 0, -12), (E, "E", "E", 14, 4), (G_pt, "G", "G", 0, 14),
             (I_pt, "I", "I", -12, 14), (H, "H", "H", 0, 14), (F, "F", "F", 12, 14),
             (p3, "3", "3", -12, 14), (p4, "4", "4", -10, -10), (p8, "8", "8", 8, -10),
             (p6, "6", "6", 12, 4)])
    s.text((178, 34), "B", "B")
    s.text((254, 38), "C", "C")
    s.text((202, 74), "R", "R")
    s.text((254, 74), "T", "T")
    s.text((132, 152), "R'", "R")
    s.text((158, 156), "M", "M")
    s.text((202, 156), "N", "N")
    s.text((180, 194), "O", "O")
    s.text((186, 224), "Q", "Q")
    s.text((254, 224), "S", "S")
    s.text((198, 248), "P", "P")
    s.text((154, 248), "K", "K")
    s.text((54, 392), "9", "9")
    s.text((74, 422), "X", "X")
    s.text((104, 380), "y", "y")
    s.text((150, 380), "a", "a")
    s.text((202, 380), "7", "7")
    s.text((284, 380), "Z", "Z")
    write_svg("appendix_geometrica/prop_09/0119.g76.svg", s)
    count += 1

    # g77: Tab. X Fig. 77 (Appendix Prop. X: Conjugate Hyperbolas & Asymptotes)
    s = CalibratedSVG(360, 480, "Ceva 1678 Tabula X Fig. 77: Appendix Prop. X Hyperbolas")
    A, C, E, D = (62.0, 48.0), (308.0, 48.0), (308.0, 438.0), (62.0, 438.0)
    G = (185.0, 243.0)
    B, F = (185.0, 178.0), (185.0, 308.0)
    s.seg(A, C, "AC", width=2.0)
    s.seg(C, E, "CE", width=2.0)
    s.seg(E, D, "ED", width=2.0)
    s.seg(D, A, "DA", width=2.0)
    s.seg(A, E, "AE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, D, "CD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg((62, 68), (308, 68), "SL", width=1.6)
    s.seg((62, 178), (308, 178), "VT", width=1.8)
    s.seg((62, 243), (308, 243), "NM", width=1.8)
    s.seg((62, 308), (308, 308), "OR", width=1.8)
    s.seg((62, 420), (308, 420), "HK", width=1.6)
    s.seg((185, 160), (185, 326), "BF", width=1.8)
    s.seg((268, 108), (268, 392), "QP", width=1.7)
    # Upper and lower hyperbola branches: y = cy +/- sqrt(a^2 + k*dx^2)
    a_h = 65.0
    pts_up, pts_dn = [], []
    for i in range(-24, 25):
        dx = i * 5.0
        dy = math.sqrt(a_h * a_h + 1.65 * dx * dx)
        if G[1] - dy >= 62.0:
            pts_up.append((G[0] + dx, G[1] - dy))
            pts_dn.append((G[0] + dx, G[1] + dy))
    s.path("M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_up), "hyp_upper",
           stroke="var(--geom-secondary, #0284c7)", width=2.2)
    s.path("M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_dn), "hyp_lower",
           stroke="var(--geom-secondary, #0284c7)", width=2.2)
    _pts(s, [(A, "A", "A", -14, -4), (C, "C", "C", 14, -4), (D, "D", "D", -14, 14),
             (E, "E", "E", 14, 14), (B, "B", "B", 12, 12), (F, "F", "F", 12, -8)])
    s.pt(G, "G", "G", dx=14, dy=-4, highlight=True)
    for lbl, x, y in [
        ("S", 46, 74), ("L", 322, 74), ("V", 46, 184), ("T", 322, 184),
        ("N", 46, 248), ("M", 322, 248), ("O", 46, 314), ("R", 322, 314),
        ("H", 46, 424), ("K", 322, 424), ("Q", 268, 98), ("R'", 280, 146),
        ("V'", 280, 194), ("+", 280, 238), ("Y", 280, 298), ("Z", 280, 355), ("P", 262, 408),
    ]:
        s.text((x, y), lbl, lbl, size=14)
    write_svg("appendix_geometrica/prop_10/0119.g77.svg", s)
    count += 1

    # g78: Tab. X Fig. 78 (Appendix Prop. XI: Parabola & Cone Frustum)
    s = CalibratedSVG(340, 360, "Ceva 1678 Tabula X Fig. 78: Appendix Prop. XI")
    B, A, C = (165.0, 32.0), (42.0, 322.0), (318.0, 305.0)
    F = (176.0, 162.0)
    S = intersect_lines(B, F, A, C)
    E = intersect_lines(B, A, F, (F[0] - 80, F[1] + 5))
    D = intersect_lines(B, C, F, (F[0] + 80, F[1] - 5))
    N = lerp(B, A, 0.80)
    I_pt = intersect_lines(B, C, N, (N[0] + 200, N[1] - 12))
    K = intersect_lines(B, S, N, I_pt)
    O_pt = intersect_lines(A, C, E, (E[0] + 8, E[1] + 160))
    P_pt = intersect_lines(A, C, D, (D[0] + 10, D[1] + 160))
    L = intersect_lines(E, O_pt, N, I_pt)
    G = intersect_lines(D, P_pt, N, I_pt)
    s.seg(B, A, "BA", width=2.2)
    s.seg(B, C, "BC", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(B, S, "BS", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(E, D, "ED", width=1.9)
    s.seg(N, I_pt, "NI", width=1.9)
    s.seg(E, O_pt, "EO", width=1.8)
    s.seg(D, P_pt, "DP", width=1.8)
    s.path("M 66 320 Q 176 38 296 306", "parabola_RFQ", stroke="var(--geom-secondary, #0284c7)", width=2.2)
    _pts(s, [(B, "B", "B", -14, 0), (A, "A", "A", -8, 18), (C, "C", "C", 14, 4),
             (E, "E", "E", -14, 0), (D, "D", "D", 14, 0), (S, "S", "S", 0, 18),
             (O_pt, "O", "O", 0, 18), (P_pt, "P", "P", 0, 18), (N, "N", "N", -14, 0),
             (I_pt, "I", "I", 14, 0), (K, "K", "K", 12, -10), (L, "L", "L", 12, -8),
             (G, "G", "G", -12, -8)])
    s.pt(F, "F", "F", dx=10, dy=-10, highlight=True)
    for lbl, x, y in [("R", 68, 338), ("Q", 285, 324), ("M", 86, 260), ("H", 268, 268)]:
        s.text((x, y), lbl, lbl, size=14)
    write_svg("appendix_geometrica/prop_11/0121.g78.svg", s)
    count += 1

    # g79: Tab. X Fig. 79 (Appendix Prop. XII: Parabolic Segment & Triangle)
    s = CalibratedSVG(340, 360, "Ceva 1678 Tabula X Fig. 79: Appendix Prop. XII")
    Apex = (162.0, 52.0)
    A, E = (18.0, 326.0), (312.0, 326.0)
    F = (162.0, 326.0)
    C = (162.0, 188.0)
    B = intersect_lines(Apex, A, C, (C[0] - 80, C[1]))
    D = intersect_lines(Apex, E, C, (C[0] + 80, C[1]))
    I_pt = lerp(Apex, A, 0.78)
    N = lerp(Apex, E, 0.78)
    O_pt = intersect_lines(Apex, F, I_pt, N)
    P_pt = intersect_lines(A, D, I_pt, N)
    K = intersect_lines(A, C, I_pt, N)
    s.seg(Apex, A, "ApexA", width=2.2)
    s.seg(Apex, E, "ApexE", width=2.2)
    s.seg(A, E, "AE", width=2.2)
    s.seg(Apex, F, "ApexF", width=1.9)
    s.seg(B, D, "BD", width=1.9)
    s.seg(I_pt, N, "IN", width=1.9)
    s.seg(A, C, "AC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(A, D, "AD", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.path("M 18 326 Q 162 56 306 318", "parabola_ACE", stroke="var(--geom-secondary, #0284c7)", width=2.2)
    _pts(s, [(A, "A", "A", -8, 16), (E, "E", "E", 14, 4), (F, "F", "F", 12, -10),
             (B, "B", "B", -14, -4), (D, "D", "D", 14, -4), (I_pt, "I", "I", -14, 0),
             (N, "N", "N", 14, 0), (K, "K", "K", 4, 16), (P_pt, "P", "P", -10, -10),
             (O_pt, "O", "O", 12, -10)])
    s.pt(C, "C", "C", dx=10, dy=-12, highlight=True)
    s.text((62, 272), "L", "L", size=14)
    s.text((248, 272), "H", "H", size=14)
    write_svg("appendix_geometrica/prop_12/0121.g79.svg", s)
    count += 1

    # g83: Tab. X Fig. 83 (Appendix Prop. XVI: Hyperbolic Solid of Revolution)
    s = CalibratedSVG(460, 260, "Ceva 1678 Tabula X Fig. 83: Appendix Prop. XVI Hyperbolic Solid")
    G, D, C = (95.0, 125.0), (145.0, 125.0), (425.0, 125.0)
    B, A = (95.0, 222.0), (145.0, 222.0)
    E_top, F = (145.0, 28.0), (172.0, 28.0)
    s.seg((95, 28), F, "top_edge", width=2.0)
    s.seg((95, 28), B, "GB", width=2.0)
    s.seg(B, (172, 222), "bot_edge", width=2.0)
    s.seg(E_top, A, "EA", width=2.0)
    s.seg(G, C, "GC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    # Hyperbolic branches x - D_x = k / |y - D_y|
    k_h = 2600.0
    pts_up, pts_dn = [], []
    for i in range(45):
        dy = 97.0 - i * 2.0
        dx = k_h / dy
        if D[0] + dx <= 315.0:
            pts_up.append((D[0] + dx, D[1] - dy))
            pts_dn.append((D[0] + dx, D[1] + dy))
    s.path("M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_up), "hyp_top",
           stroke="var(--geom-secondary, #0284c7)", width=2.1)
    s.path("M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_dn), "hyp_bot",
           stroke="var(--geom-secondary, #0284c7)", width=2.1)
    M = (D[0] + k_h / 48.0, D[1] + 48.0)
    s.seg(D, M, "DM", stroke="var(--geom-highlight, #d97706)", width=1.9)
    _pts(s, [(G, "G", "G", -14, 4), (E_top, "E", "E", -14, 14), (F, "F", "F", 14, 4),
             (B, "B", "B", -14, 4), (A, "A", "A", 0, 18), (M, "M", "M", 12, 12),
             (C, "C", "C", 0, 18)])
    s.pt(D, "D", "D", dx=-12, dy=14, highlight=True)
    write_svg("appendix_geometrica/prop_16/0121.g83.svg", s)
    count += 1

    return count


if __name__ == "__main__":
    n1 = build_liber_primus()
    n2 = build_liber_secundus()
    n3 = build_appendix_geometrica()
    print(f"Built {n1} Liber Primus + {n2} Liber Secundus + {n3} Appendix = {n1 + n2 + n3} SVGs")
