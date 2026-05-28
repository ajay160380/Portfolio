import { createContext, useContext, useEffect, useState } from "react";

type Theme = "crimson" | "purple";

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [theme, setTheme] = useState<Theme>(() => {
    const savedTheme = localStorage.getItem("app-theme") as Theme;
    return savedTheme || "crimson";
  });

  useEffect(() => {
    // Remove all theme classes and apply the current one
    document.body.classList.remove("theme-crimson", "theme-purple");
    document.body.classList.add(`theme-${theme}`);
    localStorage.setItem("app-theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === "crimson" ? "purple" : "crimson"));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
};
