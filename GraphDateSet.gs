function GraphDate() {
  var app = SpreadsheetApp;
  var as = app.getActiveSpreadsheet().getSheetByName("Graph");
  // Set today()
  var st = as.getRange(1,3).setValue('=today()');
  // Set today as string
  var getst = as.getRange(1,3).getValue();
  var setst = as.getRange(1,3).setValue(getst);
  
}
