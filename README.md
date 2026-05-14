<h1>Sparee</h1>

<div class="badges">
    <img src="https://img.shields.io/badge/React-18.2.0-blue?style=flat-square" alt="React Version">
    <img src="https://img.shields.io/badge/Python-3.10-green?style=flat-square" alt="Python Version">
</div>

<p>A <strong>full-stack web application</strong> for short-term staffing. You can manage job posts, applications, payments, and real-time messaging. Built with <strong>React, Redux Toolkit Query, FastAPI, PostgreSQL, Redis and WebSockets</strong>.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#folder-structure">Folder Structure</a></li>
    <li><a href="#api--chat-flow">API & Chat Flow</a></li>
    <li><a href="#future-enhancements">Future Enhancements</a></li>
</ul>

<h2 id="demo">Demo</h2>
<p>⚠️ To be uploaded</p>
  
<h2 id="features">Features</h2>
<ul>
    <li>Job Board Management: Create, update, delete, and view applications</li>
    <li>Job Application Management: Create, delete, and status updating</li>
    <li>Real-Time Chat: WebSocket-based messaging per job or user to communicate job information</li>
    <li>Search & Filter: Easily filter jobs</li>
</ul>

<h2 id="tech-stack">Tech Stack</h2>
<ul>
    <li>Frontend: React, Redux Toolkit Query, TailwindCSS</li>
    <li>Backend: Python, FastAPI, SQLAlchemy</li>
    <li>Database: PostgreSQL</li>
    <li>Others: Docker, Redis</li>
</ul>

<h2 id="screenshots">Screenshots</h2>
  <table>
    <tr>
      <th>Dashboard</th>
      <th>Chat</th>
      <th>Documents</th>
    </tr>
    <tr>
      <td><p>⚠️ To be uploaded</p></td>
      <td><p>⚠️ To be uploaded</p></td>
      <td><p>⚠️ To be uploaded</p></td>
    </tr>
  </table>

<h2 id="getting-started">Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Node.js &ge; 18</li>
    <li>Python &ge; 3.10</li>
    <li>PostgreSQL &ge; 14</li>
</ul>

<h3>Clone the repository</h3>
<pre>git clone git@github.com:reitoserizawa/sparee.git
cd sparee</pre>

<h3>Frontend Setup (Dev)</h3>
<pre>cd frontend
npm install
npm run dev</pre>

<h3>Backend Setup (Dev)</h3>
<pre>cd backend
cp .env.example .env          # fill in your values
docker compose up --build -d
docker compose exec web alembic --config migrations/alembic.ini upgrade head</pre>

<h2 id="folder-structure">Folder Structure</h2>
<pre>
├── backend
│   ├── app                 # App entry
|   |   ├── models          # SQLAlchemy models
|   │   ├── api             # API endpoints
|   │   ├── models          # SQLAlchemy models
|   |   └── ...
│   └── ...
├── frontend
│   ├── src
│   │   ├── components      # Reusable UI components
│   │   |   ├── pages       # Main pages
│   │   |   └── store       # Redux Toolkit slices / RTK Query setup
│   │   └── utils            # Helpers and API clients
└── README.html
</pre>

<h2 id="api--chat-flow">API & Chat Flow</h2>
<p>⚠️ To be uploaded</p>

<h2 id="future-enhancements">Future Enhancements</h2>
<ul>
    <li>Push notifications for new messages or job status updates</li>
    <li>Collaboration for multiple recruiters or teams</li>
    <li>Advanced search & filtering (full-text search)</li>
</ul>
