const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const hasModal = html.includes('id="highscoreModal"');
const hasOpenBtn = html.includes('onclick="openHighscoreModal()"');
const hasCloseFunc = html.includes('function closeHighscoreModal()');
const noInlineLeaderboard = !html.includes('id="leaderboardSection"');

console.log('Modal HTML:', hasModal);
console.log('Open Button:', hasOpenBtn);
console.log('Close Func:', hasCloseFunc);
console.log('No Inline Leaderboard:', noInlineLeaderboard);
