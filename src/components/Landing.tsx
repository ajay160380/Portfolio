import { PropsWithChildren } from "react";
import "./styles/Landing.css";

const Landing = ({ children }: PropsWithChildren) => {
  return (
    <>
      <div className="landing-section" id="landingDiv">
        <div className="landing-container">
          <div className="landing-intro">
            <div className="landing-greeting">
              <span className="greeting-line"></span>
              <h2>Hello! I'm</h2>
            </div>
            <h1>
              AJAY
              <br />
              <span>VISHWAKARMA</span>
            </h1>
            <div className="landing-status">
              <span className="status-dot"></span>
              Available for work
            </div>
          </div>
          <div className="landing-info">
            <h3>A Passionate</h3>
            <h2 className="landing-info-h2">
              <div className="landing-h2-1">AI/ML Dev</div>
              <div className="landing-h2-2">Full Stack</div>
            </h2>
            <h2>
              <div className="landing-h2-info">AI/ML Dev</div>
              <div className="landing-h2-info-1">Full Stack</div>
            </h2>
          </div>
          <div className="landing-scroll-indicator">
            <div className="scroll-mouse">
              <div className="scroll-wheel"></div>
            </div>
            <span>Scroll Down</span>
          </div>
        </div>
        {children}
      </div>
    </>
  );
};

export default Landing;

