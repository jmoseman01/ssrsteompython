from decimal import Decimal
def allcheck(array):
	num = 1
	length=len(array)
	indexs=range(length-1)
	for index in indexs:
		if array[index] == array[index+1]:
			num += 1
	if num == length:
		return False
	else:
		return True


def lambdax(lambdax,start,end,deltax):
	array=[]
	num = start
	while num <= end:
		y = lambdax
		#print y
		output=y(num)
		#print num
		#print output
		if type(output) != type(Decimal(".5")):
			array.append(Decimal(`output`))
		else:
			array.append(output)
		num+=deltax
	return array
#tel (terminating entitiy level)
#teln (terminating entity level number)
#e1 = output ploynomial array
def tegen(d,deltax):
	te=Decimal("1")
	for i in range(1,d+1):
		te*=deltax*i
	return te

#from math import factorial
class ssrsteom:

	def __init__(self, e1,start=Decimal("1"),deltax=Decimal("1")):
		self.deltax=deltax
		self.start=start
		
		current=[]
		self.e1 = e1
		#counter = prev
		counter = 1
		if allcheck(e1) == False:
			self.degree = 0

		exec("prevlayer="+"e"+`counter`)
		while allcheck(current) and allcheck(prevlayer):
		#prev layer
			exec("prevlayer="+"e"+`counter`)
		#current layer
			exec("current="+"e"+`counter+1`+"=[]")
		#enum list of prev
			
			prevlengthlist=range(len(prevlayer))
			prevlengthlist.reverse()
		#generate entitiy level + 1 of last	
			
			for z in prevlengthlist:
				if z <> 0:
					current.append(prevlayer[z]-prevlayer[z-1])
			current.reverse()
			exec("self.e"+`counter+1`+"=current")
			if allcheck(current)==False:
				self.degree = counter
			counter += 1
		#counter = entity level
		
		self.teln=counter
		self.tel='e'+`counter`
		#termination entity degree factorial	
		self.tef=tegen(self.degree,self.deltax)
		#termination entity degree*c lastnumber
		exec("self.te=self.e"+`self.teln`+"[0]")
		self.highc=self.te/self.tef
		self.tcn=self.degree
		exec("self.c"+`self.degree`+"=self.highc")
		self.highcfuncstr=`self.highc`+"*x**"+`self.tcn`
		self.mca=self.degree+1
		self.highsen=self.degree
		elist=[]
		for enum in range(1,self.teln+1):
			exec("appendlist=self.e"+`enum`)
			elist.append(appendlist)
		self.elist=elist
		#### highc object se(self.degree) #####
		#self.chighfunctionstr=`self.highc`+"*x**"+`self.tcn`
		#exec("highse=ssrsteom(lambdax(lambda x:"+self.chighfunctionstr+",self.degree+1))")
		#exec("self.se"+`self.degree`+"=highse")
		#self.highse=highse
