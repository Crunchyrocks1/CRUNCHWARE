def handleRemoveReadonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  
        func(path)
    else:
        raise


def update():
    print(Message1)

    
    current_directory = os.getcwd()

    
    target_directory = os.path.join(current_directory, "CRUNCHWARE")

    
    if os.path.isdir(os.path.join(current_directory, ".git")):
        print(Fore.BLUE + "[+]" + Fore.YELLOW + " Repository already exists, updating...")
        try:
            result = subprocess.run(
                ['git', '-C', current_directory, 'pull'],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print(result.stdout)  
        except subprocess.CalledProcessError as e:
            log(Fore.RED + f"Error updating the repository: {e.stderr}")
            kernel32.Sleep(5000)
            return
    else:
        
        if os.path.exists(target_directory):
            print(Fore.BLUE + "[+]" + Fore.RED + " Removing existing 'CRUNCHWARE' directory...")
            shutil.rmtree(target_directory, onerror=handleRemoveReadonly)  


        print(Fore.BLUE + "[+]" + Fore.YELLOW + " Cloning repository into subdirectory 'CRUNCHWARE'...")
        try:
            subprocess.run(
                ['git', 'clone', url, target_directory],  
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        except subprocess.CalledProcessError as e:
            log(Fore.RED + f"Error cloning the repository: {e.stderr}")
            kernel32.Sleep(5000)
            return
