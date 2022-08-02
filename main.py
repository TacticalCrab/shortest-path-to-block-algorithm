from operator import add
from tabnanny import check
from sample_data import generate_sample_data

# Solution
def check_shortest_path(BLOCK_SERVICES, blocks):
    BLOCKS_LENGTH = len(blocks)

    result_index = -1  # Initial solution
    result_path = -1
    missing_services_amount = -1
    result_max_path = -1


    for index, block in enumerate(blocks):
        missing_services = {}

        for block_service in BLOCK_SERVICES:
            if not block[block_service]:
                missing_services[block_service] = -1

        # Initial variables
        tindex = index
        length = 0

        if index == 0:
            # Right ( x < max)
            tindex += 1
            while tindex < BLOCKS_LENGTH:
                length += 1
                for service in missing_services:
                    if blocks[tindex][service]:
                        if missing_services[service] == -1:
                            missing_services[service] = length
                        elif length < missing_services[service]:
                            missing_services[service] = length
                tindex += 1

        elif index == BLOCKS_LENGTH:
            # Left ( x > 0)
            tindex -= 1
            while tindex >= 0:
                length += 1
                for service in missing_services:
                    if blocks[tindex][service]:
                        if missing_services[service] == -1:
                            missing_services[service] = length
                        elif length < missing_services[service]:
                            missing_services[service] = length
                tindex -= 1

        else:
            # Left ( x > 0)
            tindex -= 1
            while tindex >= 0:
                length += 1
                for service in missing_services:
                    if blocks[tindex][service]:
                        if missing_services[service] == -1:
                            missing_services[service] = length
                        elif length < missing_services[service]:
                            missing_services[service] = length
                tindex -= 1

            # Reset variables
            length = 0
            tindex = index

            # Right ( x < max)
            tindex += 1
            while tindex < BLOCKS_LENGTH:
                length += 1
                for service in missing_services:
                    if blocks[tindex][service]:
                        if missing_services[service] == -1:
                            missing_services[service] = length
                        elif length < missing_services[service]:
                            missing_services[service] = length
                tindex += 1

        # Sum services
        additional_path = 0
        v_missing_services = 0
        max_path = -1

        for length in missing_services.values():
            if max_path == -1:
                max_path = length
            elif length < max_path:
                max_path = length

        for service in missing_services:
            if missing_services[service] == -1:
                v_missing_services += 1
            else:
                additional_path += missing_services[service]

        # Test results
        if result_path == -1 or missing_services_amount == -1:
            result_index = index
            result_path = additional_path
            missing_services_amount = v_missing_services
            result_max_path = max_path

        elif additional_path < result_path and v_missing_services <= missing_services_amount:
            result_index = index
            result_path = additional_path
            missing_services_amount = v_missing_services
            result_max_path = max_path
        
        elif additional_path == result_path and v_missing_services <= missing_services_amount:
            if max_path < result_max_path:
                result_index = index
                result_path = additional_path
                missing_services_amount = v_missing_services
                result_max_path = max_path

    return result_index

if __name__ == '__main__':
    # You can change those values
    length = 10
    services = ["gym", "school", "store"]

    # Auto generate data
    blocks = generate_sample_data(length, services) 

    # Manual data
    # Uncomment to set
    blocks = [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True},

    ]
    services = blocks[0].keys()

    print(*blocks, sep="\n")

    index = check_shortest_path(services, blocks)
    print("Shortest path, to all services has:", index)
