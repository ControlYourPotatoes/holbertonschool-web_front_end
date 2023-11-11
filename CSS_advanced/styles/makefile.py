#!/usr/bin/env python3
file_names = ['11-style.css', '12-style.css', '13-style.css', '14-style.css', '15-style.css', '16-style.css', '17-style.css', '18-style.css', '19-style.css', '20-style.css', '21-style.css', '22-style.css', '23-style.css', '24-style.css', '25-style.css', '26-style.css', '27-style.css', '28-style.css', '29-style.css', '30-style.css', '31-style.css', '32-style.css']

for file_name in file_names:
    with open(file_name, 'w') as file:
        # You can add default content to your CSS files here if needed
        file.write("/* Default CSS content */\n")
