## Database related notes
### GraphDB
1. Concept
    1. Using graph (nodes and edges) to represent data and its relationship.
    2. Nodes : Can have name, key-value pair **property**. Each node is an entity, this is different from RDB.
    3. Edges : Same as nodes. Link nodes together to represent the relationship between nodes. It is directed.
    4. Label : Both nodes and edges can have label, this is different from property. We can use label to represent the conept of group.
2. Cypher
    1. Is's the language for GraphDB, similar to SQL.
    2. There are plenty of interesting use case, and it's powerful due to the property of graph. 
    3. Simple example : 
    ```cypher
    CREATE (you:Person {name:"You"})
    RETURN you
   
    MATCH  (you:Person {name:"You"})
    CREATE (you)-[like:LIKE]->(neo:Database {name:"Neo4j" })
    RETURN you,like,neo

    MATCH (you:Person {name:"You"})
    FOREACH (name in ["Johan","Rajesh","Anna","Julia","Andrew"] |
    CREATE (you)-[:FRIEND]->(:Person {name:name}))

    MATCH (you {name:"You"})-[:FRIEND]->(yourFriends)
    RETURN you, yourFriends

    MATCH (neo:Database {name:"Neo4j"})
    MATCH (anna:Person {name:"Anna"})
    CREATE (anna)-[:FRIEND]->(:Person:Expert {name:"Amanda"})-[:WORKED_WITH]->(neo)
    ```
    4. Use case example : [NBA Playoff prediction](https://neo4j.com/graphgist/nba-playoff-prediction)

### Index in DB
1. Promary Index : An ordered index, usually the key attribute of the table.
2. Secondary Index : May be non-ordered. Can be other candidate key or non-key value.
3. Clustering Index : Ordered index, non-key value.
4. Multi-level index : To make the index structure smaller.

**Dense and Sparse** <br />
One-to-One or One-to-Many. If it's sparse, it first find the head of the data block, then sequential search.
