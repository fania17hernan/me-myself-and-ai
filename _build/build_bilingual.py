# -*- coding: utf-8 -*-
"""Builds Me, Myself & AI: level-select landing + per-level hubs + modules, EN (root) & ES (/es/)."""
import os, json, html as _html
from bili_common import CSS, FONTS, GAUGE, js_str
import bili_en, bili_es

OUT = "/sessions/busy-epic-pascal/mnt/09 AI Projects/me-myself-and-ai"

# Supabase "suggest a topic" backend (publishable key, safe to embed; table is RLS insert-only)
SUPA_URL = "https://pdbqrjqlwqjqzefmmlhd.supabase.co"
SUPA_KEY = "sb_publishable_IdA-Ju152TgBx-wEGMd0Yg_iV7_wvkO"

def render_suggest(ui, source, lang):
    fid = "sg_" + source.replace("-", "_")
    return (
      '<section class="suggest card">'
      '<h3 style="margin-top:0">%s</h3>'
      '<p class="soft" style="margin-bottom:14px">%s</p>'
      '<form id="%s" novalidate>'
      '<textarea id="%s_t" maxlength="1000" rows="3" placeholder="%s" required></textarea>'
      '<input id="%s_e" type="email" maxlength="200" placeholder="%s" autocomplete="off">'
      '<input type="text" id="%s_hp" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
      '<button type="submit" class="btn btn-primary" id="%s_b">%s</button>'
      '<p class="sg-msg" id="%s_m" role="status"></p>'
      '</form></section>'
      '<script>(function(){var f=document.getElementById("%s");if(!f)return;'
      'var t=document.getElementById("%s_t"),e=document.getElementById("%s_e"),'
      'hp=document.getElementById("%s_hp"),b=document.getElementById("%s_b"),m=document.getElementById("%s_m");'
      'f.addEventListener("submit",function(ev){ev.preventDefault();if(hp.value)return;'
      'var s=(t.value||"").trim();if(!s)return;b.disabled=true;m.textContent="";'
      'fetch(%s+"/rest/v1/topic_suggestions",{method:"POST",headers:{"apikey":%s,"Authorization":"Bearer "+%s,"Content-Type":"application/json","Prefer":"return=minimal"},'
      'body:JSON.stringify({suggestion:s,email:(e.value||"").trim()||null,lang:%s,source:%s})})'
      '.then(function(r){if(r.ok){f.innerHTML="<p class=\\"sg-ok\\">"+%s+"</p>";}else{m.textContent=%s;b.disabled=false;}})'
      '.catch(function(){m.textContent=%s;b.disabled=false;});});})();</script>'
    ) % (
      _html.escape(ui["suggest_heading"]), _html.escape(ui["suggest_sub"]),
      fid, fid, _html.escape(ui["suggest_ph"], quote=True), fid, _html.escape(ui["suggest_email_ph"], quote=True),
      fid, fid, _html.escape(ui["suggest_button"]), fid,
      fid, fid, fid, fid, fid, fid,
      json.dumps(SUPA_URL), json.dumps(SUPA_KEY), json.dumps(SUPA_KEY),
      json.dumps(lang), json.dumps(source),
      json.dumps(ui["suggest_thanks"]), json.dumps(ui["suggest_error"]), json.dumps(ui["suggest_error"]),
    )

