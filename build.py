#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a hand-crafted static personal site (no template, no framework).
Mimics the single-page academic style of wannabeyourfriend.github.io,
populated with Song Jincheng's resume + migrated book-review & music modules.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)

post_list = load("postList.json")
playlist = load("playlist_full.json")

SITE_BASE = "https://zephyr-song.github.io"
AVATAR = "https://github.com/Zephyr-Song.png"

# ---------------------------------------------------------------------------
# Book reviews — recovered from the original Gmeek site's GitHub Issues (the real
# content store) and rendered to HTML, so the new site is fully self-contained
# and no longer depends on the (currently broken) old Gmeek Pages build.
# ---------------------------------------------------------------------------
reviews_data = load("reviews_rendered.json")
rev_rows = []
for r in reviews_data:
    tags = "".join('<span class="tag">%s</span>' % t for t in r.get("labels", []))
    rev_rows.append(
        '      <details class="rev-item">\n'
        '        <summary>\n'
        '          <span class="rev-title">%s</span>\n'
        '          <span class="rev-meta"><span class="rev-date">%s</span>%s</span>\n'
        '        </summary>\n'
        '        <div class="rev-body">%s</div>\n'
        '      </details>' % (r.get("title", ""), r.get("date", ""), tags, r.get("html", ""))
    )
reviews_html = "\n".join(rev_rows)

# ---------------------------------------------------------------------------
# Music (migrated from the NetEase playlist)
# ---------------------------------------------------------------------------
songs = playlist.get("songs", [])[:10]
def artist_names(ar):
    return " / ".join(a.get("name", "") for a in ar if a.get("name"))

music_html = "\n".join(
    f'''      <a class="song" href="https://music.163.com/song/{s.get('id')}" target="_blank" rel="noopener">
        <span class="song-name">{s.get('name','')}</span>
        <span class="song-artist">{artist_names(s.get('ar', []))}</span>
        <span class="song-album">{s.get('al', {}).get('name','')}</span>
      </a>'''
    for s in songs
)

# ---------------------------------------------------------------------------
# Static content
# ---------------------------------------------------------------------------
NAV = """
    <header class="nav" id="top">
      <a class="brand" href="#top">Song Jincheng <span class="brand-mark">&#10038;</span></a>
      <nav class="nav-links">
        <a href="#about">About</a>
        <a href="#education">Education</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Projects</a>
        <a href="#reviews">Reviews</a>
        <a href="#music">Music</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>"""

ABOUT = """
    <section class="section" id="about">
      <div class="sec-num">01</div>
      <div class="about-inner">
        <img class="avatar" src="{avatar}" alt="Song Jincheng">
        <div class="about-text">
          <h1>Song Jincheng <span class="cn">宋锦程</span></h1>
          <p class="lede">Final-year Computer Science undergraduate at Xi&rsquo;an Jiaotong-Liverpool University (XJTLU).</p>
          <p>I work at the intersection of computer vision, large language models, and human-centered design &mdash; from making autonomous-driving perception robust in bad weather, to building LLM tools that help student researchers reason about research ethics. I also write, and I build small, delightful web things.</p>
          <p class="micro">Also known as <strong>Zephyr / 旧城</strong> &middot; GitHub <a href="https://github.com/Zephyr-Song" target="_blank" rel="noopener">@Zephyr-Song</a></p>
        </div>
      </div>
    </section>""".format(avatar=AVATAR)

EDUCATION = """
    <section class="section" id="education">
      <div class="sec-num">02</div>
      <h2>Education</h2>
      <div class="entry">
        <div class="entry-head">
          <span class="entry-where">Xi&rsquo;an Jiaotong-Liverpool University</span>
          <span class="entry-when">Undergraduate</span>
        </div>
        <div class="entry-sub">BEng, Intelligent Computing Systems &middot; Computer Science</div>
        <ul class="bullets">
          <li>School Honors &mdash; 8th in long jump &amp; 6th in triple jump, men&rsquo;s undergraduate group, 16th Suzhou City Sports Meeting.</li>
          <li>English proficiency &mdash; capable of reading academic literature; <strong>GRE 330</strong>.</li>
          <li>Artificial Intelligence Foundations (56h, Grade 86.5 / A) &mdash; instructor Prof. Dr. habil. Bj&ouml;rn W. Schuller (Imperial College London).</li>
        </ul>
      </div>
    </section>"""

