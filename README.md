download

option 1: use pre-built executable
download the latest `.exe` from [Releases](https://github.com/lydsleepy/application-counter-widget/releases)

option 2: run from source
in terminal:
  git clone https://github.com/lydsleepy/application-counter-widget.git
  cd application-counter-widget
  python -m venv venv
  venv\Scripts\activate
  python main.py

option 3: build ur own executable
in terminal:
  pip install pyinstaller
  pyinstaller --onefile --noconsole main.py

find the .exe in dist/ folder
--noconsole and --windowed are the same thing, u can use either


gitignore should have:
  build/
  dist/
  *.spec
