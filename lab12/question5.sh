#!/bin/bash


# Function to perform division
function divide() {
    local num1=$1
    local num2=$2

    # Check if denominator is zero
    if [ "$num2" -eq 0 ]; then
        echo "Error: Division by zero is not allowed."
        return 1
    fi

    # Calculate quotient (with 2 decimal places) using bc
    local quotient=$(echo "scale=2; $num1 / $num2" | bc)

    # Calculate remainder using modulo
    local remainder=$((num1 % num2))

    echo "Quotient: $quotient"
    echo "Remainder: $remainder"
}

# --- Main script ---
read -p "Enter numerator: " num1
read -p "Enter denominator: " num2

divide "$num1" "$num2"
