import React from 'react';

const GitHubLogin = () => {
  const handleLogin = () => {
    const clientId = 'Ov23lifxMWPYCuQC1VTn';
    const redirectUri = 'http://localhost:8000/oauth/callback';
    const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}`;

    window.location.href = githubAuthUrl;
  };

  return (
    <div>
      <button onClick={handleLogin}>Login with GitHub</button>
    </div>
  );
};

export default GitHubLogin;
