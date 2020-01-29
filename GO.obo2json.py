import json


class GeneOntology(object):

    def __init__(self, path):
        self.path = path
        self.total = []

    # Use a dictionary to remove extra values to Simplified procedure
    # def rebuild_list(self,record_name):
    #     records = {id,is_a}
    #
    #     list = rebuile_list('HEADER'')
    #     records.get(record_name)


    # Define a function to read and store data
    def read_storage_data(self):

        id = {}         #Use a dictionary to store each keyword
        id_number = ""  # Store the value of each row as a string

        is_obsolete = {}
        is_obsolete_number = ""

        is_class_level = {}
        is_class_level_number = ""

        transitive_over = {}
        transitive_over_number = ""

        # There is a place where the keyword “def” conflicts, so I want to change the name here.
        DEF = {}
        DEF_number = ""

        property_value = {}
        property_value_number = ""

        namespace = {}
        namespace_number = ""

        comment = {}
        comment_number = ""

        intersection_of = {}
        intersection_of_number = ""

        xref = {}
        xref_number = ""

        name = {}
        name_number = ""

        disjoint_from = {}
        disjoint_from_number = ""

        replaced_by = {}
        replaced_by_number = ""

        relationship = {}
        relationship_number = ""

        alt_id = {}
        alt_id_number = ""

        holds_over_chain = {}
        holds_over_chain_number = ""

        subset = {}
        subset_number = ""

        expand_assertion_to = {}
        expand_assertion_to_number = ""

        is_transitive = {}
        is_transitive_number = ""

        is_metadata_tag = {}
        is_metadata_tag_number = ""

        inverse_of = {}
        inverse_of_number = ""

        created_by = {}
        created_by_number = ""

        creation_date = {}
        creation_date_number = ""

        consider = {}
        consider_number = ""

        is_a = {}
        is_a_list = []  # A field name may have multiple values, so it is stored in the form of a “list”.

        synonym = {}
        synonym_list = []

        newdic = []
        f = open(self.path, 'r', encoding="utf-8")
        for line in f.readlines():
            lable = line.split(":")[0]        # Read the list ‘name’, starting from the position of '0', ending with ":", reading all field names

            # View the name of the list that was read

            # print(lable)

            # Start to judge

            if lable == "id":                 # Judge the label for storage
                id_number = line[3:].strip()  # Remove the label and colon, occupy 3 positions, and strip() is used to remove the trailing spaces.

            elif lable == "is_obsolete":
                is_obsolete_number = line[12:].strip()

            elif lable == "is_class_level":
                is_class_level_number = line[15:].strip()

            elif lable == "transitive_over":
                transitive_over_number = line[16:]

            elif lable == "def":
                DEF_number = line[5:].strip()

            elif lable == "property_value":
                property_value_number = line[15:].strip()

            elif lable == "namespace":
                namespace_number = line[10:].strip()

            elif lable == "comment":
                comment_number = line[8:].strip()

            elif lable == "intersection_of":
                intersection_of_number = line[16:].strip()

            elif lable == "xref":
                xref_number = line[5:].strip()

            elif lable == "name":
                name_number = line[5:].strip()

            elif lable == "disjoint_from":
                disjoint_from_number = line[14:].strip()

            elif lable == "replaced_by":
                replaced_by_number = line[12:].strip()

            elif lable == "relationship":
                relationship_number = line[13:].strip()

            elif lable == "alt_id":
                alt_id_number = line[7:].strip()

            elif lable == "holds_over_chain":
                holds_over_chain_number = line[17:].strip()

            elif lable == "subset":
                subset_number = line[7:].strip()

            elif lable == "expand_assertion_to":
                expand_assertion_to_number = line[20:].strip()

            elif lable == "is_transitive":
                is_transitive_number = line[14:].strip()

            elif lable == "is_metadata_tag":
                is_metadata_tag_number = line[16:].strip()

            elif lable == "inverse_of":
                inverse_of_number = line[11:].strip()

            elif lable == "created_by":
                created_by_number = line[11:].strip()

            elif lable == "creation_date":
                creation_date_number = line[14:].strip()

            elif lable == "consider":
                consider_number = line[9:].strip()


            elif lable == "is_a":
                is_a_list.append(line[5:].strip().split('\n'))

            elif lable == "synonym":
                synonym_list.append(line[8:].strip().split('\n'))




            # Put "[" as the end of the store.
            # If you want to "[" as the beginning of your storage, you will have to change the storage format of the data.

            elif line[0] == "[":

                # Assign values ​​and store the data in newdic[]

                id["id"] = id_number
                newdic.append(id)

                is_obsolete["is_obsolete"] = is_obsolete_number
                newdic.append(is_obsolete)

                is_class_level["is_class_level"] = is_class_level_number
                newdic.append(is_class_level)

                transitive_over["transitive_over"] = transitive_over_number
                newdic.append(transitive_over)

                DEF["def"] = DEF_number
                newdic.append(DEF)

                property_value["property_value"] = property_value_number
                newdic.append(property_value)

                namespace["namespace"] = namespace_number
                newdic.append(namespace)

                comment["comment"] = comment_number
                newdic.append(comment)

                intersection_of["intersection_of"] = intersection_of_number
                newdic.append(intersection_of)

                xref["xref"] = xref_number
                newdic.append(xref)

                name["name"] = name_number
                newdic.append(name)

                disjoint_from["disjoint_from"] = disjoint_from_number
                newdic.append(disjoint_from)

                replaced_by["replaced_by"] = replaced_by_number
                newdic.append(replaced_by)

                relationship["relationship"] = relationship_number
                newdic.append(relationship)

                alt_id["alt_id"] = alt_id_number
                newdic.append(alt_id)

                holds_over_chain["holds_over_chain"] = holds_over_chain_number
                newdic.append(holds_over_chain)

                subset["subset"] = subset_number
                newdic.append(subset)

                expand_assertion_to["expand_assertion_to"] = expand_assertion_to_number
                newdic.append(expand_assertion_to)

                is_transitive["is_transitive"] = is_transitive_number
                newdic.append(is_transitive)

                is_metadata_tag["is_metadata_tag"] = is_metadata_tag_number
                newdic.append(is_metadata_tag)

                inverse_of["inverse_of"] = inverse_of_number
                newdic.append(inverse_of)

                created_by["created_by"] = created_by_number
                newdic.append(created_by)

                creation_date["creation_date"] = creation_date_number
                newdic.append(creation_date)

                consider["consider"] = consider_number
                newdic.append(consider)

                is_a["is_a"] = is_a_list
                newdic.append(is_a)

                synonym["synonym"] = synonym_list
                newdic.append(synonym)

                # Save newdic in the total data set
                self.total.append(newdic)

                # Initialize all new tags
                id = {}
                id_number = ""

                is_obsolete = {}
                is_obsolete_number = ""

                is_class_level = {}
                is_class_level_number = ""

                transitive_over = {}
                transitive_over_number = ""

                DEF = {}
                DEF_number = ""

                property_value = {}
                property_value_number = ""

                namespace = {}
                namespace_number = ""

                comment = {}
                comment_number = ""

                intersection_of = {}
                intersection_of_number = ""

                xref = {}
                xref_number = ""

                name = {}
                name_number = ""

                disjoint_from = {}
                disjoint_from_number = ""

                replaced_by = {}
                replaced_by_number = ""

                relationship = {}
                relationship_number = ""

                alt_id = {}
                alt_id_number = ""

                holds_over_chain = {}
                holds_over_chain_number = ""

                subset = {}
                subset_number = ""

                expand_assertion_to = {}
                expand_assertion_to_number = ""

                is_transitive = {}
                is_transitive_number = ""

                is_metadata_tag = {}
                is_metadata_tag_number = ""

                inverse_of = {}
                inverse_of_number = ""

                created_by = {}
                created_by_number = ""

                creation_date = {}
                creation_date_number = ""

                is_a = {}
                is_a_list = []

                synonym = {}
                synonym_list = []

                # Initialize newdic
                newdic = []

            # total.append(newdic)
        # self.total.append(newdic)             #You append an empty newdic, so there is an empty one behind []


if __name__ == "__main__":
    class1 = GeneOntology('C:\\Users\\Administrator\\Downloads\\Gene_ontology.obo')
    class1.read_storage_data()
    print(class1.total)

    jsObj = json.dumps(class1.total)  #序列化：encoding，把一个python对象编码转化成json字符串，json.dumps()
    fileObject = open('C:\\Users\\Administrator\\Downloads\\jsonFile.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()
    
