const fs = require('fs');

// Simple benchmark simulation based on index.html structure
let gameData = {
    items: [],
    lastPlayed: []
};

// Populate with 10,000 items to make the stringify cost visible
for (let i = 0; i < 10000; i++) {
    gameData.items.push({
        id: i,
        title: `Anime Title ${i}`,
        youtube: `https://youtube.com/embed/xxxxx${i}`,
        difficulty: Math.floor(Math.random() * 3) + 1,
        hints: [`Hint 1 for ${i}`, `Hint 2 for ${i}`]
    });
}

const iterations = 1000;

console.time('Baseline: stringify on every updateStats()');
for (let i = 0; i < iterations; i++) {
    const itemsCount = gameData.items.length;
    const storageSize = (JSON.stringify(gameData).length / 1024).toFixed(2);
    // document.getElementById('statsCount').textContent = itemsCount;
    // document.getElementById('statsSize').textContent = storageSize + ' KB';
}
console.timeEnd('Baseline: stringify on every updateStats()');

// Optimized version
console.time('Optimized: cached stringify size');
let cachedSize = (JSON.stringify(gameData).length / 1024).toFixed(2);

// update function
for (let i = 0; i < iterations; i++) {
    const itemsCount = gameData.items.length;
    const storageSize = cachedSize;
    // document.getElementById('statsCount').textContent = itemsCount;
    // document.getElementById('statsSize').textContent = storageSize + ' KB';
}
console.timeEnd('Optimized: cached stringify size');
