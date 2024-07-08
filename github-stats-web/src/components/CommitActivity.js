import React, { useEffect, useState } from 'react';
import axios from 'axios';
import GitHubChart from './GitHubChart';

const CommitActivity = ({ username, repoName }) => {
  const [chartData, setChartData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCommitActivity = async () => {
      try {
        const response = await axios.get(`api/github/${username}/repos/${repoName}/activity`);
        const weeklyData = response.data;

        const labels = weeklyData.map((week, index) => `Week ${index + 1}`);
        const data = weeklyData.map(week => week.total);

        setChartData({
          labels,
          datasets: [
            {
              label: 'Commits per week',
              data,
              backgroundColor: 'rgba(75,192,192,0.4)',
              borderColor: 'rgba(75,192,192,1)',
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

    fetchCommitActivity();
  }, [username, repoName]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading data: {error.message}</div>;

  return <GitHubChart data={chartData} />;
};

export default CommitActivity;
