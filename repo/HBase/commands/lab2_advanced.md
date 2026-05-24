# HBase Lab 2 — Advanced

## 2.1 Filters

### PrefixFilter — Rows starting with a value
```hbase
scan 'student', {FILTER => "PrefixFilter('1')"}
```

### RowFilter — Match an exact row key
```hbase
scan 'student', {FILTER => "RowFilter(=,'binary:2')"}
```

### SingleColumnValueFilter — Filter by column value
```hbase
# Find all engineering students
scan 'student', {
  FILTER => "SingleColumnValueFilter('academic','faculty',=,'binary:engineering')"
}

# Find students with grade B
scan 'student', {
  FILTER => "SingleColumnValueFilter('academic','grade',=,'binary:B')"
}
```

### ColumnPrefixFilter — Columns starting with a prefix
```hbase
scan 'student', {FILTER => "ColumnPrefixFilter('gr')"}
```

---

## 2.2 FilterList — Combine Multiple Filters

```hbase
# Engineering students in year 3 (AND logic)
scan 'student', {
  FILTER => "FilterList(MUST_PASS_ALL,
    SingleColumnValueFilter('academic','faculty',=,'binary:engineering'),
    SingleColumnValueFilter('academic','year',=,'binary:3')
  )"
}
```

---

## 2.3 Alter Table — Add a Column Family

```hbase
alter 'student', NAME => 'contact'

put 'student', 1, 'contact:email', 'ali@uni.edu'
put 'student', 2, 'contact:email', 'sara@uni.edu'

describe 'student'
```

---

## 2.4 Versioning

```hbase
# Enable versioning — keep up to 5 versions
alter 'student', NAME => 'personal', VERSIONS => 5

# Update a cell multiple times
put 'student', '2', 'personal:city', 'cairo'
put 'student', '2', 'personal:city', 'giza'
put 'student', '2', 'personal:city', 'alex'

# Retrieve all versions
get 'student', '2', {COLUMN => 'personal:city', VERSIONS => 3}
```

---

## 2.5 Table Lifecycle

```hbase
disable 'student'      # required before dropping
is_disabled 'student'  # check status
enable 'student'       # re-enable
disable 'student'      # must disable before drop
drop 'student'
list                   # confirm it's gone
```

> ⚠️ You cannot drop a table that is still enabled.