# ---------- extra CSS for landing/level cards ----------
EXTRA_CSS = """
  .lcard{display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:20px;box-shadow:var(--sh1);margin-bottom:14px;text-decoration:none;color:var(--ink)}
  .lcard:hover{border-color:var(--accent)}
  .lcard.soon{opacity:.62;cursor:default}
  .lnum{flex:0 0 46px;height:46px;border-radius:14px;background:var(--warm);color:var(--accent-deep);font:600 20px 'Fraunces',serif;display:flex;align-items:center;justify-content:center}
  .lbody{flex:1;min-width:0}
  .lname{font:700 18px/1.25 'Inter';margin-bottom:3px}
  .ltag{font:400 14px/1.4 'Inter';color:var(--ink-soft)}
  .lmeta{font:500 12px/1.4 'Inter';color:var(--accent-deep);margin-top:6px;text-transform:uppercase;letter-spacing:.08em}
  .lmeta.soonlbl{color:var(--ink-soft)}
  .lring{flex:0 0 34px;height:34px;border-radius:50%;background:conic-gradient(var(--accent) 0deg, var(--line) 0deg);display:flex;align-items:center;justify-content:center}
  .lring span{width:26px;height:26px;border-radius:50%;background:var(--surface);font:600 10px 'Inter';display:flex;align-items:center;justify-content:center;color:var(--ink-soft)}
  .util{display:flex;gap:12px;margin-top:6px}
  .util .tile{flex:1;background:var(--warm);border-radius:16px;padding:16px;text-decoration:none;color:var(--ink)}
  .util .tile .tt{font:700 15px 'Inter';margin-bottom:3px}
  .util .tile .ts{font:400 12.5px/1.35 'Inter';color:var(--ink-soft)}
  .backlink{display:inline-block;font:600 13px/1.4 'Inter';color:var(--accent-deep);text-decoration:none;margin:4px 0 4px}
  .backlink:hover{text-decoration:underline}
  .suggest{border:1px solid var(--line);border-top:3px solid var(--highlight)}
  .suggest h3{font:700 17px/1.3 'Inter'}
  .suggest textarea,.suggest input[type=email]{width:100%;background:var(--paper);border:1.5px solid var(--line);border-radius:12px;padding:12px 14px;font:400 16px 'Inter';color:var(--ink);margin-bottom:10px;resize:vertical;font-family:'Inter',sans-serif}
  .suggest textarea:focus,.suggest input[type=email]:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(191,85,56,.15)}
  .suggest .btn-primary{width:100%}
  .hp{position:absolute !important;left:-9999px !important;width:1px;height:1px;opacity:0;pointer-events:none}
  .sg-msg{margin:10px 0 0;color:var(--error);font-size:14px}
  .sg-ok{margin:0;color:var(--success);font-weight:600;font-size:16px}
"""

LANDING_CSS = """
  .outcomes{list-style:none;margin:4px 0 16px;padding:0}
  .outcomes li{position:relative;padding-left:28px;margin-bottom:10px;font:500 16px/1.45 'Inter';color:var(--ink)}
  .outcomes li:before{content:'\\2713';position:absolute;left:0;top:0;color:var(--success);font-weight:700}
  .facts{display:inline-block;background:var(--warm);color:var(--accent-deep);font:600 13.5px/1.4 'Inter';
         border-radius:999px;padding:9px 16px;margin:0 0 14px}
  .whylink{display:block;font:600 15px/1.4 'Inter';color:var(--accent-deep);text-decoration:none;margin:0 0 8px}
  .whylink:hover{text-decoration:underline}
"""

ABOUT_CSS = """
  .about-body{max-width:62ch}
  .about-body p{font:400 17px/1.7 'Inter';color:var(--ink);margin-bottom:16px}
  .about-body p.lead{font:600 26px/1.2 'Fraunces',serif;color:var(--ink);margin-bottom:18px}
  .about-body strong{font-weight:600}
  @media(min-width:768px){.about-body p{font-size:18px}}
"""

