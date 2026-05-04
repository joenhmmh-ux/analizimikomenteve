import sys
from pathlib import Path

# Add the parent directory to the path so Source can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if __name__ == "__main__":
    from Source.app import app
    import os
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=False, host="0.0.0.0", port=port, use_reloader=False)
