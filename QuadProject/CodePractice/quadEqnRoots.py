import matplotlib.pyplot as mp
import numpy as np
import streamlit as st
import io

def findRoots(a, b, c):
    # D = (b^2 - (4*a*c))
    #if D == 0: Equal roots
    #if D < 0: Distinct and Complex roots
    #if D > 0: Distinct and real roots
    D = (b**2 - (4*a*c))

    #Roots calculation, roots -> (-b (+/-) sqrt(D))/(2*a)
    realPart = round((b * -1)/(a * 2), 2)
    roots = []
    if D < 0:                                           #if roots are not real
        roots.append(False)
        imgPart = (abs(D) ** 0.5)/(a * 2)
        roots.append(f'{realPart} + i{round(imgPart, 2)}')
        roots.append(f'{realPart} - i{round(imgPart, 2)}')
    elif D == 0:                                        #Real and Equal Roots
        roots.append(True)
        roots.append(realPart)
        roots.append(realPart)
    else:                                               #Real and distinct Roots
        roots.append(True)
        secPart = round((D ** 0.5)/(a * 2), 2)
        roots.append(realPart+secPart)
        roots.append(realPart-secPart)
    return roots


def plotForReal(r1, r2, a, b, c):
    
    xAxis = np.linspace(r1-5, r2+5, 400)
    yAxis = a*(xAxis**2) + b*xAxis + c 
    mp.plot(xAxis, yAxis, label='Equation Line')
    mp.xlabel('x')
    mp.ylabel('y')
    mp.title('Plot of Quadratic Equation with Real Roots')
    mp.grid(True)

    # make the axis line a litter bolder
    mp.axhline(0, color='black',linewidth=1.5)
    mp.axvline(0, color='black',linewidth=1.5)
    
    mp.legend()
    # mp.show()
    img_buffer = io.BytesIO()
    mp.savefig(img_buffer, format='jpeg')
    img_buffer.seek(0)

    st.image(img_buffer)
    

def main():
    st.write("<h1 style='text-align:center;'>Quadratic Equation Solver</h1>", unsafe_allow_html=True)
    st.write("Example of a quadratic equation:  aX^2 + bX + c = 0\n")
    # quadratic quation -> aX^2 + bX + c = 0
    # print("Example of a quadratic equation:  aX^2 + bX + c = 0\n")
    # try:
    #     a = int(input("a: "))
    #     if a == 0:
    #         print('Invalid Equation')
    #         return
    #     b = int(input('b: '))
    #     c = int(input('c: '))
    try:
        a = st.number_input("Enter value of a:", step=1.0, value=1.0)
        # a = int(input("a: "))
        if a == 0:
         st.write('Invalid Equation')
         return
        b = st.number_input("Enter value of b:", step=1.0, value=0.0)
        # b = int(input('b: '))
    
        c = st.number_input("Enter value of c:", step=1.0, value=0.0)
    # c = int(input('c: '))

    except:
        st.write("Incorrect Input")
        return
    if st.button("Solve"):
        roots = findRoots(a, b, c)
    # roots = findRoots(a, b, c)
        st.markdown(f'**Roots: {roots[1]}, {roots[2]}**')
        if roots[0]:
            plotForReal(roots[1], roots[2], a, b, c)

    

if __name__ == "__main__":
    main()