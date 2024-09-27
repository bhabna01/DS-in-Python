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


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a == 1 or b == 1 else 0


class NotGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input(f"Enter Pin input for gate {self.getLabel()}--> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

    def performGateLogic(self):
        pin = self.getPin()
        return 0 if pin == 1 else 1


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


class Bit:
    def __init__(self, value):
        self.value = value

    def getOutput(self):
        return self.value


class FullAdder:
    def __init__(self, label):
        self.label = label
        self.xor1 = XorGate(f"{label}-XOR1")
        self.xor2 = XorGate(f"{label}-XOR2")
        self.and1 = AndGate(f"{label}-AND1")
        self.and2 = AndGate(f"{label}-AND2")
        self.or_gate = OrGate(f"{label}-OR")

    def performAdd(self):
        sum_result = self.xor2.getOutput()
        carry_result = self.or_gate.getOutput()
        return sum_result, carry_result

    def setInputs(self, a, b, cin):
        # Set inputs for XOR1, AND1, and AND2 gates
        Connector(a, self.xor1)
        Connector(b, self.xor1)
        Connector(a, self.and1)
        Connector(b, self.and1)
        Connector(cin, self.and2)

        # Set inputs for XOR2 and OR gates
        Connector(self.xor1, self.xor2)
        Connector(cin, self.xor2)
        Connector(self.and1, self.or_gate)
        Connector(self.and2, self.or_gate)


class FullAdder8Bit:
    def __init__(self):
        self.full_adders = [FullAdder(f"FA{i}") for i in range(8)]

    def add(self, a, b):
        cin = Bit(0)  # Initial carry-in is 0
        sum_bits = []
        carry_out = cin

        for i in range(8):
            # Set inputs for the current full-adder
            self.full_adders[i].setInputs(a[i], b[i], carry_out)
            # Get sum and carry-out for the current full-adder
            sum_bit, carry_out = self.full_adders[i].performAdd()
            sum_bits.append(Bit(sum_bit))  # Wrap the result in a Bit object

        return sum_bits, carry_out


def main():
    # Create 8-bit inputs as lists of Bit objects
    A = [Bit(int(bit)) for bit in input("Enter 8-bit binary number A: ")]
    B = [Bit(int(bit)) for bit in input("Enter 8-bit binary number B: ")]

    # Check if inputs are 8-bit
    if len(A) != 8 or len(B) != 8:
        print("Please enter 8-bit binary numbers!")
        return

    # Create 8-bit full-adder instance
    fa_8bit = FullAdder8Bit()
    sum_bits, carry_out = fa_8bit.add(A, B)

    # Display the result
    print("Sum:", "".join(str(bit.getOutput()) for bit in sum_bits))
    print("Carry Out:", carry_out.getOutput())


if __name__ == "__main__":
    main()
