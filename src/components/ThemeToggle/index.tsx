import { useTheme } from "../../context/ThemeProvider";
import { IoColorPalette } from "react-icons/io5";
import "./ThemeToggle.css";

const ThemeToggle = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <button 
      className={`theme-toggle-btn ${theme}`} 
      onClick={toggleTheme}
      title={`Theme: ${theme.toUpperCase()} (Click to toggle)`}
      aria-label="Toggle Color Theme"
      data-cursor="disable"
    >
      <IoColorPalette className="theme-icon" />
      <span className="theme-text">{theme.toUpperCase()}</span>
      <span className="theme-indicator" />
    </button>
  );
};

export default ThemeToggle;
