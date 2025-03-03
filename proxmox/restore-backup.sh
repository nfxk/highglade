# Find the latest .vma.zst file
latest_file=$(ls -t /var/lib/vz/dump/ | grep '.vma.zst$' | head -n 1)

# Check if a file was found
if [ -z "$latest_file" ]; then
  echo "Error: No .vma.zst file found in /var/lib/vz/dump/"
  exit 1
fi

# Construct the full path to the latest file
full_path="/var/lib/vz/dump/$latest_file"

# stop VM in order to restore the backup
qm stop 100

# Proceed with qmrestore using the full path and filename
qmrestore "$full_path" 100 --force true

# start when restore is completed
qm start 100
