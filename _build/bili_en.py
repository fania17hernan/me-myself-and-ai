# -*- coding: utf-8 -*-
"""English content + UI strings."""

UI = {
 "lang_label":"Español","hub_title":"Me, Myself &amp; AI, AI foundations for smart professionals",
 "module_word":"Module","min":"min","in_module":"In this module",
 "k_problem":"The problem","k_analogy":"The core analogy","k_how":"How it actually works",
 "k_foryou":"What this means for you","k_takeaway":"One takeaway","takeaway_h1":"Say it to a colleague",
 "takeaway_after":"That's the whole module in one sentence. If you can explain this to someone at work tomorrow, it stuck. Quick check, three questions, no grades, just proof it landed.",
 "k_quiz":"Quick check · 3 questions","k_complete":"Module complete",
 "start":"Start the module","cont":"Continue","finish":"Finish","back":"Back",
 "step":"Step","of":"of","complete":"Complete",
 "done_perfect":"Full tank. 🎉","done_plain":"Module complete 🎉",
 "score_pre":"You got ","score_mid":" of 3 on the quick check",
 "score_perfect":", perfect drive.","score_imperfect":", and the misses taught you something, which is the point.",
 "course_home":"Course home","next_btn":"Start Module {n} →","back_home_btn":"Back to course home",
 "all_done":"You've finished all five foundations. Proud of you.",
 # hub
 "hub_eyebrow":"AI foundations · 5 short modules",
 "hub_h1":"Finally, AI that makes sense for <em>your</em> work.",
 "hub_tagline":"Five sticky ideas. One analogy each. About 10 minutes a module, no jargon, no engineering degree required.",
 "hub_prog":"{d} of 5 done",
 "hub_footer":"Built for capable professionals who keep hearing about AI and want the part that actually matters. Start with Module 1, the rest build on it.",
 # landing + levels
 "landing_eyebrow":"AI literacy · built for professionals",
 "landing_h1":"What do you want to understand today?",
 "landing_tagline":"Understand AI well enough to actually use it at work, in plain language, one analogy at a time.",
 "o1":"Spot when AI is bluffing before you forward its work to your boss.",
 "o2":"Get real value from the tools you (or your team) already pay for.",
 "o3":"Hold your own in any AI conversation at work.",
 "facts_pill":"19 lessons · ~10 min each · always free · English &amp; Spanish",
 "why_link":"Why I built this →",
 # About page
 "about_title":"About","about_eyebrow":"About","about_h1":"Why I built this","about_cta":"Start the course →",
 "about_body":"<p class=\"lead\">Hi, I'm Stephanie. 👋</p>"
   "<p>I've spent my career in product, program, and change management, leading transformation and cross-functional initiatives across retail, healthcare, automotive tech, and global travel. My work has always lived at the messy intersection of new technology and the people being asked to adopt it.</p>"
   "<p>If there's one thing I've learned helping large companies change, it's that the technology is rarely the hard part. The hard part is supporting people through it, and the most common failure I see is organizations rolling out tools without ever teaching their workforce how to actually use them. In the era of AI, that gap is widening fast: the pace is relentless, and a lot of genuinely capable people feel left behind.</p>"
   "<p>Here's what the hype misses. Companies can deploy AI, but they can't scale it without their human experts. People are the ones who feed it institutional knowledge, validate what it produces, improve it through feedback loops, orchestrate it, and point it in the right direction. The real value was never AI replacing you, it's you becoming the <em>expert in the loop</em>, directing it. That's exactly why it matters that the humans stay the experts.</p>"
   "<p>So this course starts small, with the tasks that feel almost too simple to hand to AI, but that quietly save you hours of tedious work, and builds until you're tackling more of your day with confident, guided assistance.</p>"
   "<p><strong>Me, Myself &amp; AI</strong> is everything I wish I could have handed those teams on day one. Plain language, one analogy at a time, in English and Spanish. No jargon, no gatekeeping, just the part that helps you stay the expert as the tools get smarter.</p>",
 "level_word":"Level","lesson_word":"Lesson","of_word":"of","modules_word":"lessons",
 "coming_soon":"Coming soon","all_levels":"All levels",
 "level_prog":"{d} of {n} done","overall_prog":"{d} of {t} lessons done",
 "next_module":"Next lesson →","more_levels":"Explore more levels →","back_to_level":"Back to {lvl}",
 "glossary_title":"Glossary","glossary_sub":"Every term, in plain words. Look up anything, any time.",
 "prof_title":"By profession","prof_sub":"Lessons tuned to your job, student, PM, teacher, realtor and more. (Coming soon)",
 # glossary page
 "glossary_h1":"Glossary","glossary_intro":"Every term you'll bump into, in plain words, each tied to its analogy. Tap a card to jump to the lesson.",
 "glossary_search_ph":"Search a term…","glossary_analogy_label":"Think of it as","glossary_learn":"Learn it →","glossary_none":"No terms match that search.",
 # suggest-a-topic
 "suggest_heading":"Want a topic we haven't covered yet?",
 "suggest_sub":"Tell me what you'd like to learn next, your ideas shape what I build.",
 "suggest_ph":"e.g. How do I write better prompts for emails?",
 "suggest_email_ph":"Email (optional, only if you'd like a reply)",
 "suggest_button":"Send it",
 "suggest_thanks":"Got it, thank you! 🙌 Your idea is in.",
 "suggest_error":"Hmm, that didn't send. Mind trying again in a moment?",
}

