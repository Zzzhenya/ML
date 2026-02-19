# None -> general null
# NaN -> numeric null
# empty 
# zero and false
# not empty

def NULL_not_found(object: any) -> int:
	# bool needs to be before int: python identify bools 
	# as both int and bool

	if not object:
		if (object is None):
			print("Nothing :", object , type(object))
		elif (isinstance(object, bool) and (object == False)):
			print("Fake :", object , type(object))
		elif (object == 0): #isinstance(object,int) and (
			print("Zero :", object , type(object))
		elif (hasattr(object, "__len__")  and len(object) == 0):
			print("Empty :", object , type(object))
		else:
			print("Type not found")
			return (1)
	else:
		if (isinstance(object, float) and (object != object)):
			print("Cheese :", object , type(object))
		else:
			print("Type not found")
			return (1)
	return(0)


