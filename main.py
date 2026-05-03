"""
💀 MISS ALIYA - GITHUB REPO / ACCOUNT HUNTER 💀
Kisi bhi URL (Render, Vercel, Streamlit) ka GitHub repo ya account dhundho
Deploy on: Render.com
"""

from flask import Flask, request, render_template_string, jsonify
import requests
import re
from urllib.parse import urlparse

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💀 MISS ALIYA - GITHUB HUNTER 💀</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 650px;
            margin: 0 auto;
        }
        
        .card {
            background: rgba(20, 20, 40, 0.95);
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 20px;
            border: 2px solid #00ff41;
            box-shadow: 0 0 30px rgba(0, 255, 65, 0.2);
        }
        
        h1 {
            color: #00ff41;
            text-align: center;
            font-size: 26px;
            margin-bottom: 10px;
        }
        
        h1 span {
            color: #ff9933;
        }
        
        .subtitle {
            text-align: center;
            color: #888;
            font-size: 11px;
            margin-bottom: 30px;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #00d4ff;
            font-size: 12px;
            margin-bottom: 8px;
        }
        
        input {
            width: 100%;
            padding: 14px;
            background: #0a0a0a;
            border: 1px solid #333;
            border-radius: 12px;
            color: #00ff41;
            font-family: 'Courier New', monospace;
            font-size: 14px;
        }
        
        input:focus {
            outline: none;
            border-color: #00ff41;
            box-shadow: 0 0 10px rgba(0, 255, 65, 0.2);
        }
        
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #00ff41, #00cc33);
            color: #000;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s;
        }
        
        button:hover {
            transform: scale(1.02);
        }
        
        .result-card {
            margin-top: 20px;
            padding: 20px;
            background: #0a0a0a;
            border-radius: 12px;
            border-left: 4px solid #00ff41;
        }
        
        .result-title {
            color: #00ff41;
            font-size: 14px;
            margin-bottom: 10px;
        }
        
        .result-link {
            color: #00d4ff;
            font-size: 16px;
            word-break: break-all;
        }
        
        .result-link a {
            color: #00d4ff;
            text-decoration: none;
        }
        
        .result-link a:hover {
            text-decoration: underline;
        }
        
        .error {
            color: #ff0055;
        }
        
        .loading {
            color: #ffdd00;
            text-align: center;
            padding: 20px;
        }
        
        .footer {
            text-align: center;
            color: #555;
            font-size: 9px;
            margin-top: 20px;
        }
        
        .badge {
            display: inline-block;
            background: rgba(0, 255, 65, 0.1);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 10px;
            color: #00ff41;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>💀 MISS ALIYA <span>GITHUB HUNTER</span> 💀</h1>
            <div class="subtitle">[ KISI BHI URL KA GITHUB REPO / ACCOUNT DHUNDHO ]</div>
            
            <div class="input-group">
                <label>🔗 ENTER ANY URL (Render, Vercel, Streamlit, etc.)</label>
                <input type="text" id="targetUrl" placeholder="https://anything.onrender.com" value="https://">
            </div>
            
            <button onclick="huntGithub()">🔍 HUNT GITHUB</button>
            
            <div id="result"></div>
        </div>
        
        <div class="footer">
            💀 MISS ALIYA ULTRA • GITHUB REPO HUNTER • 2026 💀
        </div>
    </div>
    
    <script>
        async function huntGithub() {
            const url = document.getElementById('targetUrl').value.trim();
            if (!url) {
                alert('Please enter a URL');
                return;
            }
            
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<div class="loading">⏳ Searching GitHub repo/account...</div>';
            
            try {
                const response = await fetch('/hunt', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ url: url })
                });
                
                const data = await response.json();
                
                if (data.found) {
                    let typeText = data.type === 'repo' ? '📁 GITHUB REPO FOUND' : '👤 GITHUB ACCOUNT FOUND';
                    resultDiv.innerHTML = `
                        <div class="result-card">
                            <div class="result-title">✅ ${typeText}</div>
                            <div class="result-link"><a href="${data.github_url}" target="_blank">${data.github_url}</a></div>
                            <div style="margin-top: 10px; font-size: 11px; color: #666;">🔍 Searched: ${data.method}</div>
                        </div>
                    `;
                } else {
                    resultDiv.innerHTML = `
                        <div class="result-card">
                            <div class="result-title error">❌ NO GITHUB INFO FOUND</div>
                            <div style="color:#888; font-size:12px;">Possible reasons:</div>
                            <div style="color:#888; font-size:11px; margin-top:5px;">• Private repository</div>
                            <div style="color:#888; font-size:11px;">• Deployed without GitHub (Docker/CLI)</div>
                            <div style="color:#888; font-size:11px;">• No public GitHub link on site</div>
                        </div>
                    `;
                }
            } catch (error) {
                resultDiv.innerHTML = '<div class="result-card error">❌ Error occurred. Try again.</div>';
            }
        }
    </script>