MODULES = [
{
 "n":1,"mins":9,"title":"Tokens &amp; Rate Limits: The Gas Tank","analogy_name":"The Gas Tank",
 "subtitle":"Why does AI cut off mid-answer? Why did it just… stop? By the end of this module you'll know exactly why, and how to never get stranded again.",
 "in_module":["One analogy you'll never forget (the gas tank)","What a \"token\" actually is, in plain English","Three habits that make AI cheaper, faster, and less frustrating"],
 "hook_title":"It died mid-sentence.",
 "hook":"<p>True story: I was deep in a real project, on a roll, AI assistant doing exactly what I needed. I pasted in one more big chunk of work and hit enter.</p><p>Nothing. Then a timeout error. Then, when it finally answered, it stopped <em>mid-sentence</em>, like someone yanked the cord out of the wall.</p><p>If that's ever happened to you, you probably assumed you did something wrong, or the tool was broken. Neither. Something very predictable happened, and once you can see it, you can work around it every single time.</p>",
 "analogy":"<p>Think of tokens like gas in a tank. Every word you type burns a little gas. Every word the AI writes back burns gas too. When the tank hits empty, the car stops, even mid-sentence, even on the highway.</p><p style=\"margin-bottom:0\">And <strong>rate limits</strong>? That's the gas station that only lets you fill up so many times per hour. Come back too often and they make you wait.</p>",
 "analogy_after":"<p>That's the whole mental model. Everything else in this module is just details about how big the tank is and how the gas gets burned.</p>",
 "how_title":"What's actually in the tank",
 "how":"<p>A <span class=\"term\">token</span> <span class=\"soft\">(plain English: a chunk of a word)</span> is the unit AI actually reads and writes. A token is roughly three-quarters of a word, so 100 words is about 130 tokens. Close enough: <strong>words ≈ tokens</strong>.</p><h3>Both directions burn gas</h3><p>Here's what surprises people: it's not just what you type. <strong>Input</strong> (your message, plus everything earlier in the conversation) and <strong>output</strong> (the AI's reply) both count. Ask a short question that needs a long answer? That burns plenty of fuel too.</p><h3>Why long conversations get slow and pricey</h3><p>Each time you send a message, the AI re-reads the whole conversation so far. So message 40 in a long chat burns way more gas than message 2, you're hauling the entire trip history with you.</p><h3>Every car has a different tank</h3><p>Claude, ChatGPT, and Gemini each have different tank sizes and different gas-station rules, and they change them often. The sizes don't matter, the <em>behavior</em> does: every tool has a limit, and every tool acts weird the same way when you hit it.</p><h3>What \"empty\" looks like</h3><ul><li><strong>Truncation</strong>, the answer cuts off mid-sentence (out of gas)</li><li><strong>Timeout or error</strong>, it gives up before finishing (engine flooded)</li><li><strong>\"Try again later\"</strong>, you hit the rate limit (gas station says come back in an hour)</li></ul>",
 "foryou_title":"Drive like you know there's a tank",
 "foryou":"<h3>1. Break big tasks into trips</h3><p>Don't paste a 40-page document and ask for everything at once. Ask for the summary first. Then the risks. Then the rewrite. Three short trips beat one stalled-out haul.</p><h3>2. Start fresh when you change topics</h3><p>A new chat is a full tank. If you're done with the budget analysis and moving to the offsite agenda, open a new conversation instead of dragging the old one along.</p><h3>3. When it cuts off, just say \"continue\"</h3><p>Truncation isn't failure, the tank ran dry mid-answer. Reply \"please continue\" and it picks up where it stopped. Works almost every time.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Take one big task you'd normally dump in a single message and split it into three smaller asks. Notice the difference in speed and quality.</p></div>",
 "takeaway":"AI has a gas tank. Long conversations burn more fuel. Break big tasks into trips.",
 "quiz":[
   {"q":"1. Your AI's answer stops mid-sentence. What most likely happened?","a":1,"opts":["It got confused by your question","It ran out of tokens, the tank hit empty","The internet connection dropped"],"good":"Exactly. Out of gas, even mid-sentence. Reply “continue” and it refuels.","bad":"Not quite, here's the thing: it ran out of tokens mid-answer. The fix is simple: reply “please continue.”"},
   {"q":"2. Which burns fuel (tokens)?","a":2,"opts":["Only what you type","Only what the AI writes back","Both, input and output"],"good":"Right, both directions burn fuel. Short question, long answer? Still pricey.","bad":"Almost, both count. Your input AND the AI's output burn tokens, which is why both long questions and long answers drain the tank."},
   {"q":"3. You're switching from a budget analysis to planning an offsite. Best move?","a":0,"opts":["Start a new chat, fresh tank for a new trip","Keep the same chat so it remembers everything","Ask it to type faster"],"good":"Fresh tank, fresh trip. New topic = new chat is the single best habit from this module.","bad":"Tempting, but dragging the old conversation along burns fuel on every message. New topic = new chat = full tank."}
 ],
 "next_teaser":"<strong>Next up: Module 2: The Whiteboard.</strong> Why does AI forget what you told it 20 messages ago? (Hint: it's not getting dumber.)"
},
{
 "n":2,"mins":8,"title":"Context Windows: The Whiteboard","analogy_name":"The Whiteboard",
 "subtitle":"Why does AI forget what you told it 20 messages ago? It's not getting dumber, and the fix takes ten seconds.",
 "in_module":["What a \"context window\" actually is","Why long chats lose the thread","Simple ways to keep AI on track"],
 "hook_title":"“Wait, I already told you that.”",
 "hook":"<p>You explained the whole project at the start, the client, the deadline, the tone you wanted. Forty messages later, the AI has forgotten all of it. It's suggesting things you ruled out an hour ago.</p><p>It feels like it stopped listening. Like it got lazy, or dumber. It didn't. Something very specific happened, and once you see it, the fix takes about ten seconds.</p>",
 "analogy":"<p>AI doesn't have a memory, it has a whiteboard. Everything written on the board right now is everything it knows. Your messages, its replies, all of it crammed onto one board.</p><p style=\"margin-bottom:0\">When the board fills up, the oldest notes get wiped to make room for new ones. It's not getting dumber. The board is just full.</p>",
 "analogy_after":"<p>That's the whole idea. “Forgetting” isn't a personality flaw, it's an erased corner of a whiteboard.</p>",
 "how_title":"How the board fills up",
 "how":"<p>The <span class=\"term\">context window</span> <span class=\"soft\">(plain English: the whiteboard)</span> is everything the AI can see at once, the entire conversation so far, sitting in front of it.</p><h3>When it's full, old notes vanish</h3><p>The AI doesn't “recall” earlier parts of the chat. It reads whatever is currently on the board and responds. Once something scrolls off the top, it's gone, unless you write it down again.</p><h3>This isn't human memory</h3><p>You remember a conversation from last Tuesday. AI starts every single reply by reading only what's on the board right now. By default, nothing carries over between separate chats at all.</p><h3>System prompts = permanent marker</h3><p>Some instructions get written in permanent marker, they stay visible no matter how full the board gets. That's what a <strong>system prompt</strong>, or the setup inside a Claude Project or custom GPT, actually is.</p><h3>Tools that give you a bigger board</h3><p>Features like Claude Projects, custom GPTs, and “memory” settings let you pin important notes so they don't get wiped. Useful once you're past the basics.</p>",
 "foryou_title":"Keep what matters on the board",
 "foryou":"<h3>1. Restate the important stuff</h3><p>When a chat gets long, don't assume it remembers. Paste the key facts again: “Reminder: deadline is Friday, audience is execs, keep it under one page.” You're rewriting the note before it gets wiped.</p><h3>2. New topic, new board</h3><p>Start a fresh chat when you switch subjects. A clean board with only relevant notes beats a cluttered one full of stuff that no longer matters.</p><h3>3. Put recurring context in permanent marker</h3><p>If you find yourself re-explaining the same background every time, put it in a Project or custom instructions once, so it's always on the board without you retyping it.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Next time a long chat starts drifting, paste a one-line reminder of the key facts. Watch it snap back on track.</p></div>",
 "takeaway":"AI has a whiteboard, not a memory. Keep important context visible.",
 "quiz":[
   {"q":"1. Your AI “forgets” something you said early in a long chat. Why?","a":1,"opts":["It's malfunctioning","The board filled up and earlier notes got wiped","It's ignoring you on purpose"],"good":"Exactly, the whiteboard filled and the oldest notes were erased. Totally normal.","bad":"Not quite, nothing's broken. The whiteboard filled up, so the earliest notes got wiped to make room."},
   {"q":"2. A long chat is losing the thread. Best fix?","a":1,"opts":["Keep repeating the exact same question","Restate the key facts so they're back on the board","Type in all caps so it pays attention"],"good":"Right, rewrite the note. Restating key context puts it back in front of the AI.","bad":"The fix is to restate the key facts, that puts the important notes back on the board where the AI can see them."},
   {"q":"3. Where does a Project instruction or system prompt live?","a":0,"opts":["In permanent marker, always visible","On a sticky note that falls off","Nowhere, it's deleted instantly"],"good":"Yes, permanent marker. It stays on the board no matter how full things get.","bad":"Think permanent marker, system prompts and Project setups stay visible no matter how full the board gets."}
 ],
 "next_teaser":"<strong>Next up: Module 3: The Test Drive vs. the Lease.</strong> Should you actually pay for AI, or is the free version fine?"
},
{
 "n":3,"mins":9,"title":"Free vs. Paid: The Test Drive vs. the Lease","analogy_name":"The Test Drive vs. the Lease",
 "subtitle":"Should you upgrade? Are you missing something on the free tier? Here's how to decide without wasting $20.",
 "in_module":["What you actually get free vs. paid","The signs it's truly time to upgrade","The ROI math for busy people"],
 "hook_title":"That little “Upgrade” button.",
 "hook":"<p>It sits there in the corner, quietly implying you're using the lite version, that the real magic is locked behind $20 a month. So you wonder: am I missing the good stuff?</p><p>Mostly, you're not. The free tier is genuinely powerful. But there's a clear moment when paying is worth it, and a lot of FOMO that isn't. Let's sort out which is which.</p>",
 "analogy":"<p>Free tier is a test drive. Same car, same engine, but you only go around the block, and someone from the dealership is riding along watching.</p><p style=\"margin-bottom:0\">Paid is the full lease: longer drives, the premium trim, no one hovering. And here's the thing, you don't sign a lease before you know you actually like driving the car.</p>",
 "analogy_after":"<p>So the question isn't “is paid better?” It's “have I driven enough to know I need the lease?”</p>",
 "how_title":"What you're actually paying for",
 "how":"<p>The most important myth to kill: the free tier is <em>not</em> a crippled demo. You get a genuinely capable model that handles most everyday tasks well.</p><h3>What's usually gated behind paid</h3><ul><li>The newest, smartest models</li><li>More messages before you hit limits</li><li>File and image uploads, longer responses</li><li>Faster speeds when servers are busy</li><li>Extras: voice, image generation, and automation/API access</li></ul><h3>The “hovering” part</h3><p>Free tiers may use your conversations to improve the product, and they cut you off sooner during busy hours. Paid generally means more privacy controls and fewer interruptions.</p><h3>The plans change constantly</h3><p>Claude, ChatGPT, and Gemini reshuffle what's free all the time. Don't memorize today's comparison chart, learn the signal for when <em>you</em> need more.</p>",
 "foryou_title":"How to decide",
 "foryou":"<h3>1. Start free, genuinely</h3><p>Drafting, summarizing, brainstorming, rewriting: the free tier does all of it. Use it for real work until something actually gets in your way.</p><h3>2. Upgrade when you hit a wall daily</h3><p>The real signal isn't the ad, it's friction. Hitting message limits every day, needing to analyze files, wanting the newest model for serious work. That's when the lease pays off.</p><h3>3. Do the two-hours math</h3><p>For a small business owner: $20/month is about one coffee a week. If the tool saves you two hours a week, it's paid for itself many times over. If it doesn't, cancel. There's no lease penalty.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Notice the next time the free tier annoys you, a limit, a missing feature. Write down what it was. Two of those in a week is your upgrade signal.</p></div>",
 "takeaway":"Start free. Upgrade when the limits annoy you, that's the sign you're actually using it.",
 "quiz":[
   {"q":"1. When should you upgrade to a paid plan?","a":1,"opts":["Immediately, to get the “real” version","When you hit limits daily or need a gated feature","Never, paid is a scam"],"good":"Exactly, let friction be the signal, not the upgrade button.","bad":"The signal is friction: upgrade when you're hitting limits regularly or need a feature that's locked, not just because the button's there."},
   {"q":"2. Is the free tier a crippled version?","a":1,"opts":["Yes, it's basically a demo","No, same core model, with some features gated","Only on weekends"],"good":"Right, same engine. You're getting a genuinely capable model for free.","bad":"Not really, it's the same core model. Paid mostly unlocks extras and higher limits, not a smarter brain."},
   {"q":"3. An owner wonders if $20/mo is worth it. Best way to decide?","a":2,"opts":["Ask a friend what they do","Flip a coin","Compare the cost to the hours it saves you"],"good":"Yes, hours saved vs. cost. If it saves two hours a week, it's an easy yes.","bad":"Best move: compare $20 to the hours it saves you each week. Save two hours? It's paid for itself."}
 ],
 "next_teaser":"<strong>Next up: Module 4: The Confident Intern.</strong> Why AI sometimes makes things up, and sounds completely sure doing it."
},
{
 "n":4,"mins":10,"title":"Hallucination: The Confident Intern","analogy_name":"The Confident Intern",
 "subtitle":"The AI gave you wrong info and sounded totally sure. Can you trust it? Here's exactly when to double-check.",
 "in_module":["Why AI makes things up","When the risk is highest","How to catch it before it bites you"],
 "hook_title":"It made up a study. Confidently.",
 "hook":"<p>It handed you a statistic and a source. Clean, specific, exactly what you needed. You almost dropped it into your deck. Then you went to find the study, and it doesn't exist.</p><p>The unsettling part isn't that it was wrong. It's <em>how sure it sounded</em>. Same confident tone it uses when it's right. Once you understand why, you'll never get fooled the same way again.</p>",
 "analogy":"<p>AI is a brilliant intern on their first day. They've read everything ever written, so they'll answer any question with total confidence.</p><p style=\"margin-bottom:0\">But they've never actually <em>done</em> the job. So sometimes they'll make up a statistic or cite a paper that doesn't exist, not to deceive you, but because they're predicting what a good answer <em>sounds like</em>, not looking it up.</p>",
 "analogy_after":"<p>Brilliant, eager, and occasionally, confidently wrong. That's the intern, and that's your AI.</p>",
 "how_title":"Why it happens",
 "how":"<p>An AI generates the next most likely word, over and over. Usually the most likely words happen to be true. Sometimes the most natural-<em>sounding</em> answer just isn't real. That's a <span class=\"term\">hallucination</span> <span class=\"soft\">(plain English: a confident made-up answer)</span>.</p><h3>It's structural, not a bug</h3><p>Making things up is baked into how the technology works, it predicts, it doesn't fact-check. Newer models do it less, but none are immune.</p><h3>Where the risk is highest</h3><ul><li>Specific facts and exact numbers</li><li>Citations, sources, quotes, and links</li><li>Recent events (especially after the model's training cutoff)</li><li>Anything niche, obscure, or rarely written about</li></ul><h3>The trap: it sounds the same either way</h3><p>The AI is just as fluent and confident when it's wrong as when it's right. Confidence is not a signal of accuracy. That single fact will protect you more than anything else in this course.</p>",
 "foryou_title":"How to catch it",
 "foryou":"<h3>1. Treat it as a first draft, never the final word</h3><p>For facts, it's a great starting point and a terrible place to stop. Use it to get moving, then verify before anything leaves your hands.</p><h3>2. Make it show its work</h3><p>Ask: “cite your sources” and “tell me what you're not sure about.” Then actually click the sources to confirm they exist and say what it claims.</p><h3>3. Never go solo on high-stakes calls</h3><p>Legal, medical, financial, or anything with real consequences, the AI is a research assistant, not the expert who signs off. Confirm with a qualified human.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Next time AI gives you a fact or a source, pause and verify it before you use it. Build the reflex now, while the stakes are low.</p></div>",
 "takeaway":"AI is a confident intern. Always check the work before you sign off on it.",
 "quiz":[
   {"q":"1. Why does AI sometimes “make things up”?","a":1,"opts":["It's broken","It predicts likely-sounding words rather than looking up truth","It's lying on purpose"],"good":"Exactly, it predicts what sounds right, which is usually but not always true.","bad":"It's not malice or a glitch, it predicts the next likely-sounding word instead of looking facts up. Usually right, sometimes not."},
   {"q":"2. When is hallucination risk highest?","a":1,"opts":["When writing a poem or brainstorming","With specific facts, numbers, and citations","Never, modern AI is always right"],"good":"Right, facts, numbers, and sources are the danger zone. Always verify those.","bad":"Highest risk is with specifics: exact facts, numbers, citations, and recent events. Creative tasks are much safer."},
   {"q":"3. AI gives a confident answer to a legal question. Best move?","a":2,"opts":["Trust it, it sounded sure","Ask the same question again","Verify with a qualified professional before acting"],"good":"Yes, confidence isn't accuracy. High stakes means confirm with a real expert.","bad":"Confidence isn't accuracy. For legal, medical, or financial calls, verify with a qualified professional before acting."}
 ],
 "next_teaser":"<strong>Next up: Module 5: The Sous Chef.</strong> Turning everything you've learned into your first real AI habit."
},
{
 "n":5,"mins":10,"title":"Your First AI Workflow: The Sous Chef","analogy_name":"The Sous Chef",
 "subtitle":"You get it in theory. Now here's how to actually use AI for real work, starting with one task this week.",
 "in_module":["How to pick your first use case","A bad prompt vs. a good one","The habit that makes it stick"],
 "hook_title":"Okay… now what do I type?",
 "hook":"<p>You understand tokens, whiteboards, and confident interns. But the blank chat box still stares back at you. Cursor blinking. “Now what do I actually <em>do</em> with this?”</p><p>This is where most people quit, not because AI is hard, but because nobody showed them the first move. So let's make the first move dead simple.</p>",
 "analogy":"<p>AI is your sous chef, not your head chef. You decide the dish, the flavor, who's eating. You're in charge of the vision.</p><p style=\"margin-bottom:0\">The sous chef preps the ingredients, handles the repetitive chopping, and makes you faster. But you set the direction, and you always taste the food before it leaves the kitchen.</p>",
 "analogy_after":"<p>Keep that hierarchy and AI becomes genuinely useful. Flip it, letting the sous chef run the kitchen, and that's where people get burned.</p>",
 "how_title":"Your first dish, step by step",
 "how":"<p>Don't try to “use AI” in the abstract. Pick <strong>one</strong> use case and actually run it.</p><h3>Pick one</h3><p>Email drafting, meeting prep, summarizing a long document, or brainstorming. Choose the one thing you do often that drains you.</p><h3>Bad prompt vs. good prompt</h3><p><span class=\"soft\">Bad:</span> “Write an email.”, you'll get something generic and useless.</p><p><span class=\"soft\">Good:</span> “Write a friendly 3-sentence email to a client moving our meeting from Tuesday to Thursday. Apologize briefly and offer two new times.” Same task, wildly better result. The difference is the prep you handed your sous chef.</p><h3>The editing mindset</h3><p>AI hands you a draft. Your job is to make it yours, trim it, fix it, add your voice. The draft is the prep work, not the plated dish.</p><h3>Where people get stuck</h3><p>Expecting a perfect result on the first try. Real use is a quick back-and-forth: draft, nudge, refine. Thirty seconds, not one magic prompt.</p>",
 "foryou_title":"Build the habit",
 "foryou":"<h3>1. Choose your one task today</h3><p>The recurring thing that drains you, that's your starting dish. Don't shop for more; just pick it.</p><h3>2. Give it the full recipe</h3><p>Who it's for, the tone, the length, the key facts. The more context you hand over, the better what comes back. Specifics in, quality out.</p><h3>3. Ten minutes a day, one week</h3><p>Use AI for that single task, ten minutes a day, for a week, before adding anything new. Habit first, breadth later. That's how it actually sticks.</p><div class=\"card\"><h3 style=\"margin-top:0\">Your assignment</h3><p style=\"margin-bottom:0\">Pick your one task right now. Tomorrow morning, spend ten minutes doing it with AI. That's the whole start.</p></div>",
 "takeaway":"You're the head chef. AI is your sous chef. Set the vision, delegate the prep.",
 "quiz":[
   {"q":"1. Best way to start using AI for real work?","a":1,"opts":["Try to automate everything at once","Pick one use case and practice it daily","Wait until you've mastered all the theory"],"good":"Exactly, one use case, practiced daily. Depth beats breadth at the start.","bad":"Start small: pick one use case and practice it daily. Trying to do everything at once is how people give up."},
   {"q":"2. What makes a good prompt?","a":1,"opts":["Keeping it as short as possible","Specific details, audience, tone, length, facts","Using fancy technical words"],"good":"Right, specifics are the prep you hand your sous chef. More context, better dish.","bad":"Good prompts are specific: audience, tone, length, key facts. That's the prep that gets you a usable result."},
   {"q":"3. The AI's first draft isn't perfect. What does a head chef do?","a":2,"opts":["Give up, AI doesn't work","Publish it exactly as-is","Edit and refine it until it's yours"],"good":"Yes, you taste and adjust. The draft is prep; you plate the final dish.","bad":"A head chef tastes and adjusts, edit the draft until it's yours. The first draft is prep, not the final plate."}
 ],
 "next_teaser":"<strong>That's the foundation. 🍽️</strong> You can now explain AI better than most people you work with, gas tanks, whiteboards, interns, and all. Go cook something."
},
{
 "n":6,"mins":8,"title":"Chats vs. Projects: The Phone Call &amp; the Office","analogy_name":"The Phone Call vs. the Office",
 "subtitle":"You keep re-explaining the same background every time you open a new chat. There's a place where the AI just… keeps it. Here's the difference.",
 "in_module":["Why a normal chat forgets everything","What a \"Project\" actually is","When to use each, with examples"],
 "hook_title":"Starting over. Again.",
 "hook":"<p>Monday you explained your client, your goals, your style. Tuesday you opened a new chat and pasted it all again. Wednesday, again. By Friday you're basically the AI's personal assistant, re-briefing it every morning.</p><p>There's a feature built exactly for this, and most people never touch it because no one told them what it's for.</p>",
 "analogy":"<p>A regular chat is a <strong>phone call</strong>. Great for a quick question, but when you hang up, it's over. Nothing's saved. Next time you call, you start from scratch.</p><p style=\"margin-bottom:0\">A <strong>Project</strong> is a <strong>dedicated office</strong>. Your files, your notes, your standing instructions all live on the desk. You walk in, and everything for that one job is already there, every single time.</p>",
 "analogy_after":"<p>Remember the whiteboard from Level 1? A phone call is a whiteboard that gets wiped when you hang up. A Project is a room where the important notes stay on the wall.</p>",
 "how_title":"What actually lives in the office",
 "how":"<p>A <span class=\"term\">Project</span> <span class=\"soft\">(in plain words: a saved workspace)</span> is a room you set up once and keep coming back to.</p><h3>Three things live there</h3><ul><li><strong>Reference files</strong>, the documents the AI should always have on hand</li><li><strong>Standing instructions</strong>, your tone, rules, and goals, written once</li><li><strong>Every chat for that job</strong>, all in one place, not scattered</li></ul><h3>Each chat inside still has its own whiteboard</h3><p>You'll still start fresh conversations inside the office, but now they all share the same desk of context. You set up the room once; the briefings stop.</p><h3>Different names, same idea</h3><p>Claude calls them Projects. ChatGPT has Projects and custom GPTs. The concept is identical: a persistent room versus a one-time call.</p>",
 "foryou_title":"Give each job a room",
 "foryou":"<h3>1. One job = one Project</h3><p>A client, a course you're taking, your book, your job search, each gets its own office so its context never bleeds together.</p><h3>2. Put the background in the room, not in every message</h3><p>Drop your reference docs and standing instructions in once. Stop re-pasting them.</p><h3>3. Quick question? Just call.</h3><p>Not everything needs an office. A one-off, \"what's a good subject line for this?\", is perfectly fine as a plain chat.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Take the one thing you re-explain most often and set it up as a Project. Next time, just walk in.</p></div>",
 "takeaway":"A chat is a phone call. A Project is an office where your context lives. Big ongoing job? Give it a room.",
 "quiz":[
   {"q":"1. You're on your fifth chat this week re-pasting the same background. Better move?","a":1,"opts":["Keep re-pasting it each time","Set up a Project so the background lives in one place","Just write shorter messages"],"good":"Exactly, set up the office once and the re-briefing stops.","bad":"The fix is a Project: set the background up once in its own room, and you stop re-pasting it every time."},
   {"q":"2. What's a plain chat best for?","a":0,"opts":["Quick, one-off questions","A long job with lots of files","Storing your reference docs"],"good":"Right, a phone call is perfect for quick one-offs.","bad":"A plain chat is the phone call, best for quick one-offs. Big ongoing work belongs in a Project."},
   {"q":"3. What can live inside a Project?","a":2,"opts":["Only one message","Nothing, it's just a label","Files, standing instructions, and all the related chats"],"good":"Yes, files, instructions, and every chat for that job, all in one room.","bad":"A Project holds your files, your standing instructions, and all the chats for that job, the whole office."}
 ],
 "next_teaser":"<strong>Next up: The Workbench.</strong> Sometimes the AI builds the actual thing, a doc, a sheet, a little app, right beside the chat. That panel has a name."
},
{
 "n":7,"mins":7,"title":"Artifacts: The Workbench","analogy_name":"The Workbench",
 "subtitle":"Sometimes the AI builds the actual thing, a document, a spreadsheet, a little app, right next to the chat. That panel has a name, and it changes how you work.",
 "in_module":["What an \"artifact\" is","Why it beats burying work in the chat","How to build real things with it"],
 "hook_title":"It built it… then it scrolled away.",
 "hook":"<p>The AI wrote you a beautiful one-pager. Then you asked two more questions, and now it's buried somewhere up in the conversation, mixed in with chit-chat. You scroll, you hunt, you copy the wrong version.</p><p>There's a better way to work, and on many tools it's already sitting right next to you.</p>",
 "analogy":"<p>Picture a <strong>workbench</strong> next to where you're talking. The conversation happens on one side; on the other, the AI <strong>builds the actual thing</strong>, and lays it on the bench where you can see it, pick it up, and change it.</p><p style=\"margin-bottom:0\">The chat is where you discuss. The workbench is where the product gets made.</p>",
 "analogy_after":"<p>Instead of your good work scrolling off into the conversation, it sits on the bench, a real object you can keep refining.</p>",
 "how_title":"How the workbench works",
 "how":"<p>An <span class=\"term\">artifact</span> <span class=\"soft\">(in plain words: a built thing on its own panel)</span> opens beside the chat whenever the AI makes something you'd want to use, not just read.</p><h3>It updates in place</h3><p>Ask for a change, \"make it shorter,\" \"add a column\", and the same artifact updates, instead of the AI dumping a whole new wall of text into the chat.</p><h3>What shows up there</h3><ul><li>Documents and letters</li><li>Spreadsheets and tables</li><li>Code, and simple working apps or web pages</li><li>Diagrams and charts</li></ul><h3>You can keep it</h3><p>Edit it, copy it, download it, or keep iterating. (Claude calls it Artifacts; ChatGPT calls it Canvas, same workbench.)</p>",
 "foryou_title":"Use the bench for anything you'll keep",
 "foryou":"<h3>1. If you'll reuse it, put it on the bench</h3><p>A reusable draft, a tracker, a template, ask the AI to build it as an artifact so it doesn't get lost.</p><h3>2. Iterate, don't restart</h3><p>\"Shorten the intro,\" \"add a column for status\", let the workbench update instead of starting a new chat.</p><h3>3. Take it with you</h3><p>When it's ready, copy or download it. The bench hands you a finished object, not a transcript to dig through.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Ask the AI to build something on the workbench, a meeting agenda, a simple tracker, then ask for two changes and watch it update in place.</p></div>",
 "takeaway":"An artifact is the workbench beside the chat, where the AI builds the actual thing, and you can edit it, keep it, and take it with you.",
 "quiz":[
   {"q":"1. The AI wrote a great doc, but it's buried in a long chat. What feature keeps it as an editable object?","a":0,"opts":["An artifact (the workbench)","A brand-new chat","The gas tank"],"good":"Exactly, the artifact lives on its own panel so it doesn't scroll away.","bad":"That's the artifact, the workbench panel that keeps your built thing separate and editable."},
   {"q":"2. You want the doc it made to be shorter. Best move?","a":1,"opts":["Start over from scratch","Ask it to update the artifact in place","Paste it into a new chat"],"good":"Right, the workbench updates the same object. No starting over.","bad":"Just ask it to update the artifact, the workbench changes the same object instead of regenerating everything."},
   {"q":"3. What typically appears on the workbench?","a":2,"opts":["Only plain chat text","Your account settings","Docs, spreadsheets, code, and simple apps"],"good":"Yes, anything you'd want to use, not just read.","bad":"The workbench is for things you'll use: documents, spreadsheets, code, and simple apps, not just chat text."}
 ],
 "next_teaser":"<strong>Next up: The Set of Keys.</strong> What if the AI could pull straight from your email or calendar, instead of you copy-pasting all day?"
},
{
 "n":8,"mins":8,"title":"Connectors: The Set of Keys","analogy_name":"The Set of Keys",
 "subtitle":"What if the AI could pull straight from your email, calendar, or Drive, instead of you copy-pasting? That's a connector. And it comes with a little responsibility.",
 "in_module":["What a connector actually does","The keys analogy, and the trust it asks for","Where to start, safely"],
 "hook_title":"Copy. Paste. Repeat.",
 "hook":"<p>You paste an email into the chat to get a summary. Then a calendar screenshot. Then three paragraphs from a doc. You're the courier, ferrying information back and forth by hand all day.</p><p>What if the AI could just go get it? It can, if you hand it a key.</p>",
 "analogy":"<p>A connector is a <strong>key to one of your other rooms</strong>. Hand the AI the key to your email, your calendar, your Drive, and it can walk in, grab what it needs, and bring it back.</p><p style=\"margin-bottom:0\">No more carrying everything by hand. But a key is a key: you only give it for rooms you trust it in.</p>",
 "analogy_after":"<p>The power is real, and so is the responsibility. The good news: you hold the keyring, and you decide which doors open.</p>",
 "how_title":"How connectors work",
 "how":"<p>A <span class=\"term\">connector</span> <span class=\"soft\">(in plain words: a link to another app)</span> ties the AI to a tool you already use, so it can work with what's in there.</p><h3>You choose which keys</h3><p>You connect app by app, on purpose. Nothing is connected until you say so, and you can take the key back any time.</p><h3>Read vs. act</h3><p>Some connectors just <strong>fetch</strong> (\"summarize today's calendar\"). Others can <strong>act</strong> (\"draft a reply\"). Know which kind you've handed over.</p><h3>Trust is the whole game</h3><p>Only connect tools you trust, and only the rooms a task actually needs. A connector should never be where you hand over banking logins or passwords, that's off-limits, full stop.</p>",
 "foryou_title":"Start small, stay in control",
 "foryou":"<h3>1. Begin with read-only wins</h3><p>\"Summarize my unread email.\" \"What's on my calendar tomorrow?\" Low risk, instantly useful.</p><h3>2. One room at a time</h3><p>Add a key when a real task needs it, not all of them at once on day one.</p><h3>3. You hold the keyring</h3><p>You can disconnect any connector whenever you want. If something feels off, take the key back.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Connect just one tool you trust, your calendar is a great start, and ask it to summarize your week.</p></div>",
 "takeaway":"A connector is a key to another room. Hand the AI the key and it fetches what you need itself, start read-only, and only share rooms you trust.",
 "quiz":[
   {"q":"1. What does a connector let the AI do?","a":1,"opts":["Think faster","Reach into another app you use to fetch things","Lower your monthly bill"],"good":"Exactly, it's a key into your other rooms, like email or calendar.","bad":"A connector is a key into another app you use, so the AI can fetch and work with what's there itself."},
   {"q":"2. Safest way to start with connectors?","a":1,"opts":["Connect everything at once","Read-only tasks on one app you trust","Hand over your banking login"],"good":"Right, one trusted room, read-only. Banking logins are never appropriate here.","bad":"Start small: read-only tasks on one app you trust. And never hand a connector your banking login or passwords."},
   {"q":"3. Who controls which connectors are active?","a":0,"opts":["You do, connect or disconnect any time","The AI decides for you","They're permanent once turned on"],"good":"Yes, you hold the keyring and can take any key back.","bad":"You're in control, you hold the keyring and can disconnect any connector whenever you want."}
 ],
 "next_teaser":"<strong>Next up: The Trained Specialist.</strong> Tired of giving the same instructions every time? You can train a helper once, and it remembers."
},
{
 "n":9,"mins":8,"title":"Custom Assistants: The Trained Specialist","analogy_name":"The Trained Specialist",
 "subtitle":"Tired of explaining the same instructions every single time? You can train a helper once, and from then on, it just knows.",
 "in_module":["What a custom assistant is","The trained-specialist analogy","How to make your first one"],
 "hook_title":"\"Write it in my tone. For execs. Keep it short.\"",
 "hook":"<p>You type some version of that instruction every time. Same tone notes, same audience, same format, over and over, like onboarding a brand-new temp every single morning.</p><p>What if you could train one helper once, and it showed up already knowing the job? You can.</p>",
 "analogy":"<p>Instead of briefing a new temp each day, you train a <strong>specialist</strong>, once. You teach them your tone, your rules, your task, show them a few examples.</p><p style=\"margin-bottom:0\">From then on, they show up already knowing how you like it. No re-briefing. They're <em>your</em> specialist.</p>",
 "analogy_after":"<p>This is really Levels 1 and 2 combined: a dedicated room (a Project) with your instructions written in permanent marker on the whiteboard.</p>",
 "how_title":"How to train one",
 "how":"<p>A <span class=\"term\">custom assistant</span> <span class=\"soft\">(in plain words: a helper you set up once)</span> bundles your instructions, and sometimes reference files, into its own reusable helper.</p><h3>Set it up once</h3><p>Give it a name, tell it its job, hand it a few good examples and any docs it should always use.</p><h3>It reuses that every time</h3><p>No re-explaining. \"Social post writer.\" \"Meeting-notes summarizer.\" \"Email in my voice.\" You pick the right one and go.</p><h3>Same idea, different names</h3><p>Claude Projects, ChatGPT's custom GPTs, Gemini's Gems. All the same move: a specialist trained once and reused.</p>",
 "foryou_title":"Train your first specialist",
 "foryou":"<h3>1. Spot your repeats</h3><p>The task you brief the same way every week is your first specialist. That's where the time savings hide.</p><h3>2. Train it with examples</h3><p>Paste two or three good past examples so it matches your voice, far better than telling it to \"be professional.\"</p><h3>3. Name it and reuse it</h3><p>Give it a clear name so you grab the right specialist next time, instead of starting from a blank page.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Pick one task you repeat weekly. Set up a custom assistant for it with two example outputs. Use it instead of starting fresh.</p></div>",
 "takeaway":"A custom assistant is a specialist you train once. Teach it the job, give it examples, and it shows up ready every time.",
 "quiz":[
   {"q":"1. What's the point of a custom assistant (custom GPT / Gem / Project)?","a":1,"opts":["It makes the AI cheaper","Save your instructions once so you don't re-explain every time","It deletes your old chats"],"good":"Exactly, train it once, skip the daily re-briefing forever.","bad":"The point is reuse: save your instructions once so you stop re-explaining the same thing every time."},
   {"q":"2. Best way to train it to match your voice?","a":0,"opts":["Give it two or three good examples of your work","Just tell it to \"be professional\"","Use longer, fancier words"],"good":"Right, examples teach voice far better than adjectives.","bad":"Show, don't tell: two or three good examples of your real work teach your voice better than any instruction."},
   {"q":"3. A custom assistant is basically…","a":2,"opts":["a brand-new kind of AI","a faster internet connection","a Project with standing instructions baked in"],"good":"Yes, a dedicated room plus permanent-marker instructions. Levels 1 and 2 combined.","bad":"It's really a Project (a dedicated room) with your standing instructions baked in, everything you learned in Levels 1 and 2."}
 ],
 "next_teaser":"<strong>That's your toolkit. 🧰</strong> Chats, Projects, the workbench, keys, and trained specialists, you now know what every button actually does. More levels coming soon."
},
{
 "n":10,"mins":7,"title":"Custom Instructions: The House Rules","analogy_name":"The House Rules",
 "subtitle":"You keep telling the AI the same things, be concise, no jargon, write like me. Say it once, permanently. Here's how.",
 "in_module":["What custom instructions are","The house-rules analogy","What to put in yours today"],
 "hook_title":"“Please stop using corporate buzzwords.”",
 "hook":"<p>You type some version of the same correction every time, be concise, drop the fluff, no bullet points, write like a human. Every new chat, you re-train it from zero.</p><p>There's a place to write these down once, and the AI follows them in every conversation from then on.</p>",
 "analogy":"<p>Imagine new guests in your home. Without rules, they guess: shoes on or off? Feet on the couch? With the house rules posted on the fridge, everyone just knows.</p><p style=\"margin-bottom:0\">Custom instructions are house rules for the AI, written once, followed in every conversation.</p>",
 "analogy_after":"<p>It's the system-prompt idea from Level 1 (permanent marker on the whiteboard), except now <em>you</em> hold the marker.</p>",
 "how_title":"How the house rules work",
 "how":"<p><span class=\"term\">Custom instructions</span> <span class=\"soft\">(in plain words: your standing preferences)</span> are settings you fill in once that quietly apply to every chat.</p><h3>Usually two halves</h3><ul><li><strong>About you</strong>, your role, what you do, who your answers are for</li><li><strong>How to respond</strong>, tone, length, format, things to avoid</li></ul><h3>Always on the whiteboard</h3><p>Think of them as written in permanent marker: present in every conversation without you ever retyping them.</p><h3>Where to find them</h3><p>Usually under settings or “personalization.” Claude and ChatGPT both have it; it takes two minutes to set up.</p>",
 "foryou_title":"Write your first rules today",
 "foryou":"<h3>1. Start with your three pet peeves</h3><p>The corrections you give most, “be concise,” “no jargon,” “give me a few options.” Those are your first three rules.</p><h3>2. Tell it who you are</h3><p>Your role and what you do, so answers land in your world instead of generic-land.</p><h3>3. Update as you go</h3><p>Any time you find yourself correcting the same thing twice, that's a new house rule.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Open the settings and write your three most common corrections as house rules. Notice how the next chats already behave.</p></div>",
 "takeaway":"Custom instructions are house rules for AI, write your preferences once, and every chat follows them.",
 "quiz":[
   {"q":"1. You correct the AI's tone in every new chat. Better move?","a":1,"opts":["Keep correcting it each time","Put it in custom instructions so every chat follows it","Use a bigger font"],"good":"Exactly, write it once as a house rule and every chat respects it.","bad":"The fix is custom instructions: write it once and it applies across all your chats."},
   {"q":"2. What belongs in custom instructions?","a":1,"opts":["One-time questions","Your standing preferences, who you are and how you want responses","Your password"],"good":"Right, who you are and how you want answers, set once.","bad":"Standing preferences belong here: who you are and how you want responses. Never your password."},
   {"q":"3. Custom instructions are basically…","a":1,"opts":["a faster model","the system prompt, but written by you","a brand-new chat"],"good":"Yes, the system prompt, except now you hold the marker.","bad":"They're the system prompt, just written by you instead of the tool."}
 ],
 "next_teaser":"<strong>Next up: The Notebook.</strong> Level 1 said AI has no memory, just a whiteboard that wipes. That's changing, some AI now keeps a notebook."
},
{
 "n":11,"mins":7,"title":"Memory: The Notebook That Keeps Notes","analogy_name":"The Notebook",
 "subtitle":"Level 1 said AI has no memory, just a whiteboard that wipes. That's changing. Some AI now keeps a notebook. Here's what that means for you.",
 "in_module":["What AI “memory” actually is","Notebook vs. the old whiteboard","How to use it (and keep it tidy)"],
 "hook_title":"“Wait, it remembered that?”",
 "hook":"<p>You mention in one chat that you don't eat meat. Weeks later, in a totally new chat, it suggests a recipe, and it's meat-free. A little spooky?</p><p>It's a real feature, not mind-reading. And once you get it, it's genuinely useful.</p>",
 "analogy":"<p>The whiteboard wipes when it fills up and when you start a new chat. <strong>Memory</strong> is a little notebook the AI keeps on the side. When something seems worth remembering, your name, your preferences, your projects, it jots a note.</p><p style=\"margin-bottom:0\">New chat, fresh whiteboard, but the notebook comes along.</p>",
 "analogy_after":"<p>So now there are two things: the whiteboard (this one conversation) and the notebook (a few facts that carry across conversations).</p>",
 "how_title":"How the notebook works",
 "how":"<p><span class=\"term\">Memory</span> <span class=\"soft\">(in plain words: facts saved across chats)</span> lets the AI carry a few key details from one conversation to the next.</p><h3>It's selective, not a recording</h3><p>It saves short notes, “prefers brief answers,” “runs a bakery”, not entire conversations.</p><h3>You can see and edit it</h3><p>Most tools let you open the notebook to view, delete, or turn off what's in there. It's your notebook.</p><h3>Different from custom instructions</h3><p>House rules are what <em>you</em> set on purpose. Memory is what the AI <em>notices</em> and saves over time.</p>",
 "foryou_title":"Use it, and keep it tidy",
 "foryou":"<h3>1. Lean on it for stable facts</h3><p>Your role, your business, ongoing projects, the things worth carrying chat to chat.</p><h3>2. Peek in now and then</h3><p>Open the memory settings occasionally and delete anything wrong or out of date.</p><h3>3. Turn it off for sensitive stuff</h3><p>Starting a private or temporary chat keeps that conversation out of the notebook.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Open your AI's memory settings and see what it's noted about you. Delete anything that doesn't fit.</p></div>",
 "takeaway":"Memory is the AI's notebook, a few facts it carries across chats. Useful, but peek inside now and then and tidy it up.",
 "quiz":[
   {"q":"1. AI mentions something you said weeks ago, in a brand-new chat. What's happening?","a":1,"opts":["It's broken","Memory, it saved a note that carries across chats","It's reading your mind"],"good":"Exactly, it jotted a note in its notebook and carried it over.","bad":"It's memory: a note in its notebook that carries from one chat to another. No mind-reading."},
   {"q":"2. How is memory different from the whiteboard?","a":1,"opts":["They're the same thing","The whiteboard is one chat; the notebook carries facts between chats","Memory is just faster"],"good":"Right, whiteboard is this conversation; notebook crosses conversations.","bad":"The whiteboard is a single chat; the notebook carries a few facts between chats. Different jobs."},
   {"q":"3. You find something wrong in its memory. What can you do?","a":1,"opts":["Nothing, it's permanent","View and delete it in the settings","Start a whole new account"],"good":"Yes, open memory settings and delete it. It's your notebook.","bad":"You can view and delete it in the memory settings, you control the notebook."}
 ],
 "next_teaser":"<strong>Next up: Eyes and Ears.</strong> AI isn't just a text box. You can show it a photo, talk to it out loud, even point your camera."
},
{
 "n":12,"mins":7,"title":"Beyond Text: Giving AI Eyes and Ears","analogy_name":"Eyes and Ears",
 "subtitle":"AI isn't just a text box. You can show it a photo, talk to it out loud, even point your camera. Here's what “multimodal” really means.",
 "in_module":["What “multimodal” means","The eyes-and-ears analogy","Real ways to use it this week"],
 "hook_title":"You don't have to type everything.",
 "hook":"<p>A photo of a confusing form. A whiteboard full of meeting scribbles. A long voice ramble while you walk. You assume you have to transcribe it all into the chat box first.</p><p>You don't. AI can look and listen now.</p>",
 "analogy":"<p>For years AI could only read and write, like pen pals trading letters. Now it has <strong>eyes</strong> (it can see images and screens) and <strong>ears</strong> (it can hear you talk).</p><p style=\"margin-bottom:0\">Same brilliant mind, now it can take in the world the way you do, not just through typed words.</p>",
 "analogy_after":"<p>“Multimodal” is just the technical word for “more than one sense”, eyes and ears on top of reading.</p>",
 "how_title":"How eyes and ears work",
 "how":"<p>A <span class=\"term\">multimodal</span> <span class=\"soft\">(in plain words: handles images and audio, not just text)</span> AI lets you hand it pictures and voice, and some can speak back.</p><h3>Show it things</h3><p>A photo of a document, a screenshot, a chart, a handwritten note, ask “what does this say?” or “summarize this.”</p><h3>Talk to it</h3><p>Voice mode lets you have a spoken back-and-forth, great while cooking, driving (safely), or thinking out loud.</p><h3>Know the limits</h3><p>It can misread blurry photos or messy handwriting. Verify anything important, remember the confident intern.</p>",
 "foryou_title":"Use its senses this week",
 "foryou":"<h3>1. Snap instead of type</h3><p>Photograph a receipt, a form, a sign, ask it to pull out the details for you.</p><h3>2. Talk when typing is a pain</h3><p>Use voice to brainstorm or draft while you're walking or driving.</p><h3>3. Screenshot your confusion</h3><p>Stuck on a setting or an error message? Show it the screen instead of describing it.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Take a photo of something confusing, a form, a label, and ask the AI to explain it.</p></div>",
 "takeaway":"Modern AI has eyes and ears, show it a photo or talk to it, not just type. That's all “multimodal” means.",
 "quiz":[
   {"q":"1. “Multimodal” means the AI can…?","a":1,"opts":["Think in several languages only","Handle images and audio, not just typed text","Run on several phones"],"good":"Exactly, eyes and ears: images and audio on top of text.","bad":"It means handling images and audio, not just typed text, its eyes and ears."},
   {"q":"2. You have a photo of a confusing form. Best move?","a":1,"opts":["Type the whole form out first","Show it the photo and ask what it means","It can't help with images"],"good":"Right, just show it the photo. That's what its eyes are for.","bad":"Just show it the photo and ask, no need to transcribe the whole thing first."},
   {"q":"3. It misreads your blurry handwritten note. The lesson?","a":1,"opts":["AI is useless","Verify important details, even its eyes can misread","Never use images"],"good":"Yes, its eyes can slip too. Verify the important details.","bad":"The lesson: verify important details. Even its eyes can misread a blurry image."}
 ],
 "next_teaser":"<strong>Next up: The Recipe Box.</strong> Found a prompt that works great? Don't reinvent it every time. Save it like a recipe."
},
{
 "n":13,"mins":7,"title":"Saved Prompts: Your Recipe Box","analogy_name":"The Recipe Box",
 "subtitle":"Found a prompt that works great? Don't reinvent it every time. Save it like a recipe and reuse it forever.",
 "in_module":["Why a good prompt is worth saving","The recipe-box analogy","Building your first few"],
 "hook_title":"It worked perfectly. Then you lost it.",
 "hook":"<p>Last month you wrote a prompt that turned messy notes into a clean summary, perfectly. Today you need it again, and you're rewriting it from memory, worse than before.</p><p>Good prompts are assets. Stop throwing them away.</p>",
 "analogy":"<p>A great prompt is a <strong>recipe</strong>: a tested set of steps that reliably produces a good dish. You wouldn't reinvent your best recipe from scratch each time, you'd write it on a card and keep it in the box.</p><p style=\"margin-bottom:0\">Saved prompts are your recipe box for AI.</p>",
 "analogy_after":"<p>It ties right back to Level 1's Sous Chef: a saved prompt is the recipe you hand your sous chef, ready to cook.</p>",
 "how_title":"How to build a recipe box",
 "how":"<p>A <span class=\"term\">saved prompt</span> <span class=\"soft\">(in plain words: a reusable instruction you keep)</span> is simply a prompt you store and pull out when you need it.</p><h3>Where they live</h3><p>A notes app, a doc, or built-in features (saved prompts, templates, even a custom assistant from Level 2).</p><h3>Make them reusable</h3><p>Leave blanks to fill in: “Summarize [paste notes] for [audience] in [length].” Now one recipe serves a hundred dishes.</p><h3>Build a small box, not a library</h3><p>Five great recipes you use weekly beat fifty you forget you have.</p>",
 "foryou_title":"Start your box",
 "foryou":"<h3>1. Save the next one that works</h3><p>When a prompt nails it, copy it somewhere before it scrolls away forever.</p><h3>2. Add fill-in blanks</h3><p>Turn a one-time prompt into a template with [brackets] for the parts that change each time.</p><h3>3. Keep the box close</h3><p>A pinned note or a doc you can copy-paste from in seconds, that's all it takes.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Next time a prompt works well, save it with a couple of [brackets] so you can reuse it on anything.</p></div>",
 "takeaway":"A good prompt is a recipe. Save the ones that work in a recipe box, with blanks to fill in, and reuse them forever.",
 "quiz":[
   {"q":"1. You wrote a prompt that works great. Smartest move?","a":1,"opts":["Rewrite it from memory next time","Save it somewhere so you can reuse it","Use it once and forget it"],"good":"Exactly, drop it in your recipe box before it's gone.","bad":"The smart move is to save it somewhere reusable, not rewrite it from memory every time."},
   {"q":"2. What makes a saved prompt reusable?","a":1,"opts":["Making it as long as possible","Fill-in blanks ([brackets]) for the parts that change","Fancy vocabulary"],"good":"Right, brackets let one recipe serve a hundred situations.","bad":"Fill-in blanks make it reusable, [brackets] for the parts that change each time."},
   {"q":"3. How big should your recipe box be?","a":1,"opts":["As large as possible","A few great ones you actually use weekly","Exactly one"],"good":"Yes, a few you truly use beat dozens you forget.","bad":"Keep it small: a few great recipes you use weekly beat a giant pile you forget."}
 ],
 "next_teaser":"<strong>Last one: The Night Shift.</strong> What if AI did a whole job while you slept and left it ready for your review? Meet loops."
},
{
 "n":14,"mins":8,"title":"Loops: The Night Shift","analogy_name":"The Night Shift",
 "subtitle":"What if AI didn't wait for you to ask, but woke up on its own, did one defined job, and left the results for you to review? That's a loop.",
 "in_module":["What a loop actually is","The night-shift analogy (job, keys, schedule, logbook)","Why boundaries matter more than a smarter AI"],
 "hook_title":"Work that happens while you sleep.",
 "hook":"<p>So far you've driven every task by hand, ask, wait, ask again. But the real unlock is work that happens <em>without</em> you: a helper that wakes up on a schedule, does one job, and leaves it ready for you in the morning.</p><p>It sounds like science fiction. It's just a loop, and the idea is simpler than the hype makes it sound.</p>",
 "analogy":"<p>A loop is like hiring someone for the <strong>night shift</strong>. You don't hover over them. You give them four things: one clear job, a key to only the rooms they need, a clock-in time, and a shared logbook everyone can read.</p><p style=\"margin-bottom:0\">They clock in, do the job, write it in the log, and clock out. You read the log in the morning and decide what's good to keep.</p>",
 "analogy_after":"<p>Remember the trained specialist from Level 2? A loop is that same specialist, but on a recurring shift, instead of waiting for you to call.</p>",
 "how_title":"What's actually in a loop",
 "how":"<p>A <span class=\"term\">loop</span> <span class=\"soft\">(in plain words: a job an agent repeats on a schedule)</span> always has four parts:</p><ul><li><strong>The job</strong>, the one thing it owns</li><li><strong>Permissions</strong>, which “rooms” it's allowed to touch</li><li><strong>The schedule</strong>, when it wakes up</li><li><strong>The logbook</strong>, shared notes that live outside the chat</li></ul><h3>Most of a loop isn't even AI</h3><p>The schedule is just a timer. The permissions are just settings. The review is just you. The AI only handles the judgment part; boring, predictable software does the rest, and that's exactly why a good loop is reliable.</p><h3>Boundaries beat brains</h3><p>The magic isn't a smarter agent. It's a tightly defined role: one job, and a short list of things it must <em>never</em> do.</p><h3>Nothing ships without you</h3><p>A good loop prepares the work and leaves it for approval. You're always the final yes, the night shift never opens the store on its own.</p>",
 "foryou_title":"Set up your first night shift",
 "foryou":"<h3>1. Pick one boring, repeating job</h3><p>A morning news summary, sorting your inbox, drafting your standup notes. Small and repetitive is perfect.</p><h3>2. Write the “shift card” first</h3><p>Before anything runs: what's the job, what may it touch, what must it never do, and how will you know it did well? If you can't grade it, it's not ready to run alone.</p><h3>3. Keep a human gate</h3><p>Let it <em>prepare</em>, not <em>publish</em>. It drafts; you review and send. That one rule keeps mistakes cheap and visible.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Write a shift card for one repeating task, job, allowed, forbidden, how you'll grade it. Even on paper, you'll see which work is safe to hand over.</p></div>",
 "takeaway":"A loop is the night shift: give AI one job, limited keys, a schedule, and a logbook, then review the work in the morning.",
 "quiz":[
   {"q":"1. What's a “loop,” really?","a":1,"opts":["A bug that keeps repeating","A job an agent does on repeat, on a schedule, without you kicking it off","A longer chat that never ends"],"good":"Exactly, a recurring job: it wakes up, does one thing, logs it, sleeps.","bad":"A loop is a recurring job: an agent wakes on a schedule, does one defined task, logs it, and sleeps, no one starting it each time."},
   {"q":"2. What makes a loop reliable?","a":1,"opts":["A bigger, smarter model","Tight boundaries, one job, limited keys, and your review","Letting it do as much as possible"],"good":"Right, boundaries, not brains. One job, limited permissions, a human gate.","bad":"It's boundaries, not brains: one clear job, limited permissions, and you reviewing the output. That's where reliability comes from."},
   {"q":"3. Best first loop to set up?","a":1,"opts":["Something high-stakes, like sending money","One small repeating task you still review before anything ships","Nothing, loops are only for engineers"],"good":"Yes, start small and boring, with you as the final yes.","bad":"Start with one small, repeating, low-stakes task, and keep yourself as the gate before anything ships."}
 ],
 "next_teaser":"<strong>One more for this level: the Pilot's Seat.</strong> As AI does more on its own, where do you fit? In the most important seat of all."
},
{
 "n":15,"mins":8,"title":"Vibe Coding: Director, Not Bricklayer","analogy_name":"Director, Not Bricklayer",
 "subtitle":"People keep saying you can “build an app just by describing it.” That's vibe coding. Here's what it really is, and what it isn't.",
 "in_module":["What “vibe coding” actually means","The director-vs-bricklayer analogy","What it's great for, and where it bites"],
 "hook_title":"“Wait, I can just… describe it?”",
 "hook":"<p>You've seen the posts: someone with no coding background says “build me a website that does X,” and minutes later it exists. It feels like magic, or like a trick. It's neither.</p><p>It's called vibe coding, and once you see the shape of it, you'll know exactly when to reach for it, and when not to.</p>",
 "analogy":"<p>Building software used to mean laying every brick yourself, learning the exact words, stacking them perfectly, one typo and the wall falls. Vibe coding makes you the <strong>director</strong> instead of the bricklayer.</p><p style=\"margin-bottom:0\">You describe the building you want in plain language. The AI lays the bricks. You look at what it built, say “make this taller, move that door,” and it adjusts.</p>",
 "analogy_after":"<p>You still need taste and direction, a director who can't tell good from bad gets a bad film. But you don't need to know how to mix the concrete.</p>",
 "how_title":"How vibe coding works",
 "how":"<p><span class=\"term\">Vibe coding</span> <span class=\"soft\">(in plain words: building software by describing it in everyday language)</span> means you steer with words and the AI writes the actual code.</p><h3>It's a conversation, not one magic sentence</h3><p>You describe, it builds, you react: “smaller,” “add a login,” “that's broken, fix it.” The first version is a starting point, like a draft.</p><h3>What it's great for</h3><p>Quick tools, prototypes, simple sites, automating a small personal task, things where “good enough and fast” wins.</p><h3>Where it bites</h3><p>Anything with real stakes, money, private data, lots of users, still needs real engineering review. Vibe coding gets you a working draft fast; it doesn't replace the judgment that keeps things safe.</p>",
 "foryou_title":"How to direct well",
 "foryou":"<h3>1. Describe the outcome, not the code</h3><p>“A page where people can book a 30-minute call with me” beats trying to name technical pieces you don't know yet.</p><h3>2. Build in small steps</h3><p>One feature at a time. Get it working, then add the next, easier to steer than asking for everything at once.</p><h3>3. Know your ceiling</h3><p>Great for personal tools and prototypes. The moment real money or real user data is involved, bring in someone who can review the bricks.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Describe one tiny tool you wish existed, a tip calculator, a simple tracker, and direct the AI to build it, one small change at a time.</p></div>",
 "takeaway":"Vibe coding makes you the director, not the bricklayer, describe what you want in plain words and the AI builds it. Bring real review when the stakes get real.",
 "quiz":[
   {"q":"1. “Vibe coding” means…?","a":1,"opts":["Coding only when you're in a good mood","Building software by describing it in plain language while the AI writes the code","A new programming language"],"good":"Exactly, you direct in words, the AI lays the bricks.","bad":"It means building software by describing what you want in plain language, the AI writes the actual code."},
   {"q":"2. In vibe coding, your job is to be the…?","a":0,"opts":["Director, taste and direction","Bricklayer, typing the code yourself","Customer who just waits"],"good":"Right, you provide taste and direction; the AI does the laying.","bad":"You're the director: you bring taste and direction. The AI is the bricklayer that writes the code."},
   {"q":"3. When should you bring in real engineering review?","a":1,"opts":["Never, vibe coding handles everything","When real money, private data, or many users are involved","Only if the AI refuses"],"good":"Yes, high stakes still need a human who can check the work.","bad":"When the stakes are real, money, private data, lots of users, get a human who can review the code. Vibe coding gives you a fast draft, not a safety guarantee."}
 ],
 "next_teaser":"<strong>Next up: The Dining Room &amp; the Kitchen.</strong> Every app has two halves. Once you see them, “frontend” and “backend” stop being scary words."
},
{
 "n":16,"mins":7,"title":"Frontend vs. Backend: The Dining Room &amp; the Kitchen","analogy_name":"The Dining Room &amp; the Kitchen",
 "subtitle":"“Frontend,” “backend”, thrown around constantly. They're just the two halves of every app, and you already understand both from eating at a restaurant.",
 "in_module":["What frontend and backend mean","The restaurant analogy","Why it helps you talk to builders"],
 "hook_title":"Two words, one restaurant.",
 "hook":"<p>Every time someone talks about an app, “frontend” and “backend” show up, and nod-along is the usual response. But these two are simple, and you've experienced both every time you've eaten out.</p>",
 "analogy":"<p>Think of an app as a restaurant. The <strong>frontend</strong> is the <strong>dining room</strong>, the part guests see and touch: the tables, the menu, the lighting, the buttons you tap.</p><p style=\"margin-bottom:0\">The <strong>backend</strong> is the <strong>kitchen</strong>, out of sight, where the actual work happens: orders get made, ingredients are stored, the real cooking gets done.</p>",
 "analogy_after":"<p>This is the Sous Chef from Level 1, grown into a whole restaurant. The dining room is what you experience; the kitchen is what makes it possible.</p>",
 "how_title":"How the two halves work",
 "how":"<p>The <span class=\"term\">frontend</span> <span class=\"soft\">(plain words: the dining room, what users see)</span> is everything on your screen: layout, colors, buttons, the form you fill in.</p><h3>The backend is the kitchen</h3><p>The <span class=\"term\">backend</span> <span class=\"soft\">(plain words: the kitchen, the behind-the-scenes engine)</span> handles the work the guest never sees: saving your data, checking your password, doing the calculations.</p><h3>They pass orders back and forth</h3><p>You tap “place order” in the dining room; the kitchen makes it and sends the result back out. (How they pass those orders is the next lesson, the waiter.)</p><h3>Why you'd care</h3><p>When something's wrong, knowing which half it's in helps: a button that looks off is a dining-room issue; a payment that won't process is a kitchen one.</p>",
 "foryou_title":"Why this is worth knowing",
 "foryou":"<h3>1. You can describe problems precisely</h3><p>“It looks broken on my phone” (dining room) vs. “it won't save my changes” (kitchen). Builders instantly know where to look.</p><h3>2. You'll follow tech conversations</h3><p>“We need a frontend tweak” now means “a change to what users see”, no mystery.</p><h3>3. You'll scope ideas better</h3><p>A visual change is usually small; a kitchen change (new data, new logic) is usually bigger. Handy when planning.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Open any app you use and name the parts: which bits are the dining room (what you see) and which must be happening in the kitchen (saving, checking, calculating)?</p></div>",
 "takeaway":"Frontend is the dining room you see; backend is the kitchen that does the work. Every app is a restaurant with both.",
 "quiz":[
   {"q":"1. The “frontend” of an app is…?","a":0,"opts":["The dining room, what users see and tap","The kitchen, the hidden engine","The delivery driver"],"good":"Exactly, the part guests see and interact with.","bad":"The frontend is the dining room: the part you see and tap. The hidden engine is the backend."},
   {"q":"2. Where does the “backend” do its work?","a":1,"opts":["On the screen, in plain view","Behind the scenes, saving data, checking logins, doing the logic","Only on your phone"],"good":"Right, the kitchen, out of sight, doing the real work.","bad":"The backend is the kitchen: behind the scenes, saving data, checking logins, running the logic."},
   {"q":"3. “It won't save my changes” is most likely a…?","a":1,"opts":["Dining-room (frontend) issue","Kitchen (backend) issue","Wi-Fi router issue"],"good":"Yes, saving is kitchen work, so it's a backend issue.","bad":"Saving data happens in the kitchen, so that's a backend issue, not a dining-room one."}
 ],
 "next_teaser":"<strong>Next up: The Waiter.</strong> How does the dining room talk to the kitchen? Meet the most useful tech word you'll learn: the API."
},
{
 "n":17,"mins":7,"title":"APIs: The Waiter","analogy_name":"The Waiter",
 "subtitle":"“API” might be the most-used tech word you've never had explained. It's just the waiter between the dining room and the kitchen.",
 "in_module":["What an API actually is","The waiter analogy","Why APIs quietly run your digital life"],
 "hook_title":"The word that's everywhere.",
 "hook":"<p>API. It's in every tech conversation, every tutorial, every pricing page. People say it like you should already know. You don't have to fake it anymore, it's genuinely simple.</p>",
 "analogy":"<p>Back in our restaurant: you (the dining room) don't march into the kitchen and start cooking. You tell the <strong>waiter</strong> what you want from the menu. The waiter takes your order to the kitchen, and brings the dish back.</p><p style=\"margin-bottom:0\">An <strong>API</strong> is that waiter, the messenger that carries requests from one piece of software to another, and brings the answer back.</p>",
 "analogy_after":"<p>You never need to know how the kitchen works. You just need the menu (what you can order) and the waiter (who carries it). That's an API.</p>",
 "how_title":"How APIs work",
 "how":"<p>An <span class=\"term\">API</span> <span class=\"soft\">(plain words: the waiter that lets two apps talk)</span> is how one program asks another program for something, in a format they both agree on.</p><h3>There's always a menu</h3><p>An API offers a set list of things you can ask for, like a menu. You can order what's on it, not whatever you imagine.</p><h3>It's how apps connect</h3><p>When your weather app shows the forecast, it asked a weather service's API. When a site lets you “log in with Google,” it's talking to Google's API. The connectors from Level 2 ride on APIs.</p><h3>Why it matters to you</h3><p>“Does it have an API?” really means “can this tool talk to my other tools?” That one question decides whether things can be automated together.</p>",
 "foryou_title":"Why this unlocks things",
 "foryou":"<h3>1. You'll understand “it integrates with…”</h3><p>That's APIs at work, one app's waiter talking to another's. It's why your tools can share data.</p><h3>2. You can ask the right question</h3><p>“Does this have an API?” tells you whether it can plug into automations and other apps later.</p><h3>3. It demystifies pricing</h3><p>“API access” on a plan just means “permission to let your other software place orders here.”</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Pick two tools you use and ask: could one place an “order” with the other? That's you thinking in APIs.</p></div>",
 "takeaway":"An API is the waiter between apps, it carries your request to another program's kitchen and brings the answer back. “Has an API?” means “can it talk to my other tools?”",
 "quiz":[
   {"q":"1. An API is best described as…?","a":1,"opts":["The kitchen itself","The waiter that carries requests between apps and brings answers back","The menu's prices"],"good":"Exactly, the messenger between two pieces of software.","bad":"An API is the waiter: it carries a request to another app's kitchen and brings the result back."},
   {"q":"2. Why does “does it have an API?” matter?","a":1,"opts":["It makes the app cheaper","It tells you whether the tool can talk to your other tools","It speeds up your Wi-Fi"],"good":"Right, an API is what lets tools connect and automate together.","bad":"It tells you whether the tool can connect to your other tools, APIs are how apps talk and automate together."},
   {"q":"3. When your weather app shows a forecast, it…?","a":0,"opts":["Asked a weather service's API for it","Guessed based on the season","Stored every forecast forever"],"good":"Yes, it ordered the forecast through an API, like asking a waiter.","bad":"It asked a weather service's API, placed an order through the waiter and got the forecast back."}
 ],
 "next_teaser":"<strong>Next up: The Filing Cabinet.</strong> Where does all that information actually live? Say hello to the database."
},
{
 "n":18,"mins":7,"title":"Databases: The Filing Cabinet","analogy_name":"The Filing Cabinet",
 "subtitle":"Every app remembers things, your account, your orders, your messages. Where does all of it live? In a database. Here's the plain-English version.",
 "in_module":["What a database is","The filing-cabinet analogy","Why “structure” is the whole point"],
 "hook_title":"Where does it all go?",
 "hook":"<p>You log in and your stuff is there, your profile, your history, your saved items. Somewhere, an app is remembering all of it, for millions of people, without mixing anyone up. That somewhere has a name.</p>",
 "analogy":"<p>A <strong>database</strong> is a giant, well-organized <strong>filing cabinet</strong>. Not a junk drawer, a cabinet with labeled drawers and folders, where every piece of information has a known place.</p><p style=\"margin-bottom:0\">Because it's organized, the app can find any record in an instant: your order from last March, that one message, your settings.</p>",
 "analogy_after":"<p>Back to the restaurant: the database is the kitchen's pantry and recipe box, the organized storage the kitchen reaches into to get things done.</p>",
 "how_title":"How databases work",
 "how":"<p>A <span class=\"term\">database</span> <span class=\"soft\">(plain words: an organized filing cabinet for information)</span> stores data in a structured way so it can be found, updated, and trusted.</p><h3>Structure is the magic</h3><p>Information is kept in consistent shapes, like a spreadsheet with agreed columns. That structure is what makes it searchable and reliable at huge scale.</p><h3>It's constantly read and written</h3><p>Every time you save, post, or buy, the app writes to the cabinet. Every time you open the app, it reads from it.</p><h3>Why you'd care</h3><p>“Our database” is just “where our information lives.” When a company says your data was in a breached database, now you know exactly what that means: the filing cabinet was opened.</p>",
 "foryou_title":"Why this is worth knowing",
 "foryou":"<h3>1. You'll understand “the data lives in…”</h3><p>It's the filing cabinet, the organized store every app keeps behind the scenes.</p><h3>2. You'll grasp why structure matters</h3><p>Messy information can't be found; structured information can. It's why apps ask for things in specific fields.</p><h3>3. You'll read the news better</h3><p>“A database was breached” = someone got into the filing cabinet. Clear, concrete, no jargon.</p><div class=\"card\"><h3 style=\"margin-top:0\">Try it this week</h3><p style=\"margin-bottom:0\">Think of an app you use and list what's in its filing cabinet about you, profile, history, preferences. That mental list <em>is</em> its database.</p></div>",
 "takeaway":"A database is an organized filing cabinet for an app's information, structured so it can find any record instantly. “The data lives in the database” just means “in the cabinet.”",
 "quiz":[
   {"q":"1. A database is best thought of as…?","a":1,"opts":["A messy junk drawer","An organized filing cabinet where information has a known place","The app's screen"],"good":"Exactly, organized storage, not a junk drawer.","bad":"It's an organized filing cabinet, structured so every record has a known place and can be found fast."},
   {"q":"2. Why does “structure” matter in a database?","a":1,"opts":["It makes the app look nicer","Structured information can be found and trusted at huge scale","It isn't important at all"],"good":"Right, structure is what makes data searchable and reliable.","bad":"Structure is the point: organized information can be found and trusted, even across millions of records."},
   {"q":"3. “A database was breached” means…?","a":0,"opts":["Someone got into the filing cabinet of stored information","The app's colors changed","The Wi-Fi went down"],"good":"Yes, someone accessed the stored information. Now the term is concrete.","bad":"It means someone got into the filing cabinet, the stored information. That's all a database is."}
 ],
 "next_teaser":"<strong>Last one: Opening the Shop.</strong> You built something. How does it go from “on your computer” to “anyone can visit”? That's deployment."
},
{
 "n":19,"mins":7,"title":"Hosting &amp; Deployment: Opening the Shop","analogy_name":"Opening the Shop",
 "subtitle":"You made something on your computer. Getting it onto the internet for anyone to visit has a name: deployment. Here's what it really means.",
 "in_module":["What hosting and deployment mean","The opening-the-shop analogy","What “going live” actually involves"],
 "hook_title":"From your laptop to the world.",
 "hook":"<p>Something built on your computer only exists for you, like a shop with the lights off and the doors locked. To let anyone visit, you have to open it to the public. In tech, that step has a name, and you actually did it earlier with this very course.</p>",
 "analogy":"<p><strong>Hosting</strong> is renting the shop space, a spot on the internet where your thing can live, open around the clock. <strong>Deployment</strong> is the act of <strong>opening the shop</strong>: putting your work in that space and flipping the sign to “open” so anyone can walk in.</p>",
 "analogy_after":"<p>This course is a real example: it was built, then deployed to a public address, the shop opened, and now anyone with the link can visit.</p>",
 "how_title":"How going live works",
 "how":"<p><span class=\"term\">Hosting</span> <span class=\"soft\">(plain words: renting space on the internet)</span> is where your site or app lives. <span class=\"term\">Deployment</span> <span class=\"soft\">(plain words: opening it to the public)</span> is the step that makes it reachable.</p><h3>Before deployment, it's private</h3><p>On your own computer, only you can see it, the shop's built but the doors are locked.</p><h3>Deployment flips the sign</h3><p>You publish it to the hosting space, and it gets a public address (a link) anyone can visit, anytime.</p><h3>Updates are re-deployments</h3><p>Change something? You deploy again, and the live version updates, like swapping the window display while the shop stays open.</p>",
 "foryou_title":"Why this is worth knowing",
 "foryou":"<h3>1. You'll understand “let's deploy it”</h3><p>It just means “open the shop”, make it live for real people to use.</p><h3>2. You'll know why a link works for everyone</h3><p>Because it's hosted, living in rented internet space that's always on, not on someone's laptop.</p><h3>3. You'll get why updates take a step</h3><p>A change isn't live until it's deployed again. Built ≠ published.</p><div class=\"card\"><h3 style=\"margin-top:0\">You already did this</h3><p style=\"margin-bottom:0\">This course went from files to a public link anyone can open, that's hosting and deployment, start to finish. You've seen the whole loop now.</p></div>",
 "takeaway":"Hosting is renting space on the internet; deployment is opening the shop so anyone can visit. Built on your computer is private; deployed is live.",
 "quiz":[
   {"q":"1. “Deployment” means…?","a":1,"opts":["Designing the logo","Publishing your work to the internet so people can use it","Deleting the project"],"good":"Exactly, opening the shop to the public.","bad":"Deployment is publishing it to the internet, opening the shop so anyone can visit."},
   {"q":"2. What is “hosting”?","a":0,"opts":["Renting always-on space on the internet for your site to live","A type of database","The frontend design"],"good":"Right, the rented shop space where your thing lives, around the clock.","bad":"Hosting is the rented space on the internet where your site lives and stays open, not a database or a design."},
   {"q":"3. You change something on a live site. To update it, you…?","a":1,"opts":["Nothing, it updates by magic","Deploy again, which refreshes the live version","Buy a new computer"],"good":"Yes, built isn't live until you deploy again.","bad":"You deploy again, built on your computer isn't live until it's published. Updates need a re-deploy."}
 ],
 "next_teaser":"<strong>You made it under the hood. 🛠️</strong> Vibe coding, the dining room and kitchen, the waiter, the filing cabinet, and opening the shop, the “scary” tech words are just a restaurant now. You can hold your own in any AI conversation."
},
{
 "n":20,"mins":8,"title":"Human in the Loop: The Pilot &amp; the Autopilot","analogy_name":"The Pilot &amp; the Autopilot",
 "subtitle":"AI can fly a lot of the plane now. But every safe flight still has a pilot, and that's the most valuable seat. Here's why it's yours.",
 "in_module":["What “human in the loop” really means","The pilot-and-autopilot analogy","How to stay the expert as AI does more"],
 "hook_title":"Who's actually flying?",
 "hook":"<p>As AI gets more capable, a quiet worry creeps in: if it can draft, analyze, and even run tasks on its own, where does that leave you? Replaced? Sidelined?</p><p>Here's the reframe that changes everything, and it's the whole reason this course exists. The most valuable seat isn't the one doing the typing. It's the one in command.</p>",
 "analogy":"<p>Modern planes basically fly themselves. Autopilot handles the long, steady stretches better than a human could. And yet every flight you'd ever board still has a <strong>pilot</strong> in the seat.</p><p style=\"margin-bottom:0\">Why? Because autopilot doesn't decide where to go, can't be held accountable, and doesn't know what to do when something unexpected happens. The pilot sets the destination, watches the instruments, and takes the controls the moment it matters. AI is the autopilot. You're the pilot.</p>",
 "analogy_after":"<p>“Human in the loop” is just the industry's name for keeping a pilot in the seat, a person who directs the AI, checks it, and stays accountable for where it lands.</p>",
 "how_title":"Why the loop needs you",
 "how":"<p><span class=\"term\">Human in the loop</span> <span class=\"soft\">(in plain words: a person who directs and checks the AI)</span> isn't a courtesy, it's what makes AI actually useful and safe at work. Four jobs only you can do:</p><h3>You bring the institutional knowledge</h3><p>AI doesn't know your customers, your history, or your unwritten rules. You feed it the context that makes its output relevant.</p><h3>You validate</h3><p>It produces fast; you judge whether it's right, on-brand, and safe to use. (Remember the confident intern.)</p><h3>You improve it through feedback</h3><p>Your corrections, “shorter,” “wrong tone,” “you missed this”, are how it gets better at <em>your</em> work over time.</p><h3>You direct and orchestrate</h3><p>You decide what's worth doing, in what order, and when to take the controls back. AI executes; you command.</p>",
 "foryou_title":"How to stay the expert",
 "foryou":"<h3>1. Start with the small, safe stuff</h3><p>Hand AI the tedious tasks that feel almost too simple, formatting, first drafts, summaries. Low risk, real time saved, and you build judgment for bigger things.</p><h3>2. Always read before you send</h3><p>Treat AI output as a draft from a sharp assistant: useful, but never final until you've checked it. Your name is on what ships.</p><h3>3. Grow the loop as your trust grows</h3><p>As you learn what it's reliable at, hand it more, and keep your hand on the controls for anything with real stakes. More leverage, same accountability.</p><div class=\"card\"><h3 style=\"margin-top:0\">The mindset shift</h3><p style=\"margin-bottom:0\">AI doesn't replace your expertise, it makes your expertise go further. The goal was never to step out of the loop. It's to become the best pilot in it.</p></div>",
 "takeaway":"AI is the autopilot; you're the pilot. Direct it, check it, and stay accountable, your expertise is what makes it safe to fly.",
 "quiz":[
   {"q":"1. What does “human in the loop” mean?","a":0,"opts":["A person who directs and checks the AI, and stays accountable","A meeting about AI","A type of AI model"],"good":"Exactly, you stay in command: directing, checking, and accountable.","bad":"It means a person stays in command, directing the AI, checking its work, and owning the outcome."},
   {"q":"2. Why does capable AI still need a human in the loop?","a":1,"opts":["It doesn't, newer AI is fully autonomous","Because only you bring context, judgment, and accountability","To make it run slower"],"good":"Right, context, validation, feedback, and accountability are yours alone.","bad":"Because you bring what it can't: institutional knowledge, judgment, feedback, and accountability."},
   {"q":"3. Smartest way to work with capable AI?","a":2,"opts":["Hand over everything and stop checking","Refuse to use it at all","Let it draft and execute, but read and direct before anything ships"],"good":"Yes, autopilot does the work; you stay the pilot who checks and commands.","bad":"Let it do the heavy lifting, but stay the pilot, read, direct, and approve before anything ships."}
 ],
 "next_teaser":"<strong>You're the expert in the loop. 🎯</strong> Rules, memory, senses, recipes, a night shift, and now the pilot's seat. Ready to see what's under the hood? That's the final level."
},
]

