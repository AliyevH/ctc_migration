from db import SourceDB
from db import DestinationDB
from db import config
from time import sleep
import sys

sourceDB = SourceDB()
destinationDB = DestinationDB()


def column_to_column():
    ROWS = 0
    UPDATED_ROWS = 0

    for mt in config.migrationTables:
        for k, v in mt.items():
            source_table_name = v.get("SourceTableName")
            destination_table_name = v.get("DestinationTableName")
            unique_key = v.get("uniqueKey")

            migration_columns = v.get("MigrationColumns")

            source_table = getattr(sourceDB.base.classes, source_table_name)
            destination_table = getattr(destinationDB.base.classes, destination_table_name)


            source_rows = sourceDB.session.query(source_table).all()

            for row in source_rows:
                ROWS += 1
                data = {}
                for mc in migration_columns:
                    if mc.get("type_cast"):
                        temp = getattr(row, mc.get("sourceColumn"))
                        try:
                            setattr(row, mc.get("sourceColumn"), type(mc.get("type_cast"))(temp))
                        except Exception as err:
                            setattr(row, mc.get("sourceColumn"), None)
                    data.update({mc.get("destinationColumn"): getattr(row, mc.get("sourceColumn"))})

                try:
                    inserting_data = destination_table(**data)
                    destinationDB.session.add(inserting_data)
                    destinationDB.session.commit()
                    UPDATED_ROWS += 1
                except Exception as err:
                    destinationDB.session.rollback()
                    print(err)
                    print(data)
                    sleep(60)

    sourceDB.session.close()
    destinationDB.session.close()

    print(ROWS, UPDATED_ROWS)

# column_to_column()

if __name__ == "__main__":
    print(sys.argv)



# column_to_column("Cars.number", "automobiles_automobile.gos_number")