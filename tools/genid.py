import uuid

if __name__ == "__main__":
  print(uuid.uuid4().int & (1<<64)-1)
