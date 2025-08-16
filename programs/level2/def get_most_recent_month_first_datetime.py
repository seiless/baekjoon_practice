def get_most_recent_month_first_datetime(
    target_datetime: datetime,
) -> datetime.datetime:
    now = target_datetime
    return now.replace(day=1,hour=0,minute=0,second=0,microsecond=0)

def get_most_recent_month_last_dateime(
    target_datetime: datetime
) -> datetime.datetime:
    return get_most_recent_month_first_datetime(target_datetime) + relativedelta(months = 1)

def get_current_monthly_period(target_datetime:datetime) -> datetime.datetime:
    return (get_most_recent_month_first_datetime(target_datetime),
    get_most_recent_month_last_dateime(target_datetime))

def get_past_n_months(target_datetime: datetime, period: int) -> List:
    months = []
    for i in range(period):
        target_datetime = target_datetime - relativedelta(months=i)
        start_date, end_date = get_current_monthly_period(target_datetime)
        months.append((start_date,end_date))
    return months

def get_most_recent_quarter_first_datetime(
    target_datetime: datetime
) -> datetime.datetime:
    now = target_datetime
    quarter_first_month = 3 * ((now.month - 1) // 3) + 1
    return now.replace(
        month = quarter_first_month,
        day = 1,
        hour = 0,
        minute = 0,
        second = 0,
        microsecond = 0
    )

def get_most_recent_quarter_last_datetime(
    target_datetime: datetime
) -> datetime.datetime: 
    return get_most_recent_quarter_first_datetime(target_datetime) + relativedelta(months = 3)

def get_current_quarter_period(target_datetime:datetime) -> datetime.datetime:
    return (get_most_recent_quarter_first_datetime(target_datetime),
    get_most_recent_quarter_last_datetime(target_datetime))

def get_past_n_quarters(target_datetime: datetime, period: int) -> List:
    quarters = []
    for i in range(period):
        target_datetime = target_datetime - relativedelta(months=3 * i)
        start_date, end_date = get_current_quarter_period(target_datetime)
        quarters.append((start_date,end_date))
    return quarters

def get_past_n_period(
    df: SparkDataFrame, target_datetime: datetime, period_type: str, period_range: int
) -> SparkDataFrame:
    get_period_map = {"Q":get_past_n_quarters, "M":get_past_n_months}
    past_n_period = get_period_map[period_type](target_datetime,period_range)

    new_schema = StructType(
        df.schema.fields
        + [StructField(EXTRACT_START_DATETIME), TimestampType(), False]
        + [StructField(EXTRACT_END_DATETIME), TimestampType(), False]
    )

    spark = get_spark_session()
    output_df = spark.createDataFrame([], new_schema)

    for start_date, end_date in past_n_period:
        threshold_first_day_of_period = start_date
        threshold_last_day_of_period = end_date

        temp_df = (
            df.filter(
                C(CALL_DATETIME).between(
                    threshold_first_day_of_period,threshold_last_day_of_period
                )
            )
            .withColumn(EXTRACT_START_DATETIME, lit(threshold_first_day_of_period))
            .withColumn(EXTRACT_END_DATETIME, lit(threshold_last_day_of_period))
        )
        output_df = output_df.unionByName(temp_df)
    return output_df

def mock_method(spark_session, test_source_dalta_table):
    with patch.multiple(
        DatabricksDataset,
        _get_delta_table=Mock(return_value = test_source_delta_table),
        _get_spark=Mock(return_value= spark_session),
        _exists=Mock(return_value=True),
    ) as mock:
        yeald mock

def create_summarized_table(
    params:Dict[str,Any],
    target_df:DataFrame,
    n_shot_tests:DataFrame,
    product_catalog:DataFrame
) -> DataFrame:
    try: new_schema = StructType(
        target_df.select(
            [
                PROD_NAME,
                PROD_INDI,
                PRI_NAME,
                PRI_REACTION,
                CHOSEN_LEVEL,
                EXTRACT_START_DATE,
                EXTRACT_END_DATE,
                SSO_NAME,
                BEFORE_SSO_STAGE,
                AFTER_SSO_STAGE,
            ]
        ).schema.fields
        + [StructField(SUMMARIZE_VOICE, StringType(), False)]
        + [StructField(NUMBER_OF_CLI, IntegerType(), True)]
        + [StructField(NUMBER_OF_VOICE, IntegerType(), True)]
    )

    spark = get_spark.session()
    ret = spark.createDataFrame([], new_schema)

    results = []
    for k, product_data in params["beliefs"].items():
        base_temp_df = target_df.filter(C(PROD_NAME) == product_data["target_prod_name"])
        for belief_dict in product_data["beliefs"]:
            filter_sbs = belief_dict["sbs_name"]
            filter_sso_category = belief_dict["sso_category"]
            if "product_indication" in belief_dict:
                first_belief_sso_temp_df = base_temp_df.filter(
                    (C(BELIEF_NAME) == filter_sbs)
                )

@pytest.fixture(scope="session")
def test_source_data(deltatable):
    return deltatable("test",[("a","b","c","d"),(1,2,3,0),(1,4,3,1)])

@pytest.fixture(scope="session")
def test_target_df(dataframe):
    return dataframe([("a","b","c","d"),(1,21,3,0),(1,4,4,10)])

@pytest.fixture()
def mock_method(spark_session, test_source_dalta_table):
    with patch.multiple(
        DatabricksDataset,
        _get_delta_table=Mock(return_value = test_source_delta_table),
        _get_spark=Mock(return_value= spark_session),
        _exists=Mock(return_value=True),
    ) as mock:
        yeald mock

def test_merge_function(moch_method, test_target_df, test_source_delta_table):
    upsert_cond = {
        "merge_keys": ["a","b"],
        "when_mathed_update_keys":["d"],
        "when_not_matched_insert_keys":"*",
    }

    test_dataset = DatabricksDataSet(
        table = "test", write_mode = "upsert", upsert_condition = upsert_cond, database="test"
    )

    excepted = pd.DataFrame(
        columns=["a","b","c","d"], data =[(1,2,3,0),(1,21,3,0),(1,4,3,10)]
    )
    test_dataset._save(test_target_df)
    assert_delta_table_and_pandas_df_equal(
        test_source_delta_table, expected, sort_columns= ["a","b","c","d"]
    )