import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import GitHubLogin from './GitHubLogin';

const UserLogin = () => {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        throw new Error('Error logging in');
      }
      const data = await response.json();
      console.log('User logged in successfully:', data);
      // Redirect to home with user ID
      navigate(`/home/${data.user_id}`);
    } catch (error) {
      console.error('Error logging in user:', error);
    }
  };

  return (
    <div>
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" value={formData.username} onChange={handleChange} placeholder="Username" required />
      <input type="password" name="password" value={formData.password} onChange={handleChange} placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <GitHubLogin />
    </div>
  );
};

export default UserLogin;
