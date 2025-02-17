# quantum/init_qiskit.py
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import numpy as np
import json
import os
import time
import random

class QuantumKeyDistribution:
    def __init__(self):
        self.simulator = Aer.get_backend('qasm_simulator')
        
    def generate_bb84_key(self, key_length=32):
        """
        Implements the BB84 quantum key distribution protocol
        """
        # Alice's random bits
        alice_bits = np.random.randint(2, size=key_length)
        
        # Alice's random basis choices (0 for X basis, 1 for Z basis)
        alice_bases = np.random.randint(2, size=key_length)
        
        # Prepare quantum states
        qc_list = []
        for i in range(key_length):
            qc = QuantumCircuit(1, 1)
            
            # Prepare state based on bit value
            if alice_bits[i] == 1:
                qc.x(0)
                
            # Apply Hadamard if using X basis
            if alice_bases[i] == 0:
                qc.h(0)
                
            # Measure (this simulates sending to Bob)
            qc.measure(0, 0)
            qc_list.append(qc)
        
        # Bob's random basis choices
        bob_bases = np.random.randint(2, size=key_length)
        
        # Bob's measurement results
        bob_results = []
        for i, qc in enumerate(qc_list):
            # If Bob uses X basis but Alice used Z basis (or vice versa), apply H gate
            if bob_bases[i] != alice_bases[i]:
                qc.h(0)
            
            # Execute the circuit
            result = execute(qc, self.simulator, shots=1).result()
            counts = result.get_counts(qc)
            bob_results.append(int(list(counts.keys())[0]))
        
        # Determine which bits to keep (where bases match)
        matching_bases = alice_bases == bob_bases
        final_key_bits = alice_bits[matching_bases]
        
        # Convert bit array to hex string
        final_key = ''.join([str(bit) for bit in final_key_bits])
        
        # Save key info to file for the Go application to use
        key_info = {
            "key": final_key,
            "length": len(final_key),
            "matching_bases_count": np.sum(matching_bases),
            "total_bits_sent": key_length,
            "timestamp": time.time()
        }
        
        with open('quantum/latest_key.json', 'w') as f:
            json.dump(key_info, f)
        
        return key_info

# Initialize the quantum module and generate initial keys
if __name__ == "__main__":
    os.makedirs("quantum", exist_ok=True)
    
    qkd = QuantumKeyDistribution()
    
    # Generate initial key pool
    for i in range(5):
        key_info = qkd.generate_bb84_key()
        print(f"Generated quantum key: {key_info['key'][:8]}... ({key_info['length']} bits)")
        time.sleep(0.5)
    
    print("Quantum module initialized successfully")