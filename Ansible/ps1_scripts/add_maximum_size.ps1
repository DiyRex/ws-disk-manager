# Define the disk and partition numbers
$diskNumber = 1  # Replace with your disk number
$partitionNumber = 1  # Replace with your partition number

# Get the disk, partition, and volume information
$disk = Get-Disk -Number $diskNumber
$partition = Get-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber

# Get the maximum size supported for the partition
$partitionSize = Get-PartitionSupportedSize -DiskNumber $diskNumber -PartitionNumber $partitionNumber

# Calculate the size to extend
$currentSize = $partition.Size
$maxSize = $partitionSize.SizeMax
$freeSpace = $maxSize - $currentSize

# Output the current and maximum sizes for debugging
Write-Output "Current Size: $currentSize bytes"
Write-Output "Maximum Size: $maxSize bytes"
Write-Output "Free Space Available: $freeSpace bytes"

if ($freeSpace -gt 0) {
    try {
        # Resize the partition to the maximum size
        Resize-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber -Size $maxSize
        Write-Output "Partition extended to maximum size of $maxSize bytes."
    } catch {
        Write-Output "An error occurred while resizing the partition: $_"
    }
} else {
    Write-Output "The partition is already at its maximum size or no additional space is available."
}
