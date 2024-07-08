import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import HistoricalTrends from './HistoricalTrends';

const GitHubDashboard = () => {
  const { username, userId } = useParams();
  const [profile, setProfile] = useState(null);
  const [repos, setRepos] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const profileResponse = await axios.get(`https://api.github.com/users/${username}`);
        const reposResponse = await axios.get(`https://api.github.com/users/${username}/repos`);

        setProfile(profileResponse.data);
        setRepos(reposResponse.data);
        setError(null);
      } catch (err) {
        setError('User not found');
        setProfile(null);
        setRepos([]);
      }
    };

    fetchProfile();
  }, [username]);

  return (
    <div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {profile && (
        <div>
          <h2>{profile.name}</h2>
          <p>Repositories: {profile.public_repos}</p>
          <p>Followers: {profile.followers}</p>
          <p>Following: {profile.following}</p>
          <p>Company: {profile.company}</p>
          <p>Location: {profile.location}</p>
          <img src={profile.avatar_url} alt={`${profile.name}'s avatar`} width={100} />
          <HistoricalTrends userId={userId} />
        </div>
      )}
      {repos.length > 0 && (
        <div>
          <h3>Repositories:</h3>
          <ul>
            {repos.map((repo) => (
              <li key={repo.id}>
                <Link to={`/repos/${username}/${repo.name}`}>{repo.name}</Link>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default GitHubDashboard;
