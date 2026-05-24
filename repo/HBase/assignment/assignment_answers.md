# HBase Assignment — Store Inventory
## Beginner & Intermediate

---

## Overview

Build and query a product inventory system using HBase with a table called `store` across two column families.

| Table Name | Column Families | Total Records |
|------------|----------------|---------------|
| store | details, inventory | 5 products |

## Dataset

| Row Key | Name | Brand | Category | Price | Quantity | Warehouse |
|---------|------|-------|----------|-------|----------|-----------|
| 1 | laptop | dell | electronics | 1200 | 50 | A |
| 2 | phone | samsung | electronics | 800 | 120 | A |
| 3 | desk | ikea | furniture | 300 | 30 | B |
| 4 | chair | ikea | furniture | 150 | 60 | B |
| 5 | tablet | apple | electronics | 600 | 80 | A |

---

## PART A — BEGINNER

**Q1. Create the store table**
```hbase
create 'store', 'details', 'inventory'
```

---

**Q2. Insert all 5 rows**
```hbase
put 'store', 1, 'details:name', 'laptop'
put 'store', 2, 'details:name', 'phone'
put 'store', 3, 'details:name', 'desk'
put 'store', 4, 'details:name', 'chair'
put 'store', 5, 'details:name', 'tablet'

put 'store', 1, 'details:brand', 'dell'
put 'store', 2, 'details:brand', 'samsung'
put 'store', 3, 'details:brand', 'ikea'
put 'store', 4, 'details:brand', 'ikea'
put 'store', 5, 'details:brand', 'apple'

put 'store', 1, 'details:category', 'electronics'
put 'store', 2, 'details:category', 'electronics'
put 'store', 3, 'details:category', 'furniture'
put 'store', 4, 'details:category', 'furniture'
put 'store', 5, 'details:category', 'electronics'

put 'store', 1, 'inventory:price', '1200'
put 'store', 2, 'inventory:price', '800'
put 'store', 3, 'inventory:price', '300'
put 'store', 4, 'inventory:price', '150'
put 'store', 5, 'inventory:price', '600'

put 'store', 1, 'inventory:quantity', '50'
put 'store', 2, 'inventory:quantity', '120'
put 'store', 3, 'inventory:quantity', '30'
put 'store', 4, 'inventory:quantity', '60'
put 'store', 5, 'inventory:quantity', '80'

put 'store', 1, 'inventory:warehouse', 'A'
put 'store', 2, 'inventory:warehouse', 'A'
put 'store', 3, 'inventory:warehouse', 'B'
put 'store', 4, 'inventory:warehouse', 'B'
put 'store', 5, 'inventory:warehouse', 'A'
```

---

**Q3. Scan entire table**
```hbase
scan 'store'
```
> Expected: 5 rows — laptop, phone, desk, chair, tablet.

---

**Q4. Get all columns for row 3 (desk)**
```hbase
get 'store', '3'
```

---

**Q5. Get only inventory:price for row 5 (tablet)**
```hbase
get 'store', '5', {COLUMN => 'inventory:price'}
```

---

**Q6. Find all products in warehouse A**
```hbase
scan 'store', {
  COLUMNS => 'inventory:warehouse',
  FILTER  => "ValueFilter(=,'binary:A')"
}
```
> Expected: rows 1 (laptop), 2 (phone), 5 (tablet).

---

## PART B — INTERMEDIATE

**Q7. Enable versioning on inventory — keep 4 versions**
```hbase
alter 'store', NAME => 'inventory', VERSIONS => 4
```

---

**Q8. Update quantity for laptop 3 times, then retrieve all versions**
```hbase
put 'store', '1', 'inventory:quantity', '45'
put 'store', '1', 'inventory:quantity', '40'
put 'store', '1', 'inventory:quantity', '35'

get 'store', '1', {COLUMN => 'inventory:quantity', VERSIONS => 4}
```
> Expected: 4 versions — 35, 40, 45, 50 (newest first).

---

**Q9. Find all products in furniture category**
```hbase
scan 'store', {
  FILTER => "SingleColumnValueFilter('details','category',=,'binary:furniture')"
}
```
> Expected: rows 3 (desk) and 4 (chair).

---

**Q10. Find all products in warehouse B**
```hbase
scan 'store', {
  FILTER => "SingleColumnValueFilter('inventory','warehouse',=,'binary:B')"
}
```
> Expected: rows 3 (desk) and 4 (chair).

---

**Q11. Add supplier column family and insert data**
```hbase
alter 'store', NAME => 'supplier'

put 'store', '1', 'supplier:country', 'egypt'
put 'store', '2', 'supplier:country', 'korea'

describe 'store'
```
> Expected: 3 column families — details, inventory, supplier.

---

**Q12. 🏆 Electronics AND warehouse A**
```hbase
scan 'store', {
  FILTER => "SingleColumnValueFilter('details','category',=,'binary:electronics') AND SingleColumnValueFilter('inventory','warehouse',=,'binary:A')"
}
```
> Expected: rows 1 (laptop), 2 (phone), 5 (tablet).
