html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Ajay Vishwakarma Resume</title>
<style>
    @page {
        size: letter;
        margin: 0.5in 0.5in;
        background-color: #ffffff;
    }
    *, *::before, *::after {
        box-sizing: border-box;
    }
    body {
        font-family: 'Times New Roman', Times, serif;
        color: #000000;
        margin: 0;
        padding: 0;
        font-size: 10.5pt;
        line-height: 1.2;
    }
    h1 {
        text-align: center;
        color: #000000;
        font-size: 24pt;
        margin: 0 0 2px 0;
        font-weight: normal;
        text-transform: uppercase;
    }
    .subtitle {
        text-align: center;
        font-size: 11pt;
        margin: 0 0 2px 0;
    }
    .contact {
        text-align: center;
        font-size: 10.5pt;
        margin: 0 0 10px 0;
    }
    .contact a {
        color: #000000;
        text-decoration: none;
    }
    hr {
        border: none;
        border-bottom: 1px solid #000000;
        margin: 0 0 10px 0;
    }
    h2 {
        color: #000000;
        font-size: 12pt;
        text-transform: uppercase;
        margin: 10px 0 4px 0;
        border-bottom: 1px solid #000000;
        padding-bottom: 1px;
        font-weight: bold;
    }
    p {
        margin: 0 0 6px 0;
    }
    .skill-row {
        margin-bottom: 2px;
    }
    .skill-label {
        font-weight: bold;
    }
    .section-item {
        margin-bottom: 8px;
        page-break-inside: avoid;
    }
    .flex-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        width: 100%;
        margin-bottom: 1px;
    }
    .title-left {
        font-weight: bold;
        font-size: 11pt;
    }
    .date-right {
        font-weight: normal;
        font-size: 10.5pt;
    }
    .sub-title {
        font-style: italic;
        margin-bottom: 3px;
        display: flex;
        justify-content: space-between;
    }
    ul {
        margin: 2px 0 4px 0;
        padding-left: 15px;
    }
    li {
        margin-bottom: 2px;
    }