# ===================== MODULE PAGE =====================
TEMPLATE = """<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#FAF5EC">
<title>{title}, Me, Myself &amp; AI</title>
{fonts}
<style>{css}</style>
</head>
<body>
<header>
  <div class="topline">
    <a class="brand" href="index.html">Me, Myself <span class="amp">&amp;</span> AI</a>
    <span class="rightgrp">
      <a class="lang" href="{lang_href}">{lang_label}</a>
      <span class="stepl" id="stepLabel">{level_name}</span>
    </span>
  </div>
  <div class="gauge" aria-hidden="true">{gauge}<div class="ptrack"><div class="pfill" id="fill" style="width:0%"></div></div></div>
</header>
<main>
  <section class="screen on" data-title="cover">
    <a class="backlink" href="{level_slug}.html">← {level_name}</a>
    <p class="kicker">{level_name} · {lesson_word} {pos} {of_word} {count} · {mins} {min}</p>
    <h1>{title}</h1>
    <p class="soft">{subtitle}</p>
    <div class="card"><h3 style="margin-top:0">{in_module}</h3><ul style="margin-bottom:0">{in_items}</ul></div>
  </section>
  <section class="screen" data-title="problem"><p class="kicker">{k_problem}</p><h1>{hook_title}</h1>{hook}</section>
  <section class="screen" data-title="analogy"><p class="kicker">{k_analogy}</p><div class="analogy"><h2>{analogy_name}</h2>{analogy}</div>{analogy_after}</section>
  <section class="screen" data-title="how"><p class="kicker">{k_how}</p><h1>{how_title}</h1>{how}</section>
  <section class="screen" data-title="foryou"><p class="kicker">{k_foryou}</p><h1>{foryou_title}</h1>{foryou}</section>
  <section class="screen" data-title="takeaway"><p class="kicker">{k_takeaway}</p><h1>{takeaway_h1}</h1><div class="takeaway"><p>{takeaway}</p></div><p class="soft">{takeaway_after}</p></section>
  <section class="screen" data-title="quiz"><p class="kicker">{k_quiz}</p>{quiz_html}</section>
  <section class="screen" data-title="done">
    <p class="kicker">{k_complete}</p><h1 id="doneTitle">{done_perfect}</h1><p id="doneScore"></p>
    <div class="takeaway"><p>{takeaway}</p></div><p>{next_teaser}</p>{done_extra}
    <!--SUGGEST-->
  </section>
</main>
<nav class="navbar"><div class="inner">
  <button class="btn btn-ghost" id="backBtn">{back}</button>
  <button class="btn btn-primary" id="nextBtn">{start}</button>
</div></nav>
<div id="doneNav" style="display:none;max-width:640px;margin:0 auto;padding:0 20px 40px"><div style="display:flex;gap:12px;flex-wrap:wrap">{nextmod_btn}<a class="btn btn-ghost" href="{level_slug}.html">{back_to_level}</a></div></div>
<script>
(function(){{
  var GID={gid};
  var LVLNAME={j_levelname};
  var L={{step:{j_step},of:{j_of},complete:{j_complete},start:{j_start},cont:{j_cont},finish:{j_finish}}};
  var screens=[].slice.call(document.querySelectorAll('.screen'));
  var fill=document.getElementById('fill'),stepLabel=document.getElementById('stepLabel');
  var nextBtn=document.getElementById('nextBtn'),backBtn=document.getElementById('backBtn');
  var navbar=document.querySelector('.navbar'),doneNav=document.getElementById('doneNav');
  var QUIZ=6,DONE=screens.length-1;
  var i=0,answers={{}};
  try{{var sv=parseInt(localStorage.getItem('mmai-m'+GID),10);if(sv>0&&sv<DONE)i=sv;}}catch(e){{}}
  var explains={{{explains_js}}};
  function quizDone(){{return Object.keys(answers).length===3}}
  function score(){{var s=0;for(var k in answers){{if(answers[k])s++}}return s}}
  function render(){{
    screens.forEach(function(s,n){{s.classList.toggle('on',n===i)}});
    fill.style.width=Math.round(i/DONE*100)+'%';
    stepLabel.textContent=(i===0)?LVLNAME:(i===DONE)?L.complete:L.step+' '+i+' '+L.of+' '+(DONE-1);
    backBtn.style.visibility=(i===0)?'hidden':'visible';
    if(i===0)nextBtn.textContent=L.start;
    else if(i===QUIZ){{nextBtn.textContent=L.finish;nextBtn.disabled=!quizDone();}}
    else{{nextBtn.textContent=L.cont;nextBtn.disabled=false;}}
    navbar.style.display=(i===DONE)?'none':'';
    doneNav.style.display=(i===DONE)?'block':'none';
    if(i===DONE){{
      try{{localStorage.setItem('mmai-done-'+GID,'1')}}catch(e){{}}
      var s=score();
      document.getElementById('doneTitle').textContent=(s===3)?{j_done_perfect}:{j_done_plain};
      document.getElementById('doneScore').textContent={j_score_pre}+s+{j_score_mid}+(s===3?{j_score_perfect}:{j_score_imperfect});
    }}
    try{{localStorage.setItem('mmai-m'+GID,i)}}catch(e){{}}
    window.scrollTo({{top:0}});
  }}
  nextBtn.addEventListener('click',function(){{if(i<DONE){{i++;render()}}}});
  backBtn.addEventListener('click',function(){{if(i>0){{i--;render()}}}});
  [].slice.call(document.querySelectorAll('[data-q]')).forEach(function(card){{
    var q=+card.dataset.q,ans=+card.dataset.answer;
    var opts=[].slice.call(card.querySelectorAll('.qopt')),ex=card.querySelector('.explain');
    opts.forEach(function(opt,n){{
      opt.addEventListener('click',function(){{
        if(q in answers)return;
        var correct=(n===ans);answers[q]=correct;
        opts.forEach(function(o){{o.disabled=true}});
        opt.classList.add(correct?'ok':'no');
        if(!correct)opts[ans].classList.add('ok');
        ex.textContent=correct?explains[q].good:explains[q].bad;
        ex.classList.add('show',correct?'good':'bad');
        if(quizDone())nextBtn.disabled=false;
      }});
    }});
  }});
  render();
}})();
</script>
</body>
</html>
"""

