import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const HistoricalTrends = () => {
  const { userId } = useParams(); // Retrieve the userId from the URL parameters
  const [historicalData, setHistoricalData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchHistoricalData = async () => {
      try {
        const response = await axios.get(`api/profiles/${userId}/historical_data/`);
        setHistoricalData(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    if (userId) {
      fetchHistoricalData();
    } else {
      setError(new Error('User ID is undefined'));
      setLoading(false);
    }
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading historical data: {error.message}</div>;
  if (!historicalData) return <div>No historical data found.</div>;

  return (
    <div>
      <h1>Historical Trends for User {userId}</h1>
      {/* Render the historical data here */}
      {historicalData.map((data, index) => (
        <div key={index}>
          <p>Week: {data.week}</p>
          <p>Commits: {data.commits}</p>
          {/* Render other relevant historical data */}
        </div>
      ))}
    </div>
  );
};

export default HistoricalTrends;
