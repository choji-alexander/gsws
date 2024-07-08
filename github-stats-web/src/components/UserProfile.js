import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const UserProfile = () => {
  const { userId } = useParams(); // Get the ID from the URL
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true); // Add a loading state
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axios.get(`/api/profiles/user/${userId}/`);
        setProfile(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false); // Stop loading after the request finishes
      }
    };

    fetchProfile();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading profile: {error.message}</div>;
  if (!profile) return <div>No profile found.</div>;
  
  return (
    <div>
      <h1>{profile.user?.username}</h1>
      <p>{profile.bio}</p>

      {/* Render other profile details */}
    </div>
  );
};

export default UserProfile;
