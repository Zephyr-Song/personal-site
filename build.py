#!/usr/env python3
# -*- coding: utf-8 -*-
"""Build a hand-crafted static personal site (no template, no framework).
Mimics the single-page academic style of wannabeyourfriend.github.io,
populated with Song Jincheng's resume content.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)

SITE_BASE = "https://zephyr-song.github.io"

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
        <a href="#contact">Contact</a>
      </nav>
    </header>"""

ABOUT = """
    <section class="section" id="about">
      <div class="sec-num">01</div>
      <div class="about-inner">
        <div class="about-text">
          <h1>Song Jincheng</h1>
          <p class="lede">Final-year Computer Science undergraduate at Xi&rsquo;an Jiaotong-Liverpool University (XJTLU).</p>
          <p>I work at the intersection of computer vision, large language models, and human-centered design &mdash; from making autonomous-driving perception robust in bad weather, to building LLM tools that help student researchers reason about research ethics. I also write, and I build small, delightful web things.</p>
          <p class="micro">Also known as <strong>Zephyr</strong> &middot; GitHub <a href="https://github.com/Zephyr-Song" target="_blank" rel="noopener">@Zephyr-Song</a></p>
        </div>
      </div>
    </section>"""

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
        <div class="entry-head"><span class="entry-where">JOTO</span><span class="entry-when">AI Engineering</span></div>
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
          <p class="card-sub">Shanghai BFC Mall &middot; AI Shopping Guide</p>
          <p>Designed and developed an AI shopping-guide system for a Shanghai mall &mdash; system architecture, core feature build-out and iterative optimization.</p>
        </div>
        <div class="card">
          <h3>Daily Tarot Spread</h3>
          <p class="card-sub">WeChat Mini Program &middot; Daily Tarot</p>
          <p>Designed and developed a daily-tarot WeChat mini program &mdash; frontend interaction, backend API integration and feature optimization.</p>
        </div>
        <div class="card">
          <h3>Ethical Mirror</h3>
          <p class="card-sub">SafeBARS &middot; Ethics Reflection Platform</p>
          <p>A bilingual, LLM-driven Socratic platform that helps student researchers surface and fix ethics risks in their own AI/ML studies.</p>
        </div>
        <div class="card">
          <h3>More building</h3>
          <p class="card-sub">side quests</p>
          <p>Hugo blog (<a href="https://zephyrsong.qzz.io" target="_blank" rel="noopener">zephyrsong.qzz.io</a>), an AI media-automation pipeline, CityGo (a Y2K-style city-check-in app) and a pet-collection game.</p>
        </div>
      </div>
    </section>"""

CONTACT = f"""
    <section class="section" id="contact">
      <div class="sec-num">05</div>
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
  <title>Song Jincheng</title>
  <meta name="description" content="Song Jincheng — CS undergraduate at XJTLU. CV, research, projects and contact.">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{NAV}
<main>
{ABOUT}
{EDUCATION}
{EXPERIENCE}
{PROJECTS}
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
