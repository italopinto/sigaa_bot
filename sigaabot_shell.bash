#!/bin/bash

user="<your_sigaa_user>"
password="<your_sigaa_password>"
school_term=$2


homepage()
{
    /path/to/venv/bin/python /path/to/main.py $user $password $school_term 0
    exit
}

see_grades()
{
    /path/to/venv/bin/python /path/to/main.py $user $password $school_term 1
    exit
}

see_certificate()
{
    /path/to/venv/bin/python /path/to/main.py $user $password $school_term 2
    exit
}

see_history()
{
    /path/to/venv/bin/python /path/to/main.py $user $password $school_term 3
    exit
}

see_bond()
{
    /path/to/venv/bin/python /path/to/main.py $user $password $school_term 4
    exit
}

online_enrollment()
{
    /path/to/venv/bin/python /path/to/main.py $user $password $school_term 5
    exit
}

error_msg()
{
    echo ""
    echo "----------------------------------------------"
    echo "You must pass a number (or just home) and the school term!"
    echo " [home] to land in the homepage."
    echo " [1] to see the grades."
    echo " [2] to see the certificate of enrollment."
    echo " [3] to see the history."
    echo " [4] to see the bond statement."
    echo " [5] to do the online enrollment"
    echo "----------------------------------------------"
    echo "e.g.: sigaabot 1 2021-1"
    echo "----------------------------------------------"
    echo ""
    exit
}

# logical operators: && (and), || (or), ! (not equal)
# relational test: -eq to compare if an integer is equal to another one
if [[ $1 == "home" ]]; then
    homepage
fi
if [[ $1 -eq 0 || $2 -eq 0 ]]; then
    error_msg
elif [[ $1 -eq 1 ]]; then
    see_grades
elif [[ $1 -eq 2 ]]; then
    see_certificate
elif [[ $1 -eq 3 ]]; then
    see_history
elif [[ $1 -eq 4 ]]; then
    see_bond
elif [[ $1 -eq 5 ]]; then
    online_enrollment
else
    error_msg
fi
