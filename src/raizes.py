def bhaskara(a, b, c):
    """
    Computa a(s) raíz(es) de um polinômio de segundo grau
    usando a fórmula de bhaskara:

    (-b ± √b² - 4ac) / (2a)
    """
    delta = (b ** 2) - 4 * a * c

    if a == 0:
        print("O valor de a, deve ser diferente de 0")
    elif delta < 0:
        print("Sem raízes reais")
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a) 
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print(f"x1: {x1}, x2: {x2}")




def formatarComplexResult(realPart, imPart):
	#um caso simples
	if (realPart == 0 and imPart == 0):
		return "0"
	number = ""
	if (realPart != 0):
		number += str(realPart)
	if (imPart > 0):
		number += "+" + str(imPart) + "i"
	elif (imPart < 0):
		number += str(imPart) + "i"
	else:
		number += str(imPart) + "i"    
	return number


#Computa a(s) raíz(es) de um polinômio de terceiro grau usando o método de Tartaglia-Cardano:
def cardano(a,b,c,d):	
import numpy as np
  if a == 0:
    print("O valor de a, deve ser diferente de 0")
  else:
    #converte a equação para forma x^3+Ax^2+Bx+C=0
    A = b / a
    B = c / a
    C = d / a

		#constantes da conversão para y^3+py+q=0
    p = B - A * A / 3
    q = C + 2 * A * A * A / 27 - A * B / 3
		
		#discriminante
    delta = q * q / 4.0 + p * p * p / 27.0
		
    if (delta >= 0): #primeira raiz
		
      y1 = np.cbrt(-q / 2 + np.sqrt(delta)) + np.cbrt(-q / 2 - np.sqrt(delta))
      roots.append( str([(y1 - A / 3)]) ) #primeira raiz
      delta2 = -3 * y1 * y1 - 4 * p
      if (delta2 >= 0):
        roots.append( str(-y1 + np.sqrt(delta2)) / 2 - A / 3) #segunda raiz
        roots.append( str(-y1 - np.sqrt(delta2)) / 2 - A / 3) #terceira raiz
      else:
        #raízes complexas
        realPart = -y1 / 2
        imPart = np.sqrt(np.abs(delta2)) / 2
        roots.append( formatarComplexResult(realPart - A / 3, imPart) )
        roots.append( formatarComplexResult(realPart - A / 3, -imPart) )
    else:
      rho = np.sqrt(q * q / 4 + np.abs(delta))
      theta = math.acos(-q / (2 * rho))
      roots.append( str(2 * Math.cbrt(rho) * Math.cos(theta / 3) - A / 3) )
      roots.append( str(2 * Math.cbrt(rho) * Math.cos((theta + 2 * Math.PI) / 3) - A / 3) )
      roots.append( str(2 * Math.cbrt(rho) * Math.cos((theta + 4 * Math.PI) / 3) - A / 3) )

