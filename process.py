import json
import sys

def run():
    try:
        with open('index.json', 'r') as f:
            data = json.load(f)
        
        if "sources" in data:
            for item in data["sources"]:
                if 'downloadURL' in item:
                    item['file'] = item['downloadURL'].replace('sources/', '')
        else:
            print(f"Invalid original aidoku sources index.")
                
        with open('index.json', 'w') as f:
            json.dump(data["sources"], f, indent=2)
            
        with open('index.min.json', 'w') as f:
            json.dump(data["sources"], f, separators=(',', ':'))
            
        print("Process json sources file successfully.")
    except Exception as e:
        print(f"Error processing JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()

