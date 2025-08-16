#practise for neo4j.
from neo4j import GraphDatabase

# Neo4j connection details
URI = "bolt://localhost:7687"  # Change this if necessary
USERNAME = "neo4j"
PASSWORD = "password"  # Change this to your Neo4j password


class EmergencyGraph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_emergency_node(self, situation, number, advice):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_node, situation, number, advice)

    @staticmethod
    def _create_and_return_node(tx, situation, number, advice):
        query = (
            "MERGE (e:Emergency {situation: $situation}) "
            "SET e.number = $number, e.advice = $advice "
            "RETURN e"
        )
        tx.run(query, situation=situation, number=number, advice=advice)


# Data from the Prolog file
emergency_data = [
    ('police', 15, 'The emergency number for the police in Pakistan is 15.'),
    ('fire', 16, 'Call 16 immediately, provide your exact location, and stay on the line if possible.'),
    ('medical', 1122, 'Dial 1122 for medical emergency services in Pakistan.'),
    ('crime', 15, 'Call 15 immediately and provide details about the crime, location, and any suspects.'),
    ('fire_house', 16, 'Call 16 immediately, evacuate the house, and ensure everyone is safe.'),
    ('house_fire', 16, 'Call 16 immediately, evacuate the house, and ensure everyone is safe.'),
    ('emergency_remote', 1122, 'Dial 1122 or 15 for assistance.'),
    ('road_accident', 1122, 'Call 1122 and report the accident’s location, number of vehicles involved, and injuries.'),
    ('fire_building', 16, 'Call 16 and provide the address, number of floors, and any people trapped inside.'),
    ('building_fire', 16, 'Call 16 and provide the address, number of floors, and any people trapped inside.'),
]

if __name__ == "__main__":
    graph = EmergencyGraph(URI, USERNAME, PASSWORD)

    for situation, number, advice in emergency_data:
        graph.create_emergency_node(situation, number, advice)
        print(f"Added emergency: {situation}, Number: {number}, Advice: {advice}")

    graph.close()
