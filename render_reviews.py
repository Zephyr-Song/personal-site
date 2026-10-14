#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recover book-review bodies from the original Gmeek repo's GitHub Issues
(the real content store) and render them to HTML, so the new site can embed
them and stop depending on the (currently broken) Gmeek Pages site.
Run with Anaconda python (has the `markdown` lib)."""
import json, os, re
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)

post_list = load("postList.json")
issues = load("_issues.json")

# index posts by title
posts_by_title = {}
for k, v in post_list.items():
    posts_by_title[v.get("postTitle", "").strip()] = v

def norm(s):
    return re.sub(r"\s+", "", s or "")

posts_norm = {norm(t): v for t, v in posts_by_title.items()}

rendered = []
unmatched = 0
for it in issues:
    title = (it.get("title") or "").strip()
    body = it.get("body") or ""
    # drop a leading heading line so we don't duplicate the card title
    lines = body.splitlines()
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx < len(lines) and re.match(r"^#{1,6}\s", lines[idx]):
        body = "\n".join(lines[idx+1:]).strip()
    html = markdown.markdown(body, extensions=["extra", "sane_lists"])
    # date + labels: prefer the postList metadata, fall back to issue
    post = posts_by_title.get(title) or posts_norm.get(norm(title))
    if post:
        date = post.get("createdDate", "")
        labels = post.get("labels", [])
    else:
        unmatched += 1
        date = (it.get("created_at") or "")[:10]
        labels = [l["name"] for l in it.get("labels", [])]
    rendered.append({
        "title": title,
        "date": date,
        "labels": labels,
        "html": html,
    })

# keep original order (by issue number / date desc)
rendered.sort(key=lambda r: r["date"], reverse=True)

out = os.path.join(HERE, "reviews_rendered.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(rendered, f, ensure_ascii=False, indent=1)

print("rendered", len(rendered), "reviews | unmatched titles:", unmatched)
print("sample title/date/labels:", rendered[0]["title"], rendered[0]["date"], rendered[0]["labels"])
print("sample html head:", rendered[0]["html"][:160])
