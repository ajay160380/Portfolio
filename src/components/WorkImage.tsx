import { useState } from "react";
import { MdArrowOutward } from "react-icons/md";

interface Props {
  image: string;
  alt?: string;
  video?: string;
  link?: string;
  secondaryLink?: string;
}

const WorkImage = (props: Props) => {
  const [isVideo, setIsVideo] = useState(false);
  const [video, setVideo] = useState("");
  const handleMouseEnter = async () => {
    if (props.video) {
      setIsVideo(true);
      const response = await fetch(`src/assets/${props.video}`);
      const blob = await response.blob();
      const blobUrl = URL.createObjectURL(blob);
      setVideo(blobUrl);
    }
  };

  return (
    <div className="work-image">
      <div
        className="work-image-in"
        onClick={() => { if (props.link) window.open(props.link, "_blank"); }}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={() => setIsVideo(false)}
        style={{ cursor: props.link ? 'pointer' : 'default' }}
        data-cursor={"disable"}
      >
        {props.link && (
          <a 
            className="work-link" 
            href={props.link} 
            target="_blank" 
            rel="noreferrer"
            onClick={(e) => e.stopPropagation()}
            title="Primary Link"
          >
            <MdArrowOutward />
          </a>
        )}
        {props.secondaryLink && (
          <a 
            className="work-link" 
            href={props.secondaryLink} 
            target="_blank" 
            rel="noreferrer"
            style={{ right: '70px' }} 
            onClick={(e) => e.stopPropagation()}
            title="Secondary Link"
          >
            <MdArrowOutward />
          </a>
        )}
        <img src={props.image} alt={props.alt} />
        {isVideo && <video src={video} autoPlay muted playsInline loop></video>}
      </div>
    </div>
  );
};

export default WorkImage;
