import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, ArcElement, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, ArcElement, BarElement, Title, Tooltip, Legend);

const GitHubChart = ({ username, repoName }) => {
  const [chartData, setChartData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`api/github/${username}/repos/${repoName}/activity`);
        const data = response.data;

        const formattedData = {
          labels: data.map(item => item.week), // Adjust according to your data structure
          datasets: [
            {
              label: 'Commit Activity',
              backgroundColor: 'rgba(75,192,192,0.4)',
              borderColor: 'rgba(75,192,192,1)',
              data: data.map(item => item.total), // Adjust according to your data structure
            },
          ],
        };

        setChartData(formattedData);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [username, repoName]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading chart: {error.message}</div>;
  if (!chartData) return <div>No data available</div>;

  return <Line data={chartData} />;
};

export default GitHubChart;
