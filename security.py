class Security:
    def __init__(self) -> None:
        self.ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    def verify_extension(self, file):
        file = file.split(".")
        
        if file[1] in self.ALLOWED_EXTENSIONS:
            return True
        return False
        

