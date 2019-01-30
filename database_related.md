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


### Concurrency problems in DB
1. dirty read : when a transaction is allowed to read a row that has been modified by another transaction which is not committed yet.
2. non-repeatable read : when a transaction read the same row twice but get different value.
3. phantom read : when two same queries are executed, the rows retrieved by the two are different. 

### Index in DB
1. Primary Index : An ordered index, usually the key attribute of the table.
2. Secondary Index : May be non-ordered. Can be other candidate key or non-key value.
3. Clustering Index : Ordered index, non-key value.
4. Multi-level index : To make the index structure smaller.

**Dense and Sparse** <br />
One-to-One or One-to-Many. If it's sparse, it first find the head of the data block, then sequential search.

**Clustered and Non-clustered** <br />
1. There can only be one clustered index for a table.
2. Can be more than one non-clustered index.

**When should index be created?** <br />
1. A column contains a wide range of data
2. A column doesn't contain lots of null
3. Columns that are frequently used in where clauses or join condition

**When index should not be created?** <br />
1. The table is small
2. Columns that are updated frequently


### B tree
**Properties** <br />
1. All leaves are at the same level
2. It is defined by a minimum degree `t`
3. Every nodes except the root must contain at least t-1 keys. Root can contain minumum one key
4. All nodes (including root) can have at most `2t-1` keys
5. Number of children equals to the number of keys plus one
6. All keys of a node are stored in increasing order
7. B tree grows up when insertion happen.


### B+ tree
Original B tree stores pointer to the disk file block containing the key value. This technique greatly reduce the number of entries that can be packed into a node of B tree. Hence increase the level of B tree, thus increase the search time of a record. <br />
B+ tree eliminate the drawbacks by storing data pointers only at the leaf nodes of the tree, thus each nodes can store more entries. Besides, leaf nodes are connected togrther, thus only one path from root to leaf can access all leaf nodes.