# ===================== LEVEL HUB =====================
LEVELHUB = """<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#FAF5EC">
<title>{level_name}, Me, Myself &amp; AI</title>
{fonts}
<style>{css}</style>
</head>
<body>
<header>
  <div class="topline">
    <a class="brand" href="index.html">Me, Myself <span class="amp">&amp;</span> AI</a>
    <span class="rightgrp"><a class="lang" href="{lang_href}">{lang_label}</a><span class="stepl" id="progText"></span></span>
  </div>
  <div class="gauge" aria-hidden="true">{gauge}<div class="ptrack"><div class="pfill" id="fill" style="width:0%"></div></div></div>
</header>
<main>
  <a class="backlink" href="index.html">← {all_levels}</a>
  <div class="hero">
    <p class="eyebrow">{level_word} {level_id}</p>
    <h1>{level_name}</h1>
    <p class="tagline">{level_tagline}</p>
  </div>
  {cards}
</main>
<script>
(function(){{
  var mods={mods_js};var done=0;
  [].slice.call(document.querySelectorAll('.mcard')).forEach(function(c){{
    var m=c.getAttribute('data-mod');
    try{{if(localStorage.getItem('mmai-done-'+m)==='1'){{c.classList.add('done');done++;}}}}catch(e){{}}
  }});
  document.getElementById('fill').style.width=Math.round(done/mods.length*100)+'%';
  document.getElementById('progText').textContent=({j_level_prog}).replace('{{d}}',String(done)).replace('{{n}}',String(mods.length));
}})();
</script>
</body>
</html>
"""

# ===================== LANDING =====================
LANDING = """<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#FAF5EC">
<title>{hub_title}</title>
{fonts}
<style>{css}</style>
</head>
<body>
<header>
  <div class="topline">
    <span class="brand">Me, Myself <span class="amp">&amp;</span> AI</span>
    <span class="rightgrp"><a class="lang" href="{lang_href}">{lang_label}</a><span class="stepl" id="progText"></span></span>
  </div>
  <div class="gauge" aria-hidden="true">{gauge}<div class="ptrack"><div class="pfill" id="fill" style="width:0%"></div></div></div>
</header>
<main>
  <div class="hero">
    <p class="eyebrow">{landing_eyebrow}</p>
    <h1>{landing_h1}</h1>
    <p class="tagline">{landing_tagline}</p>
    <ul class="outcomes"><li>{o1}</li><li>{o2}</li><li>{o3}</li></ul>
    <p class="facts">{facts_pill}</p>
    <a class="whylink" href="about.html">{why_link}</a>
  </div>
  {level_cards}
  <div class="util">
    <a class="tile" href="glossary.html"><div class="tt">{glossary_title} →</div><div class="ts">{glossary_sub}</div></a>
    <span class="tile"><div class="tt">{prof_title}</div><div class="ts">{prof_sub}</div></span>
  </div>
  <!--SUGGEST-->
</main>
<script>
(function(){{
  var live={live_js};var done=0,total=0;
  live.forEach(function(m){{total++;try{{if(localStorage.getItem('mmai-done-'+m)==='1')done++;}}catch(e){{}}}});
  document.getElementById('fill').style.width=total?Math.round(done/total*100)+'%':'0%';
  document.getElementById('progText').textContent=({j_overall}).replace('{{d}}',String(done)).replace('{{t}}',String(total));
  // per-level rings
  [].slice.call(document.querySelectorAll('.lcard[data-mods]')).forEach(function(c){{
    var mods=c.getAttribute('data-mods').split(',').filter(Boolean);var d=0;
    mods.forEach(function(m){{try{{if(localStorage.getItem('mmai-done-'+m)==='1')d++;}}catch(e){{}}}});
    var ring=c.querySelector('.lring');var deg=mods.length?Math.round(d/mods.length*360):0;
    if(ring){{ring.style.background='conic-gradient(var(--accent) '+deg+'deg, var(--line) '+deg+'deg)';
      var sp=ring.querySelector('span');if(sp)sp.textContent=d+'/'+mods.length;}}
  }});
}})();
</script>
</body>
</html>
"""

