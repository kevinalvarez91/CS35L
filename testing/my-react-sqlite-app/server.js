const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

// Initialize express app
const app = express();
app.use(express.json());

// Configure CORS to allow requests from http://localhost:3000
app.use(cors({
  origin: 'http://localhost:3000', // Allow requests from this origin
  methods: ['GET', 'POST'], // Allow only specified HTTP methods
  credentials: true // Allow credentials (if needed)
}));

// Connect to SQLite database
const db = new sqlite3.Database('./database.sqlite', (err) => {
  if (err) {
    console.error('Error connecting to database:', err.message);
  } else {
    console.log('Connected to the SQLite database');
    // Create table if it doesn't exist
    db.run(`CREATE TABLE IF NOT EXISTS items (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      fullName TEXT NOT NULL,
      age INTEGER,
      studentType TEXT,
      email TEXT,
      phone TEXT,
      about TEXT,
      username TEXT NOT NULL,
      password TEXT NOT NULL
    )`);
  }
});

// API endpoints
app.get('/api/items', (req, res) => {
  db.all('SELECT * FROM items', [], (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

app.post('/api/items', (req, res) => {
  const { fullName, age, studentType, email, phone, about, username, password } = req.body;
  db.run(
    `INSERT INTO items (fullName, age, studentType, email, phone, about, username, password) 
     VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
    [fullName, age, studentType, email, phone, about, username, password],
    function(err) {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.json({ id: this.lastID });
    }
  );
});

// Start server
const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});