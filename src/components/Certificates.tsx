import "./styles/Certificates.css";
import { MdArrowOutward } from "react-icons/md";
import { useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger);

const onlineCerts = [
  { name: "Business Analysis & Process Management", platform: "Coursera", link: "https://coursera.org/share/0b01c7a552ca4668320dcc4d43b3c9cd" },
  { name: "Build a Free Website with WordPress", platform: "Coursera", link: "https://coursera.org/share/8b9bf68550341017ded184a3f99ba728" },
  { name: "ChatGPT for Beginners", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/ICACOUAT" },
  { name: "Python Fundamentals for Beginners", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/GDIAYRXD" },
  { name: "Artificial Intelligence Fundamentals", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/NAEPZYZS" },
  { name: "Introduction to Artificial Intelligence", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/IHIHRTTV" },
  { name: "Generative AI for Beginners", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/NPFNWUMQ" },
  { name: "C Programming in Hindi", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/CCSLHXPI" },
  { name: "C for Beginners", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/GXBYRAXH" },
  { name: "Applications of Artificial Intelligence", platform: "Great Learning", link: "https://www.mygreatlearning.com/certificate/NWPXMQVD" },
];

const Certificates = () => {
  const sectionRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    const section = sectionRef.current;
    if (!section) return;

    // Animate the heading
    gsap.fromTo(
      section.querySelector("h2"),
      { y: 80, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector("h2"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate the featured certificate
    gsap.fromTo(
      section.querySelector(".cert-featured"),
      { y: 60, opacity: 0, scale: 0.95 },
      {
        y: 0,
        opacity: 1,
        scale: 1,
        duration: 0.8,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector(".cert-featured"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate the featured image with a subtle glow
    gsap.fromTo(
      section.querySelector(".cert-featured-img"),
      { x: -40, opacity: 0 },
      {
        x: 0,
        opacity: 1,
        duration: 0.8,
        delay: 0.2,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector(".cert-featured"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate the featured info
    gsap.fromTo(
      section.querySelector(".cert-featured-info"),
      { x: 40, opacity: 0 },
      {
        x: 0,
        opacity: 1,
        duration: 0.8,
        delay: 0.3,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector(".cert-featured"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate cert cards one by one (stagger)
    const cards = section.querySelectorAll(".cert-card");
    gsap.fromTo(
      cards,
      { y: 50, opacity: 0, scale: 0.9 },
      {
        y: 0,
        opacity: 1,
        scale: 1,
        duration: 0.5,
        stagger: 0.08,
        ease: "back.out(1.2)",
        scrollTrigger: {
          trigger: section.querySelector(".cert-grid"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate cert tags with a pop effect
    const tags = section.querySelectorAll(".cert-tag");
    gsap.fromTo(
      tags,
      { scale: 0, opacity: 0 },
      {
        scale: 1,
        opacity: 1,
        duration: 0.4,
        stagger: 0.1,
        ease: "back.out(2)",
        scrollTrigger: {
          trigger: section.querySelector(".cert-tags"),
          start: "top 90%",
          toggleActions: "play none none reverse",
        },
      }
    );
  }, []);

  const handleGridMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const cards = document.querySelectorAll(".cert-card");
    cards.forEach((card) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      (card as HTMLElement).style.setProperty("--mouse-x", `${x}px`);
      (card as HTMLElement).style.setProperty("--mouse-y", `${y}px`);
    });
  };

  const handleFeaturedMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const card = e.currentTarget;
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = ((y - centerY) / centerY) * -8;
    const rotateY = ((x - centerX) / centerX) * 8;
    card.style.transform = `perspective(1500px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    card.style.transition = "none";
    card.style.setProperty("--mouse-x", `${x}px`);
    card.style.setProperty("--mouse-y", `${y}px`);
  };

  const handleFeaturedMouseLeave = (e: React.MouseEvent<HTMLDivElement>) => {
    const card = e.currentTarget;
    card.style.transform = `perspective(1500px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
    card.style.transition = "transform 0.6s cubic-bezier(0.23, 1, 0.32, 1)";
  };

  return (
    <div className="cert-section section-container" id="certificates" ref={sectionRef}>
      <div className="cert-container">
        <h2>
          My <span>Certifications</span>
        </h2>
        
        {/* Featured Certificate */}
        <div 
          className="cert-featured"
          onMouseMove={handleFeaturedMouseMove}
          onMouseLeave={handleFeaturedMouseLeave}
        >
          <div className="cert-featured-glow"></div>
          <div className="cert-featured-img">
            <img src="https://i.ibb.co/B5Lm5YD0/Tech-Expo.png" alt="Tech Expo'26 Certificate" />
            <div className="cert-shine"></div>
          </div>
          <div className="cert-featured-info">
            <div className="cert-badge">⭐ Featured Achievement</div>
            <h3>Tech Expo'26 — Certificate of Appreciation</h3>
            <h4>BBD University, Lucknow</h4>
            <p>
              Recognized for participating in Tech Expo'26 with the Smart Women's Safety Device — 
              demonstrating hardware innovation for real-world social impact at a university-level 
              technology exhibition.
            </p>
            <div className="cert-tags">
              <span className="cert-tag">Event Participation</span>
              <span className="cert-tag">Hardware Innovation</span>
              <span className="cert-tag">Social Impact</span>
            </div>
          </div>
        </div>

        {/* Online Certifications Grid */}
        <div className="cert-grid" onMouseMove={handleGridMouseMove}>
          {onlineCerts.map((cert, index) => (
            <div className="cert-card" key={index}>
              <div className="cert-card-border"></div>
              <div className="cert-card-content">
                <div className="cert-card-number">{String(index + 1).padStart(2, '0')}</div>
                <div>
                  <h4>{cert.name}</h4>
                  <p>{cert.platform}</p>
                </div>
                <a href={cert.link} target="_blank" rel="noreferrer" data-cursor="disable">
                  View Credential <MdArrowOutward className="cert-link-icon" />
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Certificates;
