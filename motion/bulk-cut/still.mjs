import { createRequire } from 'module'; import path from 'path';
const require = createRequire('/opt/node22/lib/node_modules/'); const { chromium } = require('playwright');
const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium', args:['--no-sandbox'] });
const p = await b.newPage({ viewport:{width:1920,height:1080} });
const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await p.goto('file://'+path.resolve('index.html')); await p.waitForTimeout(400);
for(const t of [10,24,40,57,72,88]){ await p.evaluate(x=>window.render(x),t); await p.screenshot({path:`out/still_${t}.png`}); }
console.log('errors:',errs); await b.close();
