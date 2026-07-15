import { useState, useRef, useEffect } from "react";
import "./styles/Terminal.css";

interface CommandOutput {
  command: string;
  output: React.ReactNode;
}

const SYSTEM_PROMPT = `You are Ajay Vishwakarma's AI Assistant Clone. You live inside his portfolio's interactive terminal.
Your job is to answer questions from recruiters and visitors as if you were Ajay, or an assistant representing him.
Here is Ajay's info:
- Name: Ajay Vishwakarma
- Role: AI/ML Developer & Full Stack Engineer
- Education: 4th-year B.Tech CSE (AI) at BBD University, Lucknow (8.82 CGPA)
- Skills: Python, TypeScript, React, Next.js, Django, FastAPI, Groq LLM, NLP, PyTorch, Docker, AWS.
- Key Projects: 
  1. EduTech AI (Full Stack SaaS with Groq LLM tutoring, Razorpay, Django)
  2. AI Tutor (NLP conversational learning paths)
  3. Expense Tracker (WhatsApp AI bot)
  4. Digital Twin Platform (Conversational clone)
- Email: ajaykumar160380@gmail.com
- Github: ajay160380
- Tone: Professional, enthusiastic, highly technical but approachable, concise (keep answers under 3 sentences unless asked for details). Do not use emojis unless appropriate. Keep responses raw text suitable for a terminal.
`;

const Terminal = () => {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState<CommandOutput[]>([
    { command: "", output: "Welcome to AjayOS (v1.0.0)\nType 'help' to see available commands or 'ask <your question>' to chat with my AI clone!" }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const terminalBodyRef = useRef<HTMLDivElement>(null);

  const askGroq = async (question: string, cmdToDisplay: string) => {
    setIsLoading(true);
    setHistory((prev) => [...prev, { command: cmdToDisplay, output: "Thinking..." }]);
    
    try {
      const apiKey = import.meta.env.VITE_GROQ_API_KEY;
      if (!apiKey) {
        throw new Error("API key not found. Please add VITE_GROQ_API_KEY to .env file.");
      }

      const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          model: "llama-3.1-8b-instant",
          messages: [
            { role: "system", content: SYSTEM_PROMPT },
            { role: "user", content: question }
          ],
          temperature: 0.7,
        })
      });

      const data = await response.json();
      
      if (data.error) {
        throw new Error(data.error.message || "Unknown API Error");
      }

      const answer = data.choices[0].message.content;
      
      setHistory((prev) => {
        const newHistory = [...prev];
        newHistory[newHistory.length - 1].output = answer;
        return newHistory;
      });

    } catch (error: any) {
      setHistory((prev) => {
        const newHistory = [...prev];
        newHistory[newHistory.length - 1].output = `Error: ${error.message}`;
        return newHistory;
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleCommand = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && !isLoading) {
      const cmd = input.trim();
      const lowerCmd = cmd.toLowerCase();
      let out: React.ReactNode = "";

      if (lowerCmd === "help") {
        out = (
          <div style={{ lineHeight: "1.8" }}>
            Available commands:<br />
            <span style={{ color: "var(--accentColor)" }}>whoami</span>  - About me<br />
            <span style={{ color: "var(--accentColor)" }}>skills</span>  - My tech stack<br />
            <span style={{ color: "var(--accentColor)" }}>contact</span> - Get in touch<br />
            <span style={{ color: "var(--accentColor)" }}>clear</span>   - Clear terminal<br />
            <span style={{ color: "#27c93f", fontWeight: "bold" }}>ask [question]</span> - Chat with my AI Clone! (e.g., "ask what are your skills")<br />
          </div>
        );
        setHistory([...history, { command: cmd, output: out }]);
        setInput("");
      } else if (lowerCmd === "whoami") {
        out = "I'm Ajay Vishwakarma, an AI/ML Developer & Full Stack Engineer passionate about building intelligent systems and scalable web apps.";
        setHistory([...history, { command: cmd, output: out }]);
        setInput("");
      } else if (lowerCmd === "skills") {
        out = "Languages: Python, TypeScript, C++\nFrameworks: React, Next.js, Django, FastAPI\nAI/ML: PyTorch, NLP, Computer Vision, LLMs";
        setHistory([...history, { command: cmd, output: out }]);
        setInput("");
      } else if (lowerCmd === "contact") {
        out = "Email: ajaykumar160380@gmail.com\nLinkedIn: ajayvishwakarma\nGitHub: ajay160380";
        setHistory([...history, { command: cmd, output: out }]);
        setInput("");
      } else if (lowerCmd === "clear") {
        setHistory([]);
        setInput("");
        return;
      } else if (lowerCmd === "sudo") {
        out = "Nice try! This incident will be reported. 🚨";
        setHistory([...history, { command: cmd, output: out }]);
        setInput("");
      } else if (lowerCmd === "") {
        setHistory([...history, { command: cmd, output: "" }]);
        setInput("");
      } else if (lowerCmd.startsWith("ask ")) {
        const question = cmd.substring(4).trim();
        if (question) {
          askGroq(question, cmd);
          setInput("");
          return;
        } else {
          out = "Usage: ask <your question>";
          setHistory([...history, { command: cmd, output: out }]);
          setInput("");
        }
      } else {
        // Automatically send any unrecognized command to the AI!
        askGroq(cmd, cmd);
        setInput("");
        return;
      }
    }
  };

  useEffect(() => {
    if (terminalBodyRef.current) {
      terminalBodyRef.current.scrollTop = terminalBodyRef.current.scrollHeight;
    }
  }, [history]);

  return (
    <div className="terminal-section section-container" id="terminal">
      <h2>
        Interactive <span>AI Console</span>
      </h2>
      <div className="terminal-container">
        <div className="terminal-window" onClick={() => document.getElementById('terminal-input')?.focus()}>
          <div className="terminal-header">
            <div className="terminal-buttons">
              <span className="t-btn close-btn"></span>
              <span className="t-btn min-btn"></span>
              <span className="t-btn max-btn"></span>
            </div>
            <div className="terminal-title">bash - ajay@portfolio: ~</div>
          </div>
          <div className="terminal-body" ref={terminalBodyRef}>
            {history.map((h, i) => (
              <div key={i} className="terminal-line">
                {h.command && (
                  <div className="command-line">
                    <span className="prompt">ajay@portfolio:~$</span> <span className="cmd-text">{h.command}</span>
                  </div>
                )}
                {h.output && <div className="output-line" style={{ whiteSpace: "pre-wrap" }}>{h.output}</div>}
              </div>
            ))}
            <div className="terminal-input-line">
              <span className="prompt">ajay@portfolio:~$</span>
              <input 
                id="terminal-input"
                type="text" 
                value={input} 
                onChange={(e) => setInput(e.target.value)} 
                onKeyDown={handleCommand}
                autoComplete="off"
                spellCheck="false"
                disabled={isLoading}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Terminal;
