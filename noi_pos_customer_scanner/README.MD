# Customer Scanner (POS)

This module extends the **Odoo Point of Sale (POS)** to allow scanning of **customer barcodes** or **QR codes** directly in the POS interface.  

---

## 📌 Features
- If the scanned code matches a **product**, the product is added to the order (default POS behavior).  
- If the scanned code does **not** match a product, the system searches among **customers (partners)**.  
- If a matching customer is found, that customer is automatically set as the **order’s customer**.  
- Supports both **barcode** and **QR code** scanning.  

---

## 🛠️ Technical Details
- Core logic is implemented in:  

static/src/js/Screens/ProductScreens/customer_scan.js

- Extends the POS **barcode scanning flow** (`BarcodeEvents`) to include customer lookups.  
- Works seamlessly with Odoo’s existing POS database for customers (`res.partner`).  
- Designed for **Odoo 17.0 POS**.  

---

## 💡 Use Case
- Perfect for businesses using:  
- **Membership cards**  
- **Loyalty programs**  
- **VIP customers**  

Example workflow:  
1. The cashier scans a customer’s membership card.  
2. If it’s a product barcode → product is added to the order.  
3. If it’s a customer barcode → customer is set for the order instantly.  
4. Checkout continues with the correct customer.  

---

## 📂 Module Structure
noi_pos_customer_scanner/
├── manifest.py
├── README.md
├── static/
│ ├── description/
│ │ └── index.html
│ └── src/
│ └── js/
│ └── Screens/
│ └── ProductScreens/
│ └── customer_scan.js


---

## 🏢 Company
**NexOrionis Techsphere**  
We specialize in Odoo development, custom modules, and business solutions.  

- 🌍 Website: [https://nexorionis.odoo.com](https://nexorionis.odoo.com)  
- 📧 Email: [nexorionis.info@gmail.com](mailto:nexorionis.info@gmail.com)  

Maintainer: **Rowan Ember**  

---

## ⚖️ License
This module is licensed under the **LGPL-3** License.  

✔️ Compatible with **Odoo 17.0 POS**
