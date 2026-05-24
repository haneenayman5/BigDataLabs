# HBase Exercises — Intermediate (Q1–Q8)

## Q1. Enable versioning on `personal` — keep up to 5 versions
```hbase
alter 'student', NAME => 'personal', VERSIONS => 5
```

---

## Q2. Update `personal:city` for student 2 three times, then retrieve all versions
```hbase
put 'student', '2', 'personal:city', 'cairo'
put 'student', '2', 'personal:city', 'giza'
put 'student', '2', 'personal:city', 'alex'

get 'student', '2', {COLUMN => 'personal:city', VERSIONS => 3}
```
> Returns all 3 stored versions with timestamps, newest first.

---

## Q3. Find all students in year 4
```hbase
scan 'student', {
  FILTER => "SingleColumnValueFilter('academic','year',=,'binary:4')"
}
```

---

## Q4. Find all students who live in cairo
```hbase
scan 'student', {
  FILTER => "SingleColumnValueFilter('personal','city',=,'binary:cairo')"
}
```

---

## Q5. Add `contact:phone` for students 1, 3, and 4
```hbase
put 'student', '1', 'contact:phone', '01001234567'
put 'student', '3', 'contact:phone', '01109876543'
put 'student', '4', 'contact:phone', '01234567890'
```

---

## Q6. Scan and return only the `contact` column family
```hbase
scan 'student', {COLUMNS => 'contact'}
```

---

## Q7. Add a new column family `enrollment` and verify
```hbase
alter 'student', NAME => 'enrollment'
describe 'student'
```
> The `describe` output should now list: `personal`, `academic`, `contact`, and `enrollment`.

---

## Q8. 🏆 Students in engineering faculty AND year 3
```hbase
scan 'student', {
  FILTER => "FilterList(MUST_PASS_ALL,
    SingleColumnValueFilter('academic','faculty',=,'binary:engineering'),
    SingleColumnValueFilter('academic','year',=,'binary:3')
  )"
}
```
> `MUST_PASS_ALL` = logical AND. Returns students 1 (ali) and 5 (youssef).
