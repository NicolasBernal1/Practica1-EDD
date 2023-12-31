from heapq import *
from random import *
from time import *
    


class Solicitud:
    def __init__(self,num_solicitud, nombre, descripcion,urgencia):
        self.num_solicitud = num_solicitud
        self.nombre = nombre
        self.descripcion = descripcion
        self.urgencia = urgencia 
        self.solicitudes = PriorityQueue()
    
    def __lt__(self,other):
        return self.urgencia < other.urgencia

    def __repr__(self):
        return self.nombre

class PriorityQueue:
    def __init__(self):
        self.pq = []
        
    
    def Solicitar(self,numero_sol,nombre:str,descripcion,urgencia:int):
        s = Solicitud(numero_sol,nombre,descripcion,urgencia)
        heappush(self.pq,(s.urgencia,s))
    
    def Solicitar_lote(self,list): #2
        for elm in list:
            heappush(self.pq,(elm[0].urgencia,elm))
        

    def Atender_lote(self): #3
        if len(self.pq) == 0:
            print("No hay solicitudes")
        else:
            atendido = heappop(self.pq)
            print(f"Clientes {atendido[1]}, de prioridad {atendido[0]}")  

    def Atender(self):
        if len(self.pq) == 0:
            print("No hay solicitudes")
        else:
            atendido = heappop(self.pq)
            print(f"Cliente {atendido[1]}, de prioridad {atendido[0]}, con problema: {atendido[1].descripcion}")
    
    def Mostrar_solicitudes(self):
        order = sorted(self.pq)
        cont = 0
        for sol in order:
            cont += 1
            print(f"{cont}: {sol}")

    def Actualizar_prioridad(self,sol_num,new_prio):
        for i in self.pq:
            if i[1].num_solicitud == sol_num:
                temp = i[1]
                self.pq.remove(i)
                heapify(self.pq)
                temp.urgencia = new_prio
                new_val = (new_prio,temp)
                heappush(self.pq,new_val)
                break
        print("No se tiene la solicitud")
    
    def Hacer_lotes(self): #1
        lotes = []
        dic = {}
        temp = sorted(self.pq)
        for elm in temp:
            if elm[0] not in dic.keys():
                dic[elm[0]] = [elm[1]]
            else:
                dic[elm[0]].append(elm[1])
        
        for i in dic.keys():
            lotes.append(dic[i])
        for i in range(len(lotes)):
            lotes[i] = sorted(lotes[i])
        

        self.pq = []
        #lotes en PQA
        pq2 = PriorityQueueAlphabetic()
        self.Solicitar_lote(pq2.Organize(lotes))
        
class PriorityQueueAlphabetic:
    def __init__(self):
        self.pq = []
    
    def Organize(self,list):
        def nomb(sol):
            return sol.nombre
        for i in range(len(list)):
            list[i] = sorted(list[i],key=nomb)
        
        return list


            



def Menu():
    PriorQ = PriorityQueue()
    while True:
        print("="*25)
        print("Menú reportes")
        print("1. Solicitar")
        print("2. Atender")
        print("3. Mostrar solicitudes")
        print("4. Actualizar prioridad")
        print("5. Solicitar con archivo")
        print("S: Salir")
        print("="*25)
        res = input("-->")  
        res = res.lower()
        if res == "s":
            break

        if res == "1":
            name = input("Nombre del cliente: ")
            desc = input("Decripción del problema: ")
            try:
                nivel_urg = int(input("Nivel de urgencia: "))
                num_sol = int(input("Numero de solicitud: "))
            except:
                print("El nivel de urgencia y numero de solicitud deben ser un enteros")
                continue
            PriorQ.Solicitar(num_sol,name,desc,nivel_urg)
        
        elif res == "2":
            PriorQ.Atender()

        elif res == "3":
            if len(PriorQ.pq) == 0:
                print("No hay solicitudes")
            else:
                PriorQ.Mostrar_solicitudes()
        
        elif res == "4":
            try:
                sol_num = int(input("Numero de la solicitud: "))
                new_urg = int(input("Nuevo nivel de urgencia: "))
            except:
                print("El numero de solicitud y nivel de urgencia deben ser enteros")
                continue
            PriorQ.Actualizar_prioridad(sol_num,new_urg)
        
        #“número de solicitud, nombre de cliente, descripción del problema, nivel de urgencia”
        elif res == "5":
            try:
                archivo = input("Nombre del archivo: ")
            except:
                print("Archivo no encontrado") 
                continue
            soli_list = []
            with open(archivo,"r") as file:
                for line in file:
                    line = line.replace("\n","")
                    line = line.split(",")
                    for idx in range(len(line)):
                        line[idx] = line[idx].lstrip()
                    soli_list.append(line)

            for soli in soli_list:
                numero_sol = int(soli[0])
                nomb = soli[1]
                prob = soli[2]
                urg = int(soli[3])
                PriorQ.Solicitar(numero_sol,nomb,prob,urg)
                
        else:
            print("Opcion invalida")


def Escenarios():
    prior = PriorityQueue()
    urg = randint(1,9)
    prior.Solicitar(1,"a","b",urg)
    #prior.Mostrar_solicitudes()
   
t1 = time()
for i in range(0):
    Escenarios()

t2 = time()

print(t2-t1)

#Menu()      

pq = PriorityQueue()
pq.Solicitar(1,"h","x",0)
pq.Solicitar(2,"g","x",1)
pq.Solicitar(3,"f","x",1)
pq.Solicitar(4,"e","x",2)
pq.Solicitar(5,"d","x",0)
pq.Solicitar(6,"c","x",1)
pq.Solicitar(7,"b","x",1)
pq.Solicitar(8,"a","x",2)

pq.Hacer_lotes()
pq.Mostrar_solicitudes()
pq.Atender_lote()
pq.Mostrar_solicitudes()









    
