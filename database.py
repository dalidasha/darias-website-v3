import os
from sqlalchemy import create_engine, text


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs

#    print(result_dicts)

#    print("type(result:", type(result))
#    result_all = result.all()
#    print("type(result.all()):", type(result_all))
#    print(type(result_all[0]))
#    first_result_dict = result_all[0]._asdict()
#    print("type(first_result_dict:", type(first_result_dict))
#    print(first_result_dict)
