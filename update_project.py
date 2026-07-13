import os
import shutil

# --- CONFIGURAÇÃO AUTOMÁTICA ---
# O script detecta a pasta onde ele está localizado
project_path = os.path.dirname(os.path.abspath(__file__))
project_name = os.path.basename(project_path)
output_file = os.path.join(project_path, 'project.txt')

# Lista de arquivos principais na raiz para incluir o conteúdo completo
files_to_include = [
    'style.css', 'functions.php', 'header.php', 'footer.php', 'index.php', 
    'front-page.php', 'single.php', 'archive.php', 'page-blog.php', 
    'page-sobre.php', 'page-contato.php', 'page-privacidade.php', 
    'page-termos.php', 'page-especialidades.php'
]

# Subdiretórios para vasculhar e incluir conteúdo dos arquivos
subdirs_to_include = ['inc', 'template-parts', 'assets/css', 'assets/js']

def get_tree(startpath):
    tree = []
    
    def build_tree(path, prefix=""):
        # Ignorar arquivos de sistema e o próprio script/saída
        ignore = ['project.txt', 'update_project.py', 'screenshot.png', '.git', '.vscode', '__pycache__']
        items = [i for i in os.listdir(path) if i not in ignore and not i.endswith('.tmp')]
        
        # Ordenar: Pastas primeiro, depois arquivos (alfabético)
        items.sort(key=lambda x: (not os.path.isdir(os.path.join(path, x)), x.lower()))
        
        count = len(items)
        for i, item in enumerate(items):
            is_last = (i == count - 1)
            connector = "└── " if is_last else "├── "
            
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                tree.append(f"{prefix}{connector}📁 {item}/")
                new_prefix = prefix + ("    " if is_last else "│   ")
                build_tree(full_path, new_prefix)
            else:
                ext = os.path.splitext(item)[1].lower()
                icon = "📄"
                if ext == '.php': icon = "🐘"
                elif ext == '.css': icon = "🎨"
                elif ext == '.js': icon = "📜"
                elif ext in ['.png', '.jpg', '.jpeg', '.webp', '.ico']: icon = "🖼️"
                elif ext == '.txt': icon = "📝"
                elif ext == '.json': icon = "⚙️"
                elif ext == '.md': icon = "📘"
                
                tree.append(f"{prefix}{connector}{icon} {item}")

    tree.append(f"📁 {project_name}/")
    build_tree(startpath)
    return "\n".join(tree) + "\n"

def update_project():
    tree_structure = get_tree(project_path)
    
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(tree_structure + "\n")
        
        # 1. Incluir arquivos da raiz
        for f_name in files_to_include:
            f_path = os.path.join(project_path, f_name)
            if os.path.exists(f_path):
                f_out.write("/* " + "="*60 + " */\n")
                f_out.write(f"// Arquivo: {project_name}/{f_name}\n\n")
                try:
                    with open(f_path, 'r', encoding='utf-8', errors='ignore') as f_in:
                        f_out.write(f_in.read() + "\n\n")
                except Exception as e:
                    f_out.write(f"Erro ao ler arquivo: {e}\n\n")

        # 2. Incluir arquivos dos subdiretórios configurados
        for subdir in subdirs_to_include:
            dir_path = os.path.join(project_path, subdir)
            if os.path.exists(dir_path):
                for root, _, files in os.walk(dir_path):
                    for f_name in files:
                        if f_name.endswith(('.php', '.css', '.js', '.txt')) and f_name != 'project.txt' and not f_name.endswith(('.min.css', '.min.js')):
                            relative_path = os.path.relpath(os.path.join(root, f_name), project_path)
                            f_out.write("/* " + "="*60 + " */\n")
                            f_out.write(f"// Arquivo: {project_name}/{relative_path}\n\n")
                            try:
                                with open(os.path.join(root, f_name), 'r', encoding='utf-8', errors='ignore') as f_in:
                                    f_out.write(f_in.read() + "\n\n")
                            except Exception as e:
                                f_out.write(f"Erro ao ler arquivo: {e}\n\n")

    print(f"Projeto atualizado com sucesso em: {output_file}")
    
    # 3. Compactar a pasta inteira em um arquivo ZIP
    import tempfile
    
    full_zip_path = os.path.join(project_path, f"{project_name}.zip")
    
    # Passo A: Prevenção de Inception (Deletar o zip antigo se existir)
    if os.path.exists(full_zip_path):
        os.remove(full_zip_path)
        print(f"Versão anterior {project_name}.zip deletada.")
        
    print(f"Iniciando compactação segura para {project_name}.zip...")
    
    # Passo B: Criar o zip em uma pasta temporária isolada do Windows
    # Isso impede absolutamente que o zip "tente engolir a si mesmo" enquanto é criado
    temp_dir = tempfile.gettempdir()
    temp_zip_base = os.path.join(temp_dir, project_name)
    
    shutil.make_archive(temp_zip_base, 'zip', project_path)
    
    # Passo C: Mover o zip finalizado de volta para a pasta do projeto
    shutil.move(temp_zip_base + '.zip', full_zip_path)
    
    print(f"Projeto compactado com sucesso em: {full_zip_path}")

if __name__ == "__main__":
    update_project()
