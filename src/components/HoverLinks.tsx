import React from "react";
import "./styles/style.css";

const HoverLinks = ({ text, cursor }: { text: React.ReactNode; cursor?: boolean }) => {
  return (
    <div className="hover-link" data-cursor={!cursor && `disable`}>
      <div className="hover-in">
        {text} <div>{text}</div>
      </div>
    </div>
  );
};

export default HoverLinks;
