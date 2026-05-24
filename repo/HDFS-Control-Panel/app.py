from flask import Flask, render_template_string, request
from commands import run_command 
from templates import HTML_TEMPLATE 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = "Waiting for command..."
    cmd_text = "None"
    last_path = "/"

    if request.method == 'POST':
       
        if 'command' in request.form:
            cmd_text = request.form.get('command')
            output = run_command(cmd_text)
            
       
        elif 'action' in request.form:
            action = request.form.get('action')
            if action == 'ls':
                last_path = request.form.get('path_entry', '/')
                cmd_text = f"hdfs dfs -ls {last_path}"
            elif action == 'cat':
                last_path = request.form.get('path_entry', '/')
                cmd_text = f"hdfs dfs -cat {last_path}"
            elif action == 'cp':
                cmd_text = f"hdfs dfs -cp {request.form.get('src_entry')} {request.form.get('dst_entry')}"
            elif action == 'mv':
                cmd_text = f"hdfs dfs -mv {request.form.get('src_entry')} {request.form.get('dst_entry')}"
            elif action == 'rm':
                cmd_text = f"hdfs dfs -rm -r {request.form.get('rm_path')}"
            elif action == 'mkdir':
                cmd_text = f"hdfs dfs -mkdir {request.form.get('rm_path')}"
                
            output = run_command(cmd_text)

    return render_template_string(HTML_TEMPLATE, output=output, cmd_text=cmd_text, last_path=last_path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