</body>
</html>
"""

class GitHubHunter:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
    
    def extract_site_name(self, url):
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            # Remove platform extensions
            extensions = [".onrender.com", ".vercel.app", ".streamlit.app", 
                         ".netlify.app", ".herokuapp.com", ".github.io"]
            for ext in extensions:
                if ext in domain:
                    domain = domain.replace(ext, "")
            return domain.split(".")[0]
        except:
            return None
    
    def scan_html_for_github(self, html):
        # Repo pattern
        repo_pattern = r'github\.com/([a-zA-Z0-9\-]+/[a-zA-Z0-9\-\._]+)'
        # Profile pattern
        profile_pattern = r'github\.com/([a-zA-Z0-9\-]+)(?:[/"\'\s]|$)'
        
        # First try repo
        matches = re.findall(repo_pattern, html, re.I)
        if matches:
            return f"https://github.com/{matches[0]}", "repo"
        
        # Then try profile
        matches = re.findall(profile_pattern, html, re.I)
        ignore = {"about", "contact", "login", "signup", "explore", "features", "security", "site", "pages"}
        for match in matches:
            if match.lower() not in ignore and len(match) > 2:
                return f"https://github.com/{match}", "profile"
        
        return None, None
    
    def search_github_api(self, site_name):
        # Search user
        try:
            user_url = f"https://api.github.com/users/{site_name}"
            resp = self.session.get(user_url)
            if resp.status_code == 200:
                return f"https://github.com/{site_name}", "profile", "GitHub API (user)"
        except:
            pass
        
        # Search repo
        try:
            search_url = f"https://api.github.com/search/repositories?q={site_name}&per_page=5"
            resp = self.session.get(search_url)
            if resp.status_code == 200:
                items = resp.json().get("items", [])
                for repo in items:
                    if site_name.lower() in repo["name"].lower():
                        return repo["html_url"], "repo", "GitHub API (repo)"
        except:
            pass
        
        return None, None, None
    
    def hunt(self, url):
        print(f"\n🎯 Hunting: {url}")
        
        site_name = self.extract_site_name(url)
        print(f"🔍 Site name: {site_name}")
        
        # Method 1: Scan web page
        try:
            resp = self.session.get(url, timeout=10)
            if resp.status_code == 200:
                github_url, gtype = self.scan_html_for_github(resp.text)
                if github_url:
                    return github_url, gtype, "web page scan"
        except:
            pass
        
        # Method 2: GitHub API search
        if site_name:
            github_url, gtype, method = self.search_github_api(site_name)
            if github_url:
                return github_url, gtype, method
        
        return None, None, None

hunter = GitHubHunter()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/hunt', methods=['POST'])
def hunt():
    data = request.get_json()
    url = data.get('url', '')
    
    if not url:
        return jsonify({'found': False, 'error': 'No URL provided'})
    
    github_url, gtype, method = hunter.hunt(url)
    
    if github_url:
        return jsonify({
            'found': True,
            'github_url': github_url,
            'type': gtype,
            'method': method
        })
    else:
        return jsonify({'found': False})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
