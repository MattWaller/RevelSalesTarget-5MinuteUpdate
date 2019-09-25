function ClearDailySales() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getSheetByName("TargetData"); 
  sheet.getRange("G2:I").clearContent();
}
