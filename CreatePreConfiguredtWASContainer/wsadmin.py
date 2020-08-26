#Create Username and Password
#AdminTask.createAuthDataEntry('[-alias PlantsAuthAlias -user db2inst1 -password db2Pa2359w0rd123 -description db2Passw0rd!123 ]')
AdminTask.createAuthDataEntry('[-alias mysqlDb -user root -password password]')
#Create JDBC Providers
#DB2JDBC=AdminTask.createJDBCProvider('[-scope Cell=DefaultCell01 -databaseType DB2 -providerType "DB2 Universal JDBC Driver Provider" -implementationType "Connection pool data source" -name "DB2 Universal JDBC Driver Provider" -classpath [/demo/db2drivers/db2jcc.jar /demo/db2drivers/db2jcc_license_cu.jar ] -nativePath [${DB2UNIVERSAL_JDBC_DRIVER_NATIVEPATH} ] ]')
#DB2JDBCXA=AdminTask.createJDBCProvider('[-scope Cell=DefaultCell01 -databaseType DB2 -providerType "DB2 Universal JDBC Driver Provider" -implementationType "XA data source" -name "DB2 Universal JDBC Driver Provider (XA)" -classpath [/demo/db2drivers/db2jcc.jar /demo/db2drivers/db2jcc_license_cu.jar ] -nativePath [${DB2UNIVERSAL_JDBC_DRIVER_NATIVEPATH} ] ]')
AdminTask.createJDBCProvider('[-scope Node=DefaultNode01 -databaseType User-defined -providerType "User-defined JDBC Provider" -implementationType User-defined -name "MYSQL JDBC Provider" -description "Custom JDBC2.0-compliant Provider configuration" -classpath [/demo/mysqldrivers/mysql-connector-java-8.0.21.jar ] -nativePath "" -implementationClassName com.mysql.cj.jdbc.MysqlConnectionPoolDataSource ]')
#Create Datasources
#AdminTask.createDatasource(DB2JDBCXA, '[-name PlantsByWebSphereDataSource -jndiName jdbc/PlantsByWebSphereDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/PlantsAuthAlias -xaRecoveryAuthAlias DefaultNode01/PlantsAuthAlias -configureResourceProperties [[databaseName java.lang.String PLANTSDB] [driverType java.lang.Integer 4] [serverName java.lang.String 169.62.104.36] [portNumber java.lang.Integer 32612]]]')
#AdminTask.createDatasource(DB2JDBC, '[-name PlantsByWebSphereDataSourceNONJTA -jndiName jdbc/PlantsByWebSphereDataSourceNONJTA -dataStoreHelperClassName com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/PlantsAuthAlias -configureResourceProperties [[databaseName java.lang.String PLANTSDB] [driverType java.lang.Integer 4] [serverName java.lang.String 169.62.104.36] [portNumber java.lang.Integer 32612]]]')
AdminTask.createDatasource('[-name MySQLDataSource -jndiName jdbc/mysqlds -dataStoreHelperClassName com.ibm.websphere.rsadapter.GenericDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/mysqlDb ]')


AdminConfig.modify('[[name "serverName"] [type "java.lang.String"] [description ""] [value "10.242.0.6"] [required "false"]]')
AdminConfig.modify('[[name "portNumber"] [type "java.lang.Integer"] [description ""] [value "6603"] [required "false"]]')
AdminConfig.modify('[[name "databaseName"] [type "java.lang.String"] [description ""] [value "cargotracker"] [required "false"]]')
AdminConfig.modify('[[name "user"] [type "java.lang.String"] [description ""] [value "root"] [required "false"]]')
AdminConfig.modify('[[name "password"] [type "java.lang.String"] [description ""] [value "password"] [required "false"]]')

#Change JPA from 2.1 to 2.0
svr = AdminConfig.getid('/Server:server1/')
AdminTask.modifyJPASpecLevel(svr, '[ -specLevel 2.0]')
#Install Application
#AdminApp.install('/demo/HelloWorld.war', '[ -appname HelloWorld -contextroot /HelloWorld]')
#AdminApp.install('/demo/pbw-ear7.ear', '[ -appname PlantsByWebSphere7 -contextroot /PlantsByWebSphere7]')
#AdminApp.install('/demo/pbw-ear8.ear', '[ -appname PlantsByWebSphere8 -contextroot /PlantsByWebSphere8]')
AdminApp.install('/demo/cargotracker-1.0.war', '[ -appname cargotracker -contextroot /cargotracker]')
#Uninstall default WAS applications
#AdminApp.uninstall('DefaultApplication')
AdminApp.uninstall('query')
#AdminApp.uninstall('ivtApp')
AdminConfig.save()