GLOSSARY_PAGE = """<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#FAF5EC">
<title>{glossary_h1}, Me, Myself &amp; AI</title>
{fonts}
<style>{css}
  .gsearch{{width:100%;background:var(--surface);border:1.5px solid var(--line);border-radius:14px;padding:14px 16px;font:400 17px 'Inter';color:var(--ink);margin:4px 0 18px}}
  .gsearch:focus{{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(191,85,56,.18)}}
  .gterm{{font:700 18px/1.3 'Inter';margin-bottom:6px}}
  .gdef{{margin-bottom:10px}}
  .gan{{font:400 14px/1.45 'Inter';color:var(--ink-soft);background:var(--warm);border-radius:12px;padding:10px 12px;margin-bottom:12px}}
  .gan b{{color:var(--accent-deep);font-weight:600}}
  .glearn{{font:600 14px 'Inter';color:var(--accent-deep);text-decoration:none}}
  .glearn:hover{{text-decoration:underline}}
  .gnone{{color:var(--ink-soft);font-style:italic;padding:8px 2px;display:none}}
</style>
</head>
<body>
<header>
  <div class="topline">
    <a class="brand" href="index.html">Me, Myself <span class="amp">&amp;</span> AI</a>
    <span class="rightgrp"><a class="lang" href="{lang_href}">{lang_label}</a><span class="stepl" id="cnt"></span></span>
  </div>
  <div class="gauge" aria-hidden="true">{gauge}<div class="ptrack"><div class="pfill" style="width:100%"></div></div></div>
</header>
<main>
  <a class="backlink" href="index.html">← {all_levels}</a>
  <div class="hero"><p class="eyebrow">{glossary_h1}</p><h1>{glossary_h1}</h1><p class="tagline">{glossary_intro}</p></div>
  <input class="gsearch" id="gsearch" type="search" placeholder="{search_ph}" autocomplete="off" aria-label="{search_ph}">
  <div id="glist">{cards}</div>
  <p class="gnone" id="gnone">{none_msg}</p>
</main>
<script>
(function(){{
  var box=document.getElementById('gsearch'),cards=[].slice.call(document.querySelectorAll('.card[data-s]'));
  var none=document.getElementById('gnone'),cnt=document.getElementById('cnt');
  function up(){{
    var q=box.value.trim().toLowerCase(),shown=0;
    cards.forEach(function(c){{var hit=c.getAttribute('data-s').indexOf(q)>-1;c.style.display=hit?'':'none';if(hit)shown++;}});
    none.style.display=shown?'none':'block';
    cnt.textContent=shown+(q?'':'');
  }}
  box.addEventListener('input',up);
  cnt.textContent=cards.length;
}})();
</script>
</body>
</html>
"""

