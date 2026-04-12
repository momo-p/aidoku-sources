import json
import os
import sys

def transform_source(item):
    target = {
        "id": item.get("id", ""),
        "name": item.get("name", ""),
        "version": item.get("version", 1),
    }
    
    if "downloadURL" in item:
        target["file"] = item["downloadURL"].replace("sources/", "")
    
    if "iconURL" in item:
        target["icon"] = item["iconURL"].replace("icons/", "")
        
    langs = item.get("languages", [])
    if len(langs) > 1:
        target["lang"] = "multi"
    elif len(langs) == 1:
        target["lang"] = langs[0]
    else:
        target["lang"] = "unknown"
        
    target["nsfw"] = 1 if item.get("contentRating", 0) >= 2 else 0
    
    return target

def run():
    file_path = 'index.json'
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        sys.exit(1)

    if not isinstance(data, dict) or "sources" not in data:
        print("Error: Expected dictionary with 'sources' key.")
        sys.exit(1)

    target_sources = [transform_source(item) for item in data["sources"]]

    if not target_sources:
        return

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(target_sources, f, indent=2, ensure_ascii=False)
    
    with open('index.min.json', 'w', encoding='utf-8') as f:
        json.dump(target_sources, f, separators=(',', ':'), ensure_ascii=False)

if __name__ == "__main__":
    run()
