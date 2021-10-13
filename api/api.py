from google.cloud import datastore

datastore_client = datastore.Client()

def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times

def store_name_in_db(name, dt):
    task = datastore.Entity(key=datastore_client.key('Task'))
    task.update({
            "name": name,
            "timestamp": dt
    })
    datastore_client.put(task)

def get_all_names():
    query = datastore_client.query(kind="Task")
    query.order = ['-timestamp']

    names = query.fetch()

    return names