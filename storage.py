from storage import Storage
Storage.save_data(200, 50)
data = Storage.load_data()
print(data)

"""if __name__ == "__main__":
    print("Testing Storage Module")
    Storage.save_data(200, 50)
    data = Storage.load_data()
    print(data)
    print("Test Complete")"""