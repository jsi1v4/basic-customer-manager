#By jose silva
# modules
import mysql.connector
import tabulate

# variable global
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'TesteBack',
}

# functions
def returnTable(fields, result):
    table = tabulate.tabulate(result, headers=fields, tablefmt='orgtbl')
    print("\n" + table)

def execQry(sql):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql)
        fields = [i[0] for i in cursor.description]
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        returnTable(fields, result)
    except mysql.connector.Error as err:
        print("\nErro: {}".format(err))

def execQrySubTt(sql1, sql2, subTt):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql1)
        fields = [i[0] for i in cursor.description]
        result = cursor.fetchall()
        cursor.execute(sql2)
        result1 = cursor.fetchall()
        cursor.close()
        conn.close()

        rowEmpty = ['-----', '-----', '-----', '-----', '-----']
        rowSubTt = [subTt] + ['', '', ''] + [i[0] for i in result1]

        result.append(rowEmpty)
        result.append(rowSubTt)
        returnTable(fields, result)
    except mysql.connector.Error as err:
        print("\nErro: {}".format(err))

def execQryCtrl(sql):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print("done...")
    except mysql.connector.Error as err:
        print("\nErro: {}".format(err))


# Table's
def tableAll():
    sql = ("SELECT " +
           "id_customer AS ID, " +
           "nm_customer AS NOME, " +
           "cpf_cnpj AS 'CPF/CNPJ', " +
           "is_active AS 'ATIVO?', " +
           "vl_total AS 'VL TOTAL' " +
           "FROM " +
           "tb_customer_account " +
           "ORDER BY " +
           "id_customer " +
           "ASC")
    execQry(sql)

def tableByName(name):
    sql = ("SELECT " +
           "id_customer AS ID, " +
           "nm_customer AS NOME, " +
           "cpf_cnpj AS 'CPF/CNPJ', " +
           "is_active AS 'ATIVO?', " +
           "vl_total AS 'VL TOTAL' " +
           "FROM " +
           "tb_customer_account " +
           "WHERE nm_customer = '" + name + "'")
    execQry(sql)

def tableByCpf(cpf):
    sql = ("SELECT " +
           "id_customer AS ID, " +
           "nm_customer AS NOME, " +
           "cpf_cnpj AS 'CPF/CNPJ', " +
           "is_active AS 'ATIVO?', " +
           "vl_total AS 'VL TOTAL' " +
           "FROM " +
           "tb_customer_account " +
           "WHERE cpf_cnpj = " + cpf + "")
    execQry(sql)

def insertTable(nome, cpf, isActive, vlTotal):
    sql = ("INSERT INTO " +
           "tb_customer_account " +
           "(" +
           "nm_customer, " +
           "cpf_cnpj, " +
           "is_active, " +
           "vl_total" +
           ") VALUES ('" +
           nome + "', " +
           cpf + ", " +
           isActive + ", " +
           vlTotal + "" +
           ")")
    execQryCtrl(sql)

def deleteByID(sID):
    sql = ("DELETE FROM " +
           "tb_customer_account " +
           "WHERE " +
           "id_customer = " +
           sID + "")
    execQryCtrl(sql)

def editByID(sID, nome, cpf, isActive, vlTotal):
    sql = ("UPDATE " +
           "tb_customer_account " +
           "SET " +
           nome + "', " +
           cpf + ", " +
           isActive + ", " +
           vlTotal + " " +
           "WHERE " +
           "id_customer = " +
           sID + "")
    execQryCtrl(sql)


#Operations
def tableSUM(arg1, arg2, arg3):
    if (not arg3):
        arg3 = '>= 0'
    else:
        arg3 = '> ' + arg3

    sql = ("SELECT * " +
           "FROM tb_customer_account " +
           "WHERE " +
           "vl_total " +
           arg3 + " " +
           "AND " +
           "id_customer " +
           "BETWEEN " +
           arg1 + " " +
           "AND " +
           arg2 + " " +
           "ORDER BY " +
           "vl_total " +
           "DESC")

    sqlTt = ("SELECT " +
           "SUM(vl_total) " +
           "FROM tb_customer_account " +
           "WHERE " +
           "vl_total " +
           arg3 + " " +
           "AND " +
           "id_customer " +
           "BETWEEN " +
           arg1 + " " +
           "AND " +
           arg2 + "")

    execQrySubTt(sql, sqlTt, 'Soma')

def tableAVG(arg1, arg2, arg3):
    if (not arg3):
        arg3 = '>= 0'
    else:
        arg3 = '> ' + arg3

    sql = ("SELECT * " +
           "FROM tb_customer_account " +
           "WHERE " +
           "vl_total " +
           arg3 + " " +
           "AND " +
           "id_customer " +
           "BETWEEN " +
           arg1 + " " +
           "AND " +
           arg2 + " " +
           "ORDER BY " +
           "vl_total " +
           "DESC")

    sqlTt = ("SELECT " +
           "AVG(vl_total) " +
           "FROM tb_customer_account " +
           "WHERE " +
           "vl_total " +
           arg3 + " " +
           "AND " +
           "id_customer " +
           "BETWEEN " +
           arg1 + " " +
           "AND " +
           arg2 + "")

    execQrySubTt(sql, sqlTt, 'Media')