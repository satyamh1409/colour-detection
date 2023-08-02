
import cv2
import pandas as pd

image_path = r'color2.jpg'
image = cv2.imread(image_path)

clicked = False 
red = green = blue = x_axis = y_axis = 0   

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname



def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global blue, green, red, x_axis, y_axis, clicked
        clicked = True
        x_axis = x
        y_axis = y
        blue, green, red = image[y, x]
        blue = int(blue)
        green = int(green)
        red = int(red)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

    cv2.imshow("image", image)
    if clicked:

        cv2.rectangle(image, (20, 20), (750, 60), (blue, green, red), -1)

        text = get_color_name(red, green, blue) + ' R=' + str(red) + ' G=' + str(green) + ' B=' + str(blue)

        cv2.putText(image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if red + green + blue >= 600:
            cv2.putText(image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

   
    if cv2.waitKey(20) & 0xFF == 27:
        break


cv2.destroyAllWindows()