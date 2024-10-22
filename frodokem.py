import hashlib
import os


def hash_function(input_data):
    return hashlib.sha3_256(input_data).digest()


# Generate a public/private key pair
def key_generation():
    secret_key = os.urandom(32)
    public_key = hash_function(secret_key)
    return public_key, secret_key


# Alice encapsulates a shared key using Bob's public key
def encapsulate_key(public_key):
    shared_key = hash_function(public_key)
    ciphertext = hash_function(public_key + shared_key)
    return shared_key, ciphertext


# Bob decapsulates the key using his private key
def decapsulate_key(secret_key, ciphertext):
    public_key = hash_function(secret_key)  # Recreate public key from Bob's private key
    derived_shared_key = hash_function(public_key)  # Derive shared key
    if hash_function(public_key + derived_shared_key) == ciphertext:
        return derived_shared_key
    else:
        raise ValueError("Decapsulation failed: invalid key.")


# Example of communication between Alice and Bob
def alice_bob_communication():
    public_key_bob, secret_key_bob = key_generation()
    shared_key_alice, ciphertext = encapsulate_key(public_key_bob)
    try:
        shared_key_bob = decapsulate_key(secret_key_bob, ciphertext)
        print("Shared key (Alice):", shared_key_alice.hex())
        print("Shared key (Bob):  ", shared_key_bob.hex())
        print("Key exchange successful!")
    except ValueError as e:
        print(e)


alice_bob_communication()
