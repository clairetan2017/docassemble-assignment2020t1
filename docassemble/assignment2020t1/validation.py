import re 
from docassemble.base.util import *

def check_nric(string): 
  if not re.match(r'[ST][0-9]{7}[A-I,J,Z]', string): 
    validation_error('Incorrect NRIC format.')  
  
  weights = [2, 7, 6, 5, 4, 3, 2, 1]
  number_to_letter = {10: "A", 9: "B", 8: "C", 7: "D", 6: "E", 5: "F", 4: "G", 3: "H", 2: "I", 1: "Z", 0: "J"}
  
  for c in range(7):
    total_nric = sum(int(c) * w for c, w in zip(string[1:8],weights))
    
  if string[0] == 'T': 
     total_nric = total_nric + 4
  
  checksum_nric = total_nric % 11
  
  if not number_to_letter[checksum_nric] == string[8]:
    validation_error('Invalid NRIC Number.')
  return True

       