const firebaseUrl = "FIREBASE-API-URL";
const apiKey = "FIREBASE-API-KEY";
function updateCurrencyPairs() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  var currencies = ["USD", "KRW", "JPY", "CNY", "EUR", "GBP"];

  var startRow = 2;
  var startColumn = 2;
  let total_list = {};

  for (let i = 0; i < currencies.length; i++) {
    for (let j = 0; j < currencies.length; j++) {
      // 중복제거
      if (i === j) continue;

      // 페어
      let currencyPair = `${currencies[i]}${currencies[j]}`;

      let row = startRow + i;
      let column = startColumn + j;

      sheet
        .getRange(row, column)
        .setFormula(
          `=GOOGLEFINANCE("CURRENCY:${currencies[i]}${currencies[j]}")`
        );

      SpreadsheetApp.flush();
      let exchangeRate = sheet.getRange(row, column).getValue();

      total_list[currencyPair] = exchangeRate;
    }
  }
  const now = new Date().toISOString();
  total_list["currenttime"] = now + "UTC +9";
  const options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(total_list),
  };
  const urlWithKey = firebaseUrl + ".json?auth=" + apiKey;
  Logger.log(JSON.stringify(total_list));
  try {
    const response = UrlFetchApp.fetch(urlWithKey, options);
    Logger.log("데이터 저장 완료: " + response.getContentText());
  } catch (e) {
    Logger.log("Firebase 저장 중 오류 발생: " + e);
  }
}
