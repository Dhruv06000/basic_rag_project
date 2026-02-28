import os

def load_documents(folder_path):
  documents = []

  for file in os.listdir(folder_path):
      file_path = os.path.join(folder_path, file)

      if os.path.isfile(file_path) and file.endswith('.txt'):
          with open(file_path, 'r', encoding='utf-8') as f:
              documents.append({
                  "filename": file,
                  "content": f.read()
              })
  return documents