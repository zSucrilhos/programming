#Variable inicialization
vo=int(0)
vf=int(0)
to=int(0)
tf=int(0)
delta_v=int(0)
delta_t=int(0)
af=int(0)
goto="Y"
import math
#############################
print("CALCULATE ACCELERATION (PHYSICS)")

#Line wrap
print()
print("Units:")
print("Velocity should be expressed in km/h")
print("Time should be expressed in seconds")

#Line wrap
print()
print()

while goto == "Y":
    vo=int(input("Type the initial velocity: "))
    vf=int(input("Type the final velocity: "))

    #Line wrap
    print()

    to=float(input("Type the initial time: "))
    tf=float(input("Type the final time: "))
    #Calculates the veloocity variation
    delta_v = vf-vo
    #Calculates the time variation
    delta_t = tf-to
    #Returns the result of the division of delta_v by delta_t
    #and stores it in the 'fa' variable (final acceleration)
    fa=delta_v/delta_t

    #Line wrap
    print()
    print("The acceleratioon is %.2f m/s" %(fa))
    #Line wrap
    print()
    goto=input("Calculate again? (Y/N): ")
        
else:
    print("Farewell!")

print()
a=float((math.pi))
print(a*32)

