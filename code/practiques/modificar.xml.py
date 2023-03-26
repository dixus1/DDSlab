import xml.etree.ElementTree as ET

# Abrir el archivo XML
tree = ET.parse("./latest.qkdb.xml")
root = tree.getroot()

# Buscar todos los elementos <VULN> en el archivo XML
vuln_elems = root.findall(".//VULN")

# Recorrer todos los elementos <VULN>
for vuln_elem in vuln_elems:
    # Verificar si existe un elemento <TITLE> en el elemento <VULN>
    title_elem = vuln_elem.find("DIAGNOSIS")# Buscar todos los elementos VULN en el árbol

    if title_elem is None:
     # Si no existe, crear un nuevo elemento TITLE y agregarlo al elemento raíz
     title_elem = ET.Element("DIAGNOSIS")
     title_elem.text = "diagnosis"
     vuln_elem.append(title_elem)


    title_elem = vuln_elem.find("CONSEQUENCE")
    if title_elem is None:
        #Si no exite, crear un nuevo elemnto CONSEQUENCE y agregarlo al elemento raiz
        title_elem = ET.Element("CONSEQUENCE")
        title_elem.text = "consequence"
        vuln_elem.append(title_elem)


    title_elem = vuln_elem.find("SOLUTION")
    if title_elem is None:
        #Si no exite, crear un nuevo elemnto SOLUTION y agregarlo al elemento raiz
        title_elem = ET.Element("SOLUTION")
        title_elem.text = "solution"
        vuln_elem.append(title_elem)


# Guardar los cambios en el archivo XML
tree.write("./latest.qkdb.out.xml")

