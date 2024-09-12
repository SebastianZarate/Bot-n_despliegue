import paramiko
import tkinter as tk
from tkinter import messagebox

hostname = '127.0.0.1'
port = 22
username = 'sebastian'

def deploy():
    try:
        # Conexión SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print("Conectando al servidor SSH...")
        # Conexión al servidor usando la nueva clave 
        ssh.connect('127.0.0.1', username='sebastian', key_filename='/home/sebastian/.ssh/id_ecdsa')  
        
        print("Conexión establecida, ejecutando el script remoto...")
        
        # Ejecutar el script remoto
        stdin, stdout, stderr = ssh.exec_command('/usr/local/bin/desplegar.sh')
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        ssh.close()

        if error:
            messagebox.showerror("Error", f"Error en el despliegue: {error}")
        else:
            messagebox.showinfo("Éxito", f"Despliegue completado con éxito: {output}")

    except Exception as e:
        messagebox.showerror("Error", f"Error en la conexión: {str(e)}")

# Interfaz gráfica con Tkinter
app = tk.Tk()
app.title("Desplegar nueva versión")
app.geometry("300x150")

# Crear botón
deploy_button = tk.Button(app, text="Desplegar nueva versión", command=deploy)
deploy_button.pack(pady=20)

app.mainloop()
