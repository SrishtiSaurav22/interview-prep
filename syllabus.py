from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

WIDTH, HEIGHT = A4

# Color palette
CORAL    = colors.HexColor("#D85A30")
PURPLE   = colors.HexColor("#7F77DD")
BLUE     = colors.HexColor("#378ADD")
TEAL     = colors.HexColor("#1D9E75")
GRAY     = colors.HexColor("#888780")
BG_LIGHT = colors.HexColor("#F7F6F3")
BORDER   = colors.HexColor("#D3D1C7")
TEXT_PRI = colors.HexColor("#1A1A18")
TEXT_SEC = colors.HexColor("#5F5E5A")
WHITE    = colors.white

doc = SimpleDocTemplate(
    "/mnt/user-data/outputs/Interview_Prep_Syllabus_Srishti.pdf",
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=16*mm, bottomMargin=16*mm
)

styles = getSampleStyleSheet()

def style(name, **kw):
    return ParagraphStyle(name, **kw)

S = {
    "title": style("title", fontName="Helvetica-Bold", fontSize=20, textColor=TEXT_PRI, spaceAfter=2),
    "subtitle": style("subtitle", fontName="Helvetica", fontSize=11, textColor=TEXT_SEC, spaceAfter=8),
    "week_title": style("week_title", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE, leading=16),
    "week_label": style("week_label", fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#E0DFF8"), leading=14),
    "topic_name": style("topic_name", fontName="Helvetica-Bold", fontSize=10, textColor=TEXT_PRI, spaceAfter=2),
    "topic_detail": style("topic_detail", fontName="Helvetica", fontSize=9, textColor=TEXT_SEC, leading=14),
    "time_note": style("time_note", fontName="Helvetica-Oblique", fontSize=8.5, textColor=colors.HexColor("#9E9D97")),
    "note_title": style("note_title", fontName="Helvetica-Bold", fontSize=9, textColor=TEXT_SEC, spaceAfter=4),
    "note_item": style("note_item", fontName="Helvetica", fontSize=9, textColor=TEXT_SEC, leading=14),
    "legend_item": style("legend_item", fontName="Helvetica", fontSize=9, textColor=TEXT_SEC),
    "section_label": style("section_label", fontName="Helvetica-Bold", fontSize=8, textColor=TEXT_SEC),
}

USABLE = WIDTH - 36*mm

# Weeks data
weeks = [
    {
        "range": "Weeks 1–2",
        "title": "Linux, Bash & Git — foundations",
        "tag": "shakiest",
        "color": CORAL,
        "topics": [
            ("Linux essentials",
             "File system hierarchy, permissions (chmod/chown), process management (ps, kill, top), cron jobs, users & groups",
             "~3 sessions × 40 min"),
            ("Bash scripting",
             "Variables, conditionals, loops, functions, piping, redirects, writing automation scripts. Practice: write 5 real scripts for tasks you'd do anyway",
             "~3 sessions × 40 min"),
            ("Git internals for interviews",
             "Rebase vs merge, cherry-pick, stash, reset vs revert, conflict resolution, branching strategies (GitFlow basics)",
             "~2 sessions × 40 min"),
        ]
    },
    {
        "range": "Weeks 3–4",
        "title": "Docker & CI/CD",
        "tag": "shakiest",
        "color": CORAL,
        "topics": [
            ("Docker fundamentals",
             "Images vs containers, Dockerfile writing, multi-stage builds, volumes, networking (bridge/host), docker-compose. Practice: containerise Biblo's backend",
             "~4 sessions × 40 min"),
            ("GitHub Actions (CI/CD)",
             "Workflow YAML syntax, triggers, jobs/steps, secrets, matrix builds, caching. Practice: add a real pipeline to Biblo — lint + test + build on push",
             "~3 sessions × 40 min — this also improves your Biblo project"),
        ]
    },
    {
        "range": "Week 5",
        "title": "Databases — SQL & NoSQL",
        "tag": "backend",
        "color": PURPLE,
        "topics": [
            ("PostgreSQL / MySQL (interview depth)",
             "Joins, indexing strategy, EXPLAIN plans, transactions & ACID, normalization, window functions — you're already using this in Biblo so focus on the why, not the how",
             "~3 sessions × 40 min"),
            ("MongoDB",
             "Document model, aggregation pipeline, indexing, schema design trade-offs vs relational. Common interview: when would you pick MongoDB over Postgres?",
             "~2 sessions × 40 min"),
        ]
    },
    {
        "range": "Week 6",
        "title": "Backend — FastAPI, REST & JWT",
        "tag": "Biblo-reinforced",
        "color": TEAL,
        "topics": [
            ("FastAPI & Pydantic",
             "Dependency injection, async vs sync handlers, request validation, error handling, background tasks, OpenAPI generation — revisit Biblo's backend with interview eyes",
             "~3 sessions × 40 min"),
            ("REST principles & JWT",
             "Idempotency, HTTP verbs, status codes, versioning. JWT: structure, signing, expiry, refresh token pattern, security pitfalls",
             "~2 sessions × 40 min"),
        ]
    },
    {
        "range": "Week 7",
        "title": "AWS / Cloud — interview framing",
        "tag": "your real strength",
        "color": BLUE,
        "topics": [
            ("Storytelling your AWS experience",
             "You have 350+ resolved cases — translate each service (OpenSearch, MSK, Kinesis, Kendra) into a 2-min STAR story. Interviewers don't need theory from you; they need to hear you reason about systems",
             "~2 sessions × 40 min — write, don't just think"),
            ("System design with AWS primitives",
             "Practice designing 2–3 systems using services you've touched: a real-time data pipeline, a search system, a notification system. Know the trade-offs, not just the services",
             "~3 sessions × 40 min"),
        ]
    },
    {
        "range": "Week 8",
        "title": "Full review + mock interviews",
        "tag": "consolidation",
        "color": GRAY,
        "topics": [
            ("Weak spot revisit",
             "Spend the first half of the week on whichever of weeks 1–7 felt least solid. Don't try to cover everything — plug the single biggest gap",
             "~3 sessions × 40 min"),
            ("Mock interview practice",
             "2–3 timed mock sessions (Pramp, Interviewing.io, or with a friend). One DSA round, one system design round, one behavioural round per session",
             "~2–3 sessions × 40 min"),
        ]
    },
]

not_on_list = [
    ("Flutter", "Biblo is your live project. Keep building. That's better than any tutorial."),
    ("C/C++", "Your DSA track covers this. No separate slot needed."),
    ("Dart", "Comes with Flutter. Passive reinforcement is enough."),
    ("Python", "You're writing it in Biblo's backend. Already covered."),
    ("Canva, JSON, YAML", "Not interview topics. Skip entirely."),
]

story = []

# Title block
story.append(Paragraph("Interview Prep Syllabus", S["title"]))
story.append(Paragraph("Srishti Saurav · 8-week plan · 30–45 min/day · targeting Backend, Full-stack, Cloud & Flutter roles", S["subtitle"]))
story.append(HRFlowable(width=USABLE, thickness=0.5, color=BORDER, spaceAfter=10))

# Legend
legend_data = [
    [colors.HexColor("#D85A30"), "Shakiest areas (priority)"],
    [colors.HexColor("#7F77DD"), "Backend / databases"],
    [colors.HexColor("#378ADD"), "AWS / cloud framing"],
    [colors.HexColor("#1D9E75"), "Biblo-reinforced"],
    [colors.HexColor("#888780"), "Review / mock"],
]

legend_cells = []
for col, label in legend_data:
    cell = Table(
        [[Paragraph(f"  {label}", S["legend_item"])]],
        colWidths=[90]
    )
    cell.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LINEAFTER" if True else "x", (0,0),(0,0), 0, col), # placeholder
    ]))
    legend_cells.append(cell)

