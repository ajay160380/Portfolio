import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import "./styles/Blogs.css";
import { FaArrowRight, FaCalendarAlt, FaBookOpen } from "react-icons/fa";

gsap.registerPlugin(ScrollTrigger);

const blogPosts = [
  {
    id: 1,
    title: "Building an AI Tutor with Groq LLM & Django",
    summary: "A deep dive into integrating Groq's lightning-fast inference with a robust Django backend to create conversational learning paths.",
    date: "Aug 15, 2026",
    readTime: "6 min read",
    link: "#",
    tags: ["AI", "Django", "Groq"]
  },
  {
    id: 2,
    title: "Mastering React Three Fiber for 3D Portfolios",
    summary: "Learn how to build immersive, performant 3D web experiences using R3F, Drei, and GSAP for seamless animations.",
    date: "Jul 22, 2026",
    readTime: "8 min read",
    link: "#",
    tags: ["React", "Three.js", "Web3D"]
  },
  {
    id: 3,
    title: "Optimizing Next.js Apps for Production",
    summary: "Best practices for deploying scalable full-stack Next.js applications, covering caching, server components, and edge rendering.",
    date: "Jun 10, 2026",
    readTime: "5 min read",
    link: "#",
    tags: ["Next.js", "Performance"]
  }
];

const Blogs = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const cardsRef = useRef<(HTMLAnchorElement | null)[]>([]);

  useEffect(() => {
    const ctx = gsap.context(() => {
      gsap.fromTo(
        ".blogs-header",
        { y: 50, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: {
            trigger: ".blogs-section",
            start: "top 80%",
          },
        }
      );

      cardsRef.current.forEach((card, index) => {
        if (!card) return;
        gsap.fromTo(
          card,
          { y: 100, opacity: 0 },
          {
            y: 0,
            opacity: 1,
            duration: 0.8,
            delay: index * 0.15,
            ease: "power3.out",
            scrollTrigger: {
              trigger: ".blogs-section",
              start: "top 75%",
            },
          }
        );
      });
    }, containerRef);

    return () => ctx.revert();
  }, []);

  return (
    <div className="blogs-section section-container" id="blogs" ref={containerRef}>
      <h2 className="blogs-header">
        Latest <span>Articles</span>
      </h2>
      <div className="blogs-grid">
        {blogPosts.map((post, i) => (
          <a 
            key={post.id} 
            href={post.link} 
            className="blog-card"
            ref={(el) => (cardsRef.current[i] = el)}
          >
            <div className="blog-meta">
              <span className="blog-date"><FaCalendarAlt /> {post.date}</span>
              <span className="blog-read"><FaBookOpen /> {post.readTime}</span>
            </div>
            <h3 className="blog-title">{post.title}</h3>
            <p className="blog-summary">{post.summary}</p>
            <div className="blog-footer">
              <div className="blog-tags">
                {post.tags.map(tag => (
                  <span key={tag} className="tag">{tag}</span>
                ))}
              </div>
              <div className="read-more">
                Read <FaArrowRight className="arrow-icon" />
              </div>
            </div>
          </a>
        ))}
      </div>
    </div>
  );
};

export default Blogs;
