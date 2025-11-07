import cv2 as cv
import numpy as np
import random as rng
import matplotlib.pyplot as plt

rng.seed(12345)

def find_and_draw_hull(src_gray, threshold):
    """
    Encontra o Canny e depois calcula e desenha os contornos e o fecho convexo.
    """
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    hull_list = []
    for i in range(len(contours)):
        hull = cv.convexHull(contours[i])
        hull_list.append(hull)
        
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        # Desenha os contornos
        cv.drawContours(drawing, contours, i, color)
        # Desenha o fecho convexo
        cv.drawContours(drawing, hull_list, i, color)
        
    return drawing

# --- Início da Execução Principal ---

image_path = 'pucminas.jpg'
src = cv.imread(image_path)

if src is None:
    print('Could not open or find the image:', image_path)
else:
    # --- Processamento da Imagem ---
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    src_gray = cv.blur(src_gray, (3,3))

    thresh = 100 
    
    # Gera a imagem com o fecho convexo
    processed_image = find_and_draw_hull(src_gray, thresh) 

    # Salva a imagem processada (fundo preto)
    output_filename = 'processed_hull_image.png'
    cv.imwrite(output_filename, processed_image)
    print(f"Imagem processada salva em: {output_filename}")

    # --- Exibição com Matplotlib (estilo questao1.py) ---
    
    # Cria a figura e os eixos (1 linha, 2 colunas)
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))

    # 1. Imagem Original
    # Converte de BGR (OpenCV) para RGB (Matplotlib)
    src_rgb = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    axes[0].imshow(src_rgb)
    axes[0].set_title("Imagem Original (pucminas.jpg)")
    axes[0].axis('off')

    # 2. Imagem Processada (Fecho Convexo)
    # Converte de BGR (OpenCV) para RGB (Matplotlib)
    processed_rgb = cv.cvtColor(processed_image, cv.COLOR_BGR2RGB)
    axes[1].imshow(processed_rgb)
    axes[1].set_title("Fecho Convexo (Convex Hull)")
    axes[1].axis('off')

    plt.tight_layout()
    
    # Salva a imagem de comparação
    comparison_filename = "comparison_image.png"
    plt.savefig(comparison_filename)
    print(f"Imagem de comparação salva em: {comparison_filename}")

    # Mostra o resultado
    plt.show()