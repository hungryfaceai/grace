#!/usr/bin/env python3
"""Generate chapter 01 comic preview assets as SVG (text files, PR-friendly)."""
from __future__ import annotations

from pathlib import Path

OUT_DIR = Path(__file__).parent / "images" / "chapter_01"

PAGE_NOTES = {
    1: "Stockholm sous la neige, Jacques perdu, ambiance froide.",
    2: "Entrée du club, foule lente, lumière tamisée.",
    3: "Solitude de Jacques et fatigue existentielle.",
    4: "Découverte du couple au centre de la pièce.",
    5: "Trouble intime: confiance, abandon, désir.",
    6: "Jalousie froide et sentiment d'exil intérieur.",
    7: "Le mouchoir comme liturgie minuscule.",
    8: "Sortie dans la neige, téléphone comme dernière lueur.",
}

PALETTES = {
    "snow": ("#0e1726", "#2e425f"),
    "club": ("#2d1328", "#12091d"),
    "neutral": ("#1f2636", "#0d1118"),
}


def page_palette(page: int) -> tuple[str, str]:
    if page in (1, 8):
        return PALETTES["snow"]
    if page in (2, 4, 5, 6, 7):
        return PALETTES["club"]
    return PALETTES["neutral"]


def svg_page(page: int) -> str:
    top, bottom = page_palette(page)
    note = PAGE_NOTES[page]
    title = f"Chapitre 01 — Page {page:02d}"

    # 6-panel grid with recurring silhouettes for visual consistency.
    return f"""<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='1800' viewBox='0 0 1200 1800'>
  <defs>
    <linearGradient id='bg' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0%' stop-color='{top}'/>
      <stop offset='100%' stop-color='{bottom}'/>
    </linearGradient>
    <style>
      .panel {{ fill: rgba(10,10,16,0.45); stroke: #e0e0e0; stroke-width: 3; }}
      .caption {{ font-family: Inter, Arial, sans-serif; fill: #f2f2f2; }}
      .small {{ font-size: 28px; }}
      .tiny {{ font-size: 22px; opacity: 0.95; }}
      .jacques-coat {{ fill: #1c232d; }}
      .jacques-skin {{ fill: #e7d1bb; }}
      .accent {{ fill: #9cc3ff; opacity: 0.8; }}
    </style>
  </defs>

  <rect x='0' y='0' width='1200' height='1800' fill='url(#bg)'/>

  <g transform='translate(40,40)'>
    <rect class='panel' x='0' y='0' width='1120' height='1720' rx='8'/>
    <rect class='panel' x='20' y='20' width='520' height='540'/>
    <rect class='panel' x='580' y='20' width='520' height='540'/>
    <rect class='panel' x='20' y='590' width='520' height='540'/>
    <rect class='panel' x='580' y='590' width='520' height='540'/>
    <rect class='panel' x='20' y='1160' width='520' height='540'/>
    <rect class='panel' x='580' y='1160' width='520' height='540'/>
  </g>

  <g>
    <circle class='jacques-skin' cx='210' cy='250' r='26'/>
    <rect class='jacques-coat' x='178' y='278' width='64' height='140' rx='8'/>

    <circle class='jacques-skin' cx='770' cy='250' r='26'/>
    <rect class='jacques-coat' x='738' y='278' width='64' height='140' rx='8'/>

    <circle class='jacques-skin' cx='210' cy='820' r='26'/>
    <rect class='jacques-coat' x='178' y='848' width='64' height='140' rx='8'/>

    <circle class='jacques-skin' cx='770' cy='820' r='26'/>
    <rect class='jacques-coat' x='738' y='848' width='64' height='140' rx='8'/>

    <circle class='jacques-skin' cx='210' cy='1390' r='26'/>
    <rect class='jacques-coat' x='178' y='1418' width='64' height='140' rx='8'/>

    <circle class='jacques-skin' cx='770' cy='1390' r='26'/>
    <rect class='jacques-coat' x='738' y='1418' width='64' height='140' rx='8'/>

    <rect class='accent' x='548' y='164' width='104' height='68' rx='10'/>
  </g>

  <text class='caption small' x='60' y='70'>{title}</text>
  <foreignObject x='60' y='1710' width='1080' height='70'>
    <div xmlns='http://www.w3.org/1999/xhtml' style='color:#f2f2f2;font: 22px Inter, Arial, sans-serif;'>
      {note}
    </div>
  </foreignObject>
</svg>
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i in range(1, 9):
        target = OUT_DIR / f"page_{i:02d}.svg"
        target.write_text(svg_page(i), encoding="utf-8")
    print(f"Generated 8 SVG pages in {OUT_DIR}")


if __name__ == "__main__":
    main()