LEVELS = [
 {"id":1,"slug":"level-1","name":"Start Here","tagline":"How AI behaves, so it stops surprising you.","modules":[1,2,3,4,5],"status":"live"},
 {"id":2,"slug":"level-2","name":"The Tools","tagline":"Chats, projects, artifacts, connectors, what every button actually does.","modules":[6,7,8,9],"status":"live"},
 {"id":3,"slug":"level-3","name":"Make It Yours","tagline":"Make AI work the way you do, your rules, your memory, and your seat at the controls.","modules":[10,11,12,13,14,20],"status":"live"},
 {"id":4,"slug":"level-4","name":"Under the Hood","tagline":"Vibe coding and the tech words, finally demystified, it's all a restaurant.","modules":[15,16,17,18,19],"status":"live"},
]

GLOSSARY = [
 {"term":"Token","def":"A chunk of a word, the unit AI actually reads and writes. Roughly three-quarters of a word.","analogy":"Gas in the tank, every word burns a little.","n":1},
 {"term":"Rate limit","def":"A cap on how much you can use AI within a set window of time before it makes you wait.","analogy":"A gas station that only lets you fill up so many times an hour.","n":1},
 {"term":"Input &amp; output","def":"What you send (input) and what the AI sends back (output). Both burn tokens.","analogy":"Fuel burned on the way there and the way back.","n":1},
 {"term":"Context window","def":"Everything the AI can “see” at once in a conversation. When it fills up, the oldest parts drop off.","analogy":"A whiteboard that gets wiped when it's full.","n":2},
 {"term":"System prompt","def":"Standing instructions that stay active for the whole conversation, no matter how long it runs.","analogy":"Written in permanent marker on the whiteboard.","n":2},
 {"term":"Free vs. paid tier","def":"The free plan is the same core model; paying mostly unlocks higher limits and extra features.","analogy":"A test drive vs. leasing the car.","n":3},
 {"term":"Model","def":"The underlying AI “brain.” Newer or bigger ones are smarter but can be slower or pricier.","analogy":"Picking the right vehicle for the trip.","n":3},
 {"term":"Hallucination","def":"When AI states something false with total confidence, because it predicts likely words, not verified facts.","analogy":"A confident intern making things up.","n":4},
 {"term":"Prompt","def":"What you type to the AI. The more specific it is, the better the result.","analogy":"The recipe you hand your sous chef.","n":5},
 {"term":"Chat","def":"A single conversation, quick and disposable. Nothing is kept once you move on.","analogy":"A phone call.","n":6},
 {"term":"Project","def":"A saved workspace that keeps your files, standing instructions, and chats for one job together.","analogy":"A dedicated office.","n":6},
 {"term":"Artifact (Canvas)","def":"A panel beside the chat where the AI builds an editable thing, a doc, sheet, or small app.","analogy":"A workbench next to the conversation.","n":7},
 {"term":"Connector","def":"A link that lets AI reach into another app you use, like email, calendar, or Drive, to fetch or act.","analogy":"A key to another room.","n":8},
 {"term":"Custom assistant (Custom GPT / Gem)","def":"A helper you set up once with instructions and examples, then reuse without re-explaining.","analogy":"A specialist you trained once.","n":9},
 {"term":"Custom instructions","def":"Standing preferences you set once that quietly apply to every chat.","analogy":"House rules posted on the fridge.","n":10},
 {"term":"Memory","def":"A few facts the AI saves and carries from one chat to the next. You can view and edit them.","analogy":"A notebook it keeps on the side.","n":11},
 {"term":"Multimodal","def":"AI that handles images and audio, not just text, you can show it pictures or talk to it.","analogy":"Giving it eyes and ears.","n":12},
 {"term":"Saved prompt (template)","def":"A reusable instruction you store, often with fill-in blanks, and pull out when you need it.","analogy":"A recipe in your recipe box.","n":13},
 {"term":"Loop","def":"A job an AI agent repeats on a schedule, it wakes up, does one defined task within set permissions, logs the result, and sleeps.","analogy":"A worker on the night shift.","n":14},
 {"term":"Agent","def":"An AI doing a task on its own, making decisions and taking steps toward a goal, not just answering a single question.","analogy":"An employee you delegate a job to.","n":14},
 {"term":"Vibe coding","def":"Building software by describing what you want in plain language while the AI writes the actual code.","analogy":"Being the director, not the bricklayer.","n":15},
 {"term":"Frontend","def":"The part of an app you see and interact with, layout, buttons, screens.","analogy":"The dining room of a restaurant.","n":16},
 {"term":"Backend","def":"The behind-the-scenes engine of an app, saving data, checking logins, running the logic.","analogy":"The kitchen of a restaurant.","n":16},
 {"term":"API","def":"The messenger that lets two pieces of software talk, one app requests something from another and gets an answer back.","analogy":"The waiter between dining room and kitchen.","n":17},
 {"term":"Database","def":"An organized store of an app's information, structured so any record can be found instantly.","analogy":"A well-labeled filing cabinet.","n":18},
 {"term":"Hosting &amp; deployment","def":"Hosting is renting always-on space on the internet; deployment is publishing your work there so anyone can visit.","analogy":"Renting a shop, then opening it to the public.","n":19},
 {"term":"Claude","def":"Anthropic's AI assistant, the family of models this course is built around. Good at writing, analysis, and careful reasoning.","analogy":"One of the “brands” of AI assistant.","n":0},
 {"term":"ChatGPT","def":"OpenAI's AI assistant, one of the most widely used, with a large free tier and many add-on features.","analogy":"One of the “brands” of AI assistant.","n":0},
 {"term":"Gemini","def":"Google's AI assistant, built into Google's products like Search, Docs, and Gmail.","analogy":"One of the “brands” of AI assistant.","n":0},
 {"term":"Bash","def":"A common “language” for typing commands to a computer through a text window, instead of clicking buttons.","analogy":"Speaking to your computer in plain commands instead of pointing and clicking.","n":0},
 {"term":"Command","def":"A single typed instruction you give a computer in a text window, one line that tells it to do one thing.","analogy":"Telling a worker one specific task, out loud.","n":0},
 {"term":"Terminal (command line)","def":"The plain text window where you type commands to a computer directly.","analogy":"The staff-only door to the computer, no buttons, just instructions.","n":0},
 {"term":"Human in the loop","def":"Keeping a person in charge of directing, checking, and being accountable for AI's work, even as it does more on its own.","analogy":"A pilot supervising the autopilot.","n":20},
]
