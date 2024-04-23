'''BASICS OF COMPUTER SCIENCE ALGORITHMS IN PROTEOMICS BY KATIE OSTROUCHOV'''

#Demonstrates concepts of set, list, hashmap, dictionary, vectors, arrays, and class in the context of protein sequences

import random

#List example
protein_names = ['protein1', 'protein2', 'protein3', 'protein4']
print('My intital protein name list contains:',protein_names)

#Randomly generated list of 4 protein sequences that contain 10 uppercase letters
protein_sequences = [''.join(random.choices('ACDEFGHIKLMNPQRSTVWY', k=10)) for _ in range(4)]
print('My initial sequences list contains:',protein_sequences)

#Create dictionary of protein names and sequences
protein_dict = dict(zip(protein_names, protein_sequences))
print('My protein dictionary contains:',protein_dict)

#Append to protein_names and protein_sequences lists
protein_names.append('protein5')
protein_sequences.append(''.join(random.choices('ACDEFGHIKLMNPQRSTVWY', k=10)))
print('My protein name list now contains:',protein_names)
print('My protein sequences list now contains:',protein_sequences)

#Add the second item in the list twice to the end of protein_names and protein_sequences
protein_names.append(protein_names[1])
protein_sequences.append(protein_sequences[1])
print('My protein name list now contains:',protein_names)
print('My protein sequences list now contains:',protein_sequences)

#Set Example: Determine unique elements in names and sequences and create a set to represent them
unique_protein_names = set(protein_names)
unique_protein_sequences = set(protein_sequences)
print('My unique protein names are:',unique_protein_names)
print('My unique protein sequences are:',unique_protein_sequences)

#Hashmap Example
#Create a hashmap of protein names and sequences
protein_hashmap = {}
for i in range(len(protein_names)):
    protein_hashmap[protein_names[i]] = protein_sequences[i]
print('My protein hashmap contains:',protein_hashmap)

#Create a dictionary of protein names and sequences
protein_dict = dict(zip(protein_names, protein_sequences)) 
print('My protein dictionary contains:',protein_dict)

#Vector Example
#Create a vector of protein sequences
protein_vector = protein_sequences
print('My protein vector contains:',protein_vector)

#Array Example
#Create an array of protein sequences
protein_array = protein_sequences.copy()
print('My protein array contains:',protein_array)

#Class Example 
#Create a class of protein sequences
class Protein:
    def __init__(self, sequences):
        self.sequences = sequences
    def add_sequence(self, sequence):
        self.sequences.append(sequence)
    def remove_sequence(self, index):
        self.sequences.pop(index)
    def __str__(self):
        return str(self.sequences)

#Create a new protein sequence
new_protein_sequence = ''.join(random.choices('ACDEFGHIKLMNPQRSTVWY', k=10))
print('My new protein sequence is:',new_protein_sequence)

#Add the new protein sequence to the vector, array, and class
protein_vector.append(new_protein_sequence)
protein_array.append(new_protein_sequence)
protein_class = Protein(protein_sequences)
protein_class.add_sequence(new_protein_sequence)
print('My protein vector now contains:',protein_vector)
print('My protein array now contains:',protein_array)
print('My protein class now contains:',protein_class)

#Remove the first protein sequence from the vector, array, and class
protein_vector.pop(0)
protein_array.pop(0)
protein_class.remove_sequence(0)
print('My protein vector now contains:',protein_vector)
print('My protein array now contains:',protein_array)
print('My protein class now contains:',protein_class)

#Access protein sequence using hashmap protein name
my_protein_name = 'protein2'
print('The protein sequence for',my_protein_name,'is:',protein_hashmap[my_protein_name])

#Accessing protein sequence using dictionary protein name
my_protein_name = 'protein3'
print('The protein sequence for',my_protein_name,'is:',protein_dict[my_protein_name])





