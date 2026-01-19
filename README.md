# 🎌 Anime YouTube Guessing Game Pro

> ⚠️ **STATUS: WORK IN PROGRESS** - This project is still in active development. Features may change, and improvements are ongoing.

An interactive web game where players guess anime series from hidden YouTube videos. Features visibility sliders, hint system, difficulty levels, and a complete admin panel for managing entries with LocalStorage persistence.

**Live Demo**: Open `youtube_game_hidden.html` directly in your browser

---

## 🎮 Features

### Main Game
- 🎬 **Video Guessing Game**: Identify anime from hidden YouTube videos
- 🎥 **Visibility Slider**: Adjust video visibility from 10-90%
- 💡 **Hint System**: 3 hints per round (with point penalties)
- ⭐ **Difficulty Levels**: Filter videos by difficulty (Easy/Medium/Hard)
- 🏆 **Points System**: 
  - Base: 100 points
  - +5 points per difficulty level
  - +10 points per unused hint

### Admin Panel (Password: `admin123`)
- ➕ **Add Videos**: Paste YouTube links directly from address bar
- ✏️ **Edit Videos**: Modify title, link, and difficulty
- 🗑️ **Delete Videos**: Remove entries from database
- 💾 **Data Management**: 
  - Export to JSON format
  - Import from JSON backups
  - Reset to defaults
- 📊 **Statistics**: Live display of entries and storage size

### Statistics & Tracking
- 📈 **Real-time Stats**: Points, correct answers, wrong answers
- 📊 **Accuracy Rate**: Win percentage calculation
- 💾 **LocalStorage**: All data persists in browser

---

## 🚀 Quickstart

1. **Open File**: Save `youtube_game_hidden.html` and open in browser
2. **Play**: Click "▶️ START VIDEO" to begin
3. **Admin**: Click ⚙️ button (bottom right), password: `admin123`

---

## 🎯 How to Play

1. **Start Video**: Click button to unlock hidden video
2. **Adjust Visibility**: Use slider to see video more clearly
3. **Get Hints**: Click "💡 Get Hint" for up to 3 hints
4. **Enter Answer**: Type anime name with autocomplete support
5. **Earn Points**: Faster + fewer hints = more points!

---

## 📋 Admin Panel - Tutorials

### Add Video
1. Click ⚙️ → Enter password → "New Entry" tab
2. Enter anime name
3. Paste YouTube link (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`)
4. Choose difficulty (1-10)
5. Click "✅ Add"

### Manage Videos
1. Click ⚙️ → "Manage" tab
2. Use ✏️ to edit or 🗑️ to delete

### Backup/Restore Data
1. Click ⚙️ → "Data" tab
2. **Export**: Save all videos as JSON
3. **Import**: Load previously exported data
4. **Delete**: Reset to default data

---

## 🛠️ Technical Details

### Stack
- **HTML5**: Structure and semantic markup
- **CSS3**: Responsive design, gradients, animations
- **Vanilla JavaScript**: No dependencies
- **localStorage**: Persistent data storage

### Browser Compatibility
- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Mobile browsers

### Data Structure
```json
{
  "items": [
    {
      "id": 1,
      "title": "Demon Slayer",
      "youtube": "https://www.youtube.com/embed/VQGCKyvzIM0",
      "difficulty": 3,
      "hints": ["Hint 1", "Hint 2", "Hint 3"]
    }
  ],
  "lastPlayed": []
}
```

---

## 🎨 Features in Detail

### Video Viewing
- YouTube embed with hidden overlay
- Dynamic visibility control
- Responsive container (960×540px, mobile: 100%)

### Input Handling
- **Autocomplete**: Suggests known anime names
- **Case-insensitive**: "demon slayer" = "Demon Slayer"
- **Validation**: Empty inputs ignored

### Difficulty Filter
- **Easy** (1-3 stars): Popular, well-known anime
- **Medium** (4-5 stars): Known, but not trivial
- **Hard** (6-10 stars): Niche series, challenge level

### Points Calculation
```
Points = 100 + (Difficulty × 5) + ((3 - Used Hints) × 10)
```

**Examples:**
- Demon Slayer (Difficulty 3, 0 hints): 100 + 15 + 30 = **145 Points**
- Death Note (Difficulty 5, 2 hints): 100 + 25 + 10 = **135 Points**

---

## 🔐 Security

- **Admin Password**: Default `admin123` (changeable in code)
- **Client-Side Only**: No server/API - all runs locally
- **No External Dependencies**: Completely independent

### Change Password
Open the HTML and modify this line:
```javascript
const ADMIN_PASSWORD = 'admin123';  // Change here!
```

---

## 💾 Data Storage

All data automatically stored in `localStorage`:
- Anime entries
- Game statistics
- User progress

**Clear Data**: Admin → Data → "Delete All Data"

---

## 🎨 UI/UX Features

### Design System
- 🎨 **Gradient Header**: Red (#FF1744) to Dark Red (#C41C3B)
- 📱 **Responsive Layout**: Mobile-optimized (768px breakpoint)
- ✨ **Animations**: 
  - Pulse animation for video icon
  - Hover effects on buttons
  - Smooth transitions
- 🌈 **Color Scheme**: 
  - Primary: Red
  - Success: Green
  - Warning: Orange
  - Danger: Red
  - Secondary: Blue

### Mobile Optimizations
- Responsive video container
- Flexible stats layout
- Touch-friendly button sizes
- Optimized modals for small screens

---

## 📦 Files

- `youtube_game_hidden.html` - Complete all-in-one game (single file)

---

## 🐛 Known Limitations

- YouTube videos must have embedding enabled
- Some videos may not embed due to licensing
- localStorage limit: ~5-10MB per browser/domain
- Admin password visible in code

---

## 🚀 Possible Extensions

- [ ] Backend integration (Node.js/Express)
- [ ] Database (MongoDB/Firebase)
- [ ] Multiplayer mode
- [ ] Leaderboard/Rankings
- [ ] Custom themes
- [ ] Categories (Studio, Release Year, etc.)
- [ ] Anime cover images as preview

---

## 📝 License

This project is freely usable. Use it however you like! 🎉

---

## 👨‍💻 Developer Info

**Built with**: HTML5, CSS3, Vanilla JavaScript  
**Purpose**: Fun anime guessing game with admin functionality  
**Status**: 🔄 Work in Progress

---

## 💬 Support

If you have issues or improvement suggestions, you can modify them directly in the code. The system is based completely on local storage - easy to debug!

---

**Have fun playing! 🎌🎬**