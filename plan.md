1. Modify `loadGameData` in `index.html` to validate the structure of the loaded `gameData`.
   - The user has requested to find a function that is not yet checked for faulty inputs (like an empty video array, invalid answers, missing YouTube IDs).
   - In `loadGameData()`, it tries to parse `localStorage.getItem(STORAGE_KEY)`. If successful, it assigns `gameData = JSON.parse(stored)`. But it does NOT validate if `gameData` is an object, or if `gameData.items` is a valid array of items.
   - If the user modified `localStorage` manually or there was a bug, `gameData` could be empty, have no `items`, or `items` might be an empty array or an array of invalid items.
   - We will add validation in `loadGameData`:
     - After parsing, we check if `!gameData || typeof gameData !== 'object'`.
     - We also check if `!Array.isArray(gameData.items)`.
     - We should filter `gameData.items` to only keep valid items (having id, title, and youtube link).
     - If the remaining valid items array is empty, we show a user-friendly fallback message using `showMessage('No valid entries found in local storage! Loading defaults...', 'warning');` and we reset `gameData` to `{ items: [], lastPlayed: [] }` so that `createDefaultData()` (which is called right after `loadGameData()` in `init()`) will populate it with default data.

2. Review `preprocessGameData`
   - It iterates over `gameData.items` and does `item.titleLower = item.title.toLowerCase()`. If `item` doesn't have a `title` or `gameData.items` is not an array, it might fail. Adding checks in `loadGameData` solves this.

3. Update `loadGameData` implementation details:
```javascript
<<<<<<< SEARCH
        function loadGameData() {
            const stored = localStorage.getItem(STORAGE_KEY);
            if (stored) {
                try {
                    gameData = JSON.parse(stored);
                    cachedStorageSize = (stored.length / 1024).toFixed(2);
                    preprocessGameData();
                } catch (e) {
                    console.error('Fehler beim Laden der Daten:', e);
                    gameData = { items: [], lastPlayed: [] };
                }
            }
        }
=======
        function loadGameData() {
            const stored = localStorage.getItem(STORAGE_KEY);
            if (stored) {
                try {
                    const parsedData = JSON.parse(stored);

                    if (!parsedData || typeof parsedData !== 'object' || !Array.isArray(parsedData.items)) {
                        throw new Error('Invalid data structure');
                    }

                    const validItems = parsedData.items.filter(item =>
                        item &&
                        typeof item.title === 'string' && item.title.trim() !== '' &&
                        typeof item.youtube === 'string' && item.youtube.trim() !== ''
                    );

                    if (validItems.length === 0) {
                        showMessage('No valid entries found in saved data! Loading defaults...', 'warning');
                        gameData = { items: [], lastPlayed: [] };
                    } else {
                        parsedData.items = validItems;
                        gameData = parsedData;
                        cachedStorageSize = (stored.length / 1024).toFixed(2);
                        preprocessGameData();
                    }
                } catch (e) {
                    console.error('Fehler beim Laden der Daten:', e);
                    showMessage('Error loading saved data! Loading defaults...', 'error');
                    gameData = { items: [], lastPlayed: [] };
                }
            }
        }
>>>>>>> REPLACE
```

4. Pre-commit check to make sure the tests pass.
