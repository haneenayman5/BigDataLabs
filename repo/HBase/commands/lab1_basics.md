# HBase Lab 1 — Basics

## 1.1 Create a Table

```hbase
create 'student', 'personal', 'academic'
list
describe 'student'
```

---

## 1.2 Insert Data — `put`

### Personal Data
```hbase
put 'student', 1, 'personal:name', 'ali'
put 'student', 2, 'personal:name', 'sara'
put 'student', 3, 'personal:name', 'omar'
put 'student', 4, 'personal:name', 'nada'
put 'student', 5, 'personal:name', 'youssef'

put 'student', 1, 'personal:city', 'cairo'
put 'student', 2, 'personal:city', 'alex'
put 'student', 3, 'personal:city', 'giza'
put 'student', 4, 'personal:city', 'cairo'
put 'student', 5, 'personal:city', 'tanta'

put 'student', 1, 'personal:age', '21'
put 'student', 2, 'personal:age', '22'
put 'student', 3, 'personal:age', '20'
put 'student', 4, 'personal:age', '23'
put 'student', 5, 'personal:age', '21'
```

### Academic Data
```hbase
put 'student', 1, 'academic:faculty', 'engineering'
put 'student', 2, 'academic:faculty', 'medicine'
put 'student', 3, 'academic:faculty', 'engineering'
put 'student', 4, 'academic:faculty', 'arts'
put 'student', 5, 'academic:faculty', 'engineering'

put 'student', 1, 'academic:grade', 'A'
put 'student', 2, 'academic:grade', 'B'
put 'student', 3, 'academic:grade', 'A'
put 'student', 4, 'academic:grade', 'C'
put 'student', 5, 'academic:grade', 'B'

put 'student', 1, 'academic:year', '3'
put 'student', 2, 'academic:year', '4'
put 'student', 3, 'academic:year', '2'
put 'student', 4, 'academic:year', '4'
put 'student', 5, 'academic:year', '3'
```

---

## 1.3 Scan Data — `scan`

```hbase
# Full scan
scan 'student'

# Scan with options
scan 'student', {COLUMNS => 'personal:name', LIMIT => 3, STARTROW => '2'}
```

---

## 1.4 Get Data — `get`

```hbase
# Get all columns of row 1
get 'student', '1'

# Get a specific column
get 'student', '1', {COLUMN => 'academic:grade'}
```

---

## 1.5 Scan with Filter

```hbase
# Find students with grade A
scan 'student', {
  COLUMNS => 'academic:grade',
  FILTER  => "ValueFilter(=,'binary:A')"
}
```
