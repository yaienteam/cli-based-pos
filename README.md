
# 🧾 CLI-Based POS System (Python)

A lightweight command-line Point of Sale (POS) system written in Python. This application allows small businesses or shops to manage sales, products, payments, and customer accounts using a local file system (no database required). It's ideal for learning file I/O, CLI application structure, and basic accounting logic.

---

## 📌 Features

- 📦 **Product Management**  
  Add, view, update, or delete product entries.

- 💰 **Sales Processing**  
  Handle sales transactions, generate receipts, and store them for future reference.

- 👤 **Customer Accounts**  
  Manage customer profiles and track outstanding balances.

- 🧾 **Payments Tracking**  
  Record customer payments and update account balances.

- 📊 **Reports**  
  View daily sales summaries and payment logs.

---

## 🔁 Application Flow

```text
[Start Program]
      ↓
[Main Menu]
  ├── Manage Products
  │     ├── Add Product
  │     ├── View Products
  │     └── Update/Delete Product
  │
  ├── Process Sale
  │     ├── Select Product(s)
  │     ├── Add Quantity
  │     ├── Calculate Total
  │     └── Print Receipt + Save Sale
  │
  ├── Manage Accounts
  │     ├── View Account Details
  │     ├── Add Payment
  │     └── Update Balance
  │
  ├── View Reports
  │     ├── Daily Sales
  │     └── Payments
  │
  └── Exit Program

