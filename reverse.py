def reverse(s):
	list = []	
	string = ''
	i = 0
	j = -1
	while i < len(s):
		list.append(s[j])
		i = i + 1
		j = j - 1
	return string.join(list)
print reverse("hello")
print reverse("abcdefghijklmnopqrstuvwxyz")
