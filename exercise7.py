class Simulation:

    def __init__(self, num1, name):
        self.num1 = num1
        self.name = name
    
    def writejson(self):
        output_json = "output.json"
        users = [self.num1, self.name]
        try:
            with open(output_json, mode="w") as file:
                for user in users:
                    inputs = user
                    file.write(user)
        except FileExistsError:
            print("This file already exists")
            
def main ():
    simulation = Simulation("Flavio", "Bjorn")
    simulation.writejson()

if __name__=="__main__":
    main()