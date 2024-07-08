import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UserRegistration = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const userData = {
            username: username,
            email: email,
            password: password,
        };
        console.log("Sending user data:", userData);  // Log the data being sent
        try {
            const response = await axios.post('/api/users/', userData);
            console.log(response.data);
            const userId = response.data.id;  // Assuming the response contains the user ID
            alert('Registration successful!');
            navigate(`/home/${userId}`);  // Navigate to home after successful registration
        } catch (error) {
            console.error('Error registering user:', error.response.data);
            alert('Error registering user: ' + JSON.stringify(error.response.data));
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Username:</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
            <label>Email:</label>
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <label>Password:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">Register</button>
        </form>
    );
};

export default UserRegistration;
