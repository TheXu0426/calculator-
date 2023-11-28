#
# Calculator.py- this is the calculator code 
#
#Author 
#QINGHE XU 
#
#5 SEP 2023
#7 SEP 2023 revised
#
"""

Project: Basic Calculator

Requirements:

1--- Create a Python program that functions as a basic calculator.
2--- The calculator should support the following operations: addition, subtraction, multiplication, and division.
3--- The program should take user input for the operation to be performed and two numbers on which the operation will be applied.
4--- After performing the operation, the program should display the result to the user.
5---- Provide an option for the user to exit the calculator.

Optional Enhancements:

# Allow the user to perform multiple calculations in succession without restarting the program.
# Create a user-friendly menu system for selecting operations.
# See the history of the calculation
#Graph to see how many calculation you performed for each type

"""
import math 
import matplotlib.pyplot as plt 

class BasicCalculator(object):
    
    def addition(self,a,b):
        return a + b
    
    def subtraction(self,a,b):
        return a - b
    
    def multiplication(self,a,b):
        return a * b
    
    def division(self,a,b):
        return a / b 
    
    def calculator(self):
        
        addition_list = []
        subtract_list = []
        multiplication_list =[]
        division_list = []
        history_list = []

        
        
        while True:
            print("---Please enter the first number---")
            while True:
                num_1_input = input(">")
                try:
                    num_1 = float(num_1_input)
                    break
                except ValueError:
                    print("ERROR!!!!!!! Please enter again MUST BE A NUMBER ")
            print()
            print("---Please enter the second number")
            while True:
                num_2_input = input(">")
                try:
                    num_2 = float(num_2_input)
                    break
                except ValueError:
                    print("ERROR!!!!!!! Please enter again MUST BE A NUMBER ")
            print()
            print("Please enter Your option from the menu given", '\n', '---(A)ddition---' ,'\n', '---(M)ultiplication---',"\n",'---(D)ivision---',"\n",'---(S)ubtration---','\n',"---(G)raph to see how many calculation you performed for each type---","\n","---(H)istory---",'\n''---(E)xit---','\n' )
            calculation_type = input()
            
        
            
        
            if calculation_type.upper() == "A":
                result = self.addition(num_1,num_2)
                addition_list.append(result)
                history_list.append(f"{num_1} + {num_2} = {result}")
                print("The addition answer for ",'\n',"Number 1 = ",num_1,"\n","Number 2 = ",num_2,"\n","Answer = ", result,'\n')
            
            elif calculation_type.upper() == "S":
                result = self.subtraction(num_1,num_2)
                subtract_list.append(result)
                history_list.append(f"{num_1} - {num_2} = {result}")
                print("The subtraction answer for ",'\n',"Number 1 = ",num_1,"\n","Number 2 = ",num_2,"\n","Answer = ", result,'\n')
                
            elif calculation_type.upper() == "M":
                result = self.multiplication(num_1,num_2)
                multiplication_list.append(result)
                history_list.append(f"{num_1} * {num_2} = {result}")
                print("The multiplication answer for ",'\n',"Number 1 = ",num_1,"\n","Number 2 = ",num_2,"\n","Answer = ", result,'\n')
            
            elif calculation_type.upper() == "D":
                result = self.division(num_1,num_2)
                division_list.append(result)
                history_list.append(f"{num_1} / {num_2} = {result}")
                print("The divsion answer for ",'\n',"Number 1 = ",num_1,"\n","Number 2 = ",num_2,"\n","Answer = ", result,'\n')
            
            elif calculation_type.upper() == "H":
                for i in history_list:
                    print(i)

            elif calculation_type.upper() == "G":
                type_calc = ["Addition","Subtraction","Multiplication","Division"]
                graph_color = ["red","yellow","green","blue"]
                result = [len(addition_list),len(subtract_list),len(multiplication_list),len(division_list)]
                plt.bar(type_calc, result, color = graph_color)
                plt.title("Type of calculation usage")
                plt.xlabel("Types of calculation") 
                plt.ylabel("Number of performed")
                plt.show()
            
            elif calculation_type.upper() == "E":
                return "Exiting calculator"
            
            else:
                print("ERROR !!!!!!  Invalid please enter your selction again ")





obj = BasicCalculator()
obj.calculator()

  


            




    