def render_glossary(glossary, ui, htmllang, lang_href_for):
    cards=""
    for g in sorted(glossary, key=lambda x: x["term"].lower()):
        search=(g["term"]+" "+g["def"]+" "+g["analogy"]).lower().replace('"',"")
        link=('<a class="glearn" href="module-%d.html">%s</a>'%(g["n"], ui["glossary_learn"])) if g.get("n") else ''
        cards+=('<div class="card" data-s="%s"><div class="gterm">%s</div>'
                '<p class="gdef">%s</p>'
                '<div class="gan"><b>%s:</b> %s</div>%s</div>')%(
                search, g["term"], g["def"], ui["glossary_analogy_label"], g["analogy"], link)
    return GLOSSARY_PAGE.format(
        htmllang=htmllang, fonts=FONTS, css=CSS+EXTRA_CSS, gauge=GAUGE,
        lang_href=lang_href_for("glossary.html"), lang_label=ui["lang_label"],
        all_levels=ui["all_levels"], glossary_h1=ui["glossary_h1"], glossary_intro=ui["glossary_intro"],
        search_ph=ui["glossary_search_ph"], cards=cards, none_msg=ui["glossary_none"],
    )

def render_module(m, ui, levels, htmllang, lang_href_for):
    # find level + position
    lvl=next(L for L in levels if m["n"] in L["modules"])
    mods=lvl["modules"]; pos=mods.index(m["n"])+1; count=len(mods)
    in_items="".join("<li>%s</li>"%x for x in m["in_module"])
    quiz_html=""
    for qi,q in enumerate(m["quiz"]):
        opts="".join('<button class="qopt"><span class="dot"></span>%s</button>'%o for o in q["opts"])
        quiz_html+='<div class="card" data-q="%d" data-answer="%d"><h3 style="margin-top:0">%s</h3>%s<div class="explain"></div></div>'%(qi,q["a"],q["q"],opts)
    explains_js=",".join('%d:{good:%s,bad:%s}'%(qi,js_str(q["good"]),js_str(q["bad"])) for qi,q in enumerate(m["quiz"]))
    # next button: next module in level, else more levels (landing)
    idx=mods.index(m["n"])
    if idx+1 < len(mods):
        nxt=mods[idx+1]
        nextmod='<a class="btn btn-primary" href="module-%d.html">%s</a>'%(nxt, ui["next_module"])
        done_extra=""
    else:
        nextmod='<a class="btn btn-primary" href="index.html">%s</a>'%ui["more_levels"]
        done_extra='<p class="soft">%s</p>'%ui["all_done"] if lvl["id"]==max(L["id"] for L in levels if L["status"]=="live") and False else ""
    page = TEMPLATE.format(
        htmllang=htmllang, fonts=FONTS, css=CSS+EXTRA_CSS, gauge=GAUGE,
        lang_href=lang_href_for("module-%d.html"%m["n"]), lang_label=ui["lang_label"],
        level_name=lvl["name"], level_slug=lvl["slug"], level_id=lvl["id"],
        lesson_word=ui["lesson_word"], of_word=ui["of_word"], pos=pos, count=count, min=ui["min"], mins=m["mins"],
        title=m["title"], subtitle=m["subtitle"], in_module=ui["in_module"], in_items=in_items,
        k_problem=ui["k_problem"], hook_title=m["hook_title"], hook=m["hook"],
        k_analogy=ui["k_analogy"], analogy_name=m["analogy_name"], analogy=m["analogy"], analogy_after=m["analogy_after"],
        k_how=ui["k_how"], how_title=m["how_title"], how=m["how"],
        k_foryou=ui["k_foryou"], foryou_title=m["foryou_title"], foryou=m["foryou"],
        k_takeaway=ui["k_takeaway"], takeaway_h1=ui["takeaway_h1"], takeaway=m["takeaway"], takeaway_after=ui["takeaway_after"],
        k_quiz=ui["k_quiz"], quiz_html=quiz_html,
        k_complete=ui["k_complete"], done_perfect=ui["done_perfect"], next_teaser=m["next_teaser"], done_extra=done_extra,
        back=ui["back"], start=ui["start"], nextmod_btn=nextmod, back_to_level=ui["back_to_level"].format(lvl=lvl["name"]),
        gid=m["n"], explains_js=explains_js,
        j_levelname=js_str(lvl["name"]), j_step=js_str(ui["step"]), j_of=js_str(ui["of"]),
        j_complete=js_str(ui["complete"]), j_start=js_str(ui["start"]), j_cont=js_str(ui["cont"]), j_finish=js_str(ui["finish"]),
        j_done_perfect=js_str(ui["done_perfect"]), j_done_plain=js_str(ui["done_plain"]),
        j_score_pre=js_str(ui["score_pre"]), j_score_mid=js_str(ui["score_mid"]),
        j_score_perfect=js_str(ui["score_perfect"]), j_score_imperfect=js_str(ui["score_imperfect"]),
    )
    return page.replace("<!--SUGGEST-->", render_suggest(ui, "module-%d"%m["n"], htmllang))

