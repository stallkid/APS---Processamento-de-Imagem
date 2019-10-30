import cv2
import numpy as np
import util.resize as rs
import util.filter as fr
import skimage
from PIL import Image, ImageFilter

# Definição da classe Flora
class Flora_Filter():
    # Construtor da clase Flora
    def __init__(self, input_img):
        #Imagem a ser passada na instancia da classe
        self.input_img = input_img
        #Propriedades da remoção do fundo
        self.BLUR = 21
        self.CANNY_THRESH_1 = 10
        self.CANNY_THRESH_2 = 200
        self.MASK_DILATE_ITER = 10
        self.MASK_ERODE_ITER = 10

    def Removing_Background(self):
        # Leitura da Imagem
        img = cv2.imread(self.input_img)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Detecção de Borda
        edges = cv2.Canny(gray, self.CANNY_THRESH_1, self.CANNY_THRESH_2)
        edges = cv2.dilate(edges, None)
        edges = cv2.erode(edges, None)

        # Encontrar Contorno nas Bordas
        contour_info = []
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        for c in contours:
            contour_info.append((
                c,
                cv2.isContourConvex(c),
                cv2.contourArea(c),
            ))
        contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
        max_contour = contour_info[0]

        # Mascara Preta, Poligono branco
        mask = np.zeros(edges.shape)
        cv2.fillConvexPoly(mask, max_contour[0], (255))

        # Suavizar a Mascara e borrar
        mask = cv2.dilate(mask, None, iterations=self.MASK_DILATE_ITER)
        mask = cv2.erode(mask, None, iterations=self.MASK_ERODE_ITER)
        mask = cv2.GaussianBlur(mask, (self.BLUR, self.BLUR), 0)
        mask_stack = np.dstack([mask]*3)

        
        mask_stack  = mask_stack.astype('float32') / 255.0          # Matriz Float, 
        img         = img.astype('float32') / 255.0                 # Para aplicar Blend facilmente

        # Aplica filtro de realce das Bordas do Background de flora
        flora_filter = fr.Filter("background/flora/flora.jpg", "flora")
        flora_filter.edge_enhancement()

        # Redimensiona Background
        rs_util = rs.Resize("background/flora/filtered_flora.jpg", self.input_img, "flora")
        bg_resized = skimage.img_as_float(rs_util.resize_image())

        # Une a Mascara ao Background
        masked = (mask_stack * img) + ((1-mask_stack) * bg_resized) # Blend
        masked = (masked * 255).astype('uint8')

        return masked
