// Rendert index.html Bild für Bild (deterministisch) und setzt es mit ffmpeg zu MP4 zusammen.
import { createRequire } from 'module';
import { spawn } from 'child_process';
import path from 'path'; import fs from 'fs';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
const [,, audio='out/beat.wav', outFile='out/bulk-cut.mp4', scale='1'] = process.argv;
const W=1920,H=1080;
const browser = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium', args:['--no-sandbox'] }).catch(()=>chromium.launch({args:['--no-sandbox']}));
const page = await browser.newPage({ viewport:{width:W,height:H} });
await page.goto('file://'+path.resolve('index.html')); await page.waitForTimeout(500);
const { FPS, DURATION } = await page.evaluate(()=>({FPS:window.FPS,DURATION:window.DURATION}));
const total = Math.round(FPS*DURATION*Number(scale));
const ff = spawn('ffmpeg',['-y','-f','image2pipe','-framerate',String(FPS),'-i','-','-i',audio,
  '-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-c:a','aac','-b:a','192k','-t',String(total/FPS),outFile],{stdio:['pipe','inherit','inherit']});
for(let f=0; f<total; f++){
  await page.evaluate(t=>window.render(t), f/FPS);
  const buf = await page.screenshot({type:'jpeg',quality:92});
  if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
  if(f%150===0) console.log('frame',f,'/',total);
}
ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await browser.close(); console.log('fertig',outFile);
