#!/usr/bin/env python3

def subnet_calculator(ip_address, cidr):
    """
    Calculate subnet information based on an IP address and CIDR notation.

    Args:
        ip_address (str): The base IP address (e.g., "192.168.1.0").
        cidr (int): The CIDR prefix length (e.g., 24).

    Returns:
        dict: A dictionary with subnet mask, block size, number of subnets, number of hosts, and subnet ranges.
    """
    import ipaddress

    try:
        # Convert IP address to binary and calculate the network address
        network = ipaddress.IPv4Network(f"{ip_address}/{cidr}", strict=False)

        subnet_mask = str(network.netmask)
        block_size = 256 - int(str(network.netmask).split('.')[-1])
        total_hosts = network.num_addresses
        usable_hosts = total_hosts - 2

        subnet_ranges = []
        for subnet in network.subnets(new_prefix=cidr):
            subnet_ranges.append(str(subnet))

        return {
            "IP Address": ip_address,
            "CIDR": cidr,
            "Subnet Mask": subnet_mask,
            "Block Size": block_size,
            "Number of Hosts": total_hosts,
            "Usable Hosts": usable_hosts,
            "Subnets": subnet_ranges,
        }
    except Exception as e:
        return {"error": str(e)}


# Example Usage
if __name__ == "__main__":
    while True:
        print("\nEnter an IP address (e.g., 192.168.1.0) or type 'done' to exit:")
        ip = input()
        if ip.lower() == "done":
            print("Exiting the subnet calculator. Goodbye!")
            break

        try:
            # Validate IP address
            import ipaddress
            ipaddress.IPv4Address(ip)

            cidr = int(input("Enter the CIDR (e.g., 24): "))

            result = subnet_calculator(ip, cidr)

            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print("\n--- Subnet Information ---")
                for key, value in result.items():
                    if key != "Subnets":
                        print(f"{key}: {value}")
                    else:
                        print(f"{key}:")
                        for subnet in value:
                            print(f"  - {subnet}")
        except ValueError:
            print("Invalid input. Please ensure the IP address and CIDR are correct.")
        except ipaddress.AddressValueError:
            print("Invalid IP address. Please try again.")
