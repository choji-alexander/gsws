import React from 'react';
import CommitActivity from './CommitActivity';
import GitHubChart from './GitHubChart';
import RepoStars from './RepoStars';
import ContributionsByTimeOfDay from './ContributionsByTimeOfDay';
import LanguageUsage from './LanguageUsage';
import { useParams } from 'react-router-dom';

const RepoDetails = () => {
  const { username, repoName } = useParams();

  return (
    <div>
      <h1>Repository: {repoName}</h1>
      <CommitActivity username={username} repoName={repoName} />
      <GitHubChart username={username} repoName={repoName} />
      <RepoStars username={username} repoName={repoName} />
      <ContributionsByTimeOfDay username={username} repoName={repoName} />
      <LanguageUsage username={username} repoName={repoName} />
    </div>
  );
};

export default RepoDetails;
