def load_data(path: str) -> list[str]: 
    with open(path, "r", encoding='utf-8') as file:
        return file.readlines()
    
def process_data_to_get_salaries(data: list[str]) -> list[int]: 
    return [int(line.split(',')[1]) for line in data if line.strip()]