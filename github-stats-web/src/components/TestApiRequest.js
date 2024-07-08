import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TestApiRequest = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/test/')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.error('There was an error making the request!', error);
            });
    }, []);

    return (
        <div>
            <h1>API Response:</h1>
            <p>{message}</p>
        </div>
    );
};

export default TestApiRequest;
