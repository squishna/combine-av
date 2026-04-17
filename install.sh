#!/bin/bash

# Configuration
INSTALL_DIR="$HOME/.combine-av"
BIN_DIR="$HOME/.local/bin"
APP_NAME="combine"

echo "Installing $APP_NAME..."

# Create installation directory
mkdir -p "$INSTALL_DIR/src"

# Copy source files
cp -r src/* "$INSTALL_DIR/src/"
# Also copy __init__.py if it exists (it should be in src/)

# Create bin directory if it doesn't exist
mkdir -p "$BIN_DIR"

# Create the wrapper script
CAT_WRAPPER=$(cat <<EOF
#!/bin/bash
export PYTHONPATH="$INSTALL_DIR:\$PYTHONPATH"
python3 "$INSTALL_DIR/src/main.py" "\$@"
EOF
)

echo "$CAT_WRAPPER" > "$BIN_DIR/$APP_NAME"
chmod +x "$BIN_DIR/$APP_NAME"

echo "Success! $APP_NAME has been installed."
echo ""
echo "Ensure $BIN_DIR is in your PATH. You can add this to your .bashrc or .zshrc:"
echo "export PATH=\"\$PATH:$BIN_DIR\""
echo ""
echo "You can now run the tool using: $APP_NAME"
