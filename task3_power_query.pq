let
    Source = Csv.Document(
        File.Contents("C:\Users\YourName\vehicle_sales_clean.csv"),
        [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]
    ),

    PromotedHeaders = Table.PromoteHeaders(
        Source, [PromoteAllScalars = true]
    ),

    ChangedTypes = Table.TransformColumnTypes(
        PromotedHeaders, {
            {"Date", type date},
            {"Sales", type number},
            {"Profit", type number},
            {"Quantity", Int64.Type}
        }
    ),

    RemovedDuplicates = Table.Distinct(ChangedTypes),

    RemovedNulls = Table.SelectRows(
        RemovedDuplicates,
        each [Sales] <> null and [Profit] <> null and [Quantity] <> null
    ),

    AddedProfitMargin = Table.AddColumn(
        RemovedNulls, "Profit Margin %",
        each if [Sales] = 0 then 0 else ([Profit] / [Sales]) * 100,
        type number
    ),

    AddedYear = Table.AddColumn(
        AddedProfitMargin, "Year",
        each Date.Year([Date]),
        Int64.Type
    ),

    AddedMonth = Table.AddColumn(
        AddedYear, "Month",
        each Date.MonthName([Date]),
        type text
    ),

    AddedQuarter = Table.AddColumn(
        AddedMonth, "Quarter",
        each "Q" & Text.From(Date.QuarterOfYear([Date])),
        type text
    ),

    SortedByDate = Table.Sort(
        AddedQuarter, {{"Date", Order.Ascending}}
    )

in
    SortedByDate
