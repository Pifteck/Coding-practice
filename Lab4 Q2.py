class Robot1:
    def __init__(self):
        self.batteryCharge = 5.0

    def move(self, distance):
        self.steps = 0
        self.list_steps = []
        while distance > 0:
            if self.batteryCharge < 0.5:
                print(f"Dead battery detected, cannot move! {distance} remaining.")
                charge_condition = input("Do you want to recharge? y or n: ").strip().lower()
                
                if charge_condition == "y":
                    charge = float(input("How much do you want to charge: "))
                    self.batteryReCharge(charge)
                    continue
                else:
                    print("Did not finish moving.")
                    break

            self.steps += 1
            self.list_steps.append(self.steps)
            self.batteryCharge -= 0.5
            print(self.list_steps)
            print(f"current battery: {self.batteryCharge}")
            distance -= 1

            if distance == 0:
                print("Finished moving.")

    def batteryReCharge(self,charge):
        self.batteryCharge += charge
        print(f"Battery charge is: {self.batteryCharge}")

r = Robot1()
r.move(11)