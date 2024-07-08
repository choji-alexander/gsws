import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LogOut = () => {
  const history = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await axios.post(
        '/logout/',
        null,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        }
      );

      if (response.status === 200) {
        // Clear local storage or session storage
        localStorage.removeItem('token'); // Example: Remove token from local storage

        // Redirect to login or another page after successful logout
        history('/login');
      } else {
        throw new Error('Logout failed.');
      }
    } catch (error) {
      console.error('Logout error:', error);
      // Handle error (e.g., show error message)
    }
  };

  return (
    <div>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default LogOut;
