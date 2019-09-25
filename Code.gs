function GraphUpdate() {
  // Validate Time Run Requirement
  var app = SpreadsheetApp;  
  var as = app.getActiveSpreadsheet().getSheetByName("DateTime");
  var NT = as.getRange(1,4).setValue('=(CONCATENATE(A1,".",B1))');
  var Time = as.getRange(1,4).getValue();
  if (Time >= 3.45){
    if(Time <= 4.00){
      //clear sheet data 
      var s=SpreadsheetApp.getActiveSpreadsheet().getSheetByName("RawData");
      s.getRange("A:Z").clearContent(); 
      Logger.log(Time); 
    }
  }
  
  if (Time >=10.00){
    if(Time <= 23.31){
      
      //clear sheet data 
      var s=SpreadsheetApp.getActiveSpreadsheet().getSheetByName("RawData");
      s.getRange("A:Z").clearContent(); 
      Logger.log(Time);
      
      
      //import Data
      var file = DriveApp.getFilesByName("SalesOperationsReport.csv").next();
      var csvData = Utilities.parseCsv(file.getBlob().getDataAsString());
      
      var ss = SpreadsheetApp.getActiveSpreadsheet();
      var sheet = ss.getSheetByName("RawData");
      sheet.getRange(1, 1, csvData.length, csvData[0].length).setValues(csvData);
      
      
      // Update Sales
      var app = SpreadsheetApp;
      var activeSheet = app.getActiveSpreadsheet().getSheetByName("SalesAmount");  
      var TotalSales = activeSheet.getRange(2,1).getValue();
      var MembershipSales = activeSheet.getRange(2,2).getValue();
      var ExtraItem = activeSheet.getRange(2,3).getValue();
      var RPAL = activeSheet.getRange(2,5).getValue();
      var NTax = activeSheet.getRange(2,6).getValue();
      Logger.log(TotalSales);
      Logger.log(MembershipSales);
      
      
      var as = app.getActiveSpreadsheet().getSheetByName("TargetData");
      var RowCount = as.getRange(1,12).getValue();
      var AdjCount = RowCount+2;
      Logger.log(AdjCount);
      var NewSales = as.getRange(AdjCount,7).setValue(TotalSales);
      var NewMS = as.getRange(AdjCount,8).setValue(MembershipSales);
      var NewExtra = as.getRange(AdjCount,9).setValue(ExtraItem);
      as.getRange(AdjCount,10).setValue(RPAL);
      as.getRange(AdjCount,11).setValue(NTax);
    }      
  }
}