</style>
</head>
<body>

    <h1>AJAY VISHWAKARMA</h1>
    <div class="subtitle">Software Developer | Artificial Intelligence</div>
    <div class="contact">
        Lucknow, India | +91-7905398965 | <a href="mailto:ajaykumar160380@gmail.com">ajaykumar160380@gmail.com</a> <br>
        <a href="https://linkedin.com/in/ajay-vishwakarma-71649129a" target="_blank">linkedin.com/in/ajay-vishwakarma-71649129a</a> | 
        <a href="https://github.com/ajay160380" target="_blank">github.com/ajay160380</a> | 
        <a href="https://ajay-vishwakarmaa.netlify.app" target="_blank">ajay-vishwakarmaa.netlify.app</a>
    </div>
    <hr>

    <h2>SUMMARY</h2>
    <p>Motivated Computer Science undergraduate specializing in Artificial Intelligence. Experienced in Python, data science, machine learning, and API development. Passionate about building scalable, intelligent applications with optimized performance. Seeking a Software Developer position to contribute to a high-performing engineering team.</p>

    <h2>SKILLS</h2>
    <div class="skill-row"><span class="skill-label">Programming Languages:</span> Python, SQL, HTML5</div>
    <div class="skill-row"><span class="skill-label">Frameworks &amp; Libraries:</span> Django, scikit-learn, NumPy, Pandas, Matplotlib, OpenCV</div>
    <div class="skill-row"><span class="skill-label">Domain Knowledge:</span> Artificial Intelligence, Data Analysis, Predictive Modeling, Machine Learning</div>
    <div class="skill-row"><span class="skill-label">Tools &amp; Platforms:</span> Git, GitHub, Docker, VS Code, Google Cloud Platform, PostgreSQL, Firebase</div>

    <h2>EDUCATION</h2>
    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">Babu Banarasi Das University, Lucknow, India</span>
            <span class="date-right">Expected May 2027</span>
        </div>
        <div class="sub-title">Bachelor of Technology in Computer Science and Engineering</div>
        <ul>
            <li>Completed coursework in Data Structures, Artificial Intelligence, Machine Learning, Database Management Systems, and Python Programming with a 90% academic score.</li>
        </ul>
    </div>

    <h2>EXPERIENCE</h2>
    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">Grastech</span>
            <span class="date-right">2026</span>
        </div>
        <div class="sub-title">Data Science and Artificial Intelligence Trainee</div>
        <ul>
            <li>Completed 1 month of professional training focused on advanced data science methodologies and exploratory data analysis.</li>
            <li>Deployed 2+ machine learning projects and predictive models using modern deployment pipelines to analyze datasets.</li>
        </ul>
    </div>

    <h2>PROJECTS</h2>
    
    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">EduTech AI: Interactive Course &amp; Learning Workspace</span>
            <span class="date-right">2026</span>
        </div>
        <div class="sub-title">Python, Django, Groq API (Llama-3.1), Firebase, Razorpay</div>
        <ul>
            <li>Built a high-fidelity EdTech SaaS platform utilizing a dynamic YouTube parser to instantly convert playlists (500+ videos) into interactive virtual classrooms.</li>
            <li>Integrated Groq API (Llama-3.1-8B) to generate textbook-level summaries and architectural flowcharts, with a conversational Hinglish tutor for localized learning.</li>
            <li>Implemented a Pomodoro focus room with a glassmorphism overlay and a dynamic certification engine that generates PDF graduation certificates.</li>
        </ul>
    </div>

    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">ExpenseTracker: AI Smart Expense Coach</span>
            <span class="date-right">2026</span>
        </div>
        <div class="sub-title">Python, Django, Node.js, Groq API, PostgreSQL, Docker</div>
        <ul>
            <li>Engineered an AI-powered personal finance application featuring seamless WhatsApp integration via Node.js for real-time natural language expense logging.</li>
            <li>Integrated Groq LLMs (Llama 3.1) to parse multi-lingual transaction inputs and developed a gamified analytics dashboard utilizing Django and PostgreSQL.</li>
        </ul>
    </div>

    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">House Price and Brain Tumor Prediction</span>
            <span class="date-right">2026</span>
        </div>
        <div class="sub-title">Python, scikit-learn, Pandas, OpenCV</div>
        <ul>
            <li>Engineered a house price prediction regression model processing over 1000 housing records across 12 independent variables.</li>
            <li>Programmed an automated brain tumor detection system leveraging classification algorithms to process MRI image features with over 92% model test accuracy.</li>
        </ul>
    </div>

    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">Healthcare Management Dashboard</span>
            <span class="date-right">2026</span>
        </div>
        <div class="sub-title">Python, Django, Map Integration</div>
        <ul>
            <li>Designed a centralized healthcare platform managing 3 core user modules and relational database schemas.</li>
            <li>Integrated an interactive artificial intelligence assistant and map routing component to support quick facility location and handle 10 distinct appointment workflows.</li>
        </ul>
    </div>

    <div class="section-item">
        <div class="flex-header clearfix">
            <span class="title-left">Digital Twin: Habit Prediction Application</span>
            <span class="date-right">2026</span>
        </div>
        <div class="sub-title">Python, Django, HTML5</div>
        <ul>
            <li>Developed a full stack behavioral tracking web application utilizing backend models to process 5 daily habit parameters and generate predictive insights.</li>
        </ul>
    </div>

    <h2>CERTIFICATIONS</h2>
    <ul>
        <li><strong>Microsoft Azure AI Essentials Professional Certificate</strong> &ndash; Microsoft &amp; LinkedIn Learning</li>
        <li><strong>GenAI Powered Data Analytics Job Simulation</strong> &ndash; Forage</li>
        <li><strong>Data Analytics Job Simulation</strong> &ndash; Deloitte (Forage)</li>
        <li><strong>Technology Software Development Job Simulation</strong> &ndash; Forage</li>
        <li><strong>AI and Cybersecurity Awareness</strong> &ndash; TCS iON</li>
    </ul>

    <h2>ACHIEVEMENTS</h2>
    <ul>
        <li><strong>Project Showcase (2026):</strong> Presented the IoT-based Smart Women Safety Device (featuring 3 hardware sensors) at the BBD University Technology Exposition.</li>
    </ul>

</body>
</html>
"""

from weasyprint import HTML
# Generate the PDF directly in the public folder so it's accessible for download
HTML(string=html_content).write_pdf("public/Ajay_Vishwakarma_Resume.pdf")
print("PDF generated successfully at public/Ajay_Vishwakarma_Resume.pdf")