def render_levelhub(lvl, modules_by_n, ui, htmllang, lang_href_for):
    cards=""
    for n in lvl["modules"]:
        m=modules_by_n[n]; pos=lvl["modules"].index(n)+1
        cards+=('<a class="mcard" href="module-%d.html" data-mod="%d"><div class="mnum">%d</div>'
                '<div class="mbody"><div class="mtitle">%s</div>'
                '<div class="mmeta"><span class="manalogy">%s</span> · %d %s</div></div>'
                '<div class="mcheck" aria-hidden="true"></div></a>')%(
                n,n,pos,m["title"].replace("&amp;","&"),m["analogy_name"],m["mins"],ui["min"])
    return LEVELHUB.format(
        htmllang=htmllang, fonts=FONTS, css=CSS+EXTRA_CSS, gauge=GAUGE,
        lang_href=lang_href_for("%s.html"%lvl["slug"]), lang_label=ui["lang_label"],
        all_levels=ui["all_levels"], level_word=ui["level_word"], level_id=lvl["id"],
        level_name=lvl["name"], level_tagline=lvl["tagline"], cards=cards,
        mods_js="["+",".join(str(n) for n in lvl["modules"])+"]", j_level_prog=js_str(ui["level_prog"]),
    )

def render_landing(levels, ui, htmllang, lang_href_for):
    cards=""
    live_mods=[]
    for L in levels:
        if L["status"]=="live": live_mods+=L["modules"]
        if L["status"]=="live":
            cards+=('<a class="lcard" href="%s.html" data-mods="%s"><div class="lnum">%d</div>'
                    '<div class="lbody"><div class="lname">%s</div><div class="ltag">%s</div>'
                    '<div class="lmeta">%d %s</div></div>'
                    '<div class="lring"><span></span></div></a>')%(
                    L["slug"], ",".join(str(n) for n in L["modules"]), L["id"], L["name"], L["tagline"], len(L["modules"]), ui["modules_word"])
        else:
            cards+=('<span class="lcard soon"><div class="lnum">%d</div>'
                    '<div class="lbody"><div class="lname">%s</div><div class="ltag">%s</div>'
                    '<div class="lmeta soonlbl">%s</div></div></span>')%(
                    L["id"], L["name"], L["tagline"], ui["coming_soon"])
    page = LANDING.format(
        htmllang=htmllang, fonts=FONTS, css=CSS+EXTRA_CSS+LANDING_CSS, gauge=GAUGE, hub_title=ui["hub_title"],
        lang_href=lang_href_for("index.html"), lang_label=ui["lang_label"],
        landing_eyebrow=ui["landing_eyebrow"], landing_h1=ui["landing_h1"], landing_tagline=ui["landing_tagline"],
        o1=ui["o1"], o2=ui["o2"], o3=ui["o3"], facts_pill=ui["facts_pill"], why_link=ui["why_link"],
        level_cards=cards, glossary_title=ui["glossary_title"], glossary_sub=ui["glossary_sub"],
        prof_title=ui["prof_title"], prof_sub=ui["prof_sub"],
        live_js="["+",".join(str(n) for n in live_mods)+"]", j_overall=js_str(ui["overall_prog"]),
    )
    return page.replace("<!--SUGGEST-->", render_suggest(ui, "landing", htmllang))

