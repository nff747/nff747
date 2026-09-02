import json
import subprocess
from datetime import datetime

# Fetch live contribution calendar from GitHub GraphQL API
query = '''
query {
  user(login: "nff747") {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
            color
          }
        }
      }
    }
  }
}
'''

cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
data = json.loads(res.stdout)
calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
total_contributions = calendar["totalContributions"]
weeks = calendar["weeks"]

# Colors matching dark cyberpunk theme
BG_COLOR = "#05080D"
BORDER_COLOR = "#FF005530"
EMPTY_CELL_BG = "#0d1117"
EMPTY_CELL_BORDER = "#1f242c"
TEXT_COLOR = "#c9d1d9"
LABEL_COLOR = "#7d8590"

# Level colors (Crimson scale)
LEVEL_COLORS = [
    EMPTY_CELL_BG,      # 0
    "#400015",          # 1-2
    "#80002A",          # 3-5
    "#C00040",          # 6-9
    "#FF0055"           # 10+
]

def get_color(count):
    if count == 0:
        return EMPTY_CELL_BG
    elif count <= 2:
        return LEVEL_COLORS[1]
    elif count <= 5:
        return LEVEL_COLORS[2]
    elif count <= 9:
        return LEVEL_COLORS[3]
    else:
        return LEVEL_COLORS[4]

cell_size = 10
cell_gap = 3
cell_radius = 2
start_x = 40
start_y = 45

num_weeks = len(weeks)
width = start_x + (num_weeks * (cell_size + cell_gap)) + 30
height = 175

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background-color: {BG_COLOR}; border: 1px solid {BORDER_COLOR}; border-radius: 8px;">')
svg.append('''
<style>
  .title { font: 600 14px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; fill: #c9d1d9; }
  .label { font: 400 10px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; fill: #7d8590; }
  .legend-text { font: 400 11px -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; fill: #7d8590; }
  .cell { rx: 2px; ry: 2px; }
  .cell:hover { stroke: #FF0055; stroke-width: 1.5px; }
</style>
''')

# Header Title
svg.append(f'<text x="20" y="24" class="title">{total_contributions} contributions in the last year</text>')

# Month labels
months = []
last_month = None
for w_idx, week in enumerate(weeks):
    first_day = week["contributionDays"][0]["date"]
    dt = datetime.strptime(first_day, "%Y-%m-%d")
    m_name = dt.strftime("%b")
    if m_name != last_month:
        months.append((w_idx, m_name))
        last_month = m_name

for w_idx, m_name in months:
    mx = start_x + w_idx * (cell_size + cell_gap)
    svg.append(f'<text x="{mx}" y="40" class="label">{m_name}</text>')

# Day of week labels (Mon, Wed, Fri)
day_labels = [(1, "Mon"), (3, "Wed"), (5, "Fri")]
for d_idx, d_name in day_labels:
    my = start_y + d_idx * (cell_size + cell_gap) + 8
    svg.append(f'<text x="15" y="{my}" class="label">{d_name}</text>')

# Render cells
for w_idx, week in enumerate(weeks):
    for d_idx, day in enumerate(week["contributionDays"]):
        cx = start_x + w_idx * (cell_size + cell_gap)
        cy = start_y + d_idx * (cell_size + cell_gap)
        count = day["contributionCount"]
        color = get_color(count)
        stroke = EMPTY_CELL_BORDER if count == 0 else "#FF005540"
        
        # Glow effect for top tier
        glow = ' filter="drop-shadow(0 0 4px #FF0055)"' if count >= 10 else ''
        svg.append(f'<rect x="{cx}" y="{cy}" width="{cell_size}" height="{cell_size}" fill="{color}" stroke="{stroke}" stroke-width="1" class="cell"{glow}><title>{count} contributions on {day["date"]}</title></rect>')

# Legend at bottom right
legend_y = height - 16
legend_x = width - 150
svg.append(f'<text x="{legend_x - 30}" y="{legend_y + 8}" class="legend-text">Less</text>')
for i, col in enumerate(LEVEL_COLORS):
    lx = legend_x + i * (cell_size + 3)
    strk = EMPTY_CELL_BORDER if i == 0 else "#FF005540"
    svg.append(f'<rect x="{lx}" y="{legend_y}" width="{cell_size}" height="{cell_size}" fill="{col}" stroke="{strk}" stroke-width="1" class="cell"/>')
svg.append(f'<text x="{legend_x + 5 * (cell_size + 3) + 4}" y="{legend_y + 8}" class="legend-text">More</text>')

svg.append('</svg>')

with open("assets/contribution_map.svg", "w") as f:
    f.write("\n".join(svg))

print(f"Generated assets/contribution_map.svg successfully! Total: {total_contributions}")
