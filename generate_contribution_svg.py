# Total contributions matching user profile exactly
TOTAL_CONTRIBUTIONS = 54

# Dimensions matching standard GitHub contribution card
CELL_SIZE = 10
CELL_GAP = 3
CELL_RADIUS = 2
START_X = 42
START_Y = 46

NUM_WEEKS = 53
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

# The exact 7 contribution days from the user screenshot (Week, Row):
ACTIVE_DAYS = {
    (3, 1): (2, "1 contribution in Sep"),
    (7, 6): (2, "1 contribution in Nov"),
    (34, 6): (1, "1 contribution in May"),
    (40, 3): (2, "1 contribution in Jun"),
    (42, 3): (3, "2 contributions in Jul"),
    (52, 2): (4, "13 contributions on Sep 1"),
    (52, 3): (4, "35 contributions on Sep 2")
}

# Month label positions
MONTHS = [
    (2, "Sep"),
    (6, "Oct"),
    (11, "Nov"),
    (15, "Dec"),
    (19, "Jan"),
    (24, "Feb"),
    (28, "Mar"),
    (32, "Apr"),
    (37, "May"),
    (41, "Jun"),
    (45, "Jul"),
    (50, "Aug")
]

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
svg.append(f'<text x="20" y="25" class="title">{TOTAL_CONTRIBUTIONS} contributions in the last year</text>')

# Month labels
for w_idx, m_name in MONTHS:
    mx = START_X + w_idx * (CELL_SIZE + CELL_GAP)
    svg.append(f'<text x="{mx}" y="40" class="label">{m_name}</text>')

# Day of week labels (Mon, Wed, Fri)
day_labels = [(1, "Mon"), (3, "Wed"), (5, "Fri")]
for d_idx, d_name in day_labels:
    my = START_Y + d_idx * (CELL_SIZE + CELL_GAP) + 8
    svg.append(f'<text x="15" y="{my}" class="label">{d_name}</text>')

# Render all 53 weeks x 7 days
for w in range(NUM_WEEKS):
    for d in range(NUM_DAYS):
        if w == 52 and d > 3:
            continue
            
        cx = START_X + w * (CELL_SIZE + CELL_GAP)
        cy = START_Y + d * (CELL_SIZE + CELL_GAP)
        
        if (w, d) in ACTIVE_DAYS:
            level, desc = ACTIVE_DAYS[(w, d)]
            fill, stroke = LEVEL_COLORS[level]
            glow_class = ' class="cell glow-red"' if level >= 3 else ' class="cell"'
            svg.append(f'<rect x="{cx}" y="{cy}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill}" stroke="{stroke}" stroke-width="1"{glow_class}><title>{desc}</title></rect>')
        else:
            fill, stroke = LEVEL_COLORS[0]
            svg.append(f'<rect x="{cx}" y="{cy}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill}" stroke="{stroke}" stroke-width="1" class="cell"><title>No contributions</title></rect>')

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

with open("assets/contribution_map.svg", "w") as f:
    f.write("\n".join(svg))

print("Successfully switched to glowing Cyberpunk Crimson Red while keeping all 54 contributions!")
