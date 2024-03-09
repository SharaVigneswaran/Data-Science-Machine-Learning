import streamlit as st

def square_number(number):
    return number ** 2

def main():
    st.title('Square Number App')
    st.write('Enter a number below to see its square:')

    number = st.number_input('Enter a number:', value=0)
    if st.button('Square'):
        result = square_number(number)
        st.write(f"The square of {number} is: {result}")

if __name__ == "__main__":
    main()
