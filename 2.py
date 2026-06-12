import streamlit as st

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    
    page_title="SHUBHAM KUMAR | Portfolio" ,
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    background: #F0F4FF;
    color: #1E2A4A;
}

[data-testid="stAppViewContainer"] > .main > div {
    padding: 0 !important;
    max-width: 100% !important;
}

[data-testid="block-container"] {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Hero ── */
.hero {
    background: linear-gradient(15deg, #52796f 0%, #bcb8b1 50%, #aed9e0 100%);
    padding: 75px 40px 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 280px; height: 280px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -80px; left: -40px;
    width: 220px; height: 220px;
    background: rgba(255,255,255,0.06);
    border-radius: 50%;
}
.hero-avatar {
    width: 110px; height: 110px;
    border-radius: 50%;
    background: rgba(255,255,255,0.2);
    border: 4px solid rgba(255,255,255,0.6);
    display: flex; align-items: center; justify-content: center;
    font-size: 44px;
    margin: 0 auto 20px;
    backdrop-filter: blur(8px);
}
.hero h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(28px, 5vw, 48px);
    font-weight: 800;
    color: #000;
    letter-spacing: -0.5px;
    margin-bottom: 10px;
}
.hero .tagline {
    font-size: clamp(13px, 2vw, 17px);
    color: rgba(255,255,255,0.88);
    font-weight: 400;
    max-width: 600px;
    margin: 0 auto 28px;
    line-height: 1.6;
}
.hero-links {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
    margin-bottom: 12px;
}
.hero-link {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(255,255,255,0.18);
    color: #fff !important;
    text-decoration: none !important;
    padding: 9px 20px;
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    border: 1.5px solid rgba(255,255,255,0.35);
    backdrop-filter: blur(8px);
    transition: all 0.2s;
}
.hero-link:hover {
    background: rgba(255,255,255,0.30);
    transform: translateY(-2px);
}
.hero-contact {
    color: rgba(255,255,255,0.75);
    font-size: 13px;
    margin-top: 6px;
}

/* ── Wrapper ── */
.page-wrapper {
    max-width: 1100px;
    margin: 0 auto;
    padding: 40px 20px 60px;
}

/* ── Section Title ── */
.section-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: #1E2A4A;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title::after {
    content: '';
    flex: 1;
    height: 2px;
    background: linear-gradient(90deg, #4F8EF7, transparent);
    border-radius: 2px;
}

/* ── Summary Card ── */
.summary-card {
    background: linear-gradient(135deg, #EEF4FF 0%, #F3EEFF 100%);
    border-left: 5px solid #4F8EF7;
    border-radius: 16px;
    padding: 26px 30px;
    font-size: 15px;
    line-height: 1.8;
    color: #2D3A5E;
    margin-bottom: 36px;
    box-shadow: 0 4px 20px rgba(79,142,247,0.10);
}

/* ── Experience Card ── */
.exp-card {
    background: #fff;
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 18px;
    box-shadow: 0 2px 16px rgba(30,42,74,0.07);
    border-top: 4px solid transparent;
    transition: transform 0.2s, box-shadow 0.2s;
    position: relative;
}
.exp-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(79,142,247,0.15);
}
.exp-card.gov    { border-top-color: #4F8EF7; }
.exp-card.dev    { border-top-color: #7C5CFC; }
.exp-card.data   { border-top-color: #10B981; }
.exp-card.brand  { border-top-color: #F59E0B; }
.exp-card.vol    { border-top-color: #EC4899; }

.exp-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 6px;
}
.exp-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #1E2A4A;
}
.exp-company {
    font-size: 14px;
    font-weight: 600;
    color: #4F8EF7;
    margin-bottom: 4px;
}
.exp-date {
    font-size: 12px;
    color: #7C8DB5;
    background: #F0F4FF;
    padding: 4px 12px;
    border-radius: 20px;
    white-space: nowrap;
    font-weight: 500;
}
.exp-bullets {
    margin-top: 12px;
    padding-left: 0;
    list-style: none;
}
.exp-bullets li {
    font-size: 14px;
    color: #3D4E70;
    line-height: 1.7;
    padding: 3px 0 3px 20px;
    position: relative;
}
.exp-bullets li::before {
    content: '›';
    position: absolute;
    left: 5px;
    color: #4F8EF7;
    font-weight: 700;
    font-size: 16px;
}

/* ── Project Card ── */
.proj-card {
    background: #fff;
    border-radius: 16px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 2px 16px rgba(30,42,74,0.07);
    border-left: 5px solid #7C5CFC;
    transition: transform 0.2s;
}
.proj-card:hover { transform: translateY(-3px); }
.proj-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #1E2A4A;
    margin-bottom: 4px;
}
.proj-stack {
    font-size: 12px;
    color: #7C5CFC;
    font-weight: 600;
    margin-bottom: 10px;
}
.proj-desc {
    font-size: 14px;
    color: #3D4E70;
    line-height: 1.7;
}

/* ── Skills ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 18px;
    margin-bottom: 36px;
}
.skill-category {
    background: #fff;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 2px 16px rgba(30,42,74,0.07);
}
.skill-cat-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 14px;
    padding-bottom: 8px;
    border-bottom: 2px solid #F0F4FF;
}
.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.skill-tag {
    padding: 5px 13px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 500;
}

/* ── Publication Card ── */
.pub-card {
    background: linear-gradient(135deg, #FFF7ED 0%, #FFF0FB 100%);
    border-left: 5px solid #F59E0B;
    border-radius: 16px;
    padding: 22px 28px;
    margin-bottom: 18px;
    box-shadow: 0 2px 16px rgba(245,158,11,0.10);
}
.pub-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #1E2A4A;
    margin-bottom: 6px;
}
.pub-venue {
    font-size: 13px;
    color: #92400E;
    font-weight: 500;
}

/* ── Cert & Achievement Cards ── */
.cert-card {
    background: #fff;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 12px rgba(30,42,74,0.07);
    display: flex;
    align-items: center;
    gap: 14px;
    transition: transform 0.2s;
}
.cert-card:hover { transform: translateX(4px); }
.cert-icon {
    font-size: 24px;
    flex-shrink: 0;
}
.cert-text { font-size: 14px; font-weight: 500; color: #2D3A5E; }
.cert-link {
    font-size: 12px;
    color: #4F8EF7 !important;
    text-decoration: none !important;
    font-weight: 600;
}
.cert-link:hover { text-decoration: underline !important; }

/* ── Achievement Badges ── */
.ach-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 16px;
    margin-bottom: 36px;
}
.ach-card {
    background: #fff;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 2px 14px rgba(30,42,74,0.07);
    display: flex;
    gap: 14px;
    align-items: flex-start;
    transition: transform 0.2s;
}
.ach-card:hover { transform: translateY(-3px); }
.ach-icon { font-size: 28px; flex-shrink: 0; }
.ach-title { font-size: 14px; font-weight: 600; color: #1E2A4A; margin-bottom: 2px; }
.ach-sub { font-size: 13px; color: #7C8DB5; }

/* ── Interests ── */
.interests-row {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 36px;
}
.interest-chip {
    background: #fff;
    border-radius: 50px;
    padding: 12px 22px;
    font-size: 14px;
    font-weight: 500;
    color: #2D3A5E;
    box-shadow: 0 2px 12px rgba(30,42,74,0.07);
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ── Education Card ── */
.edu-card {
    background: linear-gradient(135deg, #EEF4FF 0%, #F0FDF4 100%);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 18px;
    box-shadow: 0 2px 16px rgba(79,142,247,0.10);
}
.edu-school {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: #1E2A4A;
    margin-bottom: 4px;
}
.edu-degree {
    font-size: 14px;
    color: #4F8EF7;
    font-weight: 600;
    margin-bottom: 6px;
}
.edu-meta {
    font-size: 13px;
    color: #7C8DB5;
    font-weight: 500;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 32px 20px;
    color: #7C8DB5;
    font-size: 13px;
    background: #fff;
    border-top: 1px solid #E8EEFF;
    margin-top: 20px;
}

/* ── Responsive ── */
@media (max-width: 600px) {
    .hero { padding: 50px 20px 45px; }
    .page-wrapper { padding: 24px 14px 48px; }
    .exp-card, .proj-card { padding: 18px 18px; }
    .skills-grid { grid-template-columns: 1fr; }
    .ach-grid { grid-template-columns: 1fr; }
    .exp-header { flex-direction: column; }
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
.stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# HERO SECTION
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div class="hero-avatar">👨‍💻</div>
    <h1>SHUBHAM KUMAR</h1>
    <p class="tagline">
        Computer Engineering Graduate · Research & Data Analysis Associate at NCGG, Govt. of India ·
        Python · SQL · Policy Research · Web Development
    </p>
    <div class="hero-links">
        <a class="hero-link" href="https://www.linkedin.com/in/shubham-kumar-rawat-b69b1a19b/" target="_blank">🔗 LinkedIn</a>
        <a class="hero-link" href="https://github.com/CodingGeek2024" target="_blank">🐙 GitHub</a>
        <a class="hero-link" href="https://leetcode.com/u/CodingGeek2024/" target="_blank">⚡ LeetCode</a>
    </div>
    <p class="hero-contact">📧 Shubhamrawatk203@gmail.com &nbsp;|&nbsp; 📞 +91-8810325212</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)

# ── Professional Summary ──────────────────────────────────────────────────────
st.markdown('<div class="section-title">🧑‍💼 About Me</div>', unsafe_allow_html=True)
st.markdown("""
<div class="summary-card">
    Computer Engineering graduate from <strong>Delhi Technological University (DTU)</strong> with experience in
    government programme support, policy research, data analysis, and web development.
    Currently working with the <strong>National Centre for Good Governance (NCGG), Government of India</strong>,
    contributing to research, monitoring & evaluation, stakeholder coordination, and programme implementation.
    Skilled in <strong>Python, SQL, and data visualization</strong>, with a strong analytical mindset
    and adaptability across multidisciplinary environments.
</div>
""", unsafe_allow_html=True)

# ── Education ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
st.markdown("""
<div class="edu-card">
    <div class="edu-school">Delhi Technological University (DTU)</div>
    <div class="edu-degree">Bachelor of Technology (B.Tech) in Computer Engineering</div>
    <div class="edu-meta">Aug 2019 – Jul 2023 &nbsp;|&nbsp; CGPA: 7.34 / 10 (73.4%)</div>
    <br/>
    <div style="display:flex; flex-wrap:wrap; gap:8px; margin-top:8px;">
        <span style="background:#E8F0FF; color:#4F8EF7; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600;">Computer Network</span>
        <span style="background:#E8F0FF; color:#4F8EF7; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600;">Database Management Systems</span>
        <span style="background:#E8F0FF; color:#4F8EF7; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600;">Object-Oriented Engineering</span>
        <span style="background:#E8F0FF; color:#4F8EF7; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600;">Web Technology</span>
        <span style="background:#E8F0FF; color:#4F8EF7; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600;">Artificial Intelligence</span>
        <span style="background:#E8F0FF; color:#4F8EF7; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600;">Data Structures and Algorithms (DSA)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Professional Experience ───────────────────────────────────────────────────
st.markdown('<div class="section-title">💼 Professional Experience</div>', unsafe_allow_html=True)

experiences = [
    {
        "cls": "gov",
        "title": "Research & Data Analysis Associate",
        "company": "National Centre for Good Governance (NCGG), DARPG, Govt. of India",
        "date": "Sep 2025 – Present",
        "link": "https://ncgg.org.in/",
        "bullets": [
            "Support policy research, programme planning, and Monitoring & Evaluation (M&E) through data collection, analysis, and structured reporting.",
            "Prepare concept notes, official correspondence, proposals, databases, programme records, and progress reports for senior government officials.",
            "Coordinate stakeholder engagements and capacity-building initiatives involving national and international participants.",
            "Contributed to the Right to Services (RTS) Maharashtra initiative — supported service mapping and understanding administrative hierarchies across departments.",
            "Ensure accuracy, compliance, and timely submission of programme-related documentation and reports.",
        ]
    },
    {
        "cls": "dev",
        "title": "Web Development Intern",
        "company": "Tripfox Travellers",
        "date": "Mar 2024 – May 2024",
        "link": "https://drive.google.com/drive/folders/14kg9g3eXmaMfsFatlrnWAVyPtesb12rg",
        "bullets": [
            "Developed and maintained responsive web applications using JavaScript, ReactJS, and Node.js.",
            "Applied object-oriented programming principles to design scalable software solutions.",
            "Assisted in implementing CI/CD practices, contributing to improved deployment efficiency.",
            "Performed testing, debugging, and technical documentation to ensure software reliability.",
        ]
    },
    {
        "cls": "data",
        "title": "IT Support Associate",
        "company": "Government Digital Service",
        "date": "2019 – 2022",
        "link": None,
        "bullets": [
            "Supported citizen-facing digital platforms including Social Welfare, WCD, NSDL, and e-District Delhi services.",
            "Conducted data entry, verification, validation, and record management with strict confidentiality standards.",
            "Ensured timely and accurate processing of information to facilitate efficient public service delivery.",
        ]
    },
    {
        "cls": "rand",
        "title": "Brand Executive",
        "company": "Coding Blocks, Noida",
        "date": "Oct 2021 – Dec 2022",
        "link": "https://www.codingblocks.com/",
        "bullets": [
            "Led campus outreach initiatives to strengthen student engagement and brand visibility.",
            "Planned and executed promotional campaigns to achieve organizational targets and KPIs.",
            "Facilitated awareness regarding internships, learning opportunities, and career development initiatives.",
        ]
    },
    {
        "cls": "vol",
        "title": "Volunteer Educator",
        "company": "Desh Ke Mentor Programme, Govt. of NCT Delhi",
        "date": "Dec 2022",
        "link": "https://deshkementor.com/",
        "bullets": [
            "Mentored school students by providing academic guidance and career-related support.",
            "Encouraged informed decision-making regarding higher education and professional pathways.",
        ]
    },
]

for exp in experiences:
    link_html = f'<a href="{exp["link"]}" target="_blank" style="font-size:12px; color:#4F8EF7; font-weight:600; text-decoration:none;">[🔗 View]</a>' if exp["link"] else ""
    bullets_html = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    st.markdown(f"""
    <div class="exp-card {exp['cls']}">
        <div class="exp-header">
            <div>
                <div class="exp-title">{exp['title']} {link_html}</div>
                <div class="exp-company">{exp['company']}</div>
            </div>
            <span class="exp-date">{exp['date']}</span>
        </div>
        <ul class="exp-bullets">{bullets_html}</ul>
    </div>
    """, unsafe_allow_html=True)

# ── Research & Publications ──────────────────────────────────────────────────
st.markdown('<div class="section-title">📄 Research & Publications</div>', unsafe_allow_html=True)
st.markdown("""
<div class="pub-card">
    <div class="pub-title">
        "ChatGPT & Google Bard AI: A Review"
        <a href="https://ieeexplore.ieee.org/document/10263706" target="_blank" style="font-size:13px; color:#F59E0B; font-weight:600; text-decoration:none; margin-left:8px;">[🔗 View Paper]</a>
    </div>
    <div class="pub-venue">📌 International Conference on IoT, Communication & Automation Technology (ICICAT 2023) — IEEE-sponsored</div>
    <p style="font-size:14px; color:#3D4E70; margin-top:10px; line-height:1.7;">
        Published research examining emerging generative AI technologies (Chat GPT & Google Bard AI: A Review),
        their capabilities, comparative analysis, and real-world applications.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Projects ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🚀 Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Portfolio Website",
        "stack": "Python · Streamlit · October – November 2024",
        "link": "https://personal-portfolio2-udkwg7esaoa8q5hfbaqscd.streamlit.app/",
        "desc": "Developed and deployed a responsive portfolio website showcasing academic projects, professional experiences, publications, and achievements. Hosted on Streamlit Cloud for public access.",
        "icon": "🌐"
    },
    {
        "title": "Mortgage Calculator Web App",
        "stack": "Python · Streamlit · Pandas · December 2024",
        "link": "https://mortgage-repayments-calculator-subhamkumar.streamlit.app/",
        "desc": "Built an interactive financial calculator computing mortgage payments and amortization schedules. Integrated data visualization features with Pandas & Streamlit for an intuitive user experience.",
        "icon": "🏦"
    },
]

for proj in projects:
    link_html = f'<a href="{proj["link"]}" target="_blank" style="font-size:12px; color:#7C5CFC; font-weight:600; text-decoration:none;">[🐙 GitHub]</a>' if proj["link"] else ""
    st.markdown(f"""
    <div class="proj-card">
        <div class="proj-title">{proj['icon']} {proj['title']} {link_html}</div>
        <div class="proj-stack">🛠 {proj['stack']}</div>
        <div class="proj-desc">{proj['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Technical Skills ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🛠 Technical Skills</div>', unsafe_allow_html=True)

skill_categories = [
    {
        "title": "💻 Programming Languages",
        "color": "#4F8EF7",
        "bg": "#E8F0FF",
        "skills": ["Python", "SQL", "JavaScript"]
    },
    {
        "title": "📊 Data Analytics & Visualization",
        "color": "#10B981",
        "bg": "#D1FAE5",
        "skills": ["Microsoft Excel", "Power BI", "Tableau", "Streamlit", "Data Visualization", "Basic Statistics"]
    },
    {
        "title": "🌐 Software Development",
        "color": "#7C5CFC",
        "bg": "#EDE9FE",
        "skills": ["ReactJS", "Node.js", "OOP", "Testing & Debugging", "Technical Documentation", "CI/CD"]
    },
    {
        "title": "🏛 Research & Governance",
        "color": "#F59E0B",
        "bg": "#FEF3C7",
        "skills": ["Policy Research & Analysis", "Monitoring & Evaluation", "Programme Implementation", "Survey Analysis", "Stakeholder Coordination", "Report Writing"]
    },
    {
        "title": "🤖 AI & Productivity Tools",
        "color": "#EC4899",
        "bg": "#FCE7F3",
        "skills": ["ChatGPT", "Claude AI", "Perplexity AI", "Emergent AI", "Bolt AI"]
    },
    {
        "title": "🔧 Tools & Platforms",
        "color": "#06B6D4",
        "bg": "#CFFAFE",
        "skills": ["MS Office Suite", "E-Office", "VS Code", "GitHub", "Google Drive"]
    },
]

st.markdown('<div class="skills-grid">', unsafe_allow_html=True)
for cat in skill_categories:
    tags_html = "".join(
        f'<span class="skill-tag" style="background:{cat["bg"]}; color:{cat["color"]};">{s}</span>'
        for s in cat["skills"]
    )
    st.markdown(f"""
    <div class="skill-category">
        <div class="skill-cat-title" style="color:{cat['color']};">{cat['title']}</div>
        <div class="skill-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Certifications ────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🏅 Certifications</div>', unsafe_allow_html=True)

certs = [
    {"icon": "🐍", "text": "Crash Course on Python", "provider": "Coursera", "link": "#"},
    {"icon": "☁️", "text": "Building Modern Python Applications on AWS", "provider": "Coursera", "link": "#"},
]
for cert in certs:
    st.markdown(f"""
    <div class="cert-card">
        <span class="cert-icon">{cert['icon']}</span>
        <div>
            <div class="cert-text">{cert['text']} — <em>{cert['provider']}</em></div>
            <a class="cert-link" href="{cert['link']}" target="_blank">🔗 View Certificate</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Achievements ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🏆 Achievements</div>', unsafe_allow_html=True)

achievements = [
    {"icon": "⚡", "title": "1000+ LeetCode Problems Solved", "sub": "Data Structures & Algorithms · View Profile →", "link": "https://leetcode.com/u/CodingGeek2024/"},
    {"icon": "🥇", "title": "JEE Main 2019 — AIR 296", "sub": "All India Rank in one of India's most competitive exams", "link": None},
    {"icon": "🎯", "title": "JEE Advanced 2019 — AIR 1751", "sub": "Qualified for India's top engineering institutes", "link": None},
    {"icon": "🌍", "title": "Leadership for 21st Century Women Professionals", "sub": "Ethiopian Women Parliamentarians Delegation · NCGG ( November 2025 )", "link": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2238485&reg=6&lang=1"},
    {"icon": "🇲🇺", "title": "2nd Capacity Building Programme — Mauritius", "sub": "Senior Civil Servants Programme · NCGG ( March 2026 )", "link": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2189251&reg=3&lang=2"},
]

st.markdown('<div class="ach-grid">', unsafe_allow_html=True)
for ach in achievements:
    link_html = f'<a href="{ach["link"]}" target="_blank" style="font-size:12px; color:#4F8EF7; font-weight:600; text-decoration:none;">[🔗 View]</a>' if ach["link"] else ""
    st.markdown(f"""
    <div class="ach-card">
        <span class="ach-icon">{ach['icon']}</span>
        <div>
            <div class="ach-title">{ach['title']} {link_html}</div>
            <div class="ach-sub">{ach['sub']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Leadership ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">👥 Leadership & Activities</div>', unsafe_allow_html=True)
st.markdown("""
<div class="exp-card dev" style="border-top-color:#4F8EF7;">
    <div class="exp-header">
        <div>
            <div class="exp-title">Member — Decoder Coding Society, DTU</div>
            <div class="exp-company">Delhi Technological University</div>
        </div>
        <span class="exp-date">Aug 2019 – Jun 2023</span>
    </div>
    <ul class="exp-bullets">
        <li>Participated in coding contests, technical events, and collaborative learning initiatives.</li>
        <li>Strengthened problem-solving, teamwork, and analytical thinking capabilities through active involvement in the coding community.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── Interests ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">✨ Interests & Hobbies</div>', unsafe_allow_html=True)
interests = [
    ("🏋️", "Fitness & Strength Training"),
    ("🏏", "Outdoor Sports"),
    ("✈️", "Travel & Exploration"),
    ("💻", "Competitive Programming"),
    ("🔬", "AI & Emerging Technologies"),
]
chips_html = "".join(f'<div class="interest-chip">{icon} {label}</div>' for icon, label in interests)
st.markdown(f'<div class="interests-row">{chips_html}</div>', unsafe_allow_html=True)

# ── Core Competencies ────────────────────────────────────────────────────────
st.markdown('<div class="section-title">💡 Core Competencies</div>', unsafe_allow_html=True)
competencies = [
    "Problem Solving & Analytical Thinking", "Cross-functional Collaboration",
    "Technical Documentation", "Research & Report Writing",
    "Data Analysis & Interpretation", "Governance Evaluation",
    "Presentation & Communication Skills", "Stakeholder Management",
    "Adaptability & Continuous Learning", "Quality-focused Execution"
]
tags_html = "".join(
    f'<span style="background:#fff; color:#1E2A4A; padding:8px 16px; border-radius:25px; font-size:13px; font-weight:500; box-shadow:0 2px 10px rgba(30,42,74,0.08); border:1.5px solid #E8EEFF;">{c}</span>'
    for c in competencies
)
st.markdown(f'<div style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:36px;">{tags_html}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close page-wrapper

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>Shubham Kumar</strong> · Research & Data Analysis Associate · NCGG, Govt. of India<br/>
    📧 Shubhamrawatk203@gmail.com &nbsp;|&nbsp; 📞 +91-8810325212<br/><br/>
    <span style="font-size:12px; color:#B0BCDC;">Built with Python & Streamlit</span>
</div>
""", unsafe_allow_html=True)