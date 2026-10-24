storage_gb = float(input("Enter storage in GB: "))
storage_mb = storage_gb * 1024
storage_kb = storage_mb * 1024
storage_bytes = storage_kb * 1024
storage_tb = storage_gb / 1024

print(f"{storage_gb} GB is equal to {storage_mb} MB - Improved Output")
print(f"{storage_gb} GB is equal to {storage_kb} KB - GB Conversion Feature")
print(f"{storage_gb} GB is equal to {storage_bytes} Bytes")
print(f"{storage_gb} GB is equal to {storage_tb:.4f} TB - Added GB output")