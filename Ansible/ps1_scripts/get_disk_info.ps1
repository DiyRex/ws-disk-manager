# Define disk and partition information
$disks = Get-PhysicalDisk | Select-Object DeviceID, SerialNumber, Size, OperationalStatus
$drives = Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free

$diskInfo = @()

foreach ($drive in $drives) {
    # Get partition related to the drive letter
    $partition = Get-Partition -DriveLetter $drive.Name

    # Retrieve disk information using the partition's DiskNumber
    $disk = Get-Disk | Where-Object { $_.Number -eq $partition.DiskNumber } | Select-Object Number, @{Name="Size(GB)";Expression={[math]::round($_.Size / 1GB, 2)}}
    
    # Retrieve physical disk information including serial number
    $physicalDisk = $disks | Where-Object { $_.DeviceID -eq $partition.DiskNumber }

    # Ensure the disk object was retrieved
    if ($disk -and $physicalDisk) {
        # Calculate sizes in GB
        $sizeGB = [math]::Round($disk.'Size(GB)', 2)
        $freeGB = [math]::Round($drive.Free / 1GB, 2)
        $usedGB = [math]::Round($drive.Used / 1GB, 2)
        $partitionSizeGB = [math]::Round($partition.Size / 1GB, 2)
        $unallocatedGB = [math]::Round(($sizeGB - $partitionSizeGB), 2)
        
        # Collect disk information with DiskNumber and PartitionNumber
        $diskInfo += [PSCustomObject]@{
            DiskNumber          = $partition.DiskNumber
            PartitionNumber     = $partition.PartitionNumber
            DriveLetter         = $drive.Name
            Free                = $freeGB
            Used                = $usedGB
            SerialNumber        = $physicalDisk.SerialNumber
            Size                = $sizeGB
            UnallocatedSpace    = $unallocatedGB
        }
    } else {
        Write-Host "Disk not found for DiskNumber $($partition.DiskNumber)"
    }
}

$diskInfo | ConvertTo-Json
