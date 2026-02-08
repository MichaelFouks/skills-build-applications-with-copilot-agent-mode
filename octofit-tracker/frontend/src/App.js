import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofitapp-small.png" alt="OctoFit Logo" className="navbar-logo" />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-5">
              <div className="jumbotron text-center">
                <h1 className="display-4">🏋️ Welcome to OctoFit Tracker!</h1>
                <p className="lead">Track your fitness activities, compete with your team, and achieve your goals.</p>
                <hr className="my-4" />
                <p>Use the navigation menu to explore different sections of the app.</p>
                <div className="row mt-5">
                  <div className="col-md-4 mb-3">
                    <div className="card">
                      <div className="card-body text-center">
                        <h3>👥 Users</h3>
                        <p>Manage user profiles and track individual progress</p>
                        <Link to="/users" className="btn btn-primary">View Users</Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4 mb-3">
                    <div className="card">
                      <div className="card-body text-center">
                        <h3>🤝 Teams</h3>
                        <p>Create and manage teams for group competitions</p>
                        <Link to="/teams" className="btn btn-primary">View Teams</Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4 mb-3">
                    <div className="card">
                      <div className="card-body text-center">
                        <h3>🏃 Activities</h3>
                        <p>Log and track all fitness activities</p>
                        <Link to="/activities" className="btn btn-primary">View Activities</Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-6 mb-3">
                    <div className="card">
                      <div className="card-body text-center">
                        <h3>💪 Workouts</h3>
                        <p>Browse suggested workouts and exercises</p>
                        <Link to="/workouts" className="btn btn-primary">View Workouts</Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-6 mb-3">
                    <div className="card">
                      <div className="card-body text-center">
                        <h3>🏆 Leaderboard</h3>
                        <p>See who's leading the fitness challenge</p>
                        <Link to="/leaderboard" className="btn btn-primary">View Leaderboard</Link>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
