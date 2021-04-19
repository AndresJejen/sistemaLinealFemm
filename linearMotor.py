import femm
import sys
femm.openfemm()
femm.newdocument(0)

simulation = sys.argv[1]

# define problem parameters
femm.mi_probdef(0, 'millimeters', 'planar', 1.e-8, 0, 30)

def up_down(side):
    return ((-2*side)+1)

def convert_measures(cm):
    return cm*400/19

## Materials
femm.mi_addmaterial('Air', 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0)
femm.mi_addmaterial('Coil', 1, 1, 0, 0, 58*0.65, 0, 0, 1, 0, 0, 0)
femm.mi_addmaterial('Hiperco-50', 3520, 3520, 0, 0, 0, 0, 0, 1, 0, 0, 0)
femm.mi_addmaterial('Magnet', 1.05, 1.05, 905659, 0, 0.667, 0, 0, 1, 0, 0, 0)

bdata = [0.000000,0.290730,0.428710,0.589560,0.796270,1.020100,1.198100,1.398900,1.559600,1.783500,1.898500,1.990700,2.054400,2.118400,2.147700,2.177000,2.206500,2.241700,2.271200,2.289000,2.312600,2.341000]
hdata = [0.000000,81.170000,106.800000,136.840000,179.910000,233.410000,283.710000,344.750000,402.920000,536.640000,670.100000,893.800000,1290.400000,2209.800000,3233.700000,4549.000000,7297.800000,11554.000000,18294.000000,25071.000000,36690.000000,62037.000000]
for n in range(0,len(bdata)):
 	femm.mi_addbhpoint('Hiperco-50', bdata[n],hdata[n])

# Body
width = convert_measures(19)
halfWidth = width/2
height = convert_measures(17.8)
halfHeight = height/2

barHeight = convert_measures(2.8)

## Simulations

simulations = [0, halfWidth/2, halfWidth]
gapSimulation  = simulations[int(simulation)]

## stator arms
leftStatorGap  = convert_measures(1.8)
innerStatorGap = convert_measures(3)

bodyWidth = convert_measures(3.2)

currentWidth  = convert_measures(1)
currentHeight = convert_measures(2.2)
leftCurrentGap = convert_measures(0.8)

rampaHeight = convert_measures(0.8)

# Movil Part
MovilWidth = convert_measures(20.5)
halfMovilWidth = MovilWidth/2

middleBarHeight = convert_measures(1)
halfMiddleBarHeight = middleBarHeight/2

magnetWidth  = convert_measures(5)
magnetHeight = convert_measures(1.8)
leftMagnetSpace  = convert_measures(1.65)
innerMagnetSpace = convert_measures(1.2)

