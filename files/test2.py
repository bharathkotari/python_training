import xml.dom.minidom

def main():
	doc=xml.dom.minidom.parse("student.xml")
	print(doc.firstChild.tagName)
	print("*********************")
	hobbies=doc.getElementsByTagName("hobby")
	print("%d hobbies:"%hobbies.length)
	for activities in hobbies:
		print(activities.getAttribute("name"))
	newhobby=doc.createElement("hobby")
	newhobby.setAttribute("name","basketball")
	doc.firstChild.appendChild(newhobby)
	print(">>>>>>>>>>>>>>>>>>>>>>>")
	hobbies=doc.getElementsByTagName("hobby")
	print("%d hobbies:"%hobbies.length)
	for activities in hobbies:
		print(activities.getAttribute("name"))
	
main()