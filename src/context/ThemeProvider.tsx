import { createContext, useContext, useEffect, useState } from "react";

export type Theme = "cyan" | "emerald" | "crimson" | "purple";

interface ThemeContextType {
  theme: Theme;
  setTheme: (theme: Theme) => void;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

const THEMES: Theme[] = ["cyan", "emerald", "crimson", "purple"];

export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [theme, setTheme] = useState<Theme>(() => {
    const savedTheme = localStorage.getItem("app-theme") as Theme;
    return THEMES.includes(savedTheme) ? savedTheme : "cyan";
  });

  useEffect(() => {
    // Remove all theme classes and apply the current one
    document.body.classList.remove(
      "theme-cyan",
      "theme-emerald",
      "theme-crimson",
      "theme-purple"
    );
    document.body.classList.add(`theme-${theme}`);
    localStorage.setItem("app-theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prevTheme) => {
      const currentIndex = THEMES.indexOf(prevTheme);
      const nextIndex = (currentIndex + 1) % THEMES.length;
      return THEMES[nextIndex];
    });
  };

  return (
    <ThemeContext.Provider value={{ theme, setTheme, toggleTheme }}>
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

