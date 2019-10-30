import cv2

# Classes utilizadas
import flora
import fauna

# Função main do projeto
def main():
    # Tratamento de Erros
    try:
        # Executa a lógica da flora
        Flora = flora.Flora_Filter("images/person1.jpeg")
        flora_img = Flora.Removing_Background()
        # Executa a lógica da fauna
        Fauna = fauna.Fauna_Filter("images/person1.jpeg")
        fauna_img = Fauna.Removing_Background()

        #Salva o resultado das operações neste path
        cv2.imwrite("result/flora-result.jpg", flora_img)
        cv2.imwrite("result/fauna-result.jpg", fauna_img)

        # Indica que não houve erro
        print("Imagens salvas na pasta \"result\" com sucesso!")
    except:
        # Indica que houve um erro na operação
        print("Houve um erro durante a execução")

if __name__ == "__main__":
    main()