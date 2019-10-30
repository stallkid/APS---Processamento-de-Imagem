from PIL import Image, ImageFilter


#Classe para aplicar os filtros no dominio da imagem
class Filter():

    # Construtor da Classe
    def __init__(self, image, context):
        self.image = image
        self.context = context

    # Função para borrar a imagem
    def blur_image(self):
        imageObject = Image.open(self.image)
        blur = imageObject.filter(ImageFilter.BLUR)
        if self.context == "flora":
            blur.save("background/flora/filtered_flora-blur.jpg")
            blur.save("background/flora/filtered_flora.jpg")
        else:
            blur.save("background/fauna/filtered_fauna-blur.jpg")
            blur.save("background/fauna/filtered_fauna.jpg")

    # Função para realçar as bordas da imagem
    def edge_enhancement(self):
        imageObject = Image.open(self.image)
        edgeEnhanced = imageObject.filter(ImageFilter.EDGE_ENHANCE)

        if self.context == "flora":
            edgeEnhanced.save("background/flora/filtered_flora-edge_enhance.jpg")
            edgeEnhanced.save("background/flora/filtered_flora.jpg")
        else:
            edgeEnhanced.save("background/fauna/filtered_fauna-edge_enhance.jpg")
            edgeEnhanced.save("background/fauna/filtered_fauna.jpg")
        
        return edgeEnhanced

    # Função para realçar ainda mais as bordas da imagem
    def edge_enhancement_more(self):
        imageObject = Image.open(self.image)
        edgeEnhancedMore = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)

        if self.context == "flora":
            edgeEnhancedMore.save("background/flora/filtered_flora-edge_enhance_more.jpg")
            edgeEnhancedMore.save("background/flora/filtered_flora.jpg")
        else:
            edgeEnhanced.save("background/fauna/filtered_fauna-edge_enhance_more.jpg")
            edgeEnhanced.save("background/fauna/filtered_fauna.jpg")

        return edgeEnhancedMore
