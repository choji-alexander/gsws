import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

const GitHubIntegration = () => {
  const { userId } = useParams(); // Use useParams to get userId from the URL
  const [repoName, setRepoName] = useState('default-repo'); 
  const [repos, setRepos] = useState([]);
  const [userInfo, setUserInfo] = useState(null);
  const navigate = useNavigate();
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [reposResponse, userInfoResponse, eventsResponse] = await Promise.all([
          axios.get(`/api/users/${userId}/github_data?type=repos`),
          axios.get(`/api/users/${userId}/github_data?type=userinfo`),
          axios.get(`/api/users/${userId}/github_data?type=events`),
        ]);

        setRepos(reposResponse.data);
        setUserInfo(userInfoResponse.data);
        setEvents(eventsResponse.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching GitHub data:', error);
        setError('Error fetching GitHub data. Please try again later.');
        setLoading(false);
      }
    };

    fetchData();
  }, [userId]);

  const handleNavigateToDashboard = () => {
    navigate(`/githubDash/${userInfo.login}`);
  };

  <input
        type="text"
        value={repoName}
        onChange={(e) => setRepoName(e.target.value)}
        placeholder="Enter GitHub repository name"
      />

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>GitHub Integration</h1>
      
      <h2>User Information</h2>
      {userInfo && (
        <div>
          <p>Name: {userInfo.name}</p>
          {/* Render other user information */}
        </div>
      )}
      <button onClick={handleNavigateToDashboard}>Go to GitHub Dashboard</button>
      <h2>GitHub Repositories</h2>
      <ul>
        {repos.map((repo) => (
          <li key={repo.id}>{repo.name}</li>
        ))}
      </ul>

      <h2>GitHub Events</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>{event.type}</li>
        ))}
      </ul>
    </div>
  );
};

export default GitHubIntegration;
