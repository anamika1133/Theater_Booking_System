class TheaterBooking:
    def __init__(self, rows=5, cols=7):  # Default 5 rows, 7 columns
        self.rows = rows
        self.cols = cols
        self.seats = [['O' for _ in range(cols)] for _ in range(rows)]  # 'O' means available

    def display_seats(self):
        print("\n--- Theater Seating ---")
        print("   " + " ".join([str(i+1) for i in range(self.cols)]))  # Column numbers
        for i, row in enumerate(self.seats):
            print(f"{i+1}  " + " ".join(row))
        print()

    def book_seat(self, row, col):
        if 1 <= row <= self.rows and 1 <= col <= self.cols:
            if self.seats[row-1][col-1] == 'O':
                self.seats[row-1][col-1] = 'X'  # 'X' means booked
                print(f"✅ Seat ({row}, {col}) booked successfully!\n")
            else:
                print(f"❌ Seat ({row}, {col}) is already booked.\n")
        else:
            print("❌ Invalid seat number! Please try again.\n")

    def cancel_booking(self, row, col):
        if 1 <= row <= self.rows and 1 <= col <= self.cols:
            if self.seats[row-1][col-1] == 'X':
                self.seats[row-1][col-1] = 'O'  # Mark as available
                print(f"✅ Booking for seat ({row}, {col}) canceled.\n")
            else:
                print(f"❌ Seat ({row}, {col}) is not booked.\n")
        else:
            print("❌ Invalid seat number! Please try again.\n")

def main():
    theater = TheaterBooking()

    while True:
        print("🎭 Theater Booking System 🎟️")
        print("1️⃣ View Seats")
        print("2️⃣ Book a Seat")
        print("3️⃣ Cancel Booking")
        print("4️⃣ Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            theater.display_seats()
        elif choice == '2':
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            theater.book_seat(row, col)
        elif choice == '3':
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            theater.cancel_booking(row, col)
        elif choice == '4':
            print("🎭 Thank you for using the Theater Booking System! 🎟️")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
