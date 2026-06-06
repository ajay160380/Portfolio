import { GitHubCalendar } from 'react-github-calendar';
import "./styles/GithubStats.css";

const GithubStats = () => {
  return (
    <div className="github-section section-container" id="github">
      <div className="github-container">
        <h2>
          My <span>GitHub</span> Activity
        </h2>
        <div className="calendar-wrapper">
          <GitHubCalendar 
            username="ajay160380" 
            colorScheme="dark"
            fontSize={12}
            blockSize={11}
            blockMargin={4}
          />
        </div>
      </div>
    </div>
  );
};

export default GithubStats;
