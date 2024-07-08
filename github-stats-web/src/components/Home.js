import React from 'react';
import { Link, useParams } from 'react-router-dom';
import LogOut from './LogOut';

const Home = () => {
    const { userId } = useParams();

    return (
        <div>
            <h1>Welcome to GitHub Stats</h1>
             <nav>
                <ul>
                    <li>
                        <Link to={`/profile/user/${userId}/`}>User Profile</Link>
                    </li>
                    <li>
                        <Link to={`/githubInt/${userId}`}>GitHub Integration</Link>
                    </li>
                    <li>
                        <Link to={`/socialInt/${userId}`}>Social Integration</Link>
                    </li>
                </ul>
            </nav>
            <LogOut />
        </div>
    );
};

export default Home;
