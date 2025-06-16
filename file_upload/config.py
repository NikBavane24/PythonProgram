import os
from pathlib import Path

url="https://ps.uci.edu/~franklin/doc/file_upload.html"
base_dir=Path(__file__).resolve().parent
file_path=os.path.join(base_dir,"data","Test.pdf")