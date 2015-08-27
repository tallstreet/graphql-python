import unittest
from graphql import Parser, Operation, Fragment

class TestGraphQL(unittest.TestCase):
    def test_basic(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery{
            viewer{ 
              id 
            }
          } 
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "viewer")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
  
    def test_multi_field(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user {
                id,
                name,
                isViewerFriend
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].name, "isViewerFriend")

    def test_with_args(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
            user(id: 12356) {
              id,
              name,
              isViewerFriend
            }
          }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"id": 12356})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].name, "isViewerFriend")

    def test_with_web_example(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(id: 3500401) {
                id,
                name,
                isViewerFriend,
                profilePicture(size: 50)  {
                  uri,
                  width,
                  height
                }
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"id": 3500401})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 4)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].name, "isViewerFriend")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].name, "profilePicture")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].arguments, {"size": 50})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.fields[0].name, "uri")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.fields[1].name, "width")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.fields[2].name, "height")


    def test_with_bool_arg(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(active: true) {
                id
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"active": True})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")


    def test_with_float_arg(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(age: 21.2) {
                id
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"age": 21.2})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")

    def test_with_string_arg(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(status: "active") {
                id
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"status": "active"})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")

    def test_with_enum_arg(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(status: ACTIVE) {
                id
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"status": "ACTIVE"})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")

    def test_with_array_arg(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(status: [1, 2]) {
                id
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"status": [1, 2]})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")

    def test_with_object_arg(self):
        parser = Parser()
        doc = parser.parse_query("""query RootQuery {
              user(details: { name: "Hello world", score: 1.0 }) {
                id
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments['details']['name'], "Hello world")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments['details']['score'], 1.0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")


    def test_with_variables(self):
        parser = Parser()
        doc = parser.parse_query("""query getZuckProfile($devicePicSize: Int) {
              user(id: 4) {
                id
                name
                profilePic(size: $devicePicSize)
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "getZuckProfile")
        self.assertEqual(doc.definitions[0].variables_size, 1)
        self.assertEqual(doc.definitions[0].definitions[0].variable.value, "devicePicSize")
        self.assertEqual(doc.definitions[0].definitions[0].type, "Int")
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments["id"], 4)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].name, "profilePic")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].arguments["size"].value, "devicePicSize")

    def test_with_variables(self):
        parser = Parser()
        doc = parser.parse_query("""query getZuckProfile($devicePicSize: Int) {
              user(id: 4) {
                id
                name
                profilePic(size: $devicePicSize)
              }
            }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "getZuckProfile")
        self.assertEqual(doc.definitions[0].variables_size, 1)
        self.assertEqual(doc.definitions[0].definitions[0].variable.value, "devicePicSize")
        self.assertEqual(doc.definitions[0].definitions[0].type, "Int")
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments["id"], 4)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].name, "profilePic")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].arguments["size"].value, "devicePicSize")

    def test_with_fragments(self):
        parser = Parser()
        doc = parser.parse_query("""query withFragments {
              user(id: 4) {
                friends(first: 10) {
                  ...friendFields
                }
                mutualFriends(first: 10) {
                  ...friendFields
                }
              }
            }

            fragment friendFields on User {
              id
              name
              profilePic(size: 50)
            }
        """)
        self.assertEqual(doc.definitions_size, 2)
        self.assertIsInstance(doc.definitions[0], Operation)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "withFragments")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments["id"], 4)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 2)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments, {"first": 10})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "friends")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].selection_set.frags[0], "friendFields")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments, {"first": 10})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "mutualFriends")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].selection_set.frags[0], "friendFields")
        self.assertIsInstance(doc.definitions[1], Fragment)
        self.assertEqual(doc.definitions[1].name, "friendFields")
        self.assertEqual(doc.definitions[1].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[1].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[1].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[1].selection_set.fields[2].name, "profilePic")
        self.assertEqual(doc.definitions[1].selection_set.fields[2].arguments_size, 1)
        self.assertEqual(doc.definitions[1].selection_set.fields[2].arguments, {"size": 50})


    def test_with_nested_fragments(self):
        parser = Parser()
        doc = parser.parse_query("""query withNestedFragments {
              user(id: 4) {
                friends(first: 10) {
                  ...friendFields
                }
                mutualFriends(first: 10) {
                  ...friendFields
                }
              }
            }

            fragment friendFields on User {
              id
              name
              ...standardProfilePic
            }

            fragment standardProfilePic on User {
              profilePic(size: 50)
            }
        """)
        self.assertEqual(doc.definitions_size, 3)
        self.assertIsInstance(doc.definitions[0], Operation)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "withNestedFragments")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments["id"], 4)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 2)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments, {"first": 10})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "friends")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].selection_set.frags[0], "friendFields")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments, {"first": 10})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "mutualFriends")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].selection_set.frags[0], "friendFields")
        self.assertIsInstance(doc.definitions[1], Fragment)
        self.assertEqual(doc.definitions[1].name, "friendFields")
        self.assertEqual(doc.definitions[1].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[1].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[1].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[1].selection_set.frags[0], "standardProfilePic")
        self.assertIsInstance(doc.definitions[2], Fragment)
        self.assertEqual(doc.definitions[2].name, "standardProfilePic")
        self.assertEqual(doc.definitions[2].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[2].selection_set.fields[0].name, "profilePic")


    def xtest_kitchen_sink(self):
        parser = Parser()
        doc = parser.parse_query("""
        query queryName($foo: ComplexType, $site: Site = MOBILE) {
          whoever123is: node(id: [123, 456]) {
            id ,
            ... on User @defer {
              field2 {
                id ,
                alias: field1(first:10, after:$foo,) @include(if: $foo) {
                  id,
                  ...frag
                }
              }
            }
          }
        }
        """)
        self.assertEqual(doc.definitions_size, 1)
        self.assertEqual(doc.definitions[0].operation, "query")
        self.assertEqual(doc.definitions[0].name, "RootQuery")
        self.assertEqual(doc.definitions[0].variables_size, 0)
        self.assertEqual(doc.definitions[0].directives_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.selection_set_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].arguments, {"id": 3500401})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].name, "user")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.selection_set_size, 4)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].arguments_size, 0)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[0].name, "id")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[1].name, "name")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[2].name, "isViewerFriend")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].name, "profilePicture")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].arguments_size, 1)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].arguments, {"size": 50})
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.selection_set_size, 3)
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.fields[0].name, "uri")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.fields[1].name, "width")
        self.assertEqual(doc.definitions[0].selection_set.fields[0].selection_set.fields[3].selection_set.fields[2].name, "height")

if __name__ == '__main__':
    unittest.main()
