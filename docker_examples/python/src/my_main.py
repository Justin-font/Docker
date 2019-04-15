

lines =  open("in.txt").read().splitlines()
out = open("out.txt","w+")
out.write('dog : '+str(lines.count('dog'))+'\n')
out.write('cat : '+str(lines.count('cat')))
out.close()