for side in range(2):
    femm.mi_drawline(
        -halfWidth,
        (halfHeight)*up_down(side),
        halfWidth,
        (halfHeight)*up_down(side)
    )
    femm.mi_drawline(
        -halfWidth,
        halfHeight*up_down(side),
        -halfWidth,
        (halfHeight-barHeight)*up_down(side)
    )
    femm.mi_drawline(
        halfWidth,
        halfHeight*up_down(side),
        halfWidth,
        (halfHeight-barHeight)*up_down(side)
    )

    # Internal Bar   // MOVIL
    femm.mi_drawline(
        -halfMovilWidth+gapSimulation,
        (halfMiddleBarHeight)*up_down(side),
        halfMovilWidth+gapSimulation,
        (halfMiddleBarHeight)*up_down(side)
    )
    femm.mi_drawline(
        -halfMovilWidth+gapSimulation,
        halfMiddleBarHeight*up_down(side),
        -halfMovilWidth+gapSimulation,
        0
    )
    femm.mi_drawline(
        halfMovilWidth+gapSimulation,
        halfMiddleBarHeight*up_down(side),
        halfMovilWidth+gapSimulation,
        0
    )

    #################
    femm.mi_drawline(
        -halfWidth,
        (halfHeight-barHeight)*up_down(side),
        -halfWidth+leftStatorGap,
        (halfHeight-barHeight)*up_down(side)
    )

    femm.mi_drawline(
        -halfWidth+leftStatorGap+bodyWidth+(2*(bodyWidth+innerStatorGap)),
        (halfHeight-barHeight)*up_down(side),
        halfWidth,
        (halfHeight-barHeight)*up_down(side),
    )

    ## Inner space arms
    for innersStatorSpace in range(2):
        femm.mi_drawline(
            -halfWidth+leftStatorGap+bodyWidth+(innersStatorSpace*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight)*up_down(side),
            -halfWidth+leftStatorGap+bodyWidth+innerStatorGap+(innersStatorSpace*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight)*up_down(side),
        )


    # Magnets and arms
    for iman in range(3):
        ## Arms
        femm.mi_drawline(
            -halfWidth+leftStatorGap+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight)*up_down(side),
            -halfWidth+leftStatorGap+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side)
        )
        femm.mi_drawline(
            -halfWidth+leftStatorGap+bodyWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
            -halfWidth+leftStatorGap+bodyWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight)*up_down(side),
        )

        femm.mi_drawline(
            -halfWidth+leftStatorGap+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
            -halfWidth+leftStatorGap-currentWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight-rampaHeight)*up_down(side),
        )
        femm.mi_drawline(
            -halfWidth+leftStatorGap-currentWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight-rampaHeight)*up_down(side),
            -halfWidth+leftStatorGap-currentWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfMiddleBarHeight+magnetHeight+1)*up_down(side)
        )
        ## Face Arm
        femm.mi_drawline(
            -halfWidth+leftStatorGap-currentWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfMiddleBarHeight+magnetHeight+1)*up_down(side),
            -halfWidth+leftStatorGap+bodyWidth+(currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfMiddleBarHeight+magnetHeight+1)*up_down(side)
        )
        femm.mi_drawline(
            -halfWidth+leftStatorGap+bodyWidth+(currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfMiddleBarHeight+magnetHeight+1)*up_down(side),
            -halfWidth+leftStatorGap+bodyWidth+(currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight-rampaHeight)*up_down(side),
        )

        femm.mi_drawline(
            -halfWidth+leftStatorGap+bodyWidth+(currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight-rampaHeight)*up_down(side),
            -halfWidth+leftStatorGap+bodyWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
        )

        ## Current
        femm.mi_drawline(
            -halfWidth+leftCurrentGap+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight)*up_down(side),
            -halfWidth+leftCurrentGap+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
        )

        femm.mi_drawline(
            -halfWidth+leftCurrentGap+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
            -halfWidth+leftCurrentGap+currentWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
        )

        current_x_label = -halfWidth+leftCurrentGap+(currentWidth/2)+(iman*(bodyWidth+innerStatorGap))
        current_y_label = (halfHeight-barHeight-(currentHeight/2))*up_down(side)

        femm.mi_addblocklabel(
            current_x_label,
            current_y_label
        )

        femm.mi_addcircprop(f"circuit_{side}_{iman}", 30, 1)

        femm.mi_selectlabel(
            current_x_label,
            current_y_label
        )
        femm.mi_setblockprop('Coil', 0, 1, f"circuit_{side}_{iman}", 0, 0, 500*up_down(side)*up_down(iman%2))
        femm.mi_clearselected()
        
        femm.mi_drawline(
            -halfWidth+leftCurrentGap+bodyWidth+(2*currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight)*up_down(side),
            -halfWidth+leftCurrentGap+bodyWidth+(2*currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
        )

        femm.mi_drawline(
            -halfWidth+leftCurrentGap+bodyWidth+(2*currentWidth)+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
            -halfWidth+leftCurrentGap+bodyWidth+currentWidth+(iman*(bodyWidth+innerStatorGap)),
            (halfHeight-barHeight-currentHeight)*up_down(side),
        )

        current_x_label = -halfWidth+leftCurrentGap+currentWidth+bodyWidth+(currentWidth/2)+(iman*(bodyWidth+innerStatorGap))
        current_y_label = (halfHeight-barHeight-(currentHeight/2))*up_down(side)

        femm.mi_addblocklabel(
            current_x_label,
            current_y_label
        )

        femm.mi_selectlabel(
            current_x_label,
            current_y_label
        )
        femm.mi_setblockprop('Coil', 0, 1, f"circuit_{side}_{iman}", 0, 0, -500*up_down(side)*up_down(iman%2))
        femm.mi_clearselected()

        ## Magnets  // MOVIL
        femm.mi_drawline(
            -halfMovilWidth+leftMagnetSpace+gapSimulation+(iman*(magnetWidth+innerMagnetSpace)),
            (halfMiddleBarHeight)*up_down(side),
            -halfMovilWidth+leftMagnetSpace+gapSimulation+(iman*(magnetWidth+innerMagnetSpace)),
            (halfMiddleBarHeight+magnetHeight)*up_down(side)
        )
        femm.mi_drawline(
            -halfMovilWidth+leftMagnetSpace+gapSimulation+(iman*(magnetWidth+innerMagnetSpace)),
            (halfMiddleBarHeight+magnetHeight)*up_down(side),
            -halfMovilWidth+leftMagnetSpace+gapSimulation+magnetWidth+(iman*(magnetWidth+innerMagnetSpace)),
            (halfMiddleBarHeight+magnetHeight)*up_down(side)
        )
        femm.mi_drawline(
            -halfMovilWidth+leftMagnetSpace+gapSimulation+magnetWidth+(iman*(magnetWidth+innerMagnetSpace)),
            (halfMiddleBarHeight+magnetHeight)*up_down(side),
            -halfMovilWidth+leftMagnetSpace+gapSimulation+magnetWidth+(iman*(magnetWidth+innerMagnetSpace)),
            (halfMiddleBarHeight)*up_down(side),
        )

        x_magnets_label = -halfMovilWidth+leftMagnetSpace+gapSimulation+(iman*(magnetWidth+innerMagnetSpace))+(magnetWidth/2)
        y_magnets_label = (halfMiddleBarHeight+(magnetHeight/2))*up_down(side)

        femm.mi_addblocklabel(x_magnets_label,y_magnets_label)

        femm.mi_selectlabel(x_magnets_label,y_magnets_label)
        femm.mi_setblockprop('Magnet', 0, 1, '<None>', 90*up_down(iman%2), 0, 0)
        femm.mi_clearselected()

femm.mi_makeABC()

### Añadiendo Materiales
#### Fijos

# Arms
x_label_arms = 0
y_label_arms = halfHeight-10
femm.mi_addblocklabel(x_label_arms,y_label_arms)

femm.mi_selectlabel(x_label_arms,y_label_arms)
femm.mi_setblockprop('Hiperco-50', 0, 1, '<None>', 0, 0, 0)
femm.mi_clearselected()

femm.mi_addblocklabel(x_label_arms,-y_label_arms)

femm.mi_selectlabel(x_label_arms,-y_label_arms)
femm.mi_setblockprop('Hiperco-50', 0, 1, '<None>', 0, 0, 0)
femm.mi_clearselected()

# Air
femm.mi_addblocklabel(0,halfHeight+10)

femm.mi_selectlabel(0,halfHeight+10)
femm.mi_setblockprop('Air', 0, 1, '<None>', 0, 0, 0)
femm.mi_clearselected()

#### Moviles
x_movil_bar_label = gapSimulation
femm.mi_addblocklabel(x_movil_bar_label,0)

femm.mi_selectlabel(x_movil_bar_label,0)
femm.mi_setblockprop('Hiperco-50', 0, 1, '<None>', 0, 0, 0)
femm.mi_clearselected()


femm.mi_saveas('auto-htutor.fem')

x = input()

