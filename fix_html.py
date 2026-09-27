import os
import re

NAV_HTML = """<nav class="navbar">
        <div class="container">
            <a href="index.html" class="nav-brand">
                <img src="assets/logo.png" alt="Central Girls Track" onerror="this.style.display='none'">
                <span>CHAMPAIGN <span>CENTRAL</span></span>
            </a>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="join.html">Join</a>
                <a href="updates.html">News</a>
                <a href="support.html">Support Us</a>
                <a href="donate.html" class="nav-donate text-light">Donate Now</a>
            </div>
        </div>
    </nav>"""

FOOTER_HTML = """<!-- Global Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h3>CENTRAL GIRLS TRACK</h3>
                    <p>610 W. University<br>Champaign, IL 61820</p>
                    <p style="margin-top:1rem; color:var(--accent); font-weight:bold;">Official 501(c)(3) Organization</p>
                    <p style="margin-top:0.5rem;"><a href="mailto:Centralgirlstrackboosters@gmail.com"><i class="fa-solid fa-envelope"></i> Centralgirlstrackboosters@gmail.com</a></p>
                </div>
                <div>
                    <h3>SITE MAP</h3>
                    <div class="footer-links">
                        <a href="index.html">Home</a>
                        <a href="about.html">About</a>
                        <a href="join.html">Join</a>
                        <a href="updates.html">News</a>
                        <a href="support.html">Support Us</a>
                    </div>
                </div>
                <div>
                    <h3>ATHLETICS</h3>
                    <div class="footer-links">
                        <a href="https://www.athletic.net/team/19700/track-and-field-outdoor/2026" target="_blank">Performance Stats</a>
                        <a href="https://www.ihsa.org/schools/trends/school/0324" target="_blank">IHSA Profile</a>
                    </div>
                </div>
                <div>
                    <h3>FOLLOW OUR TEAM</h3>
                    <div class="footer-links" style="display:flex; flex-direction:row; gap:1.25rem; font-size:1.5rem; margin-top:0.5rem;">
                        <a href="https://www.facebook.com/runningmaroons/" target="_blank" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="https://www.instagram.com/runningmaroons/" target="_blank" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Champaign Central High School Girls Track. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>"""

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Navbar (Handles any variant of <nav ...> ... </nav>)
    content = re.sub(r'<nav[^>]*>.*?</nav>', NAV_HTML, content, flags=re.DOTALL)
    
    # Replace Navbar place holder if exists
    content = re.sub(r'<!-- NAVBAR_PLACEHOLDER -->\s*<nav[^>]*>.*?</nav>', NAV_HTML, content, flags=re.DOTALL)

    # Replace Footer entirely till the end of the body and html tags
    content = re.sub(r'<footer[^>]*>.*', FOOTER_HTML, content, flags=re.DOTALL)
    
    # Replace Footer placeholder
    content = re.sub(r'<!-- FOOTER_PLACEHOLDER -->\s*<footer[^>]*>.*', FOOTER_HTML, content, flags=re.DOTALL)

    # Clean up any legacy links just in case
    content = content.replace('"sponsors.html"', '"support.html"')
    content = content.replace("'sponsors.html'", "'support.html'")
    
    # Clean up old anchor tag donate button link to use the robust donate page
    content = content.replace('"support.html#donate"', '"donate.html"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'sponsors.html':
        fix_file(filename)
        print(f"Fixed {filename}")