EXPERIENCE = """
    <section class="section" id="experience">
      <div class="sec-num">03</div>
      <h2>Experience</h2>

      <h3 class="grp">Research</h3>
      <div class="entry">
        <div class="entry-head"><span class="entry-where">Robust 3D Perception for Autonomous Driving</span><span class="entry-when">CV &middot; Self-driven</span></div>
        <div class="entry-sub">Adverse-weather robustness on the KITTI dataset</div>
        <ul class="bullets">
          <li>Joint 2D&rarr;3D point-cloud modification to simulate rain, snow, fog and unexpected traffic scenarios.</li>
          <li>Combined physical simulation with diffusion models for cross-modal image&ndash;point-cloud data augmentation.</li>
          <li>Comparative experiments on 3D object-detection models verified the robustness improvement.</li>
        </ul>
      </div>
      <div class="entry">
        <div class="entry-head"><span class="entry-where">Ethical Mirror / SafeBARS</span><span class="entry-when">CHI 2027 &middot; w/ Erick</span></div>
        <div class="entry-sub">Ethics-risk reflection for student AI/ML researchers</div>
        <ul class="bullets">
          <li>Built on a risk taxonomy and a library of real reported cases; uses LLM-driven Socratic dialogue to turn generic ethics checklists into concrete, fixable issues.</li>
          <li>Multi-condition controlled design delivers a bilingual reflection platform &mdash; controlled experiments show it deepens ethical reflection and intention to act.</li>
        </ul>
      </div>

      <h3 class="grp">Internship</h3>
      <div class="entry">
        <div class="entry-head"><span class="entry-where">JOTO &middot; 聚托科技</span><span class="entry-when">AI Engineering</span></div>
        <ul class="bullets">
          <li>Integrated LLM APIs for batch translation of short-drama scripts &mdash; designed and iterated prompt templates and post-processing rules for consistent style and formatting.</li>
          <li>Wrapped multi-scenario model calls with unified authentication, retry, error logging and batch scheduling for reliable throughput at scale.</li>
          <li>Built a campus AI assistant on <strong>Dify</strong> &mdash; integrated a knowledge base and designed prompt workflows to improve response quality.</li>
        </ul>
      </div>
    </section>"""

PROJECTS = """
    <section class="section" id="projects">
      <div class="sec-num">04</div>
      <h2>Projects</h2>
      <div class="cards">
        <div class="card">
          <h3>BFC AI Shopping Guide</h3>
          <p class="card-sub">上海BFC商场 &middot; AI 智能导购系统</p>
          <p>Designed and developed an AI shopping-guide system for a Shanghai mall &mdash; system architecture, core feature build-out and iterative optimization.</p>
        </div>
        <div class="card">
          <h3>Daily Tarot Spread</h3>
          <p class="card-sub">WeChat Mini Program &middot; 塔罗日签</p>
          <p>Designed and developed a daily-tarot WeChat mini program &mdash; frontend interaction, backend API integration and feature optimization.</p>
        </div>
        <div class="card">
          <h3>Ethical Mirror</h3>
          <p class="card-sub">SafeBARS &middot; 伦理反思平台</p>
          <p>A bilingual, LLM-driven Socratic platform that helps student researchers surface and fix ethics risks in their own AI/ML studies.</p>
        </div>
        <div class="card">
          <h3>More building</h3>
          <p class="card-sub">side quests</p>
          <p>Hugo blog (<a href="https://zephyrsong.qzz.io" target="_blank" rel="noopener">zephyrsong.qzz.io</a>), an AI media-automation pipeline, CityGo (a Y2K-style city-check-in app) and a pet-collection game.</p>
        </div>
      </div>
    </section>"""

REVIEWS = f"""
    <section class="section" id="reviews">
      <div class="sec-num">05</div>
      <h2>Book Reviews <span class="cn">书评</span></h2>
      <p class="sec-note">A reading log &mdash; {len(reviews_data)} pieces recovered from the original blog&rsquo;s GitHub Issues and kept here, fully self-contained.</p>
      <div class="rev-list">
{reviews_html}
      </div>
    </section>"""

MUSIC = f"""
    <section class="section" id="music">
      <div class="sec-num">06</div>
      <h2>Music <span class="cn">音乐</span></h2>
      <p class="sec-note">A slice of what I&rsquo;m listening to &mdash; pulled from my NetEase playlist.</p>
      <div class="song-grid">
{music_html}
      </div>
    </section>"""

CONTACT = f"""
    <section class="section" id="contact">
      <div class="sec-num">07</div>
      <h2>Contact</h2>
      <ul class="contact-list">
        <li><span>Email</span><a href="mailto:jincheng.song24@student.xjtlu.edu.cn">jincheng.song24@student.xjtlu.edu.cn</a></li>
        <li><span>GitHub</span><a href="https://github.com/Zephyr-Song" target="_blank" rel="noopener">@Zephyr-Song</a></li>
        <li><span>Blog</span><a href="https://zephyrsong.qzz.io" target="_blank" rel="noopener">zephyrsong.qzz.io</a></li>
      </ul>
    </section>"""

FOOTER = """
    <footer class="footer">
      <p>&copy; 2026 Song Jincheng &middot; hand-built, with care.</p>
      <p class="foot-note">Curious, careful, and a little <em>playful</em>. &mdash; psst, press <kbd>`</kbd></p>
    </footer>"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Song Jincheng &middot; 宋锦程</title>
  <meta name="description" content="Song Jincheng (宋锦程) — CS undergraduate at XJTLU. CV, research, projects, book reviews and music.">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{NAV}
<main>
{ABOUT}
{EDUCATION}
{EXPERIENCE}
{PROJECTS}
{REVIEWS}
{MUSIC}
{CONTACT}
</main>
{FOOTER}
<script src="assets/js/main.js"></script>
</body>
</html>"""

out = os.path.join(HERE, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("wrote", out, os.path.getsize(out), "bytes")
print("reviews:", len(reviews_data), "songs:", len(songs))
