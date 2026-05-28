import "./styles/Career.css";

const Career = () => {
  return (
    <div className="career-section section-container">
      <div className="career-container">
        <h2>
          My Education <span>&</span>
          <br /> Experience
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>B.Tech CSE (Artificial Intelligence)</h4>
                <h5>BBD University, Lucknow</h5>
              </div>
              <h3>NOW</h3>
            </div>
            <p>
              Currently pursuing 3rd Year, 6th Semester. Focused on AI/ML,
              full-stack development, and building real-world projects that
              solve meaningful problems.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>NSS Volunteer</h4>
                <h5>National Service Scheme</h5>
              </div>
              <h3>2 Yrs</h3>
            </div>
            <p>
              Completed two years of service through NSS, contributing to
              outreach activities, social initiatives, and community-level
              engagement.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Tech Expo'26 — Certificate of Appreciation</h4>
                <h5>BBD University, Lucknow</h5>
              </div>
              <h3>2026</h3>
            </div>
            <p>
              Recognized for participating in Tech Expo'26 with the Smart Women's
              Safety Device — demonstrating hardware innovation for real-world
              social impact.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Career;
