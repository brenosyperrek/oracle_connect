import oracledb

oracledb.init_oracle_client(lib_dir="/opt/oracle/instantclient_23_26")  # Carregando Oracle Instan Client

def connect_to_oracle(host, port, service_name, db_user, db_password):
    try:
        dsn = f"{host}:{port}/{service_name}"  # TCP
        
        print("Conectando ao banco de dados Oracle...")

        conn = oracledb.connect(
        user=db_user,
        password=db_password,
        dsn=dsn)
    
        print("Conexão bem-sucedida!")
    
        return conn
    except oracledb.Error as e:
        print(f"Erro ao conectar ao banco de dados Oracle:{e}")
        raise
    
connect_to_oracle("oracle1", 1521, "mat1prd", "SISFOSSA_ESR_SERVICE", "HR50$Mko1#")   