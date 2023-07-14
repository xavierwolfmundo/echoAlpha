# Generate the content of the Procfile
procfile_content = "web: gunicorn project.wsgi --log-file -"

# Write the content to the Procfile
with open('Procfile', 'w') as file:
    file.write(procfile_content)
