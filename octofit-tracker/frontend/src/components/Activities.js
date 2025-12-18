import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const items = data.results || data;
        setActivities(items);
        console.log('Fetched activities:', items);
      })
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container">
      <h1 className="mb-4">Activities</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.id}</td>
              <td>{activity.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Activities;