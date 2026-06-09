import { useState, useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import "./styles/Guestbook.css";
import { FaPaperPlane, FaQuoteLeft } from "react-icons/fa";
import { HiSparkles } from "react-icons/hi2";

gsap.registerPlugin(ScrollTrigger);

interface Message {
  id: string;
  name: string;
  text: string;
  date: string;
}

const getInitials = (name: string) => {
  return name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .toUpperCase()
    .slice(0, 2);
};

const avatarColors = [
  "linear-gradient(135deg, #667eea, #764ba2)",
  "linear-gradient(135deg, #f093fb, #f5576c)",
  "linear-gradient(135deg, #4facfe, #00f2fe)",
  "linear-gradient(135deg, #43e97b, #38f9d7)",
  "linear-gradient(135deg, #fa709a, #fee140)",
  "linear-gradient(135deg, #a18cd1, #fbc2eb)",
  "linear-gradient(135deg, #fccb90, #d57eeb)",
  "linear-gradient(135deg, #e0c3fc, #8ec5fc)",
];

const getAvatarColor = (name: string) => {
  let hash = 0;
  for (let i = 0; i < name.length; i++) {
    hash = name.charCodeAt(i) + ((hash << 5) - hash);
  }
  return avatarColors[Math.abs(hash) % avatarColors.length];
};

const Guestbook = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [name, setName] = useState("");
  const [text, setText] = useState("");
  const [isSending, setIsSending] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const formRef = useRef<HTMLFormElement>(null);

  useEffect(() => {
    const saved = localStorage.getItem("guestbook_data_v2");
    if (saved) {
      let parsed = JSON.parse(saved);
      parsed = parsed.filter((m: Message) => m.id !== "1" && m.id !== "2");
      setMessages(parsed);
      localStorage.setItem("guestbook_data_v2", JSON.stringify(parsed));
    }
  }, []);

  useEffect(() => {
    const ctx = gsap.context(() => {
      gsap.fromTo(
        ".gb-title-line",
        { y: 80, opacity: 0, rotateX: 40 },
        {
          y: 0,
          opacity: 1,
          rotateX: 0,
          duration: 1.2,
          stagger: 0.15,
          ease: "power4.out",
          scrollTrigger: {
            trigger: ".guestbook-section",
            start: "top 80%",
          },
        }
      );

      gsap.fromTo(
        ".gb-subtitle",
        { y: 30, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 1,
          delay: 0.3,
          ease: "power3.out",
          scrollTrigger: {
            trigger: ".guestbook-section",
            start: "top 80%",
          },
        }
      );

      gsap.fromTo(
        ".gb-form-card",
        { y: 60, opacity: 0, scale: 0.95 },
        {
          y: 0,
          opacity: 1,
          scale: 1,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: {
            trigger: ".gb-content",
            start: "top 85%",
          },
        }
      );

      gsap.fromTo(
        ".gb-messages-card",
        { y: 60, opacity: 0, scale: 0.95 },
        {
          y: 0,
          opacity: 1,
          scale: 1,
          duration: 1,
          delay: 0.2,
          ease: "power3.out",
          scrollTrigger: {
            trigger: ".gb-content",
            start: "top 85%",
          },
        }
      );
    }, containerRef);

    return () => ctx.revert();
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim() || !text.trim()) return;

    setIsSending(true);

    setTimeout(() => {
      const newMessage: Message = {
        id: Date.now().toString(),
        name: name.trim(),
        text: text.trim(),
        date: new Date().toLocaleDateString("en-US", {
          month: "short",
          day: "numeric",
          year: "numeric",
        }),
      };

      const updatedMessages = [newMessage, ...messages];
      setMessages(updatedMessages);
      localStorage.setItem(
        "guestbook_data_v2",
        JSON.stringify(updatedMessages)
      );

      setName("");
      setText("");
      setIsSending(false);

      setTimeout(() => {
        gsap.fromTo(
          ".gb-msg:first-child",
          { scale: 0.8, opacity: 0, y: -30 },
          {
            scale: 1,
            opacity: 1,
            y: 0,
            duration: 0.6,
            ease: "back.out(1.7)",
          }
        );
      }, 50);
    }, 600);
  };

  return (
    <div
      className="guestbook-section section-container"
      id="guestbook"
      ref={containerRef}
    >
      {/* Decorative orbs */}
      <div className="gb-orb gb-orb-1"></div>
      <div className="gb-orb gb-orb-2"></div>

      <div className="gb-header">
        <div className="gb-title-line">
          <span className="gb-title-word">Digital</span>
        </div>
        <div className="gb-title-line">
          <span className="gb-title-word gb-accent">Guestbook</span>
          <HiSparkles className="gb-sparkle" />
        </div>
        <p className="gb-subtitle">
          Leave your mark — drop a message, share some love, or just say hi ✨
        </p>
      </div>

      <div className="gb-content">
        {/* Form Card */}
        <div className="gb-form-card">
          <div className="gb-form-glow"></div>
          <div className="gb-form-inner">
            <div className="gb-form-header">
              <span className="gb-form-badge">
                <FaPaperPlane /> Write
              </span>
              <h3>Leave a Note</h3>
              <p>Your message will be displayed right here for everyone to see.</p>
            </div>

            <form
              className="gb-form"
              onSubmit={handleSubmit}
              ref={formRef}
            >
              <div className="gb-input-group">
                <input
                  type="text"
                  id="gb-name"
                  placeholder=" "
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                  maxLength={30}
                  className="gb-input"
                />
                <label htmlFor="gb-name" className="gb-label">
                  Your Name
                </label>
                <div className="gb-input-line"></div>
              </div>

              <div className="gb-input-group">
                <textarea
                  id="gb-message"
                  placeholder=" "
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  required
                  maxLength={200}
                  rows={4}
                  className="gb-input gb-textarea"
                />
                <label htmlFor="gb-message" className="gb-label">
                  Your Message
                </label>
                <div className="gb-input-line"></div>
              </div>

              <div className="gb-form-footer">
                <span className="gb-char-count">
                  {text.length}/200
                </span>
                <button
                  type="submit"
                  className={`gb-submit ${isSending ? "gb-sending" : ""}`}
                  disabled={isSending}
                >
                  <span className="gb-submit-text">
                    {isSending ? "Sending..." : "Send Message"}
                  </span>
                  <FaPaperPlane className="gb-submit-icon" />
                  <div className="gb-submit-shine"></div>
                </button>
              </div>
            </form>
          </div>
        </div>

        {/* Messages Card */}
        <div className="gb-messages-card">
          <div className="gb-messages-glow"></div>
          <div className="gb-messages-inner">
            <div className="gb-messages-header">
              <span className="gb-form-badge">
                <FaQuoteLeft /> Messages
              </span>
              <div className="gb-msg-count">
                {messages.length}{" "}
                {messages.length === 1 ? "note" : "notes"}
              </div>
            </div>

            <div className="gb-messages-scroll">
              {messages.length === 0 ? (
                <div className="gb-empty">
                  <div className="gb-empty-icon">💬</div>
                  <p>No messages yet. Be the first to leave a note!</p>
                </div>
              ) : (
                messages.map((msg) => (
                  <div key={msg.id} className="gb-msg">
                    <div className="gb-msg-avatar"
                      style={{ background: getAvatarColor(msg.name) }}
                    >
                      {getInitials(msg.name)}
                    </div>
                    <div className="gb-msg-body">
                      <div className="gb-msg-top">
                        <h4>{msg.name}</h4>
                        <span className="gb-msg-date">{msg.date}</span>
                      </div>
                      <p>{msg.text}</p>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Guestbook;
