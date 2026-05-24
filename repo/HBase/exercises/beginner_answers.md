# HBase Exercises — Beginner (Q1–Q8)

## Q1. Count rows in the student table
```hbase
count 'student'
```

---

## Q2. Get only `personal:city` for row key 3
```hbase
get 'student', '3', {COLUMN => 'personal:city'}
```

---

## Q3. Scan `academic:faculty`, starting from row 2, limit 3
```hbase
scan 'student', {COLUMNS => 'academic:faculty', LIMIT => 3, STARTROW => '2'}
```

---

## Q4. Update nada's city from cairo to mansoura
```hbase
put 'student', '4', 'personal:city', 'mansoura'
```
> `put` overwrites the existing value.

---

## Q5. Delete only the `personal:age` cell for student 3
```hbase
delete 'student', '3', 'personal:age'
```

---

## Q6. Confirm deletion — get all data for row 3
```hbase
get 'student', '3'
```
> Expected: `personal:name` and `personal:city` appear, but `personal:age` is gone.

---

## Q7. Delete the entire row for student 5
```hbase
deleteall 'student', '5'
```

---

## Q8. Verify student 5 no longer exists
```hbase
scan 'student'
```
> Expected: only rows 1–4 appear; row 5 (youssef) is absent.
