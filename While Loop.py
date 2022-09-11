# Prints all letters except 'e' and 'o'
i = 0
a = 'Penecontemporaneous' # Penecontemporaneous: of, relating to, or being a geological phenomenon originating or effectuated during or soon after the formation of the rocks in which it is displayed

while i < len(a):
    if a[i] == 'e' or a[i] == 'o':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1