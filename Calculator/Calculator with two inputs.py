#!/usr/bin/python3
#Author: Alvaro Islas

# This is just a calculator that allows you to do two inputs. Meaning do one set of mathamatical operations and then do another afterwards.
# Just to see how short we can write the same code and still get the same answer. 

# Storing the results and then having it title Method 1
s = "Result:\n"
s += str("Method 1\n")

# Input Box for user interface for both mathamatical operations.
import InputBox
InputBox.ShowDialog("Enter the first number: ")
n1 = InputBox.GetInput()
InputBox.ShowDialog("Enter the operator: ")
ops = InputBox.GetInput()
InputBox.ShowDialog("Enter the second number: ")
n2 = InputBox.GetInput()

# The mathamatical operations using if statements.
if (ops == '+') : s += str(float(n1) + float(n2))
if (ops == '-') : s += str(float(n1) - float(n2))
if (ops == '*') : s += str(float(n1) * float(n2))
if (ops == '/') : s += str(float(n1) / float(n2))
if (ops == '%') : s += str(float(n1) % float(n2))
if (ops == '**') : s += str(float(n1) ** float(n2))

# This will store method 2. 
s += str("\n\nMethod 2\n")

# Input box again
InputBox.ShowDialog("Enter the first number: ")
n1 = InputBox.GetInput()
InputBox.ShowDialog("Enter the operator: ")
ops = InputBox.GetInput()
InputBox.ShowDialog("Enter the second number: ")
n2 = InputBox.GetInput()

# Now we are using definitions to identify what we will be doing. 
def Add() : return str(float(n1) + float(n2))
def Sub() : return str(float(n1) - float(n2))
def Mul() : return str(float(n1) * float(n2))
def Div() : return str(float(n1) / float(n2))
def Mod() : return str(float(n1) % float(n2))
def Exp() : return str(float(n1) ** float(n2))

# Our switch operation will allow us to go through the operation we want to achieve. 
switch = {
"+": Add(),
"-": Sub(),
"*": Mul(),
"/": Div(),
"%": Mod(),
"**": Exp()
}

# This is saying let's try to reffer to the switch to use the inputs given to us however, if something goes wrong display the following. 
try:
    s += str(switch[ops]);
except KeyError as ex:
    s += str("No matching case")

###### Message Box Code ######
from tkinter import *
root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text = s).grid(padx=10, pady=10)
root.mainloop()
