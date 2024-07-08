import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UserRegistration from './components/UserRegistration';
import TestApiRequest from './components/TestApiRequest';
import UserLogin from './components/UserLogin';
import UserList from './components/UserList';
import UserProfile from './components/UserProfile';
import SocialIntegration from './components/SocialIntegration';
import GitHubIntegration from './components/GitHubIntegration';
import Home from './components/Home';
import GitHubDashboard from './components/GitHubDashboard';
import RepoDetails from './components/RepoDetails';
import HistoricalTrends from './components/HistoricalTrends';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/register" element={<UserRegistration />} />
                <Route path="/login" element={<UserLogin />} />
                <Route path="/home/:userId" element={<Home />} />
                <Route path="/profile/user/:userId" element={<UserProfile />} />
                <Route path="/userlist" element={<UserList />} />
                <Route path="/socialInt/:userId" element={<SocialIntegration />} />
                <Route path="/githubInt/:userId" element={<GitHubIntegration />} />
                <Route path="/githubDash/:username" element={<GitHubDashboard />} />
                <Route path="/repos/:username/:repoName" element={<RepoDetails />} />
                <Route path="/historical/:userId" element={<HistoricalTrends />} />
                <Route path="/test-api" element={<TestApiRequest />} />
                {/* Add other routes here */}
            </Routes>
        </Router>
    );
}

export default App;
