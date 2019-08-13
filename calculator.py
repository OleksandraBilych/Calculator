import sys

from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot


class Calculator(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._prev_num = ''
        self._current_num = ''
        self._operator = ''

    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, current_num):
        self._current_num = current_num

    @property
    def prev_num(self):
        return self._prev_num

    @prev_num.setter
    def prev_num(self, prev_num):
        self._prev_num = prev_num

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
            Arithmetic Operator ["÷", "×", "+", "-"]
        """

        self._operator = operator

    def reset_values(self):
        self._prev_num = ''
        self._current_num = ''
        self._operator = ''

    @pyqtSlot('QString')
    def change_operator(self, text):
        """Change operator's value

        Check if the current number if valid
        If yes save current number value to num
        """
        self.operator = text
        if self.current_num:
            self.prev_num = self.current_num
            self.current_num = ""

    @pyqtSlot('QString', result='QString')
    def change_number(self, digit):
        """Change the current number

        For 0-9 digits add digit to current number if the length of digits less and equal 10
        For 'C' remove last digit
        For '.' add point to the end
        """

        if digit == 'C' or digit == "":
            self.current_num = ''
            self.prev_num = ''
        elif len(self._current_num) <= 10:
            if digit == '.':
                self.current_num += '.'
            else:
                self.current_num += digit

        return self.current_num

    @pyqtSlot(result='QString')
    def calculation(self):
        """Perform mathematical operations

        +	Addition: adds two operands	x + y
        -	Subtraction: subtracts two operands	x - y
        *	Multiplication: multiplies two operands	x * y
        /	Division (float): divides the first operand by the second	x / y
        """

        try:
            if self.operator == '+':
                result = self.str_to_float(self.prev_num) +\
                    self.str_to_float(self.current_num)
            elif self.operator == '-':
                result = self.str_to_float(self.prev_num) -\
                    self.str_to_float(self.current_num)
            elif self.operator == '÷':
                result = self.str_to_float(self.prev_num) /\
                    self.str_to_float(self.current_num)
            elif self.operator == '×':
                result = self.str_to_float(self.prev_num) *\
                    self.str_to_float(self.current_num)
            else:
                result = self.str_to_float(self.current_num)
        except ZeroDivisionError as err:
            self.reset_values()
            return 'division by zero!'
        except ValueError as err:
            self.reset_values()
            return 'malformed expression'

        self.prev_num = f"{int(result) if float(result).is_integer() else round(result,9)}"
        self.current_num = ''
        self.operator = ''

        return self.prev_num

    @staticmethod
    def str_to_float(text):
        if text == '':
            return 0.0

        return float(text)
