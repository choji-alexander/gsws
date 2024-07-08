import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const ContributionsByTimeOfDay = ({ username, repoName }) => {
  const [chartData, setChartData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchContributions = async () => {
      try {
        const response = await axios.get(`https://api.github.com/repos/${username}/${repoName}/commits`);
        const commits = response.data;

        const timeData = Array(24).fill(0);
        commits.forEach(commit => {
          const hour = new Date(commit.commit.author.date).getHours();
          timeData[hour]++;
        });

        setChartData({
          labels: [...Array(24).keys()].map(hour => `${hour}:00`),
          datasets: [
            {
              label: 'Commits by Time of Day',
              data: timeData,
              backgroundColor: 'rgba(153, 102, 255, 0.4)',
              borderColor: 'rgba(153, 102, 255, 1)',
              borderWidth: 1,
            },
          ],
        });
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchContributions();
  }, [username, repoName]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading data: {error.message}</div>;

  return <Bar data={chartData} />;
};

export default ContributionsByTimeOfDay;