# Build legend as a simple table with colored dots
leg_row = []
for col, label in legend_data:
    dot_table = Table([[""]], colWidths=[8], rowHeights=[8])
    dot_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), col),
        ("ROUNDEDCORNERS", [4]),
    ]))
    inner = Table(
        [[dot_table, Paragraph(label, S["legend_item"])]],
        colWidths=[12, 78]
    )
    inner.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),2),
        ("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    leg_row.append(inner)

legend_table = Table([leg_row], colWidths=[90]*5)
legend_table.setStyle(TableStyle([
    ("LEFTPADDING",(0,0),(-1,-1),0),
    ("RIGHTPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),0),
    ("BOTTOMPADDING",(0,0),(-1,-1),0),
]))
story.append(legend_table)
story.append(Spacer(1, 12))

# Week blocks
for week in weeks:
    color = week["color"]

    # Header row
    header_inner = Table(
        [[Paragraph(week["range"], S["week_label"]), Paragraph(week["title"], S["week_title"]), Paragraph(week["tag"], S["week_label"])]],
        colWidths=[50, USABLE - 110, 60]
    )
    header_inner.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
        ("ALIGN",(2,0),(2,0),"RIGHT"),
    ]))

    header_table = Table([[header_inner]], colWidths=[USABLE])
    header_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), color),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
        ("ROUNDEDCORNERS",[6,6,0,0]),
    ]))

    # Topics
    topic_rows = []
    for i, (name, detail, time) in enumerate(week["topics"]):
        content_cell = [
            Paragraph(name, S["topic_name"]),
            Paragraph(detail, S["topic_detail"]),
            Paragraph(time, S["time_note"]),
        ]

        dot_table = Table([[""]], colWidths=[8], rowHeights=[8])
        dot_table.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1), color),
            ("ROUNDEDCORNERS",[4]),
        ]))

        row_table = Table(
            [[dot_table, content_cell]],
            colWidths=[14, USABLE - 28]
        )
        row_table.setStyle(TableStyle([
            ("VALIGN",(0,0),(0,0),"TOP"),
            ("TOPPADDING",(0,0),(0,0),3),
            ("LEFTPADDING",(0,0),(-1,-1),0),
            ("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,1),(0,1),0),
            ("BOTTOMPADDING",(0,0),(-1,-1),0),
        ]))
        topic_rows.append([row_table])

        if i < len(week["topics"]) - 1:
            topic_rows.append([HRFlowable(width=USABLE-20, thickness=0.5, color=BORDER)])

    body_table = Table(topic_rows, colWidths=[USABLE])
    body_table.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
        ("BACKGROUND",(0,0),(-1,-1), WHITE),
        ("BOX",(0,0),(-1,-1),0.5, BORDER),
        ("ROUNDEDCORNERS",[0,0,6,6]),
    ]))

    outer = Table([[header_table],[body_table]], colWidths=[USABLE])
    outer.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(outer)
    story.append(Spacer(1, 10))

# Not on list note
story.append(HRFlowable(width=USABLE, thickness=0.5, color=BORDER, spaceBefore=4, spaceAfter=8))
story.append(Paragraph("Things NOT on this list (and why)", S["note_title"]))

note_rows = []
for skill, reason in not_on_list:
    note_rows.append([
        Paragraph(f"<b>{skill}</b>", S["note_item"]),
        Paragraph(reason, S["note_item"]),
    ])

note_table = Table(note_rows, colWidths=[90, USABLE-90])
note_table.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), BG_LIGHT),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("RIGHTPADDING",(0,0),(-1,-1),8),
    ("TOPPADDING",(0,0),(-1,-1),5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("BOX",(0,0),(-1,-1),0.5,BORDER),
    ("LINEBELOW",(0,0),(-1,-2),0.5,BORDER),
]))
story.append(note_table)

doc.build(story)
print("Done.")
