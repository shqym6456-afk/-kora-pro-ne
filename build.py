# يبني public/index.html من نسخة الـ Artifact (الأحدث) + طبقة البيانات الحية
h=open('/mnt/user-data/outputs/kora-pro.html',encoding='utf-8').read()
head=h[:h.index('<script>')]
helpers=h[h.index('const tf='):h.index('const ST={1:')]
ui=h[h.index('const QZ='):h.index('</script>')]
layer=r'''const $=id=>document.getElementById(id);
let T={},LG=[],M=[],ST={},LUT={},FEED=[],OPN=null,OTB=0,CON=false,LU=null;
const N=a=>(T[a]&&T[a].ar)||a;
const CL=new Proxy({},{get:(_,k)=>(T[k]&&T[k].c)||"#555"});
const sh=a=>`<svg class="bd" onclick="event.stopPropagation();tp('${a}')" style="background:none;width:36px;height:40px" viewBox="0 0 36 40"><path d="M3 3h30v18c0 9-7 14-15 17C10 35 3 30 3 21z" fill="${CL[a]}" stroke="#fff" stroke-opacity=".7" stroke-width="2"/><text x="18" y="24" text-anchor="middle" font-size="11" font-weight="800" fill="#fff" font-family="Cairo,sans-serif">${String(a).slice(0,3)}</text></svg>`;
const bd=a=>T[a]&&T[a].logo?`<img class="bd" alt="" src="${T[a].logo}" onclick="event.stopPropagation();tp('${a}')" onerror="this.outerHTML=sh('${a}')" style="background:none;border-radius:0;width:36px;height:40px;object-fit:contain">`:sh(a);
const bg=x=>Date.parse(new Intl.DateTimeFormat("en-CA",{timeZone:"Asia/Baghdad"}).format(x));
function apply(d){T=d.teams;LG=d.leagues;ST=d.standings;LUT=d.lineups||{};FEED=d.feed||[];LU=d.at?new Date(d.at):new Date();
const old={};M.forEach(m=>old[m.id]=m);
M=d.matches.map(m=>{const o=old[m.id];if(o){m.det=o.det;m.dt=o.dt}if(m.t){const k=Math.round((bg(new Date(m.t))-bg(new Date()))/864e5);m.d=k<=-2?-6:k>=3?7:k}else m.d=0;return m});
if(LG.length&&!LG.find(l=>l.id==S.lg))S.lg=LG[0].id}
const rf=()=>{if(OPN)op(OPN,OTB);else if(!$("ov").classList.contains("on"))R()};
async function load(){try{const r=await fetch("/api/state");apply(await r.json());rf()}catch(e){}}
function go(){const es=new EventSource("/api/stream");es.onopen=()=>{CON=true;rf()};es.onerror=()=>{CON=false};
es.onmessage=e=>{const m=JSON.parse(e.data);
if(m.type=="state"){CON=true;apply(m.data);rf()}
else if(m.type=="lb"){loadLB()}
else if(m.type=="alert"){const rel=m.kind=="win"||!m.h||!S.fav||m.h==S.fav||m.a==S.fav;if(S.nf=="off")return;if(S.nf=="fav"&&!rel)return;toast(m.text,5500);
if(m.kind=="goal"&&S.fav&&m.team==S.fav)ding();else if(navigator.vibrate)try{navigator.vibrate(120)}catch(x){}}}}
setInterval(()=>{if(!CON)load()},30000);
'''
s=head+'<script>\n'+layer+helpers+ui+'</script></body></html>'
def rep(a,b,c=1):
    global s
    assert a in s,a[:70]
    s=s.replace(a,b,c)
rep('const HAS_API=false;','const HAS_API=true;')
rep('<meta name="viewport"','<link rel="manifest" href="/manifest.json"><meta name="theme-color" content="#3b3fd8"><link rel="apple-touch-icon" href="/icons/icon-192.png">\n<meta name="viewport"')
rep('const toast=t=>{const e=$("ts");e.textContent=t;e.style.display="block";setTimeout(()=>e.style.display="none",1800)};','const toast=(t,ms=1800)=>{const e=$("ts");e.textContent=t;e.style.display="block";clearTimeout(window._tt);window._tt=setTimeout(()=>e.style.display="none",ms)};')
rep('const mid=m.s=="ns"?','const mid=m.s=="pp"||m.s=="cn"?`<div class="live" style="color:var(--gd)">${m.note||(m.s=="pp"?"مؤجلة":"ملغاة")}</div><div class="st">${tm(m)}</div>`:m.s=="ns"?',2)
rep('<div class="live">مباشر</div>','<div class="live">${m.ml||"مباشر"}</div>',2)
rep('بيانات حقيقية • لقطة ٣١ تشرين الأول ٢٠٢٦ • كل الأوقات بتوقيت بغداد','${CON?"🟢 متصل مباشرة":"🔴 غير متصل"} • آخر تحديث ${LU?tf.format(LU):"—"} • بتوقيت بغداد')
rep('الاستحواذ ${D.st[0][0]}% مقابل ${D.st[1][0]}%، والتسديدات ${D.st[0][1]} مقابل ${D.st[1][1]}.','${D.st?`الاستحواذ ${D.st[0][0]}% مقابل ${D.st[1][0]}%، والتسديدات ${D.st[0][1]} مقابل ${D.st[1][1]}.`:""}')
rep('هدف ${N(t)} (${S2(hs,as)})','هدف ${N(t)}${e[3]?" — "+e[3]:""} (${S2(hs,as)})')
rep('b=D?SL.map','b=D&&D.st?SL.map')
rep('v=p||[1,1];','v=p||TMP[m.id]||[1,1];')
rep('let CDT;function cl(){clearInterval(CDT);','let CDT;function cl(){OPN=null;clearInterval(CDT);')
rep('function op(id,tab=0){','function op0(id,tab=0){')
i=s.index('function V1()');j=s.index('function V2()')
s=s[:i]+r'''function V1(){return `<div class="sec">آخر الأحداث المباشرة</div>`+(FEED.length?FEED.map(f=>`<div class="nw s" style="cursor:default"><div class="im" style="background:linear-gradient(135deg,var(--ac),#0003)">${f.i}</div><div class="b"><h3>${f.text}</h3><p>${tf.format(new Date(f.at))}</p></div></div>`).join(""):`<p class="card st">لا توجد أحداث بعد. ستظهر هنا الأهداف والتأجيلات فور حدوثها.</p>`)}
'''+s[j:]
wrap=r'''
function op(id,tab=0){const m=M.find(x=>x.id==id);OPN=id;OTB=tab;op0(id,tab);
if(m&&m.s!="ns"&&m.s!="pp"&&m.s!="cn"&&(!m.dt||Date.now()-m.dt>12000)){m.dt=Date.now();fetch("/api/match/"+id).then(r=>r.json()).then(j=>{m.det=j;if(OPN==id)op0(id,OTB)}).catch(()=>{})}}
'''
k=s.rindex('R();\n</script>')
s=s[:k]+wrap+'R();load();go();\napi("/api/join",{uid:S.uid,nick:S.nick}).then(loadLB);setInterval(loadLB,60000);\nif("serviceWorker"in navigator)navigator.serviceWorker.register("/sw.js").catch(()=>{});\n</script></body></html>'
open('public/index.html','w',encoding='utf-8').write(s);print('built',len(s)//1024,'KB')
