class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input(f"Enter Pin A input for gate {self.getLabel()}--> "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input(f"Enter Pin B input for gate {self.getLabel()}--> "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a == 1 and b == 1 else 0


class XorGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a != b else 0


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


# New Input class to represent external inputs
class Input:

    def __init__(self, value):
        self.value = value

    def getOutput(self):
        return self.value


# Half-Adder Implementation
class HalfAdder:

    def __init__(self, label):
        self.label = label
        self.xor_gate = XorGate(f"{label}-XOR")
        self.and_gate = AndGate(f"{label}-AND")

    def performAdd(self):
        # Get the outputs of XOR and AND gates
        sum_result = self.xor_gate.getOutput()
        carry_result = self.and_gate.getOutput()
        return sum_result, carry_result


def main():
    # Create a Half Adder instance
    ha = HalfAdder("HA")

    # Get inputs from user
    a_input = int(input("Enter input A (0 or 1): "))
    b_input = int(input("Enter input B (0 or 1): "))

    # Create Input objects
    inputA = Input(a_input)
    inputB = Input(b_input)

    # Connect inputs for the half-adder using Input objects
    Connector(inputA, ha.xor_gate)
    Connector(inputB, ha.xor_gate)
    Connector(inputA, ha.and_gate)
    Connector(inputB, ha.and_gate)

    # Perform the addition
    sum_result, carry_result = ha.performAdd()

    print(f"Sum: {sum_result}, Carry: {carry_result}")


if __name__ == "__main__":
    main()
