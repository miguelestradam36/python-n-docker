class SetUpExecuter():

    os = __import__('os')
    sys = __import__('sys')

    filepath = "..\\..\\config\\defaults.yaml"
    venv_prefix = "..\\venv\\Scripts\\python -m"

    def __init__(self)->None:
        try:
            build_type = self.sys.argv[1]
            if build_type == 'docker':
                self.venv_prefix = 'python -m'
        except:
            print("Default venv configuration...")

        self.read_defaults()
        self.global_installs()
        self.install_test_modules()
        self.install_services()
        self.install_api_modules()

    def global_installs(self)->None:
        print("Checking in to global installations...")

        for module in self.yaml_config["python"]["global"]["modules"]["standard"]:
            try:
                print("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                print("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))
        
        print("\n")

    def install_services(self)->None:
        print("Checking in to api-connection and app installations...")

        for module in self.yaml_config["python"]["global"]["modules"]["standard"]:
            try:
                print("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                print("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))
        
        print("\n")

    def install_api_modules(self)->None:
        print("Checking in to services installation...")

        for module in self.yaml_config["python"]["global"]["modules"]["api-connection"]:
            try:
                print("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                print("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))
        
        print("\n")

    def install_test_modules(self)->None:
        print("Checking in to services installation...")

        import sys

        module_ = 'pytest-virtualenv'

        if module_ in sys.modules:
            print("Checking {} module into venv".format(module_))
        else:
            print("Installing {} module into venv".format(module_))
            self.os.system("{} pip install {}".format(self.venv_prefix, module_))    

        for module in self.yaml_config["python"]["global"]["modules"]["test"]:
            try:
                print("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                print("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))
        
        print("\n")

    def read_defaults(self)->None:

        fullpath = self.os.path.join(self.os.path.dirname(__file__), self.filepath)

        try:
            print("Checking {} module into venv".format("yaml"))
            assert __import__("yaml")
        except ImportError as error:
            print("Installing {} module into venv".format("PyYaml"))
            self.os.system("{} pip install {}".format(self.venv_prefix,"PyYaml"))
        finally:
            yaml = __import__("yaml")
        
        print("Reading configuration variables on YAML...")
        with open(fullpath, 'r') as file:
            self.yaml_config = yaml.safe_load(file)
        
        print("\n")