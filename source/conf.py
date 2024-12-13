version = "v2.1.0"

html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "logo": {
        "text": "Leafmachine2",
    },
    "announcement": "This documentation site is under active development as information is transcribed from the LeafMachine2 README. Some sections may be incomplete.",
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "footer_start": [],
    "footer_end": [],
    "switcher": {
        "json_url": "_static/switcher.json",
        "version_match": version,
    },
    "navbar_start": ["navbar-logo", "version-switcher"],
}
exclude_patterns = ["_build", ".venv", "docs"]
extensions = ["sphinx_design", "sphinx_copybutton"]

copybutton_image_svg = """<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 384 512"><!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M280 64h40c35.3 0 64 28.7 64 64V448c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V128C0 92.7 28.7 64 64 64h40 9.6C121 27.5 153.3 0 192 0s71 27.5 78.4 64H280zM64 112c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16H320c8.8 0 16-7.2 16-16V128c0-8.8-7.2-16-16-16H304v24c0 13.3-10.7 24-24 24H192 104c-13.3 0-24-10.7-24-24V112H64zm128-8a24 24 0 1 0 0-48 24 24 0 1 0 0 48z"/></svg>
"""
