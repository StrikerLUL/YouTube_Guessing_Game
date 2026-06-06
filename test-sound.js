const { JSDOM } = require('jsdom');
const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// The error happens because gameSettings is not accessible via window since it's a let declared inside script scope without exporting to window.
// We'll modify the JS to export it to window.
html = html.replace('let gameSettings = {', 'window.gameSettings = {');
html = html.replace(/gameSettings/g, 'window.gameSettings');

// Mock requestAnimationFrame and AudioContext
html = html.replace('<head>', '<head><script>window.requestAnimationFrame = function(callback) { return setTimeout(callback, 16); }; window.cancelAnimationFrame = clearTimeout;</script>');

const mockedHtml = html.replace(
  'const audioCtx = new (window.AudioContext || window.webkitAudioContext)();',
  'const audioCtx = { state: "suspended", resume:()=>{}, createOscillator:()=>({connect:()=>{}, start:()=>{}, stop:()=>{}, frequency:{setValueAtTime:()=>{}, exponentialRampToValueAtTime:()=>{}}}), createGain:()=>({connect:()=>{}, gain:{setValueAtTime:()=>{}, linearRampToValueAtTime:()=>{}, exponentialRampToValueAtTime:(val)=>{ if(val <= 0) throw new Error("DOMException: value must be > 0"); }}}), destination:{}, currentTime:0 };'
);

const dom = new JSDOM(mockedHtml, {
    runScripts: "dangerously",
    url: "http://localhost:8000" // avoid opaque origin error for localStorage
});
const window = dom.window;

setTimeout(() => {
    // Set volume to 0
    window.gameSettings.volume = 0;

    let caught = false;
    try {
        window.playSound('correct');
        console.log('playSound(correct) with 0 volume succeeded without error');
    } catch(e) {
        caught = true;
        console.error('Error in playSound:', e.message);
    }

    if(!caught) {
       console.log('Test passed!');
    }
}, 500);
