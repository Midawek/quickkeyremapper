import keyboard

def remap_keys():
    # Define the key remapping
    key_remap = {
        'F22': 'Ł'
    }

    # Add the remapping
    for from_key, to_key in key_remap.items():
        keyboard.add_hotkey(from_key, lambda: keyboard.write(to_key))

    # Start listening for hotkeys
    keyboard.wait()

if __name__ == "__main__":
    remap_keys()