#############################################################################################################################################3
	def printalle(self):
		for x in range(1, self.teln + 1):
			print "e"+`x`
			exec("print self.e"+`x`)
	def printalleq(self):
		for x in range(1, self.teln + 1):
			exec("print self.e"+`x`)
	
	def printall(self):
		self.printalle()
		print "degree = " + `self.degree`
		print "terminating entity level = "+`self.tel`
		print "termination entity = "+ `self.te`
		print "termination enitiy of degree = "+`self.tef`
		print "highc = "+`self.highc`
		print "min consistor amount = " + `self.mca`
		print "starting x value = "+`self.start`
		print "deltax = "+`self.deltax`
	def gen_highse(self):
		self.highcfuncstr=`self.highc`+"*x**"+`self.tcn`
		print self.highcfuncstr,self.mca,self.start
		exec("highse=ssrsteom(lambdax(lambda x:"+self.highcfuncstr+",self.start,self.mca,self.deltax),self.start,self.deltax)")
		exec("self.se"+`self.degree`+"=highse")
		self.highse=highse
		return highse
	def __add__(self,idk1):
		for foo in range(idk1):
			lastterms=[]
			appendnum=0
			for x in range(1,self.degree+2):
				exec("lastterms.append(self.e"+`x`+"[-1])")
			for terms in lastterms:
				appendnum+=terms
			self.e1.append(appendnum)
			self.__init__(self.e1,self.start,self.deltax)
	
	def __sub__(self,idk2):
		import sys
		if type(idk2) == type(1):
			if len(self.e1)-idk2 >= self.mca:		
				#for foo in range(idk2):
				self.e1[-idk2:]=[]
				self.__init__(self.e1,self.start,self.deltax)
			else:
				sys.stderr.write('operation not permitted;\n\t length of e1 must be maintained to perserve degree of ssrsteom object\n')
		elif type(self) == type(idk2):
			if len(self.e1)>len(idk2.e1):
				idk2 + (len(self.e1)-len(idk2.e1))
			elif len(idk2.e1)>len(self.e1):
				self + (len(idk2.e1)-len(self.e1))
			else:
				pass

			if self.teln <= idk2.teln:
				num = self.teln
			elif self.teln > idk2.teln:
				num = idk2.teln
			while num >= 1:
				exec("currente=self.e"+`num`)
				exec("currentidk2e=idk2.e"+`num`)
				for z in range(len(currente)):
					currente[z]=currente[z] - currentidk2e[z]
				num-=1
			self.__init__(self.e1,self.start,self.deltax)
			return self
	def gen_sa(self,index=0):
		import sys
		import copy
		if len(self.e1) >= index+self.mca:
			self.sa=ssrsteom(self.e1[index:index+self.mca],self.start,self.deltax)
			return self.sa
		else:
			self.sa=copy.deepcopy(self)
			if index<len(self.sa.e1):
				covalent = len(self.sa.e1)-index
				self.sa.__add__(self.sa.mca-covalent)
				self.sa.__init__(self.sa.e1[index:],self.start,self.deltax)
			else:
				gap=index-len(self.sa.e1)
				self.sa.__add__(self.sa.mca+gap)
				self.sa.__init__(self.sa.e1[index:],self.start,self.deltax)
			return self.sa
	def solve(self):
		import copy
		str1="x"
		self.running=copy.deepcopy(self)
		self.gen_sa().printall()
		print "\n\n"
		self.gen_highse().gen_sa().printall()
		for h in range(1,self.degree+1)[::-1]:
		
			print "\n\n"
			self.running - self.running.gen_highse()
			exec("self.c"+`self.running.teln-1`+"=self.running.highc")
			if self.running.printall()<>None:
				print self.running.gen_sa().printall()
			if self.running.teln == 1:
				break
			
		#grab constant
		str1=""
		for z in range(1,self.degree+1):
			try:
				exec("cvar=self.c"+`z`)
			except AttributeError:
				cvar=0
			if z != self.degree:
				str1+=`cvar`+"*x**"+`z`+"+"
			else:
				str1+=`cvar`+"*x**"+`z`
			
		print "function is "+str1
		exec"func=lambda x: "+str1
		self.c0=self.e1[0]-func(self.start)



		for x in range(1,self.degree+1):
			print "c"+`x`
			try:
				exec("print self.c"+`x`)
			except AttributeError:
				exec("self.c"+`x`+"=0")
				exec("print self.c"+`x`)
		d=self.degree
		r=range(1,d+1)
		r.reverse()
		u=self.degree
		ostr=""
		while u >= 0:
			exec("cnum="+"self.c"+`u`)
			ostr+=`cnum`+"x^"+`u`+"+"
			u-=1

		#ostr=ostr.replace("L","")
		for o in r:
			ostr=ostr.replace("+0x^"+`o`,"")
		ostr=ostr.replace("^1","")
		ostr=ostr.replace("x^0","")
		ostr=ostr.replace("1x","x")
		ostr=ostr.replace("0x+","")
		ostr=ostr.replace("+0","")
		ostr=ostr.replace("Decimal('","")
		ostr=ostr.replace("')","")
		print ostr[:-1]
		return ostr[:-1]
