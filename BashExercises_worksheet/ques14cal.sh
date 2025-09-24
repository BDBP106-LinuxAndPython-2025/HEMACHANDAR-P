#!/bin/bash

while true; do
    # Display the menu
    echo "======================"
    echo " MENU"
    echo "1) Show date"
    echo "2) Show calendar"
    echo "3) Show logged-in users"
    echo "4) Exit"
    echo "======================"
    
    # Ask for user choice
    read -p "Enter your choice [1-4]: " choice

    # Execute based on choice
    case $choice in
        1)
            echo "Current date and time: $(date)"
            ;;
        2)
            echo "Current month calendar:"
            cal
            ;;
        3)
            echo "Logged-in users:"
            who
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please select 1-4."
            ;;
    esac

    # Pause before showing menu again
    echo
    read -p "Press Enter to continue..." temp
done

