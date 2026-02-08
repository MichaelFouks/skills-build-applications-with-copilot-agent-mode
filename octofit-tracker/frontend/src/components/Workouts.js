import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (data.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-5">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-5">
      <div className="error-message">
        <strong>Error:</strong> {error}
      </div>
    </div>
  );

  return (
    <div className="container mt-5">
      <h2 className="page-header">Workouts</h2>
      {workouts.length === 0 ? (
        <div className="empty-state">
          <p>No workouts found.</p>
        </div>
      ) : (
        <div className="table-container">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Workout Name</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Difficulty</th>
                <th>Calories Target</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout) => (
                <tr key={workout.id}>
                  <td><strong>{workout.name}</strong></td>
                  <td><span className="badge bg-primary">{workout.workout_type}</span></td>
                  <td>{workout.duration}</td>
                  <td>
                    {workout.difficulty === 'Easy' && <span className="badge bg-success">Easy</span>}
                    {workout.difficulty === 'Medium' && <span className="badge bg-warning text-dark">Medium</span>}
                    {workout.difficulty === 'Hard' && <span className="badge bg-danger">Hard</span>}
                    {!['Easy', 'Medium', 'Hard'].includes(workout.difficulty) && <span className="badge bg-secondary">{workout.difficulty}</span>}
                  </td>
                  <td>{workout.calories_target}</td>
                  <td>{workout.description}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Workouts;
