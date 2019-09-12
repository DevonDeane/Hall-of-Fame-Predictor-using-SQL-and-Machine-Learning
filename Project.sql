Use project;

DROP PROCEDURE IF EXISTS Data_Mining;
DELIMITER $$
CREATE
PROCEDURE `Data_Mining`(tab_name VARCHAR(20),feature_1 VARCHAR(20),feature_2 VARCHAR(20),feature_3 VARCHAR(20),feature_4 VARCHAR(20),feature_5 VARCHAR(20),feature_6 VARCHAR(20),feature_7 VARCHAR(20),feature_8 VARCHAR(20),feature_9 VARCHAR(20),feature_10 VARCHAR(20))    
BEGIN
 ## Clean Table
 DROP TABLE IF EXISTS `mining`;
 
 ## Get requested table data and attributes selected
 SET @mining =CONCAT('CREATE TABLE mining as select playerid,avg( ', feature_1 ,'),',' avg(', feature_2 ,'),',' avg(', feature_3 ,'),',' avg(', feature_4 ,'),',' avg(', feature_5 ,'),',' avg(', feature_6 ,'),',' avg(', feature_7 ,'),',' avg(', feature_8 ,'),',' avg(', feature_9 ,'),',' avg(', feature_10 ,'),(max(Inducted) IS NOT NULL) as nominated FROM ',tab_name ,' left join HallOfFame using(playerid) group by playerID');
 PREPARE query0 FROM @mining;
 EXECUTE query0;
 DEALLOCATE PREPARE query0;     
     
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS Data_Split;
SET @train_0 = 0;
SET @test_0 = 0;
SET @train_1 = 0;
SET @test_1= 0; 
DELIMITER $$
CREATE
PROCEDURE `Data_Split`(test_size float)
BEGIN
  ## Declare Variables
  DECLARE Total,Num_0,Num_1 float DEFAULT 0;
  
  ## Get Needed Values
  SET @Total = (SELECT COUNT(DISTINCT playerid )
	FROM mining);
  SET @Num_0 = (SELECT COUNT(DISTINCT playerid )
	FROM mining where nominated=0);
  SET @Num_1 = (SELECT COUNT(DISTINCT playerid )
	FROM mining where nominated=1);
    
  ## Calculate Rates 
  SET @train_0 =  ROUND(((@Num_0/@Total) *test_size)*@Total);
  SET @test_0  =  ROUND(((@Num_0/@Total) *(1-test_size))*@Total);
  SET @train_1 =  ROUND(((@Num_1/@Total) *test_size)*@Total);
  SET @test_1  =  ROUND(((@Num_1/@Total) *(1-test_size))*@Total);
  
  ## CLear tables
  DROP TABLE IF EXISTS Train;
  DROP TABLE IF EXISTS Test;
  DROP TABLE IF EXISTS Class_0;
  DROP TABLE IF EXISTS Class_1;

  ## Create base tables
  CREATE TABLE  Class_0 as
	SELECT * FROM mining where nominated=0;
  CREATE TABLE Class_1  as
	SELECT * FROM mining where nominated=1;
    
  ## Extract Training & Test Tables ##
  SET @get_test_0 = CONCAT('CREATE TABLE Test as SELECT * FROM Class_0 LIMIT ',@test_0);
    PREPARE query0 FROM @get_test_0;
      EXECUTE query0;
  SET @delete_0 = CONCAT('DELETE FROM Class_0 LIMIT ',@test_0);
	PREPARE query1 FROM @delete_0;
      EXECUTE query1;
  SET @get_test_1 = CONCAT('INSERT INTO Test SELECT * FROM Class_1 LIMIT ',@test_1);
    PREPARE query2 FROM @get_test_1;
      EXECUTE query2;
  SET @delete_1 = CONCAT('DELETE FROM Class_1 LIMIT ',@test_1);
    PREPARE query3 FROM @delete_1;
      EXECUTE query3;
  SET @get_train_0 = CONCAT('CREATE TABLE Train as SELECT * FROM Class_0 LIMIT ',@train_1);
    PREPARE query4 FROM @get_train_0;
      EXECUTE query4;
  SET @get_train_1 = CONCAT('INSERT INTO Train SELECT * FROM Class_1 LIMIT ',@train_1);
    PREPARE query5 FROM @get_train_1;
      EXECUTE query5;
  ## END Extract Training & Test Tables ##
  
  ## Drop Unused tables
  DROP TABLE IF EXISTS Class_0;
  DROP TABLE IF EXISTS Class_1;
  DEALLOCATE PREPARE query0;
  DEALLOCATE PREPARE query1; 
  DEALLOCATE PREPARE query2; 
  DEALLOCATE PREPARE query3; 
  DEALLOCATE PREPARE query4; 
  DEALLOCATE PREPARE query5; 

END$$
DELIMITER 



