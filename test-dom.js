const { JSDOM } = require('jsdom');
const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// Mock requestAnimationFrame and AudioContext
html = html.replace('<head>', '<head><script>window.requestAnimationFrame = function(callback) { return setTimeout(callback, 16); }; window.cancelAnimationFrame = clearTimeout;</script>');

const mockedHtml = html.replace(
  'const audioCtx = new (window.AudioContext || window.webkitAudioContext)();',
  'const audioCtx = { state: "suspended", resume:()=>{}, createOscillator:()=>({connect:()=>{}, start:()=>{}, stop:()=>{}, frequency:{setValueAtTime:()=>{}, exponentialRampToValueAtTime:()=>{}}}), createGain:()=>({connect:()=>{}, gain:{setValueAtTime:()=>{}, linearRampToValueAtTime:()=>{}, exponentialRampToValueAtTime:()=>{}}}), destination:{}, currentTime:0 };'
);

const dom = new JSDOM(mockedHtml, {
    runScripts: "dangerously",
    url: "http://localhost:8000" // avoid opaque origin error for localStorage
});
const window = dom.window;
const document = window.document;

setTimeout(() => {
    const modal = document.getElementById('highscoreModal');
    console.log('Modal element found:', !!modal);
    console.log('Modal initially visible:', modal.classList.contains('active'));

    // Open it
    window.openHighscoreModal();
    console.log('Modal visible after openHighscoreModal():', modal.classList.contains('active'));

    // Close it
    window.closeHighscoreModal();
    console.log('Modal visible after closeHighscoreModal():', modal.classList.contains('active'));
}, 500);
