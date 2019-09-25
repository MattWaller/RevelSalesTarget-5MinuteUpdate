function SalesTarget() {
      var app = SpreadsheetApp;
      var as = app.getActiveSpreadsheet().getSheetByName("TargetData");
      // Sales Target grabber  
      var st = as.getRange(1,13).getValue();
      // Copy Spreadsheet data sales target column (Saves Graphs Properly)
      var setst = as.getRange(2,3).setValue(st);
     
}
