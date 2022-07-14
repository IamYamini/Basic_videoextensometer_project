import numpy as np
import cv2


btn_down = False

def get_points(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['lines'] = []

    # Set the callback function for any mouse event
    cv2.imshow("gray.jpg", im)
    cv2.setMouseCallback("gray.jpg", mouse_handle, data)
    cv2.waitKey(0)

    # Convert array to np.array in shape n,2,2
    points = np.uint16(data['lines'])

    return points, data['im']

def mouse_handle(event, x, y, flags, data):
    global btn_down

    if event == cv2.EVENT_RBUTTONUP and btn_down:
        #if you release the button, finish the line
        btn_down = False
        data['lines'][0].append((x, y)) #append the seconf point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255),5)
        cv2.line(data['im'], data['lines'][0][0], data['lines'][0][1], (0,0,255), 2)
        cv2.imshow("gray.jpg", data['im'])

    elif event == cv2.EVENT_MOUSEMOVE and btn_down:
        #thi is just for a ine visualization
        image = data['im'].copy()
        cv2.line(image, data['lines'][0][0], (x, y), (0,0,0), 1)
        cv2.imshow("gray.jpg", image)

    elif event == cv2.EVENT_RBUTTONDOWN and len(data['lines']) < 2:
        btn_down = True
        data['lines'].insert(0,[(x, y)]) #prepend the point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 5, 16)
        cv2.imshow("gray.jpg", data['im'])


# Running the code
img = cv2.imread('gray.jpg', 1)
pts, final_image = get_points(img)
cv2.imshow('gray.jpg', final_image)
print 
pts
cv2.waitKey(0)
