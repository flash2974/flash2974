import json

ICON_MAP = {
    "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
    "Java": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg",
    "C & C++": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg",
    "Go": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg",
    "JavaScript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
    "TypeScript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
    "HTML5": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
    "CSS": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
    "Arduino": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg",
    "MySQL": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg",
    "Docker": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg",
    "Linux": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg",
    "Make & CMake": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cmake/cmake-original.svg",
    "Git": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
    "TensorFlow/Keras": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg",
    "Vue.js (just a lil bit !)": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg",
    "SQLAlchemy": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg",
    "Flask": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg",
    "NumPy": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg",
    "VSCode": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"
}

def generate_readme():
    try:
        with open("portfolio.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(e)
        return
    
    greeting = data[0]
    socials = data[1]
    about = data[2]
    works = data[5]

    tech_html = ['<div align="left">']
    for stack_key in ["toolStack", "techStack", "frameWorkStack"]:
        stack = about.get(stack_key, [])
        for item in stack:
            tech_name = item[1]
            if tech_name in ICON_MAP:
                tech_html.append(f'  <img src="{ICON_MAP[tech_name]}" height="30" alt="{tech_name}" title="{tech_name}" />')
                tech_html.append('  <img width="12" />')
    tech_html.append('</div>')

    md = [
        f'<h2 align="left">Hi 👋! My name is {greeting["name"]} and I\'m a Computer Engineering Student, from Nantes, France 🇫🇷.</h2>',
        '',
        '###',
        '',
        '<div align="center">',
        '  <img src="https://raw.githubusercontent.com/flash2974/flash2974/stats-output/stats.svg" height="150" alt="stats graph"  />',
        '  <img src="https://raw.githubusercontent.com/flash2974/flash2974/languages-output/languages.svg" height="150" alt="languages graph"  />',
        '</div>',
        '',
        '###',
        '',
        '<img align="left" height="150" src="https://avatars.githubusercontent.com/flash2974" alt="Profile Picture" />',
        '',
        '###',
        ''
    ]

    md.extend(tech_html)
    md.extend([
        '',
        '###',
        '',
        '<div align="left">',
        f'  <a href="{socials["github"]}" target="_blank">',
        '    <img src="https://img.shields.io/static/v1?message=GitHub&logo=github&label=&color=181717&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="github logo"  />',
        '  </a>',
        f'  <a href="{socials["linkedin"]}" target="_blank">',
        '    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"  />',
        '  </a>',
        f'  <a href="mailto:{socials['email']}" target="_blank">',
        '    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="gmail logo"  />',
        '  </a>',
        '</div>',
        '',
        '###',
        '',
        '<br clear="both">',
        '',
        '<img src="https://raw.githubusercontent.com/flash2974/flash2974/snake-output/snake.svg" alt="Snake animation" />',
        '',
        '###',
        '',
        '## 🚀 My projects',
        '| Project | Description | Link |',
        '|---------|-------------|------|'
    ])

    for proj in works:
        source_link = ""
        for l in proj.get("links", []):
            if l["type"] in ["git", "gitlab"]:
                source_link = f"[🔗 Source]({l['url']})"
                break
        
        md.append(f"| **{proj['projectName']}** | {proj['description']} | {source_link} |")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))

if __name__ == "__main__":
    generate_readme()