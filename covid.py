def get_covid19_report_today(covid_data_path):
  url = 'https://covid19.ddc.moph.go.th/api/Cases/today-cases-line-lists'
  response = requests.get(url)
  decoded_content = response.content.decode('utf-8')
  with open(covid_data_path, 'w', encoding='utf-8') as f:
    f.write(decoded_content)
  print(f"Output to {covid_data_path}")
#Under DAG declaration
t1 = PythonOperator(
  task_id='get_data_from_api',
  python_callable=get_covid19_report_today,
  op_kwargs={'covid_data_path': covid_data_path},
)
t1
