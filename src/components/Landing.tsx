import { PropsWithChildren } from "react";
import { smoother } from "./Navbar";
import "./styles/Landing.css";

const Landing = ({ children }: PropsWithChildren) => {
  const handleScrollTo = (e: React.MouseEvent, targetId: string) => {
    e.preventDefault();
    if (smoother && window.innerWidth > 1024) {
      smoother.scrollTo(targetId, true, "top top");
    } else {
      const el = document.querySelector(targetId);
      if (el) {
        el.scrollIntoView({ behavior: "smooth" });
      }
    }
  };

  const handleOpenResume = (e: React.MouseEvent) => {
    e.preventDefault();
    window.open("/Ajay_Vishwakarma_Resume.pdf", "_blank", "noopener,noreferrer");
  };

  return (
    <>
      <div className="landing-section" id="landingDiv">
        <div className="landing-container">
          {/* Left Hero Card / Introduction */}
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
              Available for Data & AI/ML Roles
            </div>

            <div className="landing-badge">
              <span className="badge-spark">✦</span> Data Analyst & AI/ML Engineer
            </div>

            <div className="landing-pills">
              <span className="landing-pill">Python</span>
              <span className="landing-pill">SQL</span>
              <span className="landing-pill">Power BI</span>
              <span className="landing-pill">PyTorch</span>
              <span className="landing-pill">Tableau</span>
            </div>

            <div className="landing-stats-row">
              <div className="landing-stat-item">
                <span className="landing-stat-num">15+</span>
                <span className="landing-stat-label">Projects</span>
              </div>
              <div className="landing-stat-divider"></div>
              <div className="landing-stat-item">
                <span className="landing-stat-num">98%</span>
                <span className="landing-stat-label">Accuracy</span>
              </div>
              <div className="landing-stat-divider"></div>
              <div className="landing-stat-item">
                <span className="landing-stat-num">BI & ML</span>
                <span className="landing-stat-label">Specialist</span>
              </div>
            </div>
          </div>

          {/* Right Hero Info & Call to Action */}
          <div className="landing-info">
            <h3>A Passionate</h3>
            <h2 className="landing-role-heading">
              <span className="landing-h2-info">DATA ANALYST</span>
              <span className="landing-h2-info-1">AI/ML ENGINEER</span>
            </h2>

            <p className="landing-bio-subtitle">
              Transforming complex data into predictive ML models and actionable business intelligence dashboards.
            </p>

            <div className="landing-cta-group">
              <a
                href="#work"
                onClick={(e) => handleScrollTo(e, "#work")}
                className="landing-cta-btn primary"
                data-cursor="pointer"
              >
                <span>Explore Work</span>
                <svg
                  width="13"
                  height="13"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M7 17l9.2-9.2M17 17V8H8" />
                </svg>
              </a>
              <a
                href="/Ajay_Vishwakarma_Resume.pdf"
                onClick={handleOpenResume}
                target="_blank"
                rel="noreferrer"
                className="landing-cta-btn resume"
                data-cursor="pointer"
              >
                <span>Resume CV ↗</span>
              </a>
              <a
                href="#terminal"
                onClick={(e) => handleScrollTo(e, "#terminal")}
                className="landing-cta-btn secondary"
                data-cursor="pointer"
              >
                <span>AI Terminal &gt;_</span>
              </a>
            </div>
          </div>

          {/* Animated Scroll Indicator */}
          <div
            className="landing-scroll-indicator"
            onClick={(e) => handleScrollTo(e, "#about")}
            style={{ cursor: "pointer" }}
            data-cursor="pointer"
          >
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
