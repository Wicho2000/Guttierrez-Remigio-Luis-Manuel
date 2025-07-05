from flask import render_template, request, flash, redirect, url_for
from app import app
import subprocess
import os
import yaml

@app.route('/')
def index():
    # Listar playbooks disponibles
    playbooks = []
    playbook_dir = '/ansible/playbooks'
    if os.path.exists(playbook_dir):
        playbooks = [f for f in os.listdir(playbook_dir) if f.endswith('.yml')]
    
    return render_template('index.html', playbooks=playbooks)

@app.route('/run-playbook', methods=['POST'])
def run_playbook():
    playbook = request.form.get('playbook')
    extra_vars = request.form.get('extra_vars', '{}')
    
    try:
        # Validar extra_vars como YAML
        vars_dict = yaml.safe_load(extra_vars) if extra_vars else {}
        
        # Construir comando Ansible
        cmd = [
            'ansible-playbook',
            f'/ansible/playbooks/{playbook}',
            '-i', '/ansible/inventory/hosts'
        ]
        
        if vars_dict:
            cmd.extend(['--extra-vars', extra_vars])
        
        # Ejecutar playbook
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        output = result.stdout
        error = result.stderr
        
        return render_template('results.html', 
                            output=output, 
                            error=error,
                            playbook=playbook)
    
    except yaml.YAMLError as e:
        return render_template('results.html', 
                            error=f"Error en las variables YAML: {str(e)}",
                            playbook=playbook)
    except Exception as e:
        return render_template('results.html', 
                            error=f"Error inesperado: {str(e)}",
                            playbook=playbook)