ABOUT = """<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#FAF5EC">
<title>{about_title}, Me, Myself &amp; AI</title>
{fonts}
<style>{css}</style>
</head>
<body>
<header>
  <div class="topline">
    <a class="brand" href="index.html">Me, Myself <span class="amp">&amp;</span> AI</a>
    <span class="rightgrp"><a class="lang" href="{lang_href}">{lang_label}</a></span>
  </div>
  <div class="gauge" aria-hidden="true">{gauge}<div class="ptrack"><div class="pfill" style="width:100%"></div></div></div>
</header>
<main>
  <a class="backlink" href="index.html">← {all_levels}</a>
  <div class="hero"><p class="eyebrow">{about_eyebrow}</p><h1>{about_h1}</h1></div>
  <div class="about-body">{about_body}</div>
  <a class="btn btn-primary" href="index.html" style="margin-top:8px">{about_cta}</a>
</main>
</body>
</html>
"""

def render_about(ui, htmllang, lang_href_for):
    return ABOUT.format(
        htmllang=htmllang, fonts=FONTS, css=CSS+EXTRA_CSS+ABOUT_CSS, gauge=GAUGE,
        about_title=ui["about_title"], lang_href=lang_href_for("about.html"), lang_label=ui["lang_label"],
        all_levels=ui["all_levels"], about_eyebrow=ui["about_eyebrow"], about_h1=ui["about_h1"],
        about_body=ui["about_body"], about_cta=ui["about_cta"],
    )

def build(lang_mod, subdir, lang_href_for):
    base = OUT if subdir=="" else os.path.join(OUT, subdir)
    os.makedirs(base, exist_ok=True)
    modules_by_n={m["n"]:m for m in lang_mod.MODULES}
    for m in lang_mod.MODULES:
        open(os.path.join(base,"module-%d.html"%m["n"]),"w").write(
            render_module(m, lang_mod.UI, lang_mod.LEVELS, "es" if subdir else "en", lang_href_for))
    for L in lang_mod.LEVELS:
        if L["status"]=="live":
            open(os.path.join(base,"%s.html"%L["slug"]),"w").write(
                render_levelhub(L, modules_by_n, lang_mod.UI, "es" if subdir else "en", lang_href_for))
    open(os.path.join(base,"index.html"),"w").write(
        render_landing(lang_mod.LEVELS, lang_mod.UI, "es" if subdir else "en", lang_href_for))
    open(os.path.join(base,"glossary.html"),"w").write(
        render_glossary(lang_mod.GLOSSARY, lang_mod.UI, "es" if subdir else "en", lang_href_for))
    open(os.path.join(base,"about.html"),"w").write(
        render_about(lang_mod.UI, "es" if subdir else "en", lang_href_for))

# --- Quiz answer variety -------------------------------------------------
# Spread each module's 3 correct answers across positions A/B/C so no module
# (or level) clusters on one letter. Applied identically to EN + ES by moving
# each language's correct option to the same target index, keeping them aligned.
QUIZ_TARGETS = [[0,1,2],[1,2,0],[2,0,1],[0,2,1],[1,0,2],[2,1,0]]

def normalize_quiz(en_mods, es_mods):
    es_by_n = {m["n"]: m for m in es_mods}
    for em in en_mods:
        sm = es_by_n[em["n"]]
        pat = QUIZ_TARGETS[(em["n"]-1) % len(QUIZ_TARGETS)]
        for j, eq in enumerate(em["quiz"]):
            sq = sm["quiz"][j]
            assert eq["a"] == sq["a"], "EN/ES answer index drift at module %d q%d" % (em["n"], j)
            t = min(pat[j], len(eq["opts"]) - 1)
            for q in (eq, sq):
                c = q["a"]
                if c != t:
                    q["opts"][c], q["opts"][t] = q["opts"][t], q["opts"][c]
                    q["a"] = t

normalize_quiz(bili_en.MODULES, bili_es.MODULES)

# EN at root links to es/<same>; ES in /es/ links to ../<same>
build(bili_en, "", lambda fn: "es/"+fn)
build(bili_es, "es", lambda fn: "../"+fn)

print("Built. root:", sorted(os.listdir(OUT)))
print("es:", sorted(os.listdir(os.path.join(OUT,"es"))))
