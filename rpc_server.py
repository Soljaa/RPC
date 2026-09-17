import rpyc
import time
import pickle


class MyService(rpyc.Service):

    exposed_the_real_answer_though = 43

    def on_connect(self, conn):
        pass 

    def on_disconnect(self, conn):
        pass

    def exposed_test_connection(self):
        return True
    
    def exposed_get_answer(self):
        return 42 

    def exposed_array_sum(self, data_payload):
        start = time.time()
        array_local = pickle.loads(data_payload)
        resultado = sum(array_local)
        
        end = time.time()
        
        print(end-start)

        return resultado

    def get_question(self):
        return "Qual é  a cor do cavalo branco de Napoleão?"
    

    
if __name__ == "__main__": 
    from rpyc.utils.server import ThreadedServer 
    t = ThreadedServer(MyService, port=18861) 
    t.start()