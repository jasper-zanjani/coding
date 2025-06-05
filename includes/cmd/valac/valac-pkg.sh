# Compile GTK4 project
valac --pkg gtk4 $SOURCE_FILE

# Compile Adwaita project
valac --pkg gtk4 --pkg libadwaita-1 
