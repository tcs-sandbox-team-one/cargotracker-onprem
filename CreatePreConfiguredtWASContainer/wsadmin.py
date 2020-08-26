#Create Username and Password
#AdminTask.createAuthDataEntry('[-alias PlantsAuthAlias -user db2inst1 -password db2Pa2359w0rd123 -description db2Passw0rd!123 ]')
AdminTask.createAuthDataEntry('[-alias mysqlDb -user root -password password]')
#Create JDBC Providers
#DB2JDBC=AdminTask.createJDBCProvider('[-scope Cell=DefaultCell01 -databaseType DB2 -providerType "DB2 Universal JDBC Driver Provider" -implementationType "Connection pool data source" -name "DB2 Universal JDBC Driver Provider" -classpath [/demo/db2drivers/db2jcc.jar /demo/db2drivers/db2jcc_license_cu.jar ] -nativePath [${DB2UNIVERSAL_JDBC_DRIVER_NATIVEPATH} ] ]')
#DB2JDBCXA=AdminTask.createJDBCProvider('[-scope Cell=DefaultCell01 -databaseType DB2 -providerType "DB2 Universal JDBC Driver Provider" -implementationType "XA data source" -name "DB2 Universal JDBC Driver Provider (XA)" -classpath [/demo/db2drivers/db2jcc.jar /demo/db2drivers/db2jcc_license_cu.jar ] -nativePath [${DB2UNIVERSAL_JDBC_DRIVER_NATIVEPATH} ] ]')
MYSQLJDBC=AdminTask.createJDBCProvider('[-scope Cell=DefaultCell01 -databaseType User-defined -providerType "User-defined JDBC Provider" -implementationType "User-defined" -implementationClassName "com.mysql.cj.jdbc.MysqlConnectionPoolDataSource" -name "MySQL JDBC Provider" -classpath [/demo/mysqldrivers/mysql-connector-java-8.0.21.jar ] ]')
#Create Datasources
#AdminTask.createDatasource(DB2JDBCXA, '[-name PlantsByWebSphereDataSource -jndiName jdbc/PlantsByWebSphereDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/PlantsAuthAlias -xaRecoveryAuthAlias DefaultNode01/PlantsAuthAlias -configureResourceProperties [[databaseName java.lang.String PLANTSDB] [driverType java.lang.Integer 4] [serverName java.lang.String 169.62.104.36] [portNumber java.lang.Integer 32612]]]')
#AdminTask.createDatasource(DB2JDBC, '[-name PlantsByWebSphereDataSourceNONJTA -jndiName jdbc/PlantsByWebSphereDataSourceNONJTA -dataStoreHelperClassName com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/PlantsAuthAlias -configureResourceProperties [[databaseName java.lang.String PLANTSDB] [driverType java.lang.Integer 4] [serverName java.lang.String 169.62.104.36] [portNumber java.lang.Integer 32612]]]')
AdminTask.createDatasource(MYSQLJDBC, '[-name MySQLDataSource -jndiName jdbc/mysqlds -dataStoreHelperClassName com.ibm.websphere.rsadapter.GenericDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/mysqlDb -configureResourceProperties [[serverName java.lang.String 10.242.0.6] [portNumber java.lang.Integer 6603] [databaseName java.lang.String cargotracker] [user java.lang.String root] [password java.lang.String password]]]')
#Change JPA from 2.0 to 2.1
svr = AdminConfig.getid('/Server:server1/')
AdminTask.modifyJPASpecLevel(svr, '[ -specLevel 2.1]')
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