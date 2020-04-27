-- Handling Error
BEGIN
  DECLARE FROMDATE DATE DEFAULT '2020-03-15'; #'2019-11-04'; 
  DECLARE TODATE DATE DEFAULT '2020-03-15'; 
        
  CREATE OR REPLACE TEMP TABLE temp.loop as (
  SELECT 'a' as a
    
  );
  EXCEPTION WHEN ERROR THEN
  SELECT
        @@error.message as error_message,
        @@error.stack_trace as stack_trace,
        @@error.statement_text as statement_text,
        @@error.formatted_stack_trace as formatted_stack_trace;
  
END;