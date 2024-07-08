import React, { useState } from 'react';
import { useParams } from 'react-router-dom';

const SocialIntegration = () => {
  const { userId } = useParams();
  const [formData, setFormData] = useState({ platform: '', profile_url: '' });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`/api/users/${userId}/link_social_profile/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        throw new Error('Error linking social profile');
      }
      const data = await response.json();
      console.log('Social profile linked successfully:', data);
    } catch (error) {
      console.error('Error linking social profile:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="platform"
        value={formData.platform}
        onChange={handleChange}
        placeholder="Platform"
        required
      />
      <input
        type="text"
        name="profile_url"
        value={formData.profile_url}
        onChange={handleChange}
        placeholder="Profile URL"
        required
      />
      <button type="submit">Link Profile</button>
    </form>
  );
};

export default SocialIntegration;
