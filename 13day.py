#labex - Space Mission Management System

# -Not make any sense for me. Need to repeat #12 day lab
ince you are working with different data structures (lists, dictionaries, and sets), here are some specific pointers for each function:
1. add_mission

This function needs to update two different variables:

    Use .append() to add the mission name to the missions list.
    Use the mission name as a key to store the details (which is a dictionary) inside the mission_details dictionary.

2. update_mission

Remember that mission_details is a dictionary where each value is another dictionary.

    Access the specific mission first: mission_details[name].
    Then, update the specific key (like "Destination") within that inner dictionary.

3. display_missions

To get the output looking like the example:

    Use a for loop to iterate through the missions list.
    Inside that loop, use the mission name to look up its details in mission_details and print them.

4. list_astronauts

The goal here is a unique list, so a set is perfect!

    Iterate through all the missions in mission_details.
    The "Crew" is usually a string (e.g., "John Doe, Jane Smith"). You'll need to .split(', ') that string to get individual names.
    Use the .update() method of your set to add multiple names at once.

