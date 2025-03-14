// ItemsManager.jsx
import React, { useState, useEffect } from 'react';

function ItemsManager() {
  // Define state for each field
  const [fullName, setFullName] = useState('');
  const [age, setAge] = useState('');
  const [studentType, setStudentType] = useState('Undergraduate');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [about, setAbout] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [items, setItems] = useState([]);

  // Fetch registered users (items) from the backend
  const fetchItems = async () => {
    try {
      const response = await fetch('http://localhost:5001/api/items');
      const data = await response.json();
      setItems(data);
    } catch (error) {
      console.error('Error fetching items:', error);
    }
  };

  useEffect(() => {
    fetchItems();
  }, []);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    // Prepare payload with all form data
    const payload = {
      fullName,
      age,
      studentType,
      email,
      phone,
      about,
      username,
      password
    };
    try {
      const response = await fetch('http://localhost:5001/api/items', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (response.ok) {
        // Clear all fields on success
        setFullName('');
        setAge('');
        setStudentType('Undergraduate');
        setEmail('');
        setPhone('');
        setAbout('');
        setUsername('');
        setPassword('');
        fetchItems();
      } else {
        console.error('Error adding item');
      }
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return (
    <div>
      <h2>User Registration</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name: </label>
          <input 
            type="text" 
            value={fullName} 
            onChange={(e) => setFullName(e.target.value)} 
            placeholder="Enter your full name" 
            required 
          />
        </div>
        <div>
          <label>Age: </label>
          <input 
            type="number" 
            value={age} 
            onChange={(e) => setAge(e.target.value)} 
            placeholder="Enter your age" 
            required 
          />
        </div>
        <div>
          <label>Student Type: </label>
          <select 
            value={studentType} 
            onChange={(e) => setStudentType(e.target.value)}
          >
            <option value="Undergraduate">Undergraduate</option>
            <option value="Graduate">Graduate</option>
          </select>
        </div>
        <div>
          <label>Email: </label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            placeholder="Enter your email" 
            required 
          />
        </div>
        <div>
          <label>Phone Number: </label>
          <input 
            type="tel" 
            value={phone} 
            onChange={(e) => setPhone(e.target.value)} 
            placeholder="Enter your phone number" 
            required 
          />
        </div>
        <div>
          <label>About Me: </label>
          <textarea 
            value={about} 
            onChange={(e) => setAbout(e.target.value)} 
            placeholder="Tell us about yourself" 
          />
        </div>
        <div>
          <label>Username: </label>
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
            placeholder="Choose a username" 
            required 
          />
        </div>
        <div>
          <label>Password: </label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            placeholder="Choose a password" 
            required 
          />
        </div>
        <button type="submit">Register</button>
      </form>
      <h3>Registered Users</h3>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <strong>{item.username}</strong> ({item.fullName}), Age: {item.age}, {item.studentType}<br />
            Email: {item.email}, Phone: {item.phone}<br />
            About: {item.about}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ItemsManager;
