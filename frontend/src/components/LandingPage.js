import React from 'react';
import './LandingPage.css';

function LandingPage() {
  return (
    <div className="landing-page">
      <div className="panel left-panel">
        {/* <!-- Left panel content here --> */}
      </div>
      <div className="panel middle-panel">
        <img src="model1.jpg" alt="Model 1" />
        <h1>Spring Collection</h1>
        <p>Shop the latest styles for the season</p>
        <button>Shop Now</button>
      </div>
      <div className="panel right-panel">
        {/* <!-- Right panel content here --> */}
      </div>
    </div>
  );
}

export default LandingPage;
