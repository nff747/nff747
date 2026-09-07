#!/usr/bin/env python3
"""
Dynamic Real-Time Contribution Heatmap Vector Generator for nff747
Queries the live GitHub GraphQL API for the exact contribution calendar
and renders a pixel-perfect, dark cyberpunk neon crimson SVG.
"""

import subprocess
import json
import sys
from datetime import datetime

USERNAME = "nff747"

query = f'''
query {{
  user(login: "{USERNAME}") {{
    contributionsCollection {{
      contributionCalendar {{
        totalContributions
        weeks {{
          contributionDays {{
            contributionCount
            date
            weekday
          }}
        }}
      }}
    }}
  }}
}}
'''

try:
    res = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)
    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
except Exception as e:
    print(f"Error fetching live contribution data: {e}", file=sys.stderr)
    sys.exit(1)

total_contributions = calendar["totalContributions"]
weeks = calendar["weeks"]

CELL_SIZE = 10
CELL_GAP = 3
CELL_RADIUS = 2
START_X = 42
START_Y = 46
NUM_WEEKS = len(weeks)
NUM_DAYS = 7

WIDTH = START_X + (NUM_WEEKS * (CELL_SIZE + CELL_GAP)) + 30
HEIGHT = 175

# Color Palette matching Dark Cyberpunk Crimson Red
BG_COLOR = "#05080D"
CARD_BORDER = "#FF005530"
EMPTY_CELL_FILL = "#161b22"
EMPTY_CELL_STROKE = "#21262d"

# Crimson Level Colors
LEVEL_COLORS = {
    0: (EMPTY_CELL_FILL, EMPTY_CELL_STROKE),
    1: ("#400015", "#700025"),
    2: ("#80002A", "#b0003b"),
    3: ("#C00040", "#e6004c"),
    4: ("#FF0055", "#ff4080")
}

def get_level(count):
    if count == 0:
        return 0
    elif count <= 2:
        return 1
    elif count <= 5:
        return 2
    elif count <= 9:
        return 3
    else:
        return 4

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="{HEIGHT}" style="background-color: {BG_COLOR}; border: 1px solid {CARD_BORDER}; border-radius: 8px;">')
svg.append('''
<style>
  .title { font: 600 14px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; fill: #f0f6fc; }
  .label { font: 400 10px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; fill: #8b949e; }
  .legend-text { font: 400 11px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; fill: #8b949e; }
  .cell { rx: 2px; ry: 2px; transition: all 0.2s ease; }
  .cell:hover { stroke: #FF0055; stroke-width: 1.5px; }
  .glow-red { filter: drop-shadow(0 0 4px #FF0055); }
</style>
''')

# Header Title
svg.append(f'<text x="20" y="25" class="title">{total_contributions} contributions in the last year</text>')

# Month labels
last_month = None
last_col = -10
for w_idx, week in enumerate(weeks):
    if not week["contributionDays"]:
        continue
    dt = datetime.strptime(week["contributionDays"][0]["date"], "%Y-%m-%d")
    m_name = dt.strftime("%b")
    if m_name != last_month:
        if w_idx - last_col >= 3 and (len(weeks) - w_idx) >= 2:
            mx = START_X + w_idx * (CELL_SIZE + CELL_GAP)
            svg.append(f'<text x="{mx}" y="40" class="label">{m_name}</text>')
            last_col = w_idx
        last_month = m_name

# Day of week labels (Mon, Wed, Fri)
day_labels = [(1, "Mon"), (3, "Wed"), (5, "Fri")]
for d_idx, d_name in day_labels:
    my = START_Y + d_idx * (CELL_SIZE + CELL_GAP) + 8
    svg.append(f'<text x="15" y="{my}" class="label">{d_name}</text>')

# Render all 53 weeks x 7 days
for w_idx, week in enumerate(weeks):
    for day in week["contributionDays"]:
        d_idx = day["weekday"]
        cx = START_X + w_idx * (CELL_SIZE + CELL_GAP)
        cy = START_Y + d_idx * (CELL_SIZE + CELL_GAP)
        count = day["contributionCount"]
        date = day["date"]
        level = get_level(count)
        fill, stroke = LEVEL_COLORS[level]
        glow_class = ' class="cell glow-red"' if level >= 3 else ' class="cell"'
        title_text = f"{count} contribution{'s' if count != 1 else ''} on {date}" if count > 0 else f"No contributions on {date}"
        svg.append(f'<rect x="{cx}" y="{cy}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill}" stroke="{stroke}" stroke-width="1"{glow_class}><title>{title_text}</title></rect>')

# Legend at bottom right
legend_y = HEIGHT - 18
legend_x = WIDTH - 165
svg.append(f'<text x="{legend_x - 32}" y="{legend_y + 8}" class="legend-text">Less</text>')
for lvl in range(5):
    lx = legend_x + lvl * (CELL_SIZE + 3)
    fill, stroke = LEVEL_COLORS[lvl]
    svg.append(f'<rect x="{lx}" y="{legend_y}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill}" stroke="{stroke}" stroke-width="1" class="cell"/>')
svg.append(f'<text x="{legend_x + 5 * (CELL_SIZE + 3) + 6}" y="{legend_y + 8}" class="legend-text">More</text>')

svg.append('</svg>')

svg_content = "\n".join(svg) + "\n"

with open("assets/contribution_map.svg", "w") as f:
    f.write(svg_content)

print(f"Successfully generated assets/contribution_map.svg with {total_contributions} real-time contributions!")
