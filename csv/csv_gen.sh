# file 1
name="file1.csv"
echo "$name"
touch "$name"
for i in {1..20}; do
    echo "$i" >> "$name"
done

name="file2.csv"
echo "$name"
touch "$name"
for i in {1..30}; do
    echo "$i" >> "$name"
done

name="file3.csv"
echo "$name"
touch "$name"
for i in {1..50}; do
    echo "$i" >> "$name"
done

name="file4.csv"
echo "$name"
touch "$name"
for i in {1..20}; do
    echo "$i" >> "$name"
done

name="file5.csv"
echo "$name"
touch "$name"
for i in {1..50}; do
    echo "$i" >> "$name"
done
