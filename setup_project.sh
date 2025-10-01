#!/bin/bash

# Exit if any command fails
set -e

# --- Create directory structure ---
echo
mkdir -p src data output

# --- Generate initial files ---
# .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.env
output/
EOF

# requirements.txt
cat > requirements.txt << 'EOF'
pandas
numpy
EOF

# --- Create sample data file ---
cat > data/students.csv << 'EOF'
name,age,grade,subject
1,Alice,20,Computer Science
2,Bob,21,Mathematics
3,Charlie,22,Physics
4,Diana,23,Economics
5,Ethan,24,Biology
6,Fiona,21,Chemistry
7,George,22,Engineering
8,Hannah,20,Philosophy
EOF

# --- Set up Python template files ---
cat > src/data_analysis.py << 'EOF'
\"\"\"
Main script for the project.
TODO: Implement main logic.
\"\"\"

def main():
    # TODO: Write main execution code
    pass

if __name__ == "__main__":
    main()
EOF

cat > src/data_analysis_functions.py << 'EOF'
\"\"\"
Utility functions for the project.
TODO: Add helper functions here.
\"\"\"

def sample_function():
    # TODO: Implement this function
    pass
EOF

echo "Project setup complete!"
