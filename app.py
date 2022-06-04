from plistlib import UID
import requestHandler






def main():
    id = input()
    r = requestHandler.get_data(id)

if __name__ == "__main__":
    main()