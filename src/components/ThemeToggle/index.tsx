import { useTheme } from "../../context/ThemeProvider";
import "./ThemeToggle.css";

const ThemeToggle = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <button 
      className={`theme-toggle-btn ${theme}`} 
      onClick={toggleTheme}
      title={`Switch to ${theme === "crimson" ? "Purple" : "Crimson"} Theme`}
    >
      <div className="toggle-circle"></div>
    </button>
  );
};

export default ThemeToggle;
