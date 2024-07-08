import React, { useEffect, useState } from 'react';
import axios from 'axios';
import GitHubChart from './GitHubChart';

const RepoStars = ({ username, repoName }) => {
    const [chartData, setChartData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
      const fetchRepoStars = async () => {
        try {
          const response = await axios.get(`https://api.github.com/repos/${username}/${repoName}/stargazers`);
          const starData = response.data;
  
          const labels = starData.map(star => new Date(star.starred_at).toLocaleDateString());
          const data = starData.map(() => 1).reduce((acc, val, i) => {
            acc.push((acc[i - 1] || 0) + val);
            return acc;
          }, []);
  
          setChartData({
            labels,
            datasets: [
              {
                label: 'Stars over time',
                data,
                backgroundColor: 'rgba(255,206,86,0.4)',
                borderColor: 'rgba(255,206,86,1)',
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
  
      fetchRepoStars();
    }, [username, repoName]);
  
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error loading data: {error.message}</div>;
  
    return <GitHubChart data={chartData} />;
  };
  
  export default RepoStars;